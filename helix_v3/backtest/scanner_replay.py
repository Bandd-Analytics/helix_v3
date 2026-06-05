"""Replay market-scanner rows into baseline and vision backtests.

This module is intentionally offline-only. It reads scanner snapshots, records
baseline predictions, and labels stored model predictions against future OHLC
bars. It does not place, modify, or close MT5 orders.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

import MetaTrader5 as mt5
import pandas as pd

from config.settings import settings
from helix_v3.backtest.vision_store import VisionBacktestStore, label_many_horizons
from helix_v3.consensus.validator import MMMConsensusValidator, PROMPT_VERSION
from helix_v3.core.quant_engine import TF_MAP
from helix_v3.core.types import Direction, VisionVerdict
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.chart_exporter import MMMChartVisualizer

logger = get_logger("scanner_replay")

SCANNER_DB_PATH = Path(settings.log_dir) / "market_scanner.db"
BASELINE_PROMPT_VERSION = "scanner_baseline_v1"


@dataclass(frozen=True)
class ScannerCandidate:
    id: int
    scan_time: datetime
    symbol: str
    timeframe: str
    bid: float
    ask: float
    spread_pips: float
    session: str
    bias: Direction
    trend: Direction
    trade_readiness: int
    readiness_notes: str
    stop_hunt_active: bool
    stop_hunt_direction: Direction
    stop_hunt_breach_pips: Optional[float]
    atr_14: Optional[float]

    @classmethod
    def from_row(cls, row: sqlite3.Row | dict[str, Any]) -> "ScannerCandidate":
        data = dict(row)
        return cls(
            id=int(data["id"]),
            scan_time=_parse_time(data["scan_time"]),
            symbol=str(data["symbol"]),
            timeframe=str(data["timeframe"]),
            bid=float(data["bid"] or 0.0),
            ask=float(data["ask"] or 0.0),
            spread_pips=float(data["spread_pips"] or 0.0),
            session=str(data.get("session") or ""),
            bias=_parse_direction(data.get("bias")),
            trend=_parse_direction(data.get("trend")),
            trade_readiness=int(data["trade_readiness"] or 0),
            readiness_notes=str(data.get("readiness_notes") or ""),
            stop_hunt_active=bool(data.get("stop_hunt_active")),
            stop_hunt_direction=_parse_direction(data.get("stop_hunt_direction")),
            stop_hunt_breach_pips=_optional_float(data.get("stop_hunt_breach_pips")),
            atr_14=_optional_float(data.get("atr_14")),
        )


class ScannerReplay:
    """Build and evaluate backtest candidates from scanner history."""

    def __init__(
        self,
        scanner_db_path: Optional[Path] = None,
        store: Optional[VisionBacktestStore] = None,
    ) -> None:
        self._scanner_db_path = scanner_db_path or SCANNER_DB_PATH
        self._store = store or VisionBacktestStore()
        self._owns_store = store is None
        self._conn = sqlite3.connect(str(self._scanner_db_path))
        self._conn.row_factory = sqlite3.Row

    def close(self) -> None:
        self._conn.close()
        if self._owns_store:
            self._store.close()

    def get_candidates(
        self,
        *,
        min_readiness: int = 50,
        timeframe: str = "M15",
        limit: int = 100,
        symbols: Optional[Iterable[str]] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
    ) -> list[ScannerCandidate]:
        clauses = ["trade_readiness >= ?", "timeframe = ?"]
        params: list[Any] = [min_readiness, timeframe]

        if symbols:
            symbol_list = list(symbols)
            placeholders = ", ".join("?" for _ in symbol_list)
            clauses.append(f"symbol IN ({placeholders})")
            params.extend(symbol_list)
        if since:
            clauses.append("scan_time >= ?")
            params.append(_to_utc(since).isoformat())
        if until:
            clauses.append("scan_time <= ?")
            params.append(_to_utc(until).isoformat())

        params.append(limit)
        sql = f"""SELECT * FROM market_scans
        WHERE {' AND '.join(clauses)}
        ORDER BY trade_readiness DESC, scan_time
        LIMIT ?"""
        rows = self._conn.execute(sql, params).fetchall()
        return [ScannerCandidate.from_row(row) for row in rows]

    def record_baseline_predictions(
        self,
        candidates: Iterable[ScannerCandidate],
        *,
        policy: str = "stop_hunt_then_bias",
    ) -> list[int]:
        prediction_ids: list[int] = []
        model_name = f"scanner:{policy}"

        for candidate in candidates:
            direction = baseline_direction(candidate, policy=policy)
            confidence = min(1.0, max(0.0, candidate.trade_readiness / 100.0))
            raw_json = {
                "source": "market_scanner",
                "policy": policy,
                "scan_id": candidate.id,
                "bid": candidate.bid,
                "ask": candidate.ask,
                "spread_pips": candidate.spread_pips,
                "session": candidate.session,
                "bias": candidate.bias.value,
                "trend": candidate.trend.value,
                "trade_readiness": candidate.trade_readiness,
                "readiness_notes": candidate.readiness_notes,
                "stop_hunt_active": candidate.stop_hunt_active,
                "stop_hunt_direction": candidate.stop_hunt_direction.value,
                "stop_hunt_breach_pips": candidate.stop_hunt_breach_pips,
                "atr_14": candidate.atr_14,
            }

            existing_id = self._store.find_prediction_id(
                source="market_scanner",
                source_scan_id=candidate.id,
                model_role=policy,
                model_name=model_name,
            )
            if existing_id is not None:
                prediction_ids.append(existing_id)
                continue

            verdict = VisionVerdict(
                model_name=model_name,
                direction=direction,
                confidence=confidence,
                cycle_level=None,
                m_w_detected=False,
                rrt_detected=False,
                pin_bar_detected=False,
                setup_class="SCANNER_READINESS",
                entry_quality=candidate.trade_readiness,
                risk_flags=[],
                expected_path="Baseline scanner direction; no visual model used.",
                invalidation="Evaluate by configured replay horizon and optional SL/TP.",
                reasoning=candidate.readiness_notes,
                raw_json=raw_json,
            )
            prediction_id = self._store.record_prediction(
                symbol=candidate.symbol,
                timeframe=candidate.timeframe,
                snapshot_at=candidate.scan_time,
                provider="baseline",
                model_role=policy,
                verdict=verdict,
                prompt_version=BASELINE_PROMPT_VERSION,
                source="market_scanner",
                source_scan_id=candidate.id,
            )
            prediction_ids.append(prediction_id)

        return prediction_ids

    async def record_openai_vision_predictions(
        self,
        candidates: Iterable[ScannerCandidate],
        *,
        lookback_bars: int = 240,
    ) -> list[int]:
        if not settings.api.openai_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not configured. ChatGPT/Codex login cannot be used "
                "as an OpenAI API key by this Python process."
            )

        validator = MMMConsensusValidator(mode="openai")
        prediction_ids: list[int] = []
        for candidate in candidates:
            model_name = f"openai:structured_arbitrator:{settings.api.openai_model}"
            existing_id = self._store.find_prediction_id(
                source="market_scanner",
                source_scan_id=candidate.id,
                model_role="structured_arbitrator",
                model_name=model_name,
            )
            if existing_id is not None:
                prediction_ids.append(existing_id)
                continue

            image_b64, chart_path = self.render_candidate_chart(
                candidate,
                lookback_bars=lookback_bars,
            )
            consensus = await validator.evaluate(
                image_b64,
                candidate.symbol,
                candidate.timeframe,
            )
            if not consensus.verdicts:
                continue

            verdict = consensus.verdicts[0]
            prediction_id = self._store.record_prediction(
                symbol=candidate.symbol,
                timeframe=candidate.timeframe,
                snapshot_at=candidate.scan_time,
                provider="openai",
                model_role="structured_arbitrator",
                verdict=verdict,
                prompt_version=PROMPT_VERSION,
                chart_path=str(chart_path) if chart_path else None,
                source="market_scanner",
                source_scan_id=candidate.id,
            )
            prediction_ids.append(prediction_id)

        return prediction_ids

    def render_candidate_chart(
        self,
        candidate: ScannerCandidate,
        *,
        lookback_bars: int = 240,
    ) -> tuple[str, Optional[Path]]:
        minutes = _timeframe_minutes(candidate.timeframe)
        start = candidate.scan_time - timedelta(minutes=minutes * lookback_bars)
        df = fetch_rates_range(candidate.symbol, candidate.timeframe, start, candidate.scan_time)
        visualizer = MMMChartVisualizer()
        return visualizer.export_vision_matrix(
            df,
            candidate.symbol,
            candidate.timeframe,
            save_to_disk=True,
        )

    def evaluate_pending_predictions(
        self,
        *,
        horizons: Iterable[int] = (30, 90, 240),
        limit: int = 100,
        stop_loss_pips: Optional[float] = None,
        take_profit_pips: Optional[float] = None,
        include_evaluated: bool = False,
    ) -> int:
        predictions = self._store.get_predictions(
            status=None if include_evaluated else "PENDING",
            limit=limit,
        )
        if not predictions:
            return 0

        horizon_list = list(horizons)
        max_horizon = max(horizon_list)
        evaluated = 0

        for prediction in predictions:
            direction = _parse_direction(prediction["direction"])
            snapshot_at = _parse_time(prediction["snapshot_at"])
            raw_json = _load_raw_json(prediction.get("raw_json"))
            entry_price = _entry_price_from_prediction(prediction, raw_json)

            df = fetch_rates_range(
                str(prediction["symbol"]),
                str(prediction["timeframe"]),
                snapshot_at - timedelta(minutes=_timeframe_minutes(str(prediction["timeframe"]))),
                snapshot_at + timedelta(minutes=max_horizon),
            )
            if entry_price is None:
                entry_price = _nearest_close(df, snapshot_at)
            if entry_price is None:
                logger.warning("No entry price available for prediction #%s", prediction["id"])
                continue

            pip_size = get_pip_size(str(prediction["symbol"]))
            outcomes = label_many_horizons(
                df,
                snapshot_at=snapshot_at,
                direction=direction,
                entry_price=entry_price,
                pip_size=pip_size,
                horizons=horizon_list,
                stop_loss_pips=stop_loss_pips,
                take_profit_pips=take_profit_pips,
            )
            for outcome in outcomes:
                self._store.record_outcome(int(prediction["id"]), outcome)
            evaluated += 1

        return evaluated

    def performance_report(self, horizon_minutes: int = 90) -> str:
        rows = self._store.summarize_performance(horizon_minutes=horizon_minutes)
        if not rows:
            return f"No evaluated predictions for {horizon_minutes}m horizon."

        lines = [
            "",
            "=" * 88,
            f"  HELIX V3 VISION/BACKTEST PERFORMANCE | Horizon {horizon_minutes}m",
            "=" * 88,
            f"  {'Provider':<10} {'Role':<22} {'Model':<24} {'N':>5} {'Fav%':>7} "
            f"{'AvgP':>8} {'MFE':>8} {'MAE':>8}",
            "-" * 88,
        ]
        for row in rows:
            lines.append(
                f"  {row['provider']:<10} {row['model_role']:<22} "
                f"{row['model_name'][:24]:<24} {row['total']:>5} "
                f"{row['favorable_rate']:>6.1f}% "
                f"{_fmt(row['avg_pips']):>8} {_fmt(row['avg_mfe']):>8} {_fmt(row['avg_mae']):>8}"
            )
        lines.append("=" * 88)
        return "\n".join(lines)


def baseline_direction(candidate: ScannerCandidate, *, policy: str) -> Direction:
    if policy == "bias":
        return candidate.bias
    if policy == "trend":
        return candidate.trend
    if policy == "stop_hunt":
        return candidate.stop_hunt_direction if candidate.stop_hunt_active else Direction.NEUTRAL
    if policy == "stop_hunt_then_bias":
        return candidate.stop_hunt_direction if candidate.stop_hunt_active else candidate.bias
    raise ValueError(f"Unknown baseline policy: {policy}")


def connect_mt5() -> bool:
    mt5_cfg = settings.mt5
    init_kwargs: dict[str, Any] = {}
    if mt5_cfg.path:
        init_kwargs["path"] = mt5_cfg.path
    if mt5_cfg.login:
        init_kwargs["login"] = mt5_cfg.login
        init_kwargs["password"] = mt5_cfg.password
        init_kwargs["server"] = mt5_cfg.server
    if not mt5.initialize(**init_kwargs):
        logger.error("MT5 initialization failed: %s", mt5.last_error())
        return False
    return True


def disconnect_mt5() -> None:
    mt5.shutdown()


def fetch_rates_range(
    symbol: str,
    timeframe: str,
    start: datetime,
    end: datetime,
) -> pd.DataFrame:
    tf = TF_MAP.get(timeframe)
    if tf is None:
        raise ValueError(f"Unsupported timeframe: {timeframe}")
    rates = mt5.copy_rates_range(symbol, tf, _to_utc(start), _to_utc(end))
    if rates is None or len(rates) == 0:
        error = mt5.last_error()
        raise ConnectionError(f"MT5 range fetch failed for {symbol} {timeframe}: {error}")
    return _rates_to_df(rates)


def get_pip_size(symbol: str) -> float:
    info = mt5.symbol_info(symbol)
    if info is not None:
        return info.point * (10 if info.digits in (3, 5) else 1)
    if "JPY" in symbol:
        return 0.01
    if symbol.startswith("XAU"):
        return 0.1
    return 0.0001


def _rates_to_df(rates: Any) -> pd.DataFrame:
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df.set_index("time", inplace=True)
    df.rename(
        columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "tick_volume": "Volume",
        },
        inplace=True,
    )
    return df


def _entry_price_from_prediction(
    prediction: dict[str, Any], raw_json: dict[str, Any]
) -> Optional[float]:
    direction = _parse_direction(prediction["direction"])
    if direction == Direction.BUY and raw_json.get("ask"):
        return float(raw_json["ask"])
    if direction == Direction.SELL and raw_json.get("bid"):
        return float(raw_json["bid"])
    return None


def _nearest_close(df: pd.DataFrame, snapshot_at: datetime) -> Optional[float]:
    if df.empty:
        return None
    snap = pd.Timestamp(snapshot_at)
    if snap.tzinfo is None and df.index.tz is not None:
        snap = snap.tz_localize(timezone.utc)
    elif snap.tzinfo is not None and df.index.tz is None:
        snap = snap.tz_convert(timezone.utc).tz_localize(None)
    past = df[df.index <= snap]
    if past.empty:
        return float(df["Open"].iloc[0])
    return float(past["Close"].iloc[-1])


def _load_raw_json(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if not value:
        return {}
    try:
        parsed = json.loads(str(value))
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _parse_direction(value: Any) -> Direction:
    try:
        return Direction(str(value or "NEUTRAL").upper())
    except ValueError:
        return Direction.NEUTRAL


def _parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return _to_utc(dt)


def _to_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _timeframe_minutes(timeframe: str) -> int:
    mapping = {"M1": 1, "M5": 5, "M15": 15, "M30": 30, "H1": 60, "H4": 240, "D1": 1440}
    if timeframe not in mapping:
        raise ValueError(f"Unsupported timeframe: {timeframe}")
    return mapping[timeframe]


def _fmt(value: Any) -> str:
    return "-" if value is None else f"{float(value):+.1f}"


def _parse_horizons(raw: str) -> tuple[int, ...]:
    return tuple(int(part.strip()) for part in raw.split(",") if part.strip())


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Offline scanner/vision backtest replay")
    sub = parser.add_subparsers(dest="command", required=True)

    p_candidates = sub.add_parser("candidates", help="Show scanner candidates")
    p_candidates.add_argument("--min-readiness", type=int, default=50)
    p_candidates.add_argument("--timeframe", default="M15")
    p_candidates.add_argument("--limit", type=int, default=20)

    p_baseline = sub.add_parser("baseline", help="Record scanner baseline predictions")
    p_baseline.add_argument("--min-readiness", type=int, default=50)
    p_baseline.add_argument("--timeframe", default="M15")
    p_baseline.add_argument("--limit", type=int, default=100)
    p_baseline.add_argument(
        "--policy",
        default="stop_hunt_then_bias",
        choices=("bias", "trend", "stop_hunt", "stop_hunt_then_bias"),
    )

    p_openai = sub.add_parser("openai", help="Record OpenAI vision predictions for scanner candidates")
    p_openai.add_argument("--min-readiness", type=int, default=50)
    p_openai.add_argument("--timeframe", default="M15")
    p_openai.add_argument("--limit", type=int, default=20)
    p_openai.add_argument("--lookback-bars", type=int, default=240)

    p_eval = sub.add_parser("evaluate", help="Evaluate pending predictions with MT5 history")
    p_eval.add_argument("--limit", type=int, default=100)
    p_eval.add_argument("--horizons", default="30,90,240")
    p_eval.add_argument("--sl-pips", type=float)
    p_eval.add_argument("--tp-pips", type=float)
    p_eval.add_argument("--all", action="store_true", help="Re-evaluate already labeled rows")

    p_report = sub.add_parser("report", help="Show performance summary")
    p_report.add_argument("--horizon", type=int, default=90)

    args = parser.parse_args(argv)
    replay = ScannerReplay()
    try:
        if args.command == "candidates":
            candidates = replay.get_candidates(
                min_readiness=args.min_readiness,
                timeframe=args.timeframe,
                limit=args.limit,
            )
            for candidate in candidates:
                print(
                    f"#{candidate.id} {candidate.scan_time.isoformat()} "
                    f"{candidate.symbol} {candidate.timeframe} ready={candidate.trade_readiness} "
                    f"bias={candidate.bias.value} hunt={candidate.stop_hunt_direction.value}"
                )
        elif args.command == "baseline":
            candidates = replay.get_candidates(
                min_readiness=args.min_readiness,
                timeframe=args.timeframe,
                limit=args.limit,
            )
            ids = replay.record_baseline_predictions(candidates, policy=args.policy)
            print(f"Recorded/reused {len(ids)} baseline predictions.")
        elif args.command == "openai":
            import asyncio

            if not settings.api.openai_key:
                print(
                    "OPENAI_API_KEY is not configured. ChatGPT/Codex login cannot be used "
                    "as an OpenAI API key by this Python process."
                )
                raise SystemExit(2)
            if not connect_mt5():
                raise SystemExit(1)
            try:
                candidates = replay.get_candidates(
                    min_readiness=args.min_readiness,
                    timeframe=args.timeframe,
                    limit=args.limit,
                )
                ids = asyncio.run(
                    replay.record_openai_vision_predictions(
                        candidates,
                        lookback_bars=args.lookback_bars,
                    )
                )
            finally:
                disconnect_mt5()
            print(f"Recorded/reused {len(ids)} OpenAI vision predictions.")
        elif args.command == "evaluate":
            if not connect_mt5():
                raise SystemExit(1)
            try:
                evaluated = replay.evaluate_pending_predictions(
                    horizons=_parse_horizons(args.horizons),
                    limit=args.limit,
                    stop_loss_pips=args.sl_pips,
                    take_profit_pips=args.tp_pips,
                    include_evaluated=args.all,
                )
            finally:
                disconnect_mt5()
            print(f"Evaluated {evaluated} predictions.")
        elif args.command == "report":
            print(replay.performance_report(horizon_minutes=args.horizon))
    finally:
        replay.close()


if __name__ == "__main__":
    main()
