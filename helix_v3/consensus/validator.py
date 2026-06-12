"""MMMConsensusValidator - Multi-mode vision verification engine.

Supports four validation modes (cheapest to most robust):
  - "local": Single Anthropic API call if key available, otherwise reads
    verdict files from disk. Cheapest real analysis mode. Stale file
    verdicts (>30 min) are rejected to prevent old signals rubber-stamping.
  - "anthropic": Self-consensus via two independent Claude queries with
    different prompts (pattern + structural).
  - "openai": Single OpenAI structured-vision verdict.
  - "dual-api": Claude + GPT in parallel (requires both API keys).

Mode is auto-detected from available API keys, or can be forced via
CONSENSUS_MODE in .env.
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx

from config.settings import settings
from helix_v3.core.types import (
    ConsensusResult,
    CycleLevel,
    Direction,
    VisionVerdict,
)
from helix_v3.ai.model_roles import get_role
from helix_v3.utils.logger import get_logger

logger = get_logger("consensus_validator")

PROMPT_VERSION = "mmm_vision_v2"

VISION_SYSTEM_PROMPT = """You are an expert Market Maker Method (MMM) chart analyst.
Analyze this candlestick chart with EMA overlays (5-Red, 13-Yellow, 50-Aqua, 200-Magenta, 800-White).

Identify and report:
1. "M" or "W" geometric peak/trough formations at daily extremes
2. Railroad Tracks (RRT): consecutive opposing candles of similar size near 50 or 200 EMA
3. Pin bars or volume spikes interacting with the 50 or 200 EMA lines
4. Market Maker Cycle Level: count directional pushes relative to the 800 EMA anchor (Level 1, 2, or 3)
5. Overall directional bias based on EMA stack order and price structure
6. Setup class, entry quality, risk flags, expected path, and invalidation level/condition

You MUST respond with valid JSON only, no other text."""

# Second prompt with structural focus (used as the "second opinion" in single-model mode)
VISION_STRUCTURAL_PROMPT = """You are a quantitative structural analyst specializing in institutional order flow.
Analyze this candlestick chart with EMA overlays (5-Red, 13-Yellow, 50-Aqua, 200-Magenta, 800-White).

Focus on:
1. Institutional accumulation/distribution signatures (tight ranges followed by expansion)
2. Stop-hunt geometry: sharp wicks beyond key levels that reverse immediately
3. EMA stack alignment: are fast EMAs (5, 13) above or below slow EMAs (200, 800)?
4. Cycle position: how many directional pushes from the 800 EMA anchor (1, 2, or 3)?
5. Whether current price action suggests a reversal or continuation

You MUST respond with valid JSON only, no other text."""

VISION_JSON_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "direction": {"type": "string", "enum": ["BUY", "SELL", "NEUTRAL"]},
        "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
        "cycle_level": {"type": "integer", "enum": [0, 1, 2, 3]},
        "m_w_detected": {"type": "boolean"},
        "rrt_detected": {"type": "boolean"},
        "pin_bar_detected": {"type": "boolean"},
        "setup_class": {
            "type": "string",
            "enum": [
                "THE_33",
                "NYC_REVERSAL",
                "SECOND_LEG_MW",
                "STRAIGHTAWAY",
                "EMA_200_BOUNCE",
                "LONDON_REVERSAL",
                "NO_TRADE",
                "UNKNOWN",
            ],
        },
        "entry_quality": {"type": "integer", "minimum": 0, "maximum": 100},
        "risk_flags": {"type": "array", "items": {"type": "string"}},
        "expected_path": {"type": "string"},
        "invalidation": {"type": "string"},
        "reasoning": {"type": "string"},
    },
    "required": [
        "direction", "confidence", "cycle_level",
        "m_w_detected", "rrt_detected", "pin_bar_detected",
        "setup_class", "entry_quality", "risk_flags",
        "expected_path", "invalidation", "reasoning",
    ],
    "additionalProperties": False,
}

LOCAL_VERDICTS_DIR = Path(settings.chart.output_dir).parent / "verdicts"


class MMMConsensusValidator:
    """Multi-mode vision consensus engine.

    Auto-detects mode based on available API keys:
    - Both keys set -> dual-api (Claude + GPT-5.5)
    - Only Anthropic key -> anthropic (two independent Claude queries)
    - No keys -> local (reads from verdicts/ directory)

    Override with CONSENSUS_MODE env var.
    """

    def __init__(self, mode: Optional[str] = None) -> None:
        self._api_cfg = settings.api
        self._threshold = self._api_cfg.consensus_confidence_threshold

        if mode:
            self._mode = mode
        else:
            self._mode = self._auto_detect_mode()

        LOCAL_VERDICTS_DIR.mkdir(parents=True, exist_ok=True)
        logger.info("Consensus validator initialized in '%s' mode", self._mode)

    def _auto_detect_mode(self) -> str:
        import os
        forced = os.getenv("CONSENSUS_MODE", "").lower()
        if forced in ("anthropic", "dual-api", "openai", "local"):
            return forced

        has_anthropic = bool(self._api_cfg.anthropic_key)
        has_openai = bool(self._api_cfg.openai_key)

        if has_anthropic and has_openai:
            return "dual-api"
        elif has_anthropic:
            return "anthropic"
        else:
            return "local"

    @property
    def mode(self) -> str:
        return self._mode

    # ------------------------------------------------------------------
    # Anthropic API Calls
    # ------------------------------------------------------------------

    async def _query_anthropic(
        self,
        image_b64: str,
        client: httpx.AsyncClient,
        system_prompt: str = VISION_SYSTEM_PROMPT,
        label: str = "claude-opus-primary",
    ) -> VisionVerdict:
        payload = {
            "model": self._api_cfg.anthropic_model,
            "max_tokens": 1024,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_b64,
                            },
                        },
                        {"type": "text", "text": system_prompt},
                    ],
                }
            ],
        }

        response = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": self._api_cfg.anthropic_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json=payload,
            timeout=90.0,
        )
        response.raise_for_status()
        data = response.json()

        text_content = ""
        for block in data.get("content", []):
            if block.get("type") == "text":
                text_content += block["text"]

        return self._parse_verdict(label, text_content)

    # ------------------------------------------------------------------
    # OpenAI API Call
    # ------------------------------------------------------------------

    async def _query_openai(
        self, image_b64: str, client: httpx.AsyncClient
    ) -> VisionVerdict:
        role = get_role("structured_arbitrator")
        payload = {
            "model": role.model,
            "max_output_tokens": 1024,
            "input": [
                {"role": "system", "content": VISION_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": (
                                "Analyze this MMM chart and return the strict "
                                "backtest-ready JSON verdict."
                            ),
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{image_b64}",
                            "detail": "high",
                        },
                    ],
                },
            ],
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "mmm_vision_verdict",
                    "schema": VISION_JSON_SCHEMA,
                    "strict": True,
                }
            },
        }

        response = await client.post(
            "https://api.openai.com/v1/responses",
            headers={
                "Authorization": f"Bearer {self._api_cfg.openai_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=90.0,
        )
        response.raise_for_status()
        data = response.json()

        text_content = self._extract_openai_text(data)
        return self._parse_verdict(f"openai:{role.role_id}:{role.model}", text_content)

    @staticmethod
    def _extract_openai_text(data: Dict[str, Any]) -> str:
        if isinstance(data.get("output_text"), str):
            return data["output_text"]

        pieces: List[str] = []
        for item in data.get("output", []):
            for content in item.get("content", []):
                text = content.get("text")
                if isinstance(text, str):
                    pieces.append(text)
        return "".join(pieces)

    # ------------------------------------------------------------------
    # Local Mode (Claude Code writes verdicts to disk)
    # ------------------------------------------------------------------

    def write_local_verdict(
        self,
        symbol: str,
        timeframe: str,
        verdict_json: dict,
        label: str = "claude-code",
    ) -> Path:
        """Write a verdict JSON file for local mode consumption.

        Call this from Claude Code interactive sessions to provide vision
        analysis without API keys. The orchestrator picks these up automatically.
        """
        verdict_path = LOCAL_VERDICTS_DIR / f"{symbol}_{timeframe}.json"
        verdict_path.write_text(json.dumps(verdict_json, indent=2))
        logger.info("Local verdict written: %s", verdict_path)
        return verdict_path

    def _read_local_verdict(
        self, symbol: str, timeframe: str, label: str,
        max_age_minutes: int = 30,
    ) -> VisionVerdict:
        verdict_path = LOCAL_VERDICTS_DIR / f"{symbol}_{timeframe}.json"
        if not verdict_path.exists():
            logger.warning("No local verdict found: %s", verdict_path)
            return VisionVerdict(
                model_name=label,
                direction=Direction.NEUTRAL,
                confidence=0.0,
                cycle_level=None,
                m_w_detected=False,
                rrt_detected=False,
                pin_bar_detected=False,
                raw_json={"error": "no_local_verdict"},
            )

        # Reject stale verdict files — prevents old signals from rubber-stamping trades
        import os
        import time as _time
        age_min = (_time.time() - os.path.getmtime(verdict_path)) / 60
        if age_min > max_age_minutes:
            logger.warning(
                "Stale local verdict rejected: %s (%.0f min old, limit=%d)",
                verdict_path.name, age_min, max_age_minutes,
            )
            return VisionVerdict(
                model_name=label,
                direction=Direction.NEUTRAL,
                confidence=0.0,
                cycle_level=None,
                m_w_detected=False,
                rrt_detected=False,
                pin_bar_detected=False,
                raw_json={"error": "stale_verdict", "age_minutes": round(age_min)},
            )

        raw = verdict_path.read_text()
        return self._parse_verdict(label, raw)

    # ------------------------------------------------------------------
    # JSON Parsing
    # ------------------------------------------------------------------

    def _parse_verdict(self, model_name: str, raw_text: str) -> VisionVerdict:
        try:
            cleaned = raw_text.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("\n", 1)[-1].rsplit("```", 1)[0]
            parsed = json.loads(cleaned)
        except json.JSONDecodeError:
            logger.error("JSON parse failed for %s: %s", model_name, raw_text[:200])
            return VisionVerdict(
                model_name=model_name,
                direction=Direction.NEUTRAL,
                confidence=0.0,
                cycle_level=None,
                m_w_detected=False,
                rrt_detected=False,
                pin_bar_detected=False,
                raw_json={"error": "parse_failed", "raw": raw_text[:500]},
            )

        direction_str = parsed.get("direction", "NEUTRAL").upper()
        try:
            direction = Direction(direction_str)
        except ValueError:
            direction = Direction.NEUTRAL

        cycle_raw = parsed.get("cycle_level")
        cycle_level: Optional[CycleLevel] = None
        if cycle_raw in (1, 2, 3):
            cycle_level = CycleLevel(cycle_raw)

        risk_flags_raw = parsed.get("risk_flags", [])
        if isinstance(risk_flags_raw, list):
            risk_flags = [str(flag) for flag in risk_flags_raw]
        elif risk_flags_raw:
            risk_flags = [str(risk_flags_raw)]
        else:
            risk_flags = []

        return VisionVerdict(
            model_name=model_name,
            direction=direction,
            confidence=self._safe_float(parsed.get("confidence", 0.0)),
            cycle_level=cycle_level,
            m_w_detected=bool(parsed.get("m_w_detected", False)),
            rrt_detected=bool(parsed.get("rrt_detected", False)),
            pin_bar_detected=bool(parsed.get("pin_bar_detected", False)),
            setup_class=str(parsed.get("setup_class", "UNKNOWN")),
            entry_quality=self._safe_int(parsed.get("entry_quality", 0)),
            risk_flags=risk_flags,
            expected_path=str(parsed.get("expected_path", "")),
            invalidation=str(parsed.get("invalidation", "")),
            reasoning=str(parsed.get("reasoning", "")),
            raw_json=parsed,
        )

    @staticmethod
    def _safe_float(value: Any) -> float:
        try:
            return float(value or 0.0)
        except (TypeError, ValueError):
            return 0.0

    @staticmethod
    def _safe_int(value: Any) -> int:
        try:
            return int(float(value or 0))
        except (TypeError, ValueError):
            return 0

    # ------------------------------------------------------------------
    # Consensus Arbitration
    # ------------------------------------------------------------------

    def _arbitrate(self, verdicts: List[VisionVerdict]) -> ConsensusResult:
        dirs = [v.direction for v in verdicts]
        confs = [v.confidence for v in verdicts]
        avg_conf = sum(confs) / len(confs) if confs else 0.0

        directions_match = len(set(dirs)) == 1 and dirs[0] != Direction.NEUTRAL
        all_confident = all(c >= self._threshold for c in confs)
        agreed = directions_match and all_confident

        divergence = ""
        if not agreed:
            if not directions_match:
                divergence = f"Direction conflict: {[d.value for d in dirs]}"
            elif not all_confident:
                divergence = f"Confidence below threshold: {confs} < {self._threshold}"

        consensus = ConsensusResult(
            agreed=agreed,
            direction=dirs[0] if directions_match else Direction.NEUTRAL,
            avg_confidence=avg_conf,
            verdicts=verdicts,
            divergence_notes=divergence,
        )

        if agreed:
            logger.info(
                "CONSENSUS REACHED: %s | conf=%.2f | models=%s",
                consensus.direction.value, avg_conf,
                [v.model_name for v in verdicts],
            )
        else:
            logger.info(
                "CONSENSUS DECLINED: %s | %s",
                [d.value for d in dirs], divergence,
            )

        return consensus

    # ------------------------------------------------------------------
    # Main Evaluate Entry Point
    # ------------------------------------------------------------------

    async def evaluate(
        self,
        image_b64: str,
        symbol: str = "",
        timeframe: str = "",
    ) -> ConsensusResult:
        """Run consensus evaluation in the configured mode."""
        if self._mode == "dual-api":
            return await self._evaluate_dual_api(image_b64)
        elif self._mode == "anthropic":
            return await self._evaluate_anthropic_only(image_b64)
        elif self._mode == "openai":
            return await self._evaluate_openai_only(image_b64)
        elif self._mode == "local":
            return await self._evaluate_local(image_b64, symbol, timeframe)
        else:
            raise ValueError(f"Unknown consensus mode: {self._mode}")

    async def _evaluate_dual_api(self, image_b64: str) -> ConsensusResult:
        """Original dual-model: Claude Opus + GPT-5.5 in parallel."""
        anthropic_role = get_role("vision_pattern_primary")
        openai_role = get_role("structured_arbitrator")
        async with httpx.AsyncClient() as client:
            results = await asyncio.gather(
                self._query_anthropic(
                    image_b64,
                    client,
                    VISION_SYSTEM_PROMPT,
                    f"anthropic:{anthropic_role.role_id}:{anthropic_role.model}",
                ),
                self._query_openai(image_b64, client),
                return_exceptions=True,
            )
        return self._gather_and_arbitrate(
            results,
            [
                f"anthropic:{anthropic_role.role_id}:{anthropic_role.model}",
                f"openai:{openai_role.role_id}:{openai_role.model}",
            ],
        )

    async def _evaluate_openai_only(self, image_b64: str) -> ConsensusResult:
        """Single OpenAI structured-vision verdict for offline evaluation."""
        role = get_role("structured_arbitrator")
        async with httpx.AsyncClient() as client:
            result = await self._query_openai(image_b64, client)
        return self._gather_and_arbitrate(
            [result],
            [f"openai:{role.role_id}:{role.model}"],
        )

    async def _evaluate_anthropic_only(self, image_b64: str) -> ConsensusResult:
        """Single-model self-consensus: two Claude queries with different prompts."""
        async with httpx.AsyncClient() as client:
            results = await asyncio.gather(
                self._query_anthropic(
                    image_b64, client, VISION_SYSTEM_PROMPT, "claude-opus-primary"
                ),
                self._query_anthropic(
                    image_b64, client, VISION_STRUCTURAL_PROMPT, "claude-opus-structural"
                ),
                return_exceptions=True,
            )
        return self._gather_and_arbitrate(results, ["claude-opus-primary", "claude-opus-structural"])

    async def _evaluate_local(
        self, image_b64: str, symbol: str, timeframe: str
    ) -> ConsensusResult:
        """Local mode: single Anthropic API call if key available, else file fallback.

        This is the cheapest real analysis mode — one API call vs two in
        'anthropic' mode. Falls back to reading verdict files from disk only
        when no API key is configured.
        """
        # If we have an Anthropic key AND an image, do real single-call analysis
        if self._api_cfg.anthropic_key and image_b64:
            logger.info("Local mode: analyzing chart via single Anthropic API call")
            try:
                async with httpx.AsyncClient() as client:
                    verdict = await self._query_anthropic(
                        image_b64,
                        client,
                        VISION_SYSTEM_PROMPT,
                        "local-single-claude",
                    )
                if verdict.confidence > 0:
                    return self._arbitrate([verdict])

                logger.warning(
                    "Local API call returned zero confidence for %s — falling back to file",
                    symbol,
                )
            except Exception as e:
                logger.error("Local API call failed for %s: %s — falling back to file", symbol, e)

        # Fallback: read pre-written verdicts from disk
        v1 = self._read_local_verdict(symbol, timeframe, "claude-code-primary")
        if v1.confidence > 0:
            return self._arbitrate([v1])

        # No API, no file — return declined consensus
        logger.warning("No local verdict available for %s_%s (no API key, no verdict file)", symbol, timeframe)
        return self._arbitrate([
            VisionVerdict(
                model_name="local-unavailable",
                direction=Direction.NEUTRAL,
                confidence=0.0,
                cycle_level=None,
                m_w_detected=False,
                rrt_detected=False,
                pin_bar_detected=False,
                raw_json={"error": "no_api_key_and_no_verdict_file"},
            )
        ])

    def _gather_and_arbitrate(
        self, results: list, model_names: List[str]
    ) -> ConsensusResult:
        verdicts: List[VisionVerdict] = []
        for i, result in enumerate(results):
            name = model_names[i] if i < len(model_names) else f"model-{i}"
            if isinstance(result, Exception):
                logger.error("Vision query failed for %s: %s", name, result)
                verdicts.append(
                    VisionVerdict(
                        model_name=name,
                        direction=Direction.NEUTRAL,
                        confidence=0.0,
                        cycle_level=None,
                        m_w_detected=False,
                        rrt_detected=False,
                        pin_bar_detected=False,
                        raw_json={"error": str(result)},
                    )
                )
            else:
                verdicts.append(result)

        return self._arbitrate(verdicts)
