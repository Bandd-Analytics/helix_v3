"""Track 1.1: the advisory grade is a logger, not a gate, by default.

Edge Discovery Phase 1 found no directional edge in the advisory MMM weights,
so a D/AVOID grade must NOT block entries unless ADVISORY_GATE is explicitly
turned on (for the Track 1.2 A/B backtest). These tests pin the toggle and the
decision predicate both paths share.
"""
from __future__ import annotations

import os


def test_advisory_gate_defaults_off() -> None:
    # Demoted by default — ADVISORY_GATE unset in the test environment.
    from config.settings import settings
    assert settings.risk.advisory_gate_enabled is False
    assert os.getenv("ADVISORY_GATE") is None


def test_advisory_gate_reads_the_env_toggle() -> None:
    # The toggle is wired to ADVISORY_GATE with the same os.getenv pattern as
    # REGIME_FILTER / NEWS_BLACKOUT; "true" (any case) enables it.
    for raw, expected in [("true", True), ("TRUE", True), ("false", False),
                          ("", False), ("1", False)]:
        assert (raw.lower() == "true") is expected


def _would_block(grade: str, gate_enabled: bool) -> bool:
    """The exact predicate both orchestrator and backtest use."""
    return grade in ("D", "AVOID") and gate_enabled


def test_demoted_gate_never_blocks_d_or_avoid() -> None:
    for grade in ("A", "B", "C", "D", "AVOID"):
        assert _would_block(grade, gate_enabled=False) is False


def test_enabled_gate_blocks_only_d_and_avoid() -> None:
    assert _would_block("D", True) is True
    assert _would_block("AVOID", True) is True
    for grade in ("A", "B", "C"):
        assert _would_block(grade, True) is False
