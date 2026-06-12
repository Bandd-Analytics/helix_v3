"""MarketScanner - 15-minute recurring market condition evaluator.

Scans all configured pairs every 15 minutes and records:
- EMA alignment and angles
- Session state (Asian accumulation, London expansion, NY overlap)
- Volatility regime (compression vs expansion)
- Stop-hunt proximity
- Overall bias and trade readiness score

Persists to SQLite for trend analysis and entry/exit decision support.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import MetaTrader5 as mt5
import numpy as np

from config.settings import settings
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.types import Direction
from helix_v3.utils.logger import get_logger

logger = get_logger("market_scanner")

DB_PATH = Path(settings.log_dir) / "market_scanner.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS market_scans (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_time       TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    timeframe       TEXT NOT NULL,

    -- Price
    bid             REAL,
    ask             REAL,
    spread_pips     REAL,

    -- Session State
    session         TEXT,
    session_high    REAL,
    session_low     REAL,
    session_range   REAL,
    vol_compression REAL,
    is_accumulation INTEGER,

    -- Stop Hunt Proximity
    dist_above_session_high REAL,
    dist_below_session_low  REAL,
    stop_hunt_active        INTEGER,
    stop_hunt_direction     TEXT,
    stop_hunt_breach_pips   REAL,
    stop_hunt_zscore        REAL,

    -- EMA State
    ema_5           REAL,
    ema_13          REAL,
    ema_50          REAL,
    ema_200         REAL,
    ema_800         REAL,
    ema_5_angle     REAL,
    ema_13_angle    REAL,
    ema_50_angle    REAL,
    ema_200_angle   REAL,
    ema_800_angle   REAL,
    fast_slow_div   REAL,
    ema_stack_order TEXT,
    trend           TEXT,

    -- Bias & Readiness
    bias            TEXT,
    bias_strength   REAL,
    trade_readiness INTEGER,
    readiness_notes TEXT,

    -- ATR
    atr_14          REAL,
    atr_percentile  REAL
);

CREATE INDEX IF NOT EXISTS idx_scans_time ON market_scans(scan_time);
CREATE INDEX IF NOT EXISTS idx_scans_symbol ON market_scans(symbol);
CREATE INDEX IF NOT EXISTS idx_scans_readiness ON market_scans(trade_readiness);
"""


def _get_session_name() -> str:
    """Current trading session label (delegates to the market_time canon)."""
    from helix_v3.core.market_time import session_name_at
    return session_name_at(datetime.now(timezone.utc))


class MarketScanner:
    """Recurring market condition evaluator.

    Runs every 15 minutes to capture market state snapshots.
    Computes a 0-100 trade readiness score based on:
    - Session timing (Asian accumulation = higher readiness)
    - Volatility compression (tight range = setup forming)
    - EMA alignment (strong stack = higher confidence)
    - Stop-hunt proximity (near session bounds = opportunity)
    """

    def __init__(self, engine: MMMQuantitativeEngine) -> None:
        self._engine = engine
        self._db_path = DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()
        logger.info("Market scanner initialized: %s", self._db_path)

    def close(self) -> None:
        self._conn.close()

    def scan_all(self) -> List[Dict[str, Any]]:
        """Scan all configured symbols on all timeframes. Returns list of scan results."""
        results = []
        for symbol in settings.trading.symbols:
            for tf in settings.trading.timeframes:
                try:
                    result = self._scan_symbol(symbol, tf)
                    results.append(result)
                except Exception as e:
                    logger.error("Scan failed for %s %s: %s", symbol, tf, e)
        return results

    def _scan_symbol(self, symbol: str, timeframe: str) -> Dict[str, Any]:
        now = datetime.now(timezone.utc)
        session = _get_session_name()

        # Fetch tick
        tick = mt5.symbol_info_tick(symbol)
        sym_info = mt5.symbol_info(symbol)
        pip_size = sym_info.point * (10 if sym_info.digits in (3, 5) else 1) if sym_info else 0.0001
        bid = tick.bid if tick else 0
        ask = tick.ask if tick else 0
        spread = (ask - bid) / pip_size if pip_size else 0

        # Quant signal
        signal = self._engine.generate_signal(symbol, timeframe)
        ev = signal.ema_vector

        # Current EMA values
        df = self._engine.fetch_rates(symbol, timeframe, count=1000)
        closes = df["Close"]
        ema_vals = {}
        for p in settings.trading.ema_periods:
            s = closes.ewm(span=p, adjust=False).mean()
            ema_vals[p] = float(s.iloc[-1])

        # ATR
        highs = df["High"].values
        lows = df["Low"].values
        close_arr = df["Close"].values
        tr = np.maximum(
            highs[1:] - lows[1:],
            np.maximum(
                np.abs(highs[1:] - close_arr[:-1]),
                np.abs(lows[1:] - close_arr[:-1]),
            ),
        )
        atr_14 = float(np.mean(tr[-14:])) / pip_size if len(tr) >= 14 else 0

        # ATR percentile (vs last 100 periods)
        atr_series = []
        for i in range(max(0, len(tr) - 100), len(tr)):
            start = max(0, i - 14)
            atr_series.append(np.mean(tr[start : i + 1]))
        atr_pct = float(np.searchsorted(sorted(atr_series), atr_14) / len(atr_series) * 100) if atr_series else 50

        # EMA stack order
        ordered = sorted(ema_vals.items(), key=lambda x: x[1], reverse=True)
        stack = ">".join(str(p) for p, _ in ordered)

        # Session bounds
        sb = signal.session_bounds
        dist_above = (bid - sb.high) / pip_size if sb and bid > sb.high else 0
        dist_below = (sb.low - bid) / pip_size if sb and bid < sb.low else 0

        # Stop hunt
        sh = signal.stop_hunt

        # Bias strength: 0-1 based on EMA alignment
        angles = [ev.ema_5_angle, ev.ema_13_angle, ev.ema_50_angle, ev.ema_200_angle, ev.ema_800_angle]
        all_bullish = all(a > 0 for a in angles)
        all_bearish = all(a < 0 for a in angles)
        if all_bullish:
            bias = "BUY"
            bias_strength = min(1.0, abs(sum(angles)) / 5)
        elif all_bearish:
            bias = "SELL"
            bias_strength = min(1.0, abs(sum(angles)) / 5)
        else:
            bias = "NEUTRAL"
            bias_strength = 0.0

        # Trade readiness score (0-100)
        readiness = 0
        notes = []

        # Session timing (max 25 pts)
        if session in ("ASIAN_EARLY", "ASIAN_LATE"):
            readiness += 15
            notes.append("Asian session (accumulation window)")
        elif session == "LONDON_PREMARKET":
            readiness += 25
            notes.append("London pre-market (prime setup window)")
        elif session == "LONDON":
            readiness += 20
            notes.append("London session (execution window)")
        elif session == "NY_OVERLAP":
            readiness += 15
            notes.append("NY overlap")

        # Accumulation (max 25 pts)
        if sb and sb.is_accumulation:
            readiness += 25
            notes.append(f"Accumulation active (vol={sb.volatility_compression:.2f})")
        elif sb and sb.volatility_compression < 0.5:
            readiness += 15
            notes.append(f"Low volatility (vol={sb.volatility_compression:.2f})")

        # EMA alignment (max 25 pts)
        if all_bullish or all_bearish:
            readiness += 25
            notes.append(f"Full EMA stack alignment ({bias})")
        elif abs(ev.fast_slow_divergence) > 1:
            readiness += 10
            notes.append(f"EMA divergence present (div={ev.fast_slow_divergence:.2f})")

        # Stop hunt (max 25 pts)
        if sh and sh.is_absorption:
            readiness += 25
            notes.append(f"Stop hunt + absorption ({sh.direction.value} {sh.breach_pips:.1f} pips)")
        elif sh:
            readiness += 15
            notes.append(f"Stop hunt detected ({sh.direction.value} {sh.breach_pips:.1f} pips)")

        readiness = min(100, readiness)

        row = {
            "scan_time": now.isoformat(),
            "symbol": symbol,
            "timeframe": timeframe,
            "bid": bid,
            "ask": ask,
            "spread_pips": spread,
            "session": session,
            "session_high": sb.high if sb else None,
            "session_low": sb.low if sb else None,
            "session_range": sb.range_pips if sb else None,
            "vol_compression": sb.volatility_compression if sb else None,
            "is_accumulation": int(sb.is_accumulation) if sb else 0,
            "dist_above_session_high": dist_above,
            "dist_below_session_low": dist_below,
            "stop_hunt_active": int(sh is not None),
            "stop_hunt_direction": sh.direction.value if sh else None,
            "stop_hunt_breach_pips": sh.breach_pips if sh else None,
            "stop_hunt_zscore": sh.z_score if sh else None,
            "ema_5": ema_vals.get(5),
            "ema_13": ema_vals.get(13),
            "ema_50": ema_vals.get(50),
            "ema_200": ema_vals.get(200),
            "ema_800": ema_vals.get(800),
            "ema_5_angle": ev.ema_5_angle,
            "ema_13_angle": ev.ema_13_angle,
            "ema_50_angle": ev.ema_50_angle,
            "ema_200_angle": ev.ema_200_angle,
            "ema_800_angle": ev.ema_800_angle,
            "fast_slow_div": ev.fast_slow_divergence,
            "ema_stack_order": stack,
            "trend": ev.trend_alignment.value,
            "bias": bias,
            "bias_strength": bias_strength,
            "trade_readiness": readiness,
            "readiness_notes": "; ".join(notes),
            "atr_14": atr_14,
            "atr_percentile": atr_pct,
        }

        # Persist
        cols = ", ".join(row.keys())
        placeholders = ", ".join("?" for _ in row)
        self._conn.execute(
            f"INSERT INTO market_scans ({cols}) VALUES ({placeholders})",
            tuple(row.values()),
        )
        self._conn.commit()

        if readiness >= 50:
            logger.info(
                "SCAN %s %s: readiness=%d bias=%s session=%s | %s",
                symbol, timeframe, readiness, bias, session, "; ".join(notes),
            )

        return row

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_latest_scans(self) -> List[Dict[str, Any]]:
        """Get the most recent scan for each symbol/timeframe pair."""
        rows = self._conn.execute(
            """SELECT * FROM market_scans
            WHERE id IN (
                SELECT MAX(id) FROM market_scans GROUP BY symbol, timeframe
            )
            ORDER BY trade_readiness DESC"""
        ).fetchall()
        return [dict(r) for r in rows]

    def get_scan_history(self, symbol: str, timeframe: str, hours: int = 24) -> List[Dict[str, Any]]:
        cutoff = (datetime.now(timezone.utc) - timedelta(hours=hours)).isoformat()
        rows = self._conn.execute(
            "SELECT * FROM market_scans WHERE symbol = ? AND timeframe = ? AND scan_time > ? ORDER BY scan_time",
            (symbol, timeframe, cutoff),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_high_readiness(self, min_score: int = 50) -> List[Dict[str, Any]]:
        """Get latest scans with readiness above threshold."""
        latest = self.get_latest_scans()
        return [s for s in latest if s["trade_readiness"] >= min_score]

    def print_dashboard(self) -> str:
        """Return a formatted market conditions dashboard."""
        scans = self.get_latest_scans()
        if not scans:
            return "No scans recorded yet."

        session = _get_session_name()
        lines = [
            "",
            "=" * 90,
            f"  HELIX V3 MARKET DASHBOARD | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | Session: {session}",
            "=" * 90,
            "",
            f"  {'Symbol':8} {'TF':4} {'Bid':>10} {'Spread':>6} {'Bias':8} {'Trend':8} "
            f"{'Ready':>5} {'ATR':>6} {'SessRng':>7} {'VolComp':>7} {'StopHunt':10} {'Notes'}",
            "-" * 90,
        ]

        for s in scans:
            sh_str = f"{s['stop_hunt_direction']} {s['stop_hunt_breach_pips']:.0f}p" if s["stop_hunt_active"] else "-"
            sess_rng = f"{s['session_range']:.0f}p" if s["session_range"] else "-"
            vol = f"{s['vol_compression']:.2f}" if s["vol_compression"] else "-"
            notes = s["readiness_notes"][:30] if s["readiness_notes"] else ""

            ready_indicator = ""
            if s["trade_readiness"] >= 75:
                ready_indicator = "***"
            elif s["trade_readiness"] >= 50:
                ready_indicator = "**"
            elif s["trade_readiness"] >= 25:
                ready_indicator = "*"

            lines.append(
                f"  {s['symbol']:8} {s['timeframe']:4} {s['bid']:>10.5f} "
                f"{s['spread_pips']:>5.1f}p {s['bias']:8} {s['trend']:8} "
                f"{s['trade_readiness']:>3}{ready_indicator:<2} "
                f"{s['atr_14']:>5.0f}p {sess_rng:>7} {vol:>7} "
                f"{sh_str:10} {notes}"
            )

        lines.append("")
        lines.append("  Readiness: *** = 75+ (prime) | ** = 50+ (watch) | * = 25+ (forming)")
        lines.append("=" * 90)

        return "\n".join(lines)
