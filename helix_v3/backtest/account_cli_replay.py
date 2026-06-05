"""Account-backed vision replay through Codex and Claude Code CLIs.

This path intentionally avoids API keys. It uses the user's authenticated
ChatGPT/Codex and Claude Code sessions to analyze rendered chart images, then
stores the verdicts in the same `vision_backtests.db` used by API and baseline
backtests.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional

from helix_v3.backtest.scanner_replay import (
    ScannerCandidate,
    ScannerReplay,
    connect_mt5,
    disconnect_mt5,
)
from helix_v3.consensus.validator import PROMPT_VERSION
from helix_v3.core.types import CycleLevel, Direction, VisionVerdict
from helix_v3.utils.logger import get_logger

logger = get_logger("account_cli_replay")

BASE_DIR = Path(__file__).resolve().parents[2]
SCHEMA_PATH = Path(__file__).with_name("mmm_vision_verdict.schema.json")

VISION_PROMPT = """Analyze the attached MMM trading chart.

Return only one JSON object with these exact fields:
direction, confidence, cycle_level, m_w_detected, rrt_detected, pin_bar_detected,
setup_class, entry_quality, risk_flags, expected_path, invalidation, reasoning.

Do not include markdown or prose outside the JSON object.
Use only BUY, SELL, or NEUTRAL for direction.
Use confidence as 0.0-1.0, not 0-100.
Use cycle_level as 0, 1, 2, or 3.
Use entry_quality as an integer from 0-100.

Interpret direction as the expected trade direction from this chart state, not the prior trend.

Use these MMM concepts:
- Asian range compression and stop hunt reversal logic
- M/W formation, Railroad Tracks, pin bars, spike candles
- EMA stack and 800 EMA cycle anchor
- Level 1/2/3 market-maker cycle position
- Risk flags for late entry, weak reversal evidence, conflicting EMA structure, excessive extension, or no clean entry.

The output will be backtested, so be calibrated and conservative. Use NEUTRAL when the chart does not show a tradeable edge.
"""


@dataclass(frozen=True)
class CliProvider:
    name: str
    model_role: str
    model_name: str


CODEX_PROVIDER = CliProvider(
    name="codex",
    model_role="chatgpt_pro_vision",
    model_name="codex:chatgpt_pro",
)

CLAUDE_PROVIDER = CliProvider(
    name="claude",
    model_role="claude_max_vision",
    model_name="claude:claude_max",
)


class AccountCliReplay:
    """Run scanner candidates through account-backed local CLIs."""

    def __init__(self, replay: Optional[ScannerReplay] = None) -> None:
        self._replay = replay or ScannerReplay()
        self._owns_replay = replay is None

    def close(self) -> None:
        if self._owns_replay:
            self._replay.close()

    def record_predictions(
        self,
        provider: CliProvider,
        candidates: Iterable[ScannerCandidate],
        *,
        lookback_bars: int = 240,
    ) -> list[int]:
        prediction_ids: list[int] = []
        for candidate in candidates:
            existing_id = self._replay._store.find_prediction_id(
                source="market_scanner",
                source_scan_id=candidate.id,
                model_role=provider.model_role,
                model_name=provider.model_name,
            )
            if existing_id is not None:
                prediction_ids.append(existing_id)
                continue

            _, chart_path = self._replay.render_candidate_chart(
                candidate,
                lookback_bars=lookback_bars,
            )
            if chart_path is None:
                logger.warning("No chart path rendered for scanner row #%d", candidate.id)
                continue

            verdict_json = run_cli_verdict(provider, chart_path)
            verdict = verdict_from_json(provider.model_name, verdict_json)
            prediction_id = self._replay._store.record_prediction(
                symbol=candidate.symbol,
                timeframe=candidate.timeframe,
                snapshot_at=candidate.scan_time,
                provider=provider.name,
                model_role=provider.model_role,
                verdict=verdict,
                prompt_version=PROMPT_VERSION,
                chart_path=str(chart_path),
                source="market_scanner",
                source_scan_id=candidate.id,
            )
            prediction_ids.append(prediction_id)

        return prediction_ids


def run_cli_verdict(provider: CliProvider, chart_path: Path) -> dict[str, Any]:
    if provider.name == "codex":
        return run_codex_verdict(chart_path)
    if provider.name == "claude":
        return run_claude_verdict(chart_path)
    raise ValueError(f"Unsupported CLI provider: {provider.name}")


def run_codex_verdict(chart_path: Path) -> dict[str, Any]:
    command = [
        _resolve_executable("codex"),
        "exec",
        "--cd",
        str(BASE_DIR),
        "--sandbox",
        "read-only",
        "--output-schema",
        str(SCHEMA_PATH),
        f"--image={chart_path}",
        VISION_PROMPT,
    ]
    return _run_json_command(command)


def run_claude_verdict(chart_path: Path) -> dict[str, Any]:
    prompt = (
        f"Use the Read tool to inspect this local chart image first: {chart_path}\n\n"
        f"{VISION_PROMPT.replace('the attached MMM trading chart', 'the local MMM trading chart image')}\n"
    )
    command = [
        _resolve_executable("claude"),
        "--print",
        "--model",
        "opus",
        "--system-prompt",
        "You are a strict JSON API. Output only a single JSON object. The first character must be { and the last character must be }. Do not use markdown.",
        "--permission-mode",
        "dontAsk",
        "--tools=Read",
        prompt,
    ]
    return _run_json_command(command)


def verdict_from_json(model_name: str, data: dict[str, Any]) -> VisionVerdict:
    return VisionVerdict(
        model_name=model_name,
        direction=_parse_direction(data.get("direction")),
        confidence=_safe_float(data.get("confidence")),
        cycle_level=_parse_cycle_level(data.get("cycle_level")),
        m_w_detected=bool(data.get("m_w_detected", False)),
        rrt_detected=bool(data.get("rrt_detected", False)),
        pin_bar_detected=bool(data.get("pin_bar_detected", False)),
        setup_class=str(data.get("setup_class", "UNKNOWN")),
        entry_quality=_parse_entry_quality(data.get("entry_quality")),
        risk_flags=[str(item) for item in data.get("risk_flags", [])],
        expected_path=str(data.get("expected_path", "")),
        invalidation=str(data.get("invalidation", "")),
        reasoning=str(data.get("reasoning", "")),
        raw_json=data,
    )


def _run_json_command(command: list[str]) -> dict[str, Any]:
    result = subprocess.run(
        command,
        cwd=str(BASE_DIR),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=300,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"CLI verdict command failed with code {result.returncode}: "
            f"{result.stderr.strip() or result.stdout.strip()}"
        )
    return _extract_json(result.stdout)


def _resolve_executable(name: str) -> str:
    for candidate in (name, f"{name}.cmd", f"{name}.exe"):
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    raise FileNotFoundError(f"Unable to find executable for {name}")


def _extract_json(raw: str) -> dict[str, Any]:
    text = raw.strip()
    if not text:
        raise ValueError("CLI returned no output")
    if text.startswith("```"):
        text = text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end < start:
        return _fallback_json_from_text(raw)

    text = text[start : end + 1]
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        preview = raw.strip().replace("\n", " ")[:500]
        logger.warning("Unable to parse CLI JSON output, falling back to prose parser: %s", preview)
        return _fallback_json_from_text(raw)
    if not isinstance(parsed, dict):
        raise ValueError("CLI JSON output was not an object")
    return parsed


def _fallback_json_from_text(raw: str) -> dict[str, Any]:
    text = raw.strip()
    upper = text.upper()
    direction = "NEUTRAL"
    if any(token in upper for token in ("BEARISH", "SELL", "SHORT")):
        direction = "SELL"
    if any(token in upper for token in ("BULLISH", "BUY", "LONG")) and direction == "NEUTRAL":
        direction = "BUY"
    if any(token in upper for token in ("NO TRADE", "NO-TRADE", "NEUTRAL", "WAIT")):
        direction = "NEUTRAL"

    confidence = 0.55
    if any(token in upper for token in ("HIGH CONFIDENCE", "STRONG")):
        confidence = 0.75
    elif any(token in upper for token in ("LOW CONFIDENCE", "WEAK")):
        confidence = 0.35
    elif any(token in upper for token in ("MODERATE", "MEDIUM")):
        confidence = 0.55

    return {
        "direction": direction,
        "confidence": confidence,
        "cycle_level": 0,
        "m_w_detected": "M-TOP" in upper or "W-BOTTOM" in upper or "M/W" in upper,
        "rrt_detected": "RAILROAD" in upper or "RRT" in upper,
        "pin_bar_detected": "PIN" in upper,
        "setup_class": "UNKNOWN" if direction != "NEUTRAL" else "NO_TRADE",
        "entry_quality": int(confidence * 100),
        "risk_flags": ["parsed_from_prose"],
        "expected_path": "",
        "invalidation": "",
        "reasoning": text[:2000],
    }


def _parse_direction(value: Any) -> Direction:
    normalized = str(value or "NEUTRAL").upper()
    if normalized in ("BULLISH", "LONG", "UP"):
        normalized = "BUY"
    elif normalized in ("BEARISH", "SHORT", "DOWN"):
        normalized = "SELL"
    try:
        return Direction(normalized)
    except ValueError:
        return Direction.NEUTRAL


def _safe_float(value: Any) -> float:
    try:
        parsed = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    if parsed > 1.0:
        parsed = parsed / 100.0
    return max(0.0, min(1.0, parsed))


def _safe_int(value: Any) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def _parse_entry_quality(value: Any) -> int:
    if isinstance(value, str):
        normalized = value.strip().upper()
        mapping = {
            "NONE": 0,
            "LOW": 25,
            "WEAK": 25,
            "MODERATE": 55,
            "MEDIUM": 55,
            "HIGH": 80,
            "STRONG": 90,
        }
        if normalized in mapping:
            return mapping[normalized]
    return max(0, min(100, _safe_int(value)))


def _parse_cycle_level(value: Any) -> Optional[CycleLevel]:
    if isinstance(value, str):
        normalized = value.strip().upper().replace("LEVEL", "").replace("L", "")
    else:
        normalized = str(value or "")
    try:
        parsed = int(float(normalized))
    except (TypeError, ValueError):
        return None
    if parsed in (1, 2, 3):
        return CycleLevel(parsed)
    return None


def _provider_from_name(name: str) -> CliProvider:
    if name == "codex":
        return CODEX_PROVIDER
    if name == "claude":
        return CLAUDE_PROVIDER
    raise ValueError(f"Unknown provider: {name}")


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Replay scanner candidates through paid account CLIs")
    parser.add_argument("--provider", choices=("codex", "claude"), required=True)
    parser.add_argument("--min-readiness", type=int, default=50)
    parser.add_argument("--timeframe", default="M15")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--lookback-bars", type=int, default=240)
    args = parser.parse_args(argv)

    if not connect_mt5():
        raise SystemExit(1)

    replay = ScannerReplay()
    account_replay = AccountCliReplay(replay)
    try:
        candidates = replay.get_candidates(
            min_readiness=args.min_readiness,
            timeframe=args.timeframe,
            limit=args.limit,
        )
        ids = account_replay.record_predictions(
            _provider_from_name(args.provider),
            candidates,
            lookback_bars=args.lookback_bars,
        )
    finally:
        account_replay.close()
        disconnect_mt5()

    print(f"Recorded/reused {len(ids)} {args.provider} account-backed predictions.")


if __name__ == "__main__":
    main()
