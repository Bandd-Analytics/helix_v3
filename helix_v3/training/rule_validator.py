"""MMM Rule Validator — Backtests taught methodology rules against historical MT5 data.

Replays historical data for each pair and scores:
  - Rule hit rate (how often the taught condition correlates with market behavior)
  - Average RR (risk-reward of trades following the rule)
  - Time-to-target (how long until TP/SL hit)
  - Session dependency (which sessions the rule works best in)
  - Parameter sensitivity (how changes in thresholds affect outcomes)

Usage:
    .venv/Scripts/python.exe -m helix_v3.training.rule_validator --days 90
    .venv/Scripts/python.exe -m helix_v3.training.rule_validator --rule asian_accumulation
    .venv/Scripts/python.exe -m helix_v3.training.rule_validator --pair EURUSD --days 30
    .venv/Scripts/python.exe -m helix_v3.training.rule_validator --report
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from config.pair_profiles import PAIR_PROFILES, PairProfile, get_pair_profile
from config.settings import settings
from helix_v3.core.patterns import PatternType, TradeType, scan_patterns
from helix_v3.core.sessions import classify_sessions, get_prev_day_hod_lod
from helix_v3.core.tdi import compute_tdi
from helix_v3.utils.logger import get_logger

logger = get_logger("rule_validator")

DB_PATH = Path(settings.log_dir) / "rule_validation.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS validation_results (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name       TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    test_date       TEXT NOT NULL,
    occurrences     INTEGER DEFAULT 0,
    hits            INTEGER DEFAULT 0,
    misses          INTEGER DEFAULT 0,
    hit_rate        REAL DEFAULT 0.0,
    avg_rr          REAL DEFAULT 0.0,
    avg_time_min    REAL DEFAULT 0.0,
    best_session    TEXT DEFAULT '',
    parameters      TEXT DEFAULT '{}',
    notes           TEXT DEFAULT '',
    validated_at    TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS rule_events (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name       TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    event_time      TEXT NOT NULL,
    direction       TEXT DEFAULT '',
    outcome         TEXT DEFAULT '',
    pips_result     REAL DEFAULT 0.0,
    rr_achieved     REAL DEFAULT 0.0,
    time_to_outcome INTEGER DEFAULT 0,
    session         TEXT DEFAULT '',
    details         TEXT DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_vr_rule ON validation_results(rule_name, symbol);
CREATE INDEX IF NOT EXISTS idx_re_rule ON rule_events(rule_name, symbol);
"""


@dataclass
class RuleEvent:
    """A single occurrence where a rule condition was met."""
    rule_name: str
    symbol: str
    event_time: datetime
    direction: str = ""
    outcome: str = ""         # "HIT" / "MISS" / "NEUTRAL"
    pips_result: float = 0.0
    rr_achieved: float = 0.0
    time_to_outcome: int = 0  # minutes
    session: str = ""
    details: dict = field(default_factory=dict)


@dataclass
class ValidationResult:
    """Aggregate result for one rule on one pair."""
    rule_name: str
    symbol: str
    test_date: str
    occurrences: int = 0
    hits: int = 0
    misses: int = 0
    hit_rate: float = 0.0
    avg_rr: float = 0.0
    avg_time_min: float = 0.0
    best_session: str = ""
    parameters: dict = field(default_factory=dict)
    notes: str = ""
    events: List[RuleEvent] = field(default_factory=list)


class RuleValidator:
    """Validates MMM rules against historical market data."""

    def __init__(self) -> None:
        self._db = sqlite3.connect(str(DB_PATH))
        self._db.executescript(SCHEMA)
        self._engine = None

    def _get_engine(self):
        if self._engine is None:
            from helix_v3.core.quant_engine import MMMQuantitativeEngine
            self._engine = MMMQuantitativeEngine()
            if not self._engine.connect():
                raise ConnectionError("Cannot connect to MT5")
        return self._engine

    def _fetch_data(self, symbol: str, timeframe: str, count: int) -> pd.DataFrame:
        return self._get_engine().fetch_rates(symbol, timeframe, count)

    def _pip_size(self, symbol: str) -> float:
        return self._get_engine()._get_pip_value(symbol)

    # ==================================================================
    # Rule: Asian Accumulation
    # ==================================================================

    def validate_asian_accumulation(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: Does a valid Asian accumulation predict a tradeable day?

        Measures:
        - How often valid accumulation (range < max) leads to a clear
          directional move of >= expected_level_move_pips
        - Compare valid vs invalid accumulation days
        """
        pp = get_pair_profile(symbol)
        pip = self._pip_size(symbol)
        bars_needed = days * 96 + 200  # M15 bars
        df = self._fetch_data(symbol, "M15", bars_needed)

        sessions = classify_sessions(df, pip)
        result = ValidationResult(
            rule_name="asian_accumulation",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"max_pips": pp.asian_range_max_pips, "days": days},
        )

        events = []
        for date_str, ar in sessions.asian_ranges.items():
            ar_pips = ar["pips"]
            valid = ar_pips <= pp.asian_range_max_pips

            # Find the post-Asian bars for this date
            date = pd.Timestamp(date_str)
            day_mask = df.index.date == date.date()
            day_bars = df[day_mask]

            if len(day_bars) < 20:
                continue

            # Measure the day's total directional move after Asian
            asian_end_idx = ar.get("end_idx", 0)
            if asian_end_idx >= len(df) - 5:
                continue

            post_asian = df.iloc[asian_end_idx + 1:]
            post_day = post_asian[post_asian.index.date == date.date()]
            if post_day.empty:
                continue

            day_high = float(post_day["High"].max())
            day_low = float(post_day["Low"].min())
            day_range = (day_high - day_low) / pip

            # Did the day produce a directional move >= level move?
            hit = day_range >= pp.expected_level_move_pips * 0.5
            outcome = "HIT" if hit else "MISS"

            event = RuleEvent(
                rule_name="asian_accumulation",
                symbol=symbol,
                event_time=date,
                direction="VALID" if valid else "INVALID",
                outcome=outcome,
                pips_result=day_range,
                details={"ar_pips": ar_pips, "valid": valid, "day_range": day_range},
            )
            events.append(event)

        # Aggregate
        valid_events = [e for e in events if e.direction == "VALID"]
        invalid_events = [e for e in events if e.direction == "INVALID"]

        result.occurrences = len(valid_events)
        result.hits = sum(1 for e in valid_events if e.outcome == "HIT")
        result.misses = sum(1 for e in valid_events if e.outcome == "MISS")
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0

        invalid_hits = sum(1 for e in invalid_events if e.outcome == "HIT")
        invalid_rate = invalid_hits / len(invalid_events) if invalid_events else 0

        result.avg_rr = float(np.mean([e.pips_result for e in valid_events])) if valid_events else 0
        result.notes = (
            f"Valid accum hit rate: {result.hit_rate:.1%} ({result.hits}/{result.occurrences}) | "
            f"Invalid accum hit rate: {invalid_rate:.1%} ({invalid_hits}/{len(invalid_events)}) | "
            f"Avg day range (valid): {result.avg_rr:.0f}p"
        )
        result.events = events

        self._save_result(result)
        return result

    # ==================================================================
    # Rule: Stop Hunt Range
    # ==================================================================

    def validate_stop_hunt_range(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: What is the actual distribution of stop hunt breaches?

        Measures post-Asian breach sizes to validate the taught ranges.
        """
        pp = get_pair_profile(symbol)
        pip = self._pip_size(symbol)
        bars_needed = days * 96 + 200
        df = self._fetch_data(symbol, "M15", bars_needed)

        sessions = classify_sessions(df, pip)
        result = ValidationResult(
            rule_name="stop_hunt_range",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={
                "min_pips": pp.stop_hunt_min_pips,
                "max_pips": pp.stop_hunt_max_pips,
                "days": days,
            },
        )

        events = []
        breach_sizes = []

        for date_str, ar in sessions.asian_ranges.items():
            date = pd.Timestamp(date_str)
            asian_high = ar["high"]
            asian_low = ar["low"]

            # Post-Asian bars
            end_idx = ar.get("end_idx", 0)
            if end_idx >= len(df) - 5:
                continue

            post = df.iloc[end_idx + 1:]
            post_day = post[post.index.date == date.date()]
            if post_day.empty:
                continue

            max_high = float(post_day["High"].max())
            min_low = float(post_day["Low"].min())
            breach_above = (max_high - asian_high) / pip
            breach_below = (asian_low - min_low) / pip

            breach = max(breach_above, breach_below)
            direction = "ABOVE" if breach_above > breach_below else "BELOW"
            breach_val = breach_above if direction == "ABOVE" else breach_below

            if breach_val > 1:  # At least 1 pip breach
                in_range = pp.stop_hunt_min_pips <= breach_val <= pp.stop_hunt_max_pips
                breach_sizes.append(breach_val)

                event = RuleEvent(
                    rule_name="stop_hunt_range",
                    symbol=symbol,
                    event_time=date,
                    direction=direction,
                    outcome="IN_RANGE" if in_range else "OUT_OF_RANGE",
                    pips_result=breach_val,
                    details={
                        "breach_above": breach_above,
                        "breach_below": breach_below,
                        "in_range": in_range,
                    },
                )
                events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "IN_RANGE")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0

        if breach_sizes:
            p10 = float(np.percentile(breach_sizes, 10))
            p50 = float(np.percentile(breach_sizes, 50))
            p90 = float(np.percentile(breach_sizes, 90))
            result.notes = (
                f"Breach distribution: P10={p10:.0f}p P50={p50:.0f}p P90={p90:.0f}p | "
                f"Taught range: {pp.stop_hunt_min_pips:.0f}-{pp.stop_hunt_max_pips:.0f}p | "
                f"In range: {result.hit_rate:.1%}"
            )
            result.parameters["actual_p10"] = p10
            result.parameters["actual_p50"] = p50
            result.parameters["actual_p90"] = p90
        else:
            result.notes = "No breaches detected"

        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: M/W Direction Signal
    # ==================================================================

    def validate_mw_direction(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: When M/W forms, does following its direction produce profit?

        Scans for M/W patterns on M15 and measures what happens after.
        """
        pp = get_pair_profile(symbol)
        pip = self._pip_size(symbol)
        bars_needed = days * 96 + 200
        df = self._fetch_data(symbol, "M15", bars_needed)

        result = ValidationResult(
            rule_name="mw_direction",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days, "tolerance_pips": 20},
        )

        events = []
        # Sliding window: scan 20-bar windows for M/W
        step = 10  # Check every 10 bars to avoid too many overlapping detections
        for start in range(0, len(df) - 40, step):
            window = df.iloc[start:start + 20]
            highs = window["High"].values
            lows = window["Low"].values

            mw_dir = None
            # W-bottom
            for i in range(2, len(lows) - 2):
                if lows[i] > lows[i - 2] and lows[i] > lows[i + 2]:
                    diff = abs(lows[i - 2] - lows[i + 2]) / pip
                    if diff < 20:
                        mw_dir = "BUY"
                        break
            # M-top
            if mw_dir is None:
                for i in range(2, len(highs) - 2):
                    if highs[i] < highs[i - 2] and highs[i] < highs[i + 2]:
                        diff = abs(highs[i - 2] - highs[i + 2]) / pip
                        if diff < 20:
                            mw_dir = "SELL"
                            break

            if mw_dir is None:
                continue

            # Measure outcome: next 20 bars after the pattern
            future_start = start + 20
            future_end = min(future_start + 20, len(df))
            if future_end - future_start < 5:
                continue

            future = df.iloc[future_start:future_end]
            entry_price = float(window.iloc[-1]["Close"])

            if mw_dir == "BUY":
                max_profit = (float(future["High"].max()) - entry_price) / pip
                max_loss = (entry_price - float(future["Low"].min())) / pip
            else:
                max_profit = (entry_price - float(future["Low"].min())) / pip
                max_loss = (float(future["High"].max()) - entry_price) / pip

            hit = max_profit > max_loss and max_profit > 10
            rr = max_profit / max_loss if max_loss > 0 else 0

            event = RuleEvent(
                rule_name="mw_direction",
                symbol=symbol,
                event_time=window.index[-1].to_pydatetime(),
                direction=mw_dir,
                outcome="HIT" if hit else "MISS",
                pips_result=max_profit if hit else -max_loss,
                rr_achieved=rr,
                details={
                    "max_profit_pips": max_profit,
                    "max_loss_pips": max_loss,
                    "entry_price": entry_price,
                },
            )
            events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "HIT")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0
        result.avg_rr = float(np.mean([e.rr_achieved for e in events])) if events else 0

        # Best session analysis
        session_hits = {}
        for e in events:
            hour = e.event_time.hour
            if 1 <= hour < 8:
                sess = "ASIA"
            elif 8 <= hour < 13:
                sess = "LONDON"
            elif 13 <= hour < 22:
                sess = "NYC"
            else:
                sess = "OFF"
            session_hits.setdefault(sess, {"hits": 0, "total": 0})
            session_hits[sess]["total"] += 1
            if e.outcome == "HIT":
                session_hits[sess]["hits"] += 1

        best_sess = ""
        best_rate = 0
        for sess, data in session_hits.items():
            rate = data["hits"] / data["total"] if data["total"] > 0 else 0
            if rate > best_rate:
                best_rate = rate
                best_sess = sess
        result.best_session = best_sess

        result.notes = (
            f"M/W direction hit rate: {result.hit_rate:.1%} | "
            f"Avg RR: {result.avg_rr:.2f} | "
            f"Best session: {best_sess} ({best_rate:.1%}) | "
            f"By session: {json.dumps({s: f'{d['hits']}/{d['total']}' for s, d in session_hits.items()})}"
        )
        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: Mid-Week Reversal
    # ==================================================================

    def validate_midweek_reversal(
        self, symbol: str, days: int = 180,
    ) -> ValidationResult:
        """Test: Do Tue/Wed show more reversals than other days?"""
        pip = self._pip_size(symbol)
        df_d1 = self._fetch_data(symbol, "D1", days + 10)

        result = ValidationResult(
            rule_name="midweek_reversal",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days},
        )

        events = []
        day_reversal_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        day_totals = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

        for i in range(2, len(df_d1)):
            bar = df_d1.iloc[i]
            prev = df_d1.iloc[i - 1]
            weekday = bar.name.weekday()

            if weekday > 4:
                continue

            day_totals[weekday] += 1

            # Reversal = today's direction opposite to yesterday's
            prev_dir = 1 if prev["Close"] > prev["Open"] else -1
            curr_dir = 1 if bar["Close"] > bar["Open"] else -1
            is_reversal = prev_dir != curr_dir

            if is_reversal:
                day_reversal_counts[weekday] += 1

            event = RuleEvent(
                rule_name="midweek_reversal",
                symbol=symbol,
                event_time=bar.name.to_pydatetime(),
                direction="REVERSAL" if is_reversal else "CONTINUATION",
                outcome="HIT" if is_reversal and weekday in (1, 2) else "MISS",
                details={"weekday": weekday, "day_name": bar.name.strftime("%A")},
            )
            events.append(event)

        day_names = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri"}
        rates = {}
        for d in range(5):
            rate = day_reversal_counts[d] / day_totals[d] if day_totals[d] > 0 else 0
            rates[day_names[d]] = f"{rate:.1%} ({day_reversal_counts[d]}/{day_totals[d]})"

        midweek_hits = day_reversal_counts[1] + day_reversal_counts[2]
        midweek_total = day_totals[1] + day_totals[2]
        other_hits = sum(day_reversal_counts[d] for d in [0, 3, 4])
        other_total = sum(day_totals[d] for d in [0, 3, 4])

        result.occurrences = midweek_total
        result.hits = midweek_hits
        result.misses = midweek_total - midweek_hits
        result.hit_rate = midweek_hits / midweek_total if midweek_total > 0 else 0

        other_rate = other_hits / other_total if other_total > 0 else 0
        result.notes = (
            f"Midweek reversal rate: {result.hit_rate:.1%} vs other days: {other_rate:.1%} | "
            f"By day: {json.dumps(rates)}"
        )
        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: 90-Minute Stale Exit
    # ==================================================================

    def validate_stale_exit(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: If a position isn't in profit by 90 min, what happens after?

        Simulates: at a random entry, if not in profit after 90 min, does
        holding longer help or hurt?
        """
        pip = self._pip_size(symbol)
        df = self._fetch_data(symbol, "M15", days * 96 + 200)

        result = ValidationResult(
            rule_name="stale_exit_90min",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"stale_minutes": 90, "days": days},
        )

        events = []
        # Sample every 24 bars (6 hours) to simulate entries
        for start_idx in range(0, len(df) - 30, 24):
            entry_price = float(df.iloc[start_idx]["Close"])
            # 90 min on M15 = 6 bars
            stale_idx = start_idx + 6
            if stale_idx >= len(df):
                continue

            stale_price = float(df.iloc[stale_idx]["Close"])
            move_at_90 = (stale_price - entry_price) / pip

            # Check if NOT in profit at 90 min (either direction)
            not_profitable = abs(move_at_90) < 5  # Less than 5 pips either way

            if not not_profitable:
                continue  # Only interested in stale positions

            # What happens if you hold for another 90 min (6 more bars)?
            hold_idx = min(stale_idx + 6, len(df) - 1)
            hold_price = float(df.iloc[hold_idx]["Close"])
            move_after_hold = (hold_price - entry_price) / pip

            # Does holding improve things?
            improved = abs(move_after_hold) > abs(move_at_90) + 5

            event = RuleEvent(
                rule_name="stale_exit_90min",
                symbol=symbol,
                event_time=df.index[start_idx].to_pydatetime(),
                outcome="EXIT_CORRECT" if not improved else "HOLD_BETTER",
                pips_result=move_at_90,
                details={
                    "move_at_90min": move_at_90,
                    "move_at_180min": move_after_hold,
                    "improved": improved,
                },
            )
            events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "EXIT_CORRECT")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0

        result.notes = (
            f"90-min stale exit correct: {result.hit_rate:.1%} | "
            f"Holding longer helped: {result.misses}/{result.occurrences} times"
        )
        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: TDI Shark Fin Confirms Reversal
    # ==================================================================

    def validate_tdi_shark_fin(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: When TDI Shark Fin fires, does a reversal follow?"""
        pip = self._pip_size(symbol)
        df = self._fetch_data(symbol, "M15", days * 96 + 200)

        result = ValidationResult(
            rule_name="tdi_shark_fin",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days},
        )

        events = []
        # Sliding window: compute TDI on rolling 100-bar windows
        window_size = 100
        step = 5

        for i in range(window_size, len(df) - 20, step):
            window = df.iloc[i - window_size:i]
            tdi = compute_tdi(window)

            if not tdi.shark_fin_active:
                continue

            # Measure next 20 bars
            future = df.iloc[i:min(i + 20, len(df))]
            entry_price = float(window.iloc[-1]["Close"])

            if tdi.shark_fin_direction == "SHORT":
                max_profit = (entry_price - float(future["Low"].min())) / pip
                max_loss = (float(future["High"].max()) - entry_price) / pip
                direction = "SELL"
            else:
                max_profit = (float(future["High"].max()) - entry_price) / pip
                max_loss = (entry_price - float(future["Low"].min())) / pip
                direction = "BUY"

            hit = max_profit > max_loss and max_profit > 10
            rr = max_profit / max_loss if max_loss > 0 else 0

            event = RuleEvent(
                rule_name="tdi_shark_fin",
                symbol=symbol,
                event_time=window.index[-1].to_pydatetime(),
                direction=direction,
                outcome="HIT" if hit else "MISS",
                pips_result=max_profit if hit else -max_loss,
                rr_achieved=rr,
                details={
                    "shark_dir": tdi.shark_fin_direction,
                    "rsi": tdi.rsi,
                    "vb_width": tdi.vb_width,
                },
            )
            events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "HIT")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0
        result.avg_rr = float(np.mean([e.rr_achieved for e in events])) if events else 0

        result.notes = (
            f"Shark Fin reversal rate: {result.hit_rate:.1%} | "
            f"Avg RR: {result.avg_rr:.2f} | "
            f"Total signals: {result.occurrences}"
        )
        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: Session Produces Largest Move
    # ==================================================================

    def validate_session_moves(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: Which session produces the largest directional move?

        Per MMM, London should produce the biggest move.
        """
        pip = self._pip_size(symbol)
        df = self._fetch_data(symbol, "M15", days * 96 + 200)
        sessions = classify_sessions(df, pip)

        result = ValidationResult(
            rule_name="session_moves",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days},
        )

        session_moves = {"ASIA": [], "LONDON": [], "US": []}

        for date_str in sessions.asian_ranges:
            date = pd.Timestamp(date_str)
            day_mask = df.index.date == date.date()
            day_df = df[day_mask]
            if day_df.empty:
                continue

            labels = sessions.labels[day_mask]
            for sess_name in ["ASIA", "LONDON", "US"]:
                sess_bars = day_df[labels == sess_name]
                if sess_bars.empty:
                    continue
                move = (float(sess_bars["High"].max()) - float(sess_bars["Low"].min())) / pip
                session_moves[sess_name].append(move)

        avg_moves = {}
        for sess, moves in session_moves.items():
            avg_moves[sess] = float(np.mean(moves)) if moves else 0

        best_session = max(avg_moves, key=avg_moves.get)
        london_biggest = best_session == "LONDON"

        result.occurrences = len(sessions.asian_ranges)
        result.hits = 1 if london_biggest else 0
        result.hit_rate = 1.0 if london_biggest else 0.0
        result.best_session = best_session
        result.notes = (
            f"Avg session moves — Asia: {avg_moves.get('ASIA', 0):.0f}p, "
            f"London: {avg_moves.get('LONDON', 0):.0f}p, "
            f"NYC: {avg_moves.get('US', 0):.0f}p | "
            f"London biggest: {'YES' if london_biggest else 'NO'}"
        )
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: ADR Bounds The Day
    # ==================================================================

    def validate_adr_bounds(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: How often does price stay within the ADR range?"""
        pip = self._pip_size(symbol)
        df_d1 = self._fetch_data(symbol, "D1", days + 20)

        from helix_v3.core.tdi import _wilder_atr
        atr = _wilder_atr(df_d1["High"], df_d1["Low"], df_d1["Close"], 14)

        result = ValidationResult(
            rule_name="adr_bounds",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days},
        )

        events = []
        for i in range(15, len(df_d1)):
            bar = df_d1.iloc[i]
            adr_val = float(atr.iloc[i - 1])  # Previous day's ATR
            day_range = (float(bar["High"]) - float(bar["Low"]))
            within_adr = day_range <= adr_val * 1.1  # Allow 10% tolerance

            event = RuleEvent(
                rule_name="adr_bounds",
                symbol=symbol,
                event_time=bar.name.to_pydatetime(),
                outcome="WITHIN" if within_adr else "EXCEEDED",
                pips_result=day_range / pip,
                details={"adr_pips": adr_val / pip, "day_range_pips": day_range / pip},
            )
            events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "WITHIN")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0

        result.notes = f"Price within ADR: {result.hit_rate:.1%} ({result.hits}/{result.occurrences})"
        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: Pivot Day-Map M3/M1 Targeting (MMM-TRAIN-005)
    # ==================================================================

    def validate_pivot_day_map(
        self, symbol: str, days: int = 90,
    ) -> ValidationResult:
        """Test: Does prior-day candle color predict HOD zone via M3/M1 pivots?

        Per Steve Mauro (MMM-TRAIN-005):
        - Red prior candle → M1/M3 day (HOD between S2/S1 or PP/R1)
        - Green prior candle → M2/M4 day (HOD between S1/PP or R1/R2)

        Also tests: does targeting the pivot-projected zone improve TP accuracy
        versus a blind SL-multiple TP?
        """
        pip = self._pip_size(symbol)
        df_d1 = self._fetch_data(symbol, "D1", days + 20)

        from helix_v3.core.tdi import compute_pivots

        result = ValidationResult(
            rule_name="pivot_day_map",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days},
        )

        events = []
        m1m3_correct = 0
        m2m4_correct = 0
        m1m3_total = 0
        m2m4_total = 0
        pivot_tp_hits = 0
        blind_tp_hits = 0
        total_tested = 0

        for i in range(2, len(df_d1)):
            prev = df_d1.iloc[i - 1]
            curr = df_d1.iloc[i]

            prev_h = float(prev["High"])
            prev_l = float(prev["Low"])
            prev_c = float(prev["Close"])
            prev_o = float(prev["Open"])
            prev_bullish = prev_c > prev_o

            curr_h = float(curr["High"])
            curr_l = float(curr["Low"])

            pivots = compute_pivots(prev_h, prev_l, prev_c, prev_bullish)
            pp = pivots["PP"]
            m1 = pivots["M1"]  # (S2+S1)/2
            m2 = pivots["M2"]  # (S1+PP)/2
            m3 = pivots["M3"]  # (PP+R1)/2
            m4 = pivots["M4"]  # (R1+R2)/2
            day_type = pivots["day_type"]

            # Where did today's HOD actually land?
            hod = curr_h

            if day_type == "M1_M3":
                m1m3_total += 1
                # HOD should be in M1 zone (S2-S1) or M3 zone (PP-R1)
                in_m1_zone = pivots["S2"] <= hod <= pivots["S1"]
                in_m3_zone = pp <= hod <= pivots["R1"]
                if in_m1_zone or in_m3_zone:
                    m1m3_correct += 1
                    outcome = "CORRECT"
                else:
                    outcome = "WRONG"
            else:  # M2_M4
                m2m4_total += 1
                # HOD should be in M2 zone (S1-PP) or M4 zone (R1-R2)
                in_m2_zone = pivots["S1"] <= hod <= pp
                in_m4_zone = pivots["R1"] <= hod <= pivots["R2"]
                if in_m2_zone or in_m4_zone:
                    m2m4_correct += 1
                    outcome = "CORRECT"
                else:
                    outcome = "WRONG"

            # Test pivot-targeted TP vs blind TP
            # For a sell day (red prior): target is M1 from M3
            # For a buy day (green prior): target is M4 from M2
            total_tested += 1
            if not prev_bullish:
                # Sell day: did price travel from M3 zone down to M1?
                if curr_h >= m3 and curr_l <= m1:
                    pivot_tp_hits += 1
                # Blind TP: did price move > 1.5x ADR?
                day_range = (curr_h - curr_l) / pip
                if day_range > 50:  # rough proxy for "TP hit"
                    blind_tp_hits += 1
            else:
                # Buy day: did price travel from M2 zone up to M4?
                if curr_l <= m2 and curr_h >= m4:
                    pivot_tp_hits += 1
                day_range = (curr_h - curr_l) / pip
                if day_range > 50:
                    blind_tp_hits += 1

            event = RuleEvent(
                rule_name="pivot_day_map",
                symbol=symbol,
                event_time=curr.name.to_pydatetime(),
                direction=day_type,
                outcome=outcome,
                pips_result=(hod - pp) / pip,
                details={
                    "day_type": day_type,
                    "hod": hod,
                    "pp": pp,
                    "m1": m1, "m2": m2, "m3": m3, "m4": m4,
                    "prev_bullish": prev_bullish,
                },
            )
            events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "CORRECT")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0

        m1m3_rate = m1m3_correct / m1m3_total if m1m3_total > 0 else 0
        m2m4_rate = m2m4_correct / m2m4_total if m2m4_total > 0 else 0
        pivot_tp_rate = pivot_tp_hits / total_tested if total_tested > 0 else 0
        blind_tp_rate = blind_tp_hits / total_tested if total_tested > 0 else 0

        result.notes = (
            f"Day-type prediction: {result.hit_rate:.1%} overall | "
            f"M1/M3 days: {m1m3_rate:.1%} ({m1m3_correct}/{m1m3_total}) | "
            f"M2/M4 days: {m2m4_rate:.1%} ({m2m4_correct}/{m2m4_total}) | "
            f"Pivot TP hit: {pivot_tp_rate:.1%} vs blind: {blind_tp_rate:.1%}"
        )
        result.parameters["m1m3_rate"] = m1m3_rate
        result.parameters["m2m4_rate"] = m2m4_rate
        result.parameters["pivot_tp_rate"] = pivot_tp_rate
        result.parameters["blind_tp_rate"] = blind_tp_rate

        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Rule: Friday Exit Logic (MMM-TRAIN-007)
    # ==================================================================

    def validate_friday_exit(
        self, symbol: str, days: int = 180,
    ) -> ValidationResult:
        """Test: Does exiting positions on Friday US session reduce drawdowns?

        Per Steve Mauro (MMM-TRAIN-007):
        - Friday US session = exit context after level completion
        - Price consolidates toward end of week

        Compares: holding through Friday vs exiting at Friday 17:00 UTC.
        """
        pip = self._pip_size(symbol)
        df_d1 = self._fetch_data(symbol, "D1", days + 10)
        df_m15 = self._fetch_data(symbol, "M15", days * 96 + 200)

        result = ValidationResult(
            rule_name="friday_exit",
            symbol=symbol,
            test_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            parameters={"days": days},
        )

        events = []
        friday_exit_pnl = []
        hold_through_pnl = []

        # Find each Friday in the data
        for i in range(1, len(df_d1)):
            bar = df_d1.iloc[i]
            if bar.name.weekday() != 4:  # Not Friday
                continue

            # Get Monday's open for this week
            # Look back to find Monday (weekday 0)
            mon_idx = None
            for j in range(i, max(i - 7, 0), -1):
                if df_d1.iloc[j].name.weekday() == 0:
                    mon_idx = j
                    break
            if mon_idx is None:
                continue

            monday_open = float(df_d1.iloc[mon_idx]["Open"])
            friday_bar = df_d1.iloc[i]
            friday_close = float(friday_bar["Close"])

            # Scenario 1: Exit at Friday 17:00 UTC (US session wind-down)
            fri_date = friday_bar.name.date()
            fri_m15 = df_m15[df_m15.index.date == fri_date]
            fri_1700 = fri_m15[fri_m15.index.hour >= 17]
            if not fri_1700.empty:
                exit_at_1700 = float(fri_1700.iloc[0]["Close"])
            else:
                exit_at_1700 = friday_close

            # Scenario 2: Hold through to Monday open
            if i + 1 < len(df_d1):
                next_bar = df_d1.iloc[i + 1]
                monday_next_open = float(next_bar["Open"])
            else:
                monday_next_open = friday_close

            # Weekly move from Monday open
            week_move = (friday_close - monday_open) / pip
            fri_exit_move = (exit_at_1700 - monday_open) / pip
            hold_move = (monday_next_open - monday_open) / pip

            # Did Friday exit preserve more profit?
            # If the week was up, Friday exit should capture most of the move
            # without weekend gap risk
            if abs(week_move) > 10:  # Only count meaningful weeks
                fri_captured = fri_exit_move / week_move if week_move != 0 else 0
                hold_captured = hold_move / week_move if week_move != 0 else 0

                friday_better = abs(fri_exit_move) >= abs(hold_move)
                friday_exit_pnl.append(fri_exit_move)
                hold_through_pnl.append(hold_move)

                # Check Friday afternoon reversal (price gives back gains)
                fri_high = float(friday_bar["High"])
                fri_low = float(friday_bar["Low"])
                fri_open = float(friday_bar["Open"])
                friday_reversal = False
                if week_move > 0:
                    # Bullish week — did Friday give back gains?
                    friday_reversal = friday_close < fri_open and (fri_high - friday_close) / pip > 15
                else:
                    # Bearish week — did Friday bounce?
                    friday_reversal = friday_close > fri_open and (friday_close - fri_low) / pip > 15

                event = RuleEvent(
                    rule_name="friday_exit",
                    symbol=symbol,
                    event_time=friday_bar.name.to_pydatetime(),
                    direction="BULLISH_WEEK" if week_move > 0 else "BEARISH_WEEK",
                    outcome="FRIDAY_BETTER" if friday_better else "HOLD_BETTER",
                    pips_result=fri_exit_move - hold_move,
                    details={
                        "week_move": week_move,
                        "fri_exit_move": fri_exit_move,
                        "hold_move": hold_move,
                        "friday_reversal": friday_reversal,
                        "gap_cost": (monday_next_open - friday_close) / pip,
                    },
                )
                events.append(event)

        result.occurrences = len(events)
        result.hits = sum(1 for e in events if e.outcome == "FRIDAY_BETTER")
        result.misses = result.occurrences - result.hits
        result.hit_rate = result.hits / result.occurrences if result.occurrences > 0 else 0

        avg_fri = float(np.mean([abs(p) for p in friday_exit_pnl])) if friday_exit_pnl else 0
        avg_hold = float(np.mean([abs(p) for p in hold_through_pnl])) if hold_through_pnl else 0
        reversals = sum(1 for e in events if e.details.get("friday_reversal"))
        gap_costs = [abs(e.details.get("gap_cost", 0)) for e in events]
        avg_gap = float(np.mean(gap_costs)) if gap_costs else 0

        result.notes = (
            f"Friday exit better: {result.hit_rate:.1%} ({result.hits}/{result.occurrences}) | "
            f"Avg |move| fri exit: {avg_fri:.0f}p vs hold: {avg_hold:.0f}p | "
            f"Friday reversals: {reversals}/{result.occurrences} | "
            f"Avg weekend gap: {avg_gap:.1f}p"
        )
        result.parameters["avg_friday_exit_pips"] = avg_fri
        result.parameters["avg_hold_through_pips"] = avg_hold
        result.parameters["friday_reversal_count"] = reversals
        result.parameters["avg_gap_pips"] = avg_gap

        result.events = events
        self._save_result(result)
        return result

    # ==================================================================
    # Storage
    # ==================================================================

    def _save_result(self, r: ValidationResult) -> None:
        self._db.execute(
            """INSERT INTO validation_results
               (rule_name, symbol, test_date, occurrences, hits, misses,
                hit_rate, avg_rr, avg_time_min, best_session, parameters,
                notes, validated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                r.rule_name, r.symbol, r.test_date, r.occurrences, r.hits,
                r.misses, r.hit_rate, r.avg_rr, r.avg_time_min, r.best_session,
                json.dumps(r.parameters), r.notes,
                datetime.now(timezone.utc).isoformat(),
            ),
        )
        for e in r.events:
            self._db.execute(
                """INSERT INTO rule_events
                   (rule_name, symbol, event_time, direction, outcome,
                    pips_result, rr_achieved, time_to_outcome, session, details)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    e.rule_name, e.symbol,
                    e.event_time.isoformat() if isinstance(e.event_time, datetime) else str(e.event_time),
                    e.direction, e.outcome, e.pips_result, e.rr_achieved,
                    e.time_to_outcome, e.session, json.dumps(e.details),
                ),
            )
        self._db.commit()

    # ==================================================================
    # Run All Rules
    # ==================================================================

    ALL_RULES = [
        "asian_accumulation",
        "stop_hunt_range",
        "mw_direction",
        "midweek_reversal",
        "stale_exit_90min",
        "tdi_shark_fin",
        "session_moves",
        "adr_bounds",
        "pivot_day_map",
        "friday_exit",
    ]

    def run_all(
        self, symbol: str, days: int = 90,
    ) -> List[ValidationResult]:
        """Run all validation rules for a symbol."""
        results = []
        rule_methods = {
            "asian_accumulation": self.validate_asian_accumulation,
            "stop_hunt_range": self.validate_stop_hunt_range,
            "mw_direction": self.validate_mw_direction,
            "midweek_reversal": self.validate_midweek_reversal,
            "stale_exit_90min": self.validate_stale_exit,
            "tdi_shark_fin": self.validate_tdi_shark_fin,
            "session_moves": self.validate_session_moves,
            "adr_bounds": self.validate_adr_bounds,
            "pivot_day_map": self.validate_pivot_day_map,
            "friday_exit": self.validate_friday_exit,
        }

        for name, method in rule_methods.items():
            logger.info("Validating %s on %s (%d days)...", name, symbol, days)
            try:
                r = method(symbol, days)
                results.append(r)
                logger.info(
                    "  %s: %s — %s",
                    name, f"{r.hit_rate:.1%} ({r.hits}/{r.occurrences})", r.notes,
                )
            except Exception as e:
                logger.error("  %s: FAILED — %s", name, e)
        return results

    def generate_report(self) -> str:
        """Generate a summary report from all stored validation results."""
        cursor = self._db.execute(
            """SELECT rule_name, symbol, hit_rate, avg_rr, occurrences, notes
               FROM validation_results
               ORDER BY rule_name, symbol"""
        )
        rows = cursor.fetchall()

        lines = [
            "",
            "=" * 90,
            "  MMM RULE VALIDATION REPORT",
            f"  Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
            "=" * 90,
            "",
            f"  {'Rule':25} {'Pair':8} {'Hit Rate':>8} {'Avg RR':>7} {'N':>5}  Notes",
            "-" * 90,
        ]

        for row in rows:
            rule, sym, rate, rr, n, notes = row
            short_notes = notes[:50] if notes else ""
            lines.append(
                f"  {rule:25} {sym:8} {rate:>7.1%} {rr:>7.2f} {n:>5}  {short_notes}"
            )

        lines.append("")
        lines.append("=" * 90)

        # Status summary
        lines.append("")
        lines.append("  VALIDATION STATUS LEGEND:")
        lines.append("    VALIDATED   = hit_rate >= 60% with N >= 30")
        lines.append("    PARTIAL     = hit_rate 40-60% or N < 30")
        lines.append("    CONTRADICTED = hit_rate < 40% with N >= 30")
        lines.append("    UNTESTED    = no data")
        lines.append("")

        report = "\n".join(lines)
        return report

    def close(self) -> None:
        if self._engine:
            self._engine.disconnect()
        self._db.close()


# ==================================================================
# CLI Entry Point
# ==================================================================

def main():
    parser = argparse.ArgumentParser(description="MMM Rule Validator")
    parser.add_argument("--days", type=int, default=90, help="Lookback days")
    parser.add_argument("--pair", type=str, default=None, help="Specific pair (default: all)")
    parser.add_argument("--rule", type=str, default=None, help="Specific rule to test")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    args = parser.parse_args()

    validator = RuleValidator()

    try:
        if args.report:
            print(validator.generate_report())
            return

        pairs = [args.pair] if args.pair else list(PAIR_PROFILES.keys())

        for pair in pairs:
            print(f"\n{'='*60}")
            print(f"  Validating: {pair} ({args.days} days)")
            print(f"{'='*60}")

            if args.rule:
                method = getattr(validator, f"validate_{args.rule}", None)
                if method is None:
                    print(f"  Unknown rule: {args.rule}")
                    print(f"  Available: {', '.join(RuleValidator.ALL_RULES)}")
                    return
                r = method(pair, args.days)
                print(f"  {r.rule_name}: {r.hit_rate:.1%} ({r.hits}/{r.occurrences})")
                print(f"  {r.notes}")
            else:
                results = validator.run_all(pair, args.days)
                for r in results:
                    status = "VALIDATED" if r.hit_rate >= 0.6 and r.occurrences >= 30 else \
                             "PARTIAL" if r.hit_rate >= 0.4 or r.occurrences < 30 else \
                             "CONTRADICTED"
                    print(f"  [{status:12}] {r.rule_name:25} {r.hit_rate:>7.1%} ({r.hits}/{r.occurrences})")

        print("\n" + validator.generate_report())
    finally:
        validator.close()


if __name__ == "__main__":
    main()
