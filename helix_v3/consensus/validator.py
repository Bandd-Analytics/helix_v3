"""MMMConsensusValidator - Multi-mode vision verification engine.

Supports three validation modes:
  - "anthropic": Single-model via Anthropic API (Claude Opus). Runs two
    independent queries with different temperature/prompts for self-consensus.
  - "dual-api": Original dual-model (Claude + GPT-5.5) via API keys.
  - "local": Reads verdicts from a local JSON file written by Claude Code
    during interactive sessions (no API keys required).

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
from helix_v3.utils.logger import get_logger

logger = get_logger("consensus_validator")

VISION_SYSTEM_PROMPT = """You are an expert Market Maker Method (MMM) chart analyst.
Analyze this candlestick chart with EMA overlays (5-Red, 13-Yellow, 50-Aqua, 200-Magenta, 800-White).

Identify and report:
1. "M" or "W" geometric peak/trough formations at daily extremes
2. Railroad Tracks (RRT): consecutive opposing candles of similar size near 50 or 200 EMA
3. Pin bars or volume spikes interacting with the 50 or 200 EMA lines
4. Market Maker Cycle Level: count directional pushes relative to the 800 EMA anchor (Level 1, 2, or 3)
5. Overall directional bias based on EMA stack order and price structure

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
        "cycle_level": {"type": "integer", "enum": [1, 2, 3]},
        "m_w_detected": {"type": "boolean"},
        "rrt_detected": {"type": "boolean"},
        "pin_bar_detected": {"type": "boolean"},
        "reasoning": {"type": "string"},
    },
    "required": [
        "direction", "confidence", "cycle_level",
        "m_w_detected", "rrt_detected", "pin_bar_detected", "reasoning",
    ],
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
        if forced in ("anthropic", "dual-api", "local"):
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
        payload = {
            "model": self._api_cfg.openai_model,
            "response_format": {"type": "json_object"},
            "max_tokens": 1024,
            "messages": [
                {"role": "system", "content": VISION_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_b64}",
                                "detail": "high",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Analyze this MMM chart and return your structured JSON verdict.",
                        },
                    ],
                },
            ],
        }

        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self._api_cfg.openai_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=90.0,
        )
        response.raise_for_status()
        data = response.json()

        text_content = data["choices"][0]["message"]["content"]
        return self._parse_verdict("gpt-5.5", text_content)

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
        self, symbol: str, timeframe: str, label: str
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

        return VisionVerdict(
            model_name=model_name,
            direction=direction,
            confidence=float(parsed.get("confidence", 0.0)),
            cycle_level=cycle_level,
            m_w_detected=bool(parsed.get("m_w_detected", False)),
            rrt_detected=bool(parsed.get("rrt_detected", False)),
            pin_bar_detected=bool(parsed.get("pin_bar_detected", False)),
            raw_json=parsed,
        )

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
        elif self._mode == "local":
            return self._evaluate_local(symbol, timeframe)
        else:
            raise ValueError(f"Unknown consensus mode: {self._mode}")

    async def _evaluate_dual_api(self, image_b64: str) -> ConsensusResult:
        """Original dual-model: Claude Opus + GPT-5.5 in parallel."""
        async with httpx.AsyncClient() as client:
            results = await asyncio.gather(
                self._query_anthropic(image_b64, client, VISION_SYSTEM_PROMPT, "claude-opus"),
                self._query_openai(image_b64, client),
                return_exceptions=True,
            )
        return self._gather_and_arbitrate(results, ["claude-opus", "gpt-5.5"])

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

    def _evaluate_local(self, symbol: str, timeframe: str) -> ConsensusResult:
        """Read pre-written verdicts from disk (Claude Code interactive mode)."""
        v1 = self._read_local_verdict(symbol, timeframe, "claude-code-primary")
        v2 = self._read_local_verdict(symbol, timeframe, "claude-code-secondary")

        # If only one verdict file exists, duplicate it as single-opinion
        if v1.confidence > 0 and v2.confidence == 0:
            v2 = VisionVerdict(
                model_name="claude-code-secondary",
                direction=v1.direction,
                confidence=v1.confidence,
                cycle_level=v1.cycle_level,
                m_w_detected=v1.m_w_detected,
                rrt_detected=v1.rrt_detected,
                pin_bar_detected=v1.pin_bar_detected,
                raw_json=v1.raw_json,
            )

        return self._arbitrate([v1, v2])

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
