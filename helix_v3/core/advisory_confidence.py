"""MMM technical advisory confidence scoring.

The live execution gate still belongs to the orchestrator, consensus validator,
and gatekeeper. This module gives both offline replay and live scans the same
explainable score for whether a setup is worth advancing to vision review.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Iterable, Optional

from config.pair_profiles import get_pair_profile


@dataclass(frozen=True)
class AdvisorySetup:
    symbol: str
    direction: str
    confluence_score: int
    trade_valid: bool = True
    h4_level: int = 0
    h1_session: str = ""
    asian_range_pips: Optional[float] = None
    asian_range_ratio: Optional[float] = None
    stop_hunt_detected: bool = False
    stop_hunt_pips: Optional[float] = None
    hunt_range_ratio: Optional[float] = None
    push_count: int = 0
    m_w_forming: bool = False
    m_w_pattern: str = ""
    rrt_detected: bool = False
    tdi_state: str = "TDI_UNKNOWN"
    pattern_trade_type: str = ""
    themes: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ConvergenceSummary:
    score: float
    peer_symbols: list[str]
    themes: list[str]
    avg_peer_confluence: float
    avg_similarity: float


@dataclass(frozen=True)
class AdvisoryConfidence:
    symbol: str
    direction: str
    base_score: float
    convergence_score: float
    final_score: float
    grade: str
    action: str
    reasons: list[str]
    blockers: list[str]
    peer_symbols: list[str]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def advisory_setup_from_mtf(
    analysis: Any,
    *,
    tdi_result: Any = None,
    patterns: Any = None,
) -> AdvisorySetup:
    """Convert an MTF analysis plus optional indicator scans into advisory input."""

    symbol = str(getattr(analysis, "symbol", ""))
    direction = _enum_value(getattr(analysis, "trade_direction", "NEUTRAL"))
    profile = get_pair_profile(symbol)
    m15 = getattr(analysis, "fifteen_min", None)
    h4 = getattr(analysis, "four_hour", None)
    h1 = getattr(analysis, "one_hour", None)

    asian_range_pips = _optional_float(getattr(m15, "asian_range_pips", None))
    stop_hunt_pips = _optional_float(getattr(m15, "stop_hunt_pips", None))
    signals = _tdi_signal_values(tdi_result)
    tdi_state = classify_tdi_state(
        signals=signals,
        direction=direction,
        shark_fin_active=bool(getattr(tdi_result, "shark_fin_active", False)),
        shark_fin_direction=str(getattr(tdi_result, "shark_fin_direction", "") or ""),
        vb_squeeze=bool(getattr(tdi_result, "vb_squeeze", False)),
        rsi=_optional_float(getattr(tdi_result, "rsi", None)),
    )

    return AdvisorySetup(
        symbol=symbol,
        direction=direction,
        confluence_score=int(getattr(analysis, "confluence_score", 0) or 0),
        trade_valid=bool(getattr(analysis, "trade_valid", False)),
        h4_level=int(getattr(h4, "level_count", 0) or 0),
        h1_session=_enum_value(getattr(h1, "session_phase", "")),
        asian_range_pips=asian_range_pips,
        asian_range_ratio=_safe_ratio(asian_range_pips, profile.asian_range_max_pips),
        stop_hunt_detected=bool(getattr(m15, "stop_hunt_detected", False)),
        stop_hunt_pips=stop_hunt_pips,
        hunt_range_ratio=_safe_ratio(stop_hunt_pips, profile.stop_hunt_max_pips),
        push_count=int(getattr(m15, "push_count", 0) or 0),
        m_w_forming=bool(getattr(m15, "m_w_forming", False)),
        m_w_pattern=str(getattr(m15, "m_w_pattern", "") or ""),
        rrt_detected=bool(getattr(m15, "rrt_detected", False)),
        tdi_state=tdi_state,
        pattern_trade_type=_pattern_trade_type(patterns),
        themes=currency_theme_tags(symbol, direction),
    )


def classify_tdi_state(
    *,
    signals: Iterable[str],
    direction: str,
    shark_fin_active: bool = False,
    shark_fin_direction: str = "",
    vb_squeeze: bool = False,
    rsi: Optional[float] = None,
) -> str:
    signal_set = {str(signal).upper() for signal in signals if str(signal).upper() != "NONE"}
    direction = str(direction or "NEUTRAL").upper()
    shark_fin_direction = str(shark_fin_direction or "").upper()

    if not signal_set and not vb_squeeze and not shark_fin_active:
        return "TDI_UNKNOWN" if rsi is None else "TDI_NONE"

    if _tdi_confirms(signal_set, direction, shark_fin_direction):
        return "TDI_CONFIRM"
    if _tdi_conflicts(signal_set, direction, shark_fin_direction):
        return "TDI_CONFLICT"
    if vb_squeeze:
        return "TDI_SQUEEZE"
    return "TDI_NEUTRAL"


def score_advisory_setup(
    setup: AdvisorySetup,
    peers: Iterable[AdvisorySetup] = (),
) -> AdvisoryConfidence:
    """Score a setup using MMM structure, TDI, pair-normalized ranges, and convergence."""

    reasons: list[str] = []
    blockers: list[str] = []
    score = float(setup.confluence_score) * 0.65

    if setup.direction not in {"BUY", "SELL"}:
        blockers.append("neutral direction")
        score -= 25.0
    if not setup.trade_valid:
        blockers.append("MTF trade_valid is false")
        score -= 20.0

    if setup.m_w_forming:
        score += 8.0
        reasons.append("M/W formation present")
    else:
        score -= 15.0
        blockers.append("M/W formation missing")

    if setup.push_count >= 3:
        score += 6.0
        reasons.append("three-push structure present")
    else:
        score -= 8.0
        blockers.append("less than three pushes")

    if setup.rrt_detected:
        score += 5.0
        reasons.append("RRT detected")
    else:
        score -= 3.0

    if setup.stop_hunt_detected:
        score += 4.0
        reasons.append("stop hunt detected")
    else:
        score -= 10.0
        blockers.append("stop hunt missing")

    score += _tdi_adjustment(setup.tdi_state, reasons, blockers)
    score += _range_adjustment(setup, reasons, blockers)

    if setup.pattern_trade_type.upper() in {"THE_33", "THE_33_MW", "RRT_REVERSAL"}:
        score += 3.0
        reasons.append(f"pattern scan supports {setup.pattern_trade_type}")

    convergence = summarize_peer_convergence(setup, peers)
    if convergence.score >= 50.0:
        boost = min(12.0, convergence.score * 0.12)
        score += boost
        reasons.append(
            f"cross-pair convergence {convergence.score:.0f} "
            f"via {', '.join(convergence.peer_symbols[:4])}"
        )
    elif convergence.score > 0:
        reasons.append(f"weak cross-pair convergence {convergence.score:.0f}")

    final_score = max(0.0, min(100.0, score))
    grade, action = _grade(final_score, blockers)
    return AdvisoryConfidence(
        symbol=setup.symbol,
        direction=setup.direction,
        base_score=float(setup.confluence_score),
        convergence_score=convergence.score,
        final_score=final_score,
        grade=grade,
        action=action,
        reasons=reasons[:8],
        blockers=blockers[:8],
        peer_symbols=convergence.peer_symbols,
    )


def summarize_peer_convergence(
    setup: AdvisorySetup,
    peers: Iterable[AdvisorySetup],
) -> ConvergenceSummary:
    peer_scores: list[tuple[AdvisorySetup, float, list[str]]] = []
    own_themes = set(setup.themes or currency_theme_tags(setup.symbol, setup.direction))
    if not own_themes or setup.direction not in {"BUY", "SELL"}:
        return ConvergenceSummary(0.0, [], [], 0.0, 0.0)

    for peer in peers:
        if peer.symbol == setup.symbol or peer.direction not in {"BUY", "SELL"}:
            continue
        peer_themes = set(peer.themes or currency_theme_tags(peer.symbol, peer.direction))
        overlap = sorted(own_themes & peer_themes)
        if not overlap or peer.confluence_score < 30:
            continue
        similarity = setup_similarity(setup, peer)
        if similarity < 0.35:
            continue
        peer_scores.append((peer, similarity, overlap))

    if not peer_scores:
        return ConvergenceSummary(0.0, [], [], 0.0, 0.0)

    symbols = sorted({peer.symbol for peer, _, _ in peer_scores})
    themes = sorted({theme for _, _, overlap in peer_scores for theme in overlap})
    avg_conf = sum(peer.confluence_score for peer, _, _ in peer_scores) / len(peer_scores)
    avg_similarity = sum(similarity for _, similarity, _ in peer_scores) / len(peer_scores)
    score = min(
        100.0,
        len(symbols) * 28.0 + avg_conf * 0.35 + avg_similarity * 30.0,
    )
    return ConvergenceSummary(score, symbols, themes, avg_conf, avg_similarity)


def setup_similarity(left: AdvisorySetup, right: AdvisorySetup) -> float:
    points = 0.0
    total = 0.0

    total += 1.0
    points += 1.0 if left.m_w_forming == right.m_w_forming else 0.0

    total += 1.0
    points += 1.0 if _push_bucket(left.push_count) == _push_bucket(right.push_count) else 0.0

    total += 1.0
    points += 1.0 if left.rrt_detected == right.rrt_detected else 0.0

    total += 1.0
    points += 1.0 if left.h4_level == right.h4_level else 0.4 if left.h4_level and right.h4_level else 0.0

    total += 1.0
    points += 1.0 if left.h1_session == right.h1_session else 0.0

    total += 1.0
    points += 1.0 if _tdi_family(left.tdi_state) == _tdi_family(right.tdi_state) else 0.0

    return points / total if total else 0.0


def currency_theme_tags(symbol: str, direction: str) -> list[str]:
    direction = str(direction or "NEUTRAL").upper()
    if direction not in {"BUY", "SELL"}:
        return []
    base, quote = split_symbol(symbol)
    if direction == "BUY":
        return [f"{base}_STRENGTH", f"{quote}_WEAKNESS"]
    return [f"{base}_WEAKNESS", f"{quote}_STRENGTH"]


def split_symbol(symbol: str) -> tuple[str, str]:
    if symbol == "XAUUSD":
        return "XAU", "USD"
    if len(symbol) >= 6:
        return symbol[:3], symbol[3:6]
    return symbol, "UNKNOWN"


def _tdi_adjustment(tdi_state: str, reasons: list[str], blockers: list[str]) -> float:
    state = str(tdi_state or "TDI_UNKNOWN").upper()
    if state == "TDI_CONFIRM":
        reasons.append("TDI confirms direction")
        return 12.0
    if state == "TDI_CONFLICT":
        blockers.append("TDI conflicts with direction")
        return -20.0
    if state == "TDI_SQUEEZE":
        reasons.append("TDI volatility-band squeeze")
        return 3.0
    if state == "TDI_UNKNOWN":
        return -4.0
    if state == "TDI_NONE":
        return -2.0
    return 0.0


def _range_adjustment(setup: AdvisorySetup, reasons: list[str], blockers: list[str]) -> float:
    score = 0.0
    asian_ratio = setup.asian_range_ratio
    if asian_ratio is not None:
        if asian_ratio <= 0.5:
            score += 5.0
            reasons.append("tight Asian accumulation")
        elif asian_ratio <= 1.0:
            score += 2.0
            reasons.append("Asian range inside pair profile")
        elif asian_ratio > 1.3:
            score -= 8.0
            blockers.append("Asian range is extreme for pair")
        else:
            score -= 4.0
            blockers.append("Asian range exceeds pair max")

    hunt_ratio = setup.hunt_range_ratio
    if setup.stop_hunt_detected and hunt_ratio is not None:
        if 0 < hunt_ratio <= 1.0:
            score += 3.0
            reasons.append("stop hunt inside pair range")
        elif hunt_ratio > 1.0:
            score -= 8.0
            blockers.append("stop hunt extended beyond pair max")
    return score


def _tdi_confirms(signals: set[str], direction: str, shark_fin_direction: str) -> bool:
    if direction == "BUY":
        return bool(
            signals
            & {
                "SHARK_FIN_LONG",
                "MBL_CROSS_BULLISH",
                "SIGNAL_CROSS_BULLISH",
                "HOOK_BULLISH",
                "BULLISH_DIVERGENCE",
            }
        ) or shark_fin_direction == "LONG"
    if direction == "SELL":
        return bool(
            signals
            & {
                "SHARK_FIN_SHORT",
                "MBL_CROSS_BEARISH",
                "SIGNAL_CROSS_BEARISH",
                "HOOK_BEARISH",
                "BEARISH_DIVERGENCE",
            }
        ) or shark_fin_direction == "SHORT"
    return False


def _tdi_conflicts(signals: set[str], direction: str, shark_fin_direction: str) -> bool:
    if direction == "BUY":
        return bool(
            signals
            & {
                "SHARK_FIN_SHORT",
                "MBL_CROSS_BEARISH",
                "SIGNAL_CROSS_BEARISH",
                "HOOK_BEARISH",
                "BEARISH_DIVERGENCE",
            }
        ) or shark_fin_direction == "SHORT"
    if direction == "SELL":
        return bool(
            signals
            & {
                "SHARK_FIN_LONG",
                "MBL_CROSS_BULLISH",
                "SIGNAL_CROSS_BULLISH",
                "HOOK_BULLISH",
                "BULLISH_DIVERGENCE",
            }
        ) or shark_fin_direction == "LONG"
    return False


def _grade(score: float, blockers: list[str]) -> tuple[str, str]:
    hard_blockers = {
        "neutral direction",
        "MTF trade_valid is false",
        "M/W formation missing",
        "less than three pushes",
        "TDI conflicts with direction",
    }
    if any(blocker in hard_blockers for blocker in blockers) and score < 70.0:
        return "AVOID", "avoid"
    if score >= 80.0:
        return "A", "entry-grade"
    if score >= 70.0:
        return "B", "vision-validate"
    if score >= 60.0:
        return "C", "watch"
    if score >= 50.0:
        return "D", "low-confidence-watch"
    return "AVOID", "avoid"


def _tdi_signal_values(tdi_result: Any) -> list[str]:
    values: list[str] = []
    for signal in getattr(tdi_result, "signals", []) or []:
        value = _enum_value(signal)
        if value and value != "NONE":
            values.append(value)
    return values


def _pattern_trade_type(patterns: Any) -> str:
    trade_type = getattr(patterns, "trade_type", "")
    return _enum_value(trade_type)


def _enum_value(value: Any) -> str:
    raw = getattr(value, "value", value)
    if raw is None:
        return ""
    text = str(raw)
    if "." in text and text.split(".")[-1].isupper():
        return text.split(".")[-1]
    return text


def _safe_ratio(value: Optional[float], denominator: float) -> Optional[float]:
    if value is None or denominator <= 0:
        return None
    return float(value) / float(denominator)


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _push_bucket(push_count: int) -> str:
    if push_count >= 3:
        return "PUSH3_PLUS"
    if push_count == 2:
        return "PUSH2"
    if push_count == 1:
        return "PUSH1"
    return "PUSH0"


def _tdi_family(tdi_state: str) -> str:
    state = str(tdi_state or "TDI_UNKNOWN").upper()
    if state in {"TDI_CONFIRM", "TDI_CONFLICT"}:
        return state
    if state == "TDI_SQUEEZE":
        return "TDI_NEUTRAL"
    return state
