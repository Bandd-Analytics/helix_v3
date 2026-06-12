"""Pair-gated risk and trade management profiles.

Calibrated from MMM Book (Steve Mauro) methodology:
- 90 min stale exit if NOT in profit for standard pairs (M/W formation window is 30-90 min)
- Extended pairs tighten SL at 90 min and exit at the pair-specific limit if still not in profit
- If IN profit, trail SL to secure gains — never exit a winning trade early
- Stop hunt range 25-50 pips (pair-specific based on volatility)
- L1/L2 average move ~75 pips from peak to consolidation
- BE after 50 pips, trail after L1 consolidation clears
- Pip value differences gate risk % and lot sizing per pair
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Dict, List, Optional


@dataclass(frozen=True)
class GateRatios:
    """Universal gate ratios — fractions of ATR(20, D1) in pips (audit Tier 2.3).

    Derived 2026-06-12 from the cross-pair survey
    (tools/manual/atr_ratio_survey.py): medians of static_gate / ATR
    across the 13 FX pairs. The old per-pair pip constants were mostly
    ATR proxies (FX medians were tight); XAUUSD/US30/USTEC ratios were
    vacuous (0.003-0.07 on most gates), which is exactly why their
    fixed-pip gates passed everything. With ratios, every instrument
    gets real gates by construction.
    """
    asian_range_max: float = 0.55
    stop_hunt_min: float = 0.30
    stop_hunt_max: float = 1.00     # a hunt deeper than one daily range isn't a hunt
    expected_level_move: float = 0.95
    trail_activation: float = 0.20
    trail_distance: float = 0.15
    sl_buffer: float = 0.05
    min_sl: float = 0.25


GATE_RATIOS = GateRatios()


@dataclass
class PairProfile:
    symbol: str

    # Active for execution. False = analysis-only (still scanned, not traded).
    # CALIBRATED: disabled pairs showed negative or marginal edge in 14-day backtest.
    tradeable: bool = True

    # Risk tier: "low" = standard, "medium" = reduced risk, "high" = minimal risk
    risk_tier: str = "low"
    max_risk_pct: float = 0.01           # Max risk per trade
    max_lot_size: float = 1.0            # Hard lot cap

    # Spread
    max_spread_pips: float = 3.0         # Block entry above this

    # --- TIERED STALE EXIT (calibrated from 90-day validation) ---
    # Phase 1 (stale_minutes): Tighten SL to half original distance if NOT in profit.
    # Phase 2 (stale_exit_minutes): Full exit if STILL not in profit after extended window.
    # Low-vol pairs: 90/90 (exit immediately at 90 min — no extension).
    # Volatile crosses: 90/150 (tighten at 90, exit at 150 — data shows they need time).
    stale_minutes: int = 90              # Phase 1: tighten SL (universal)
    stale_exit_minutes: int = 90         # Phase 2: full exit (pair-specific)
    stale_max_pips: float = 0.0          # 0 = must be in profit, else stale

    # Max duration (hard cap even if in profit — session boundary)
    max_duration_minutes: int = 240

    # Trailing stop (activates ONLY when in profit)
    trail_activation_pips: float = 20.0  # Move SL to BE at this profit
    trail_distance_pips: float = 15.0    # After activation, SL trails this far behind

    # T1 partial close
    t1_rr: float = 1.0                   # RR ratio for T1
    partial_close_ratio: float = 0.50    # % of position to close at T1

    # SL placement (behind first swing high after push, per MMM)
    sl_buffer_pips: float = 3.0          # Buffer behind the structural level
    min_sl_pips: float = 20.0            # Floor for SL — prevents lot inflation from tight stops

    # MMM stop hunt range (used for entry zone detection)
    stop_hunt_min_pips: float = 25.0     # Min expected stop hunt from Asian range
    stop_hunt_max_pips: float = 50.0     # Max expected stop hunt

    # Expected L1/L2 move size (peak to consolidation)
    expected_level_move_pips: float = 75.0

    # Asian range max for valid accumulation
    asian_range_max_pips: float = 50.0

    # ATR(20, D1) this profile was resolved against (Tier 2.3).
    # 0.0 = static profile — the pip fields above are the legacy per-pair
    # estimates, used only when ATR is unavailable and for replay/signature
    # bucketing (keys must stay comparable with the historical libraries).
    # >0 = the pip gate fields were computed as GATE_RATIOS x this ATR.
    atr_pips: float = 0.0

    # Entry calibration advisory fields. These are used by replay/advisory reports
    # and are not live execution gates unless explicitly enforced by orchestration.
    min_confluence_score: int = 50
    require_m_w: bool = False
    require_push3: bool = False
    require_rrt: bool = False
    require_tdi_confirmation: bool = False
    block_tdi_conflict: bool = True
    max_asian_range_ratio: float = 1.0
    max_hunt_range_ratio: float = 1.0
    min_convergence_score: float = 0.0
    advisory_min_score: float = 70.0

    # Session exit
    close_before_session: str = "ASIAN_EARLY"

    # Notes
    notes: str = ""


# ==========================================================================
# PAIR PROFILES — calibrated from MMM Book + pip value reality
# ==========================================================================

PAIR_PROFILES: Dict[str, PairProfile] = {

    # --- Major USD Pairs ---
    # Pip value: ~$10/pip per standard lot
    # Tight spreads, most liquid, textbook MMM patterns

    "EURUSD": PairProfile(
        symbol="EURUSD",
        risk_tier="low",
        max_risk_pct=0.01,                # 1% risk — most predictable pair
        max_spread_pips=2.0,
        stale_minutes=90,
        stale_exit_minutes=90,            # Low-vol: exit at 90 (validated 64.3%)
        stale_max_pips=0.0,               # Must be in profit by 90 min
        max_duration_minutes=240,          # 4h max
        trail_activation_pips=12.0,        # Lowered from 15: catch runners earlier
        trail_distance_pips=10.0,          # Tightened from 12: lock in more profit
        sl_buffer_pips=3.0,
        min_sl_pips=15.0,                  # EUR is tight — but never less than 15
        stop_hunt_min_pips=20.0,           # EUR hunts are tighter
        stop_hunt_max_pips=75.0,           # CALIBRATED: was 40, P90=75p
        expected_level_move_pips=70.0,     # Slightly less than GBP
        asian_range_max_pips=40.0,         # EUR has tighter Asian ranges
        notes="Most liquid. ~$10/pip. Tight spreads. Textbook MMM.",
    ),

    "GBPUSD": PairProfile(
        symbol="GBPUSD",
        risk_tier="low",
        max_risk_pct=0.01,
        max_spread_pips=2.5,
        stale_minutes=90,
        stale_exit_minutes=90,            # Low-vol: exit at 90 (validated 62.0%)
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=15.0,        # Lowered from 20: catch runners earlier
        trail_distance_pips=12.0,          # Tightened from 15
        sl_buffer_pips=3.0,
        min_sl_pips=20.0,
        stop_hunt_min_pips=25.0,           # Standard MMM range
        stop_hunt_max_pips=105.0,          # CALIBRATED: was 50, P90=103p
        expected_level_move_pips=80.0,     # GBP moves bigger
        asian_range_max_pips=50.0,
        notes="Higher vol. ~$10/pip. Wider swings. Core MMM pair.",
    ),

    "AUDUSD": PairProfile(
        symbol="AUDUSD",
        risk_tier="low",
        max_risk_pct=0.01,
        max_spread_pips=2.0,
        stale_minutes=90,
        stale_exit_minutes=90,            # Low-vol: exit at 90 (validated 69.6%)
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=10.0,        # Lowered from 12: AUD is slower but catch moves
        trail_distance_pips=8.0,           # Tightened from 10
        sl_buffer_pips=3.0,
        min_sl_pips=12.0,                  # AUD is slow — tighter floor OK
        stop_hunt_min_pips=15.0,           # AUD hunts are smaller
        stop_hunt_max_pips=70.0,           # CALIBRATED: was 35, P90=68p
        expected_level_move_pips=55.0,     # Smaller ADR
        asian_range_max_pips=35.0,         # Tighter ranges
        notes="Slower, commodity-linked. ~$10/pip. Smaller stop hunts.",
    ),

    # --- GBP Cross Pairs ---
    # Non-USD pip values, wider spreads, more volatile
    # These require reduced risk because pip value amplifies losses

    "GBPAUD": PairProfile(
        symbol="GBPAUD",
        risk_tier="medium",
        max_risk_pct=0.008,               # 0.8% — AUD pip value ~$7.3/pip
        max_lot_size=0.5,
        max_spread_pips=4.0,
        stale_minutes=90,                  # Phase 1: tighten SL at 90 min
        stale_exit_minutes=150,            # CALIBRATED: was 90, holding helps (37.9% exit-correct)
        stale_max_pips=0.0,               # Must be in profit
        max_duration_minutes=300,          # 5h — crosses can trend longer
        trail_activation_pips=25.0,        # Lowered from 30: catch runs earlier
        trail_distance_pips=18.0,          # Tightened from 22
        sl_buffer_pips=5.0,               # Wider — spiky pair
        min_sl_pips=25.0,                  # Spiky — needs room
        stop_hunt_min_pips=30.0,
        stop_hunt_max_pips=105.0,          # CALIBRATED: was 60, P90=103p
        expected_level_move_pips=100.0,    # Big moves
        asian_range_max_pips=60.0,
        notes="Volatile cross. ~$7.3/pip. Spiky. Extended stale window.",
    ),

    "GBPJPY": PairProfile(
        symbol="GBPJPY",
        risk_tier="medium",
        max_risk_pct=0.008,               # 0.8% — JPY pip value ~$6.6/pip
        max_lot_size=0.5,
        max_spread_pips=4.0,
        stale_minutes=90,                  # Phase 1: tighten SL at 90 min
        stale_exit_minutes=135,            # CALIBRATED: was 90, holding helps (45.8% exit-correct)
        stale_max_pips=0.0,               # Must be in profit
        max_duration_minutes=240,
        trail_activation_pips=20.0,        # Lowered from 25: GJ runs hard, catch earlier
        trail_distance_pips=15.0,          # Tightened from 18
        sl_buffer_pips=5.0,               # Wider for JPY volatility
        min_sl_pips=25.0,                  # GJ is aggressive — never less than 25
        stop_hunt_min_pips=30.0,           # GJ stop hunts are aggressive
        stop_hunt_max_pips=130.0,          # CALIBRATED: was 60, P90=131p
        expected_level_move_pips=100.0,    # GJ does 100+ pip level moves
        asian_range_max_pips=50.0,
        notes="High vol JPY cross. ~$6.6/pip. Fast moves. Extended stale window.",
    ),

    "GBPNZD": PairProfile(
        symbol="GBPNZD",
        tradeable=False,                   # DISABLED: +$0.09 in 14-day backtest, 33% win rate
        risk_tier="medium",
        max_risk_pct=0.008,               # 0.8% — NZD pip value ~$5.8/pip
        max_lot_size=0.5,
        max_spread_pips=5.0,              # Widest spreads of the set
        stale_minutes=90,                  # Phase 1: tighten SL at 90 min
        stale_exit_minutes=150,            # CALIBRATED: was 90, holding helps (37.9% exit-correct)
        stale_max_pips=0.0,
        max_duration_minutes=300,
        trail_activation_pips=35.0,        # Very wide ATR
        trail_distance_pips=25.0,
        sl_buffer_pips=5.0,
        min_sl_pips=25.0,
        stop_hunt_min_pips=30.0,
        stop_hunt_max_pips=115.0,          # CALIBRATED: was 65, P90=114p
        expected_level_move_pips=110.0,
        asian_range_max_pips=65.0,
        notes="Widest spreads. ~$5.8/pip. Extended stale window. Big moves.",
    ),

    # --- EUR Crosses (MMM fractional disparity group) ---

    "EURJPY": PairProfile(
        symbol="EURJPY",
        tradeable=False,                   # DISABLED: 0% win rate in 14-day backtest, -$2.20
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=3.0,
        stale_minutes=90,
        stale_exit_minutes=90,            # Borderline (57.8%) — keep 90 for safety
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,
        trail_distance_pips=15.0,
        sl_buffer_pips=4.0,
        min_sl_pips=20.0,
        stop_hunt_min_pips=25.0,
        stop_hunt_max_pips=110.0,          # CALIBRATED: was 50, P90=109p
        expected_level_move_pips=85.0,
        asian_range_max_pips=50.0,
        notes="EUR+JPY cross. ~$6.6/pip. Shows cycle disparity vs EURUSD.",
    ),

    "EURGBP": PairProfile(
        symbol="EURGBP",
        tradeable=False,                   # Analysis-only until pair-specific validation exists
        risk_tier="low",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=2.5,
        stale_minutes=90,
        stale_exit_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=12.0,
        trail_distance_pips=10.0,
        sl_buffer_pips=3.0,
        min_sl_pips=12.0,
        stop_hunt_min_pips=12.0,
        stop_hunt_max_pips=45.0,
        expected_level_move_pips=45.0,
        asian_range_max_pips=30.0,
        notes="EUR/GBP cross. Analysis-only until historical MMM edge is proven.",
    ),

    "EURCHF": PairProfile(
        symbol="EURCHF",
        risk_tier="low",
        max_risk_pct=0.01,
        max_spread_pips=2.5,
        stale_minutes=90,
        stale_exit_minutes=90,            # Low-vol: exit at 90 (validated 86.5% — strongest)
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=8.0,         # Lowered from 10: catch small moves earlier
        trail_distance_pips=6.0,           # Tightened from 8
        sl_buffer_pips=3.0,
        min_sl_pips=10.0,                  # Ultra-low vol — tightest floor
        stop_hunt_min_pips=15.0,           # Tight ranges, small hunts
        stop_hunt_max_pips=40.0,           # CALIBRATED: was 30, P90=38p
        expected_level_move_pips=45.0,     # Smallest ADR of all pairs
        asian_range_max_pips=25.0,         # Often < 20 pip Asian ranges
        notes="Ultra-low vol. ~$11/pip. Tight ranges. Clean accumulation detection.",
    ),

    # --- CHF Crosses ---

    "GBPCHF": PairProfile(
        symbol="GBPCHF",
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=4.0,
        stale_minutes=90,
        stale_exit_minutes=90,            # Low-vol behavior (77.7% — validated)
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=18.0,        # Lowered from 22: catch runs earlier
        trail_distance_pips=14.0,          # Tightened from 16
        sl_buffer_pips=4.0,
        min_sl_pips=20.0,
        stop_hunt_min_pips=25.0,
        stop_hunt_max_pips=70.0,           # CALIBRATED: was 50, P90=67p
        expected_level_move_pips=85.0,
        asian_range_max_pips=50.0,
        notes="GBP vol + CHF safe-haven. ~$11/pip. Cleaner M/W than GBPNZD.",
    ),

    "USDCHF": PairProfile(
        symbol="USDCHF",
        risk_tier="low",
        max_risk_pct=0.01,
        max_spread_pips=2.0,
        stale_minutes=90,
        stale_exit_minutes=90,            # Low-vol: exit at 90 (validated 69.2%)
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=12.0,        # Lowered from 15: catch moves earlier
        trail_distance_pips=10.0,          # Tightened from 12
        sl_buffer_pips=3.0,
        min_sl_pips=15.0,
        stop_hunt_min_pips=20.0,
        stop_hunt_max_pips=55.0,           # CALIBRATED: was 40, P90=52p
        expected_level_move_pips=60.0,
        asian_range_max_pips=35.0,
        notes="Inverse EURUSD. ~$11/pip. Cross-validates EUR bias.",
    ),

    # --- JPY Majors ---

    "USDJPY": PairProfile(
        symbol="USDJPY",
        tradeable=False,                   # DISABLED: weak M/W (47.4%), weak stale exit (53.3%)
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=2.5,
        stale_minutes=90,
        stale_exit_minutes=90,            # Borderline (53.3%) — keep 90 for safety
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,
        trail_distance_pips=15.0,
        sl_buffer_pips=4.0,
        min_sl_pips=20.0,
        stop_hunt_min_pips=25.0,
        stop_hunt_max_pips=100.0,          # CALIBRATED: was 50, P90=97p
        expected_level_move_pips=80.0,
        asian_range_max_pips=45.0,
        notes="Most liquid JPY pair. ~$6.6/pip. Complements all JPY crosses.",
    ),

    "AUDJPY": PairProfile(
        symbol="AUDJPY",
        tradeable=False,                   # DISABLED: +$0.76 in 14-day backtest, 25% win rate
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=3.5,
        stale_minutes=90,
        stale_exit_minutes=90,            # Borderline (60.7%) — keep 90 for safety
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=18.0,
        trail_distance_pips=14.0,
        sl_buffer_pips=4.0,
        min_sl_pips=18.0,
        stop_hunt_min_pips=20.0,
        stop_hunt_max_pips=90.0,           # CALIBRATED: was 45, P90=89p
        expected_level_move_pips=75.0,
        asian_range_max_pips=45.0,
        notes="Commodity+JPY. ~$6.6/pip. Shows fractional disparity when AUD hits L3.",
    ),

    # --- Gold ---
    # Completely different pip value structure: 1 pip = $0.01, pip value = $1/pip per lot
    # Violent reversals, requires minimal risk and short duration

    "XAUUSD": PairProfile(
        symbol="XAUUSD",
        tradeable=False,                   # DISABLED: -$14 in 14-day backtest, parameters need fundamental rework
        risk_tier="high",
        max_risk_pct=0.005,               # 0.5% — gold is brutal
        max_lot_size=0.1,                  # Hard cap
        max_spread_pips=5.0,
        stale_minutes=90,
        stale_exit_minutes=90,            # Gold is violent — no extension
        stale_max_pips=0.0,               # Must be in profit
        max_duration_minutes=180,          # 3h max — gold reversals are violent
        trail_activation_pips=100.0,       # Gold "pips" = cents. 100 pips = $1.00 move
        trail_distance_pips=80.0,
        t1_rr=1.0,
        partial_close_ratio=0.50,
        sl_buffer_pips=30.0,              # 30 pips = $0.30
        min_sl_pips=150.0,                 # Gold min SL = $1.50 move
        stop_hunt_min_pips=200.0,         # Gold stop hunts in "pips" are huge
        stop_hunt_max_pips=15000.0,        # CALIBRATED: was 500, P90=15505p ($155 move)
        expected_level_move_pips=800.0,    # Gold level moves = $8.00
        asian_range_max_pips=8000.0,       # CALIBRATED: was 400, all days exceeded — $80 range
        notes="GOLD. 1 pip=$0.01. $1/pip/lot. Violent. Min risk. Short duration.",
    ),

    # --- Indices ---
    # Broker point/pip conventions vary. Keep analysis-only until symbol-specific
    # replay calibration proves valid risk units and positive edge.

    "US30": PairProfile(
        symbol="US30",
        tradeable=False,
        risk_tier="high",
        max_risk_pct=0.003,
        max_lot_size=0.1,
        max_spread_pips=80.0,
        stale_minutes=60,
        stale_exit_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=180,
        trail_activation_pips=250.0,
        trail_distance_pips=180.0,
        sl_buffer_pips=50.0,
        min_sl_pips=300.0,
        stop_hunt_min_pips=250.0,
        stop_hunt_max_pips=2500.0,
        expected_level_move_pips=1200.0,
        asian_range_max_pips=4000.0,
        notes="Dow/US30 index. Analysis-only; broker point values require calibration.",
    ),

    "USTEC": PairProfile(
        symbol="USTEC",
        tradeable=False,
        risk_tier="high",
        max_risk_pct=0.003,
        max_lot_size=0.1,
        max_spread_pips=80.0,
        stale_minutes=60,
        stale_exit_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=180,
        trail_activation_pips=180.0,
        trail_distance_pips=130.0,
        sl_buffer_pips=40.0,
        min_sl_pips=220.0,
        stop_hunt_min_pips=180.0,
        stop_hunt_max_pips=2200.0,
        expected_level_move_pips=900.0,
        asian_range_max_pips=3500.0,
        notes="Nasdaq/USTEC index. Analysis-only; broker point values require calibration.",
    ),
}


def get_tradeable_symbols() -> List[str]:
    """Return symbols with tradeable=True."""
    return [sym for sym, p in PAIR_PROFILES.items() if p.tradeable]


def get_pair_profile(symbol: str) -> PairProfile:
    """Get the profile for a symbol, or return a conservative default."""
    if symbol in PAIR_PROFILES:
        return PAIR_PROFILES[symbol]

    return PairProfile(
        symbol=symbol,
        risk_tier="medium",
        max_risk_pct=0.008,
        max_spread_pips=4.0,
        stale_minutes=90,
        stale_exit_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,
        trail_distance_pips=15.0,
        sl_buffer_pips=4.0,
        notes="Unknown pair — conservative defaults.",
    )


def resolve_profile(symbol: str, atr_pips: Optional[float]) -> PairProfile:
    """ATR-resolved copy of the pair profile (audit Tier 2.3).

    The eight pip-denominated gates become GATE_RATIOS x ATR(20, D1).
    Floors are true per-instrument facts, expressed in spreads:
      - sl_buffer  >= 1 full spread (a buffer inside the spread is noise)
      - trail_distance >= 2 spreads (trailing closer than spread churns)
      - min_sl     >= 4 spreads (never size off a stop the spread can eat)

    Falls back to the static profile when ATR is unavailable (None/<=0).
    """
    pp = get_pair_profile(symbol)
    if not atr_pips or atr_pips <= 0:
        return pp

    r = GATE_RATIOS
    spread = pp.max_spread_pips
    trail_distance = max(r.trail_distance * atr_pips, 2.0 * spread)
    return replace(
        pp,
        atr_pips=round(atr_pips, 1),
        asian_range_max_pips=round(r.asian_range_max * atr_pips, 1),
        stop_hunt_min_pips=round(r.stop_hunt_min * atr_pips, 1),
        stop_hunt_max_pips=round(r.stop_hunt_max * atr_pips, 1),
        expected_level_move_pips=round(r.expected_level_move * atr_pips, 1),
        trail_activation_pips=round(max(r.trail_activation * atr_pips, trail_distance), 1),
        trail_distance_pips=round(trail_distance, 1),
        sl_buffer_pips=round(max(r.sl_buffer * atr_pips, spread), 1),
        min_sl_pips=round(max(r.min_sl * atr_pips, 4.0 * spread), 1),
    )


def print_pair_profiles() -> str:
    lines = [
        "",
        "=" * 105,
        "  HELIX V3 PAIR RISK PROFILES (Calibrated from 90-day validation 2026-06-07)",
        "  Stale: Phase1=tighten SL at 90min, Phase2=exit at pair-specific limit.",
        "=" * 105,
        "",
        f"  {'Symbol':8} {'Tier':6} {'Risk%':>6} {'MaxLot':>6} {'Spread':>6} "
        f"{'MinSL':>5} {'Trail':>10} {'SLBuf':>5} {'HuntRange':>12} {'LvlMove':>7} {'Stale':>8}",
        "-" * 105,
    ]

    for _sym, p in PAIR_PROFILES.items():
        stale_str = f"{p.stale_minutes}/{p.stale_exit_minutes}"
        lines.append(
            f"  {p.symbol:8} {p.risk_tier:6} {p.max_risk_pct*100:>5.1f}% "
            f"{p.max_lot_size:>6.1f} {p.max_spread_pips:>5.1f}p "
            f"{p.min_sl_pips:>4.0f}p "
            f"{p.trail_activation_pips:>4.0f}/{p.trail_distance_pips:.0f}p "
            f"{p.sl_buffer_pips:>4.0f}p "
            f"{p.stop_hunt_min_pips:.0f}-{p.stop_hunt_max_pips:.0f}p "
            f"{p.expected_level_move_pips:>5.0f}p"
            f" {stale_str:>8}"
        )

    lines.append("")
    lines.append("  Stale: 90/90 = immediate exit at 90min. 90/150 = tighten SL at 90, exit at 150.")
    lines.append("  Risk Tiers: low=1%, medium=0.8%, high=0.5% per trade")
    lines.append("=" * 105)
    return "\n".join(lines)
