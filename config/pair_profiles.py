"""Pair-gated risk and trade management profiles.

Calibrated from MMM Book (Steve Mauro) methodology:
- 90 min universal stale exit if NOT in profit (M/W formation window is 30-90 min)
- If IN profit, trail SL to secure gains — never exit a winning trade early
- Stop hunt range 25-50 pips (pair-specific based on volatility)
- L1/L2 average move ~75 pips from peak to consolidation
- BE after 50 pips, trail after L1 consolidation clears
- Pip value differences gate risk % and lot sizing per pair
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class PairProfile:
    symbol: str

    # Risk tier: "low" = standard, "medium" = reduced risk, "high" = minimal risk
    risk_tier: str = "low"
    max_risk_pct: float = 0.01           # Max risk per trade
    max_lot_size: float = 1.0            # Hard lot cap

    # Spread
    max_spread_pips: float = 3.0         # Block entry above this

    # --- UNIVERSAL RULE: 90 min stale if NOT in profit ---
    # All pairs use 90 min. If not in profit after 90 min, exit.
    # If IN profit, the trade stays open and trails.
    stale_minutes: int = 90
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

    # MMM stop hunt range (used for entry zone detection)
    stop_hunt_min_pips: float = 25.0     # Min expected stop hunt from Asian range
    stop_hunt_max_pips: float = 50.0     # Max expected stop hunt

    # Expected L1/L2 move size (peak to consolidation)
    expected_level_move_pips: float = 75.0

    # Asian range max for valid accumulation
    asian_range_max_pips: float = 50.0

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
        stale_max_pips=0.0,               # Must be in profit by 90 min
        max_duration_minutes=240,          # 4h max
        trail_activation_pips=15.0,        # BE after 15 pips (conservative EUR)
        trail_distance_pips=12.0,          # Tight trail — EUR doesn't whipsaw much
        sl_buffer_pips=3.0,
        stop_hunt_min_pips=20.0,           # EUR hunts are tighter
        stop_hunt_max_pips=40.0,
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
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,        # GBP needs more room
        trail_distance_pips=15.0,
        sl_buffer_pips=3.0,
        stop_hunt_min_pips=25.0,           # Standard MMM range
        stop_hunt_max_pips=50.0,
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
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=12.0,        # AUD is slower
        trail_distance_pips=10.0,
        sl_buffer_pips=3.0,
        stop_hunt_min_pips=15.0,           # AUD hunts are smaller
        stop_hunt_max_pips=35.0,
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
        stale_minutes=90,                  # UNIVERSAL: 90 min
        stale_max_pips=0.0,               # Must be in profit
        max_duration_minutes=300,          # 5h — crosses can trend longer
        trail_activation_pips=30.0,        # Wide ATR needs room
        trail_distance_pips=22.0,
        sl_buffer_pips=5.0,               # Wider — spiky pair
        stop_hunt_min_pips=30.0,
        stop_hunt_max_pips=60.0,           # Wider stop hunts on crosses
        expected_level_move_pips=100.0,    # Big moves
        asian_range_max_pips=60.0,
        notes="Volatile cross. ~$7.3/pip. Spiky. Wider everything.",
    ),

    "GBPJPY": PairProfile(
        symbol="GBPJPY",
        risk_tier="medium",
        max_risk_pct=0.008,               # 0.8% — JPY pip value ~$6.6/pip
        max_lot_size=0.5,
        max_spread_pips=4.0,
        stale_minutes=90,                  # UNIVERSAL: 90 min
        stale_max_pips=0.0,               # Must be in profit
        max_duration_minutes=240,
        trail_activation_pips=25.0,        # GJ can run 150+ pips
        trail_distance_pips=18.0,
        sl_buffer_pips=5.0,               # Wider for JPY volatility
        stop_hunt_min_pips=30.0,           # GJ stop hunts are aggressive
        stop_hunt_max_pips=60.0,           # Per MMM book: more volatile = wider
        expected_level_move_pips=100.0,    # GJ does 100+ pip level moves
        asian_range_max_pips=50.0,
        notes="High vol JPY cross. ~$6.6/pip. Fast moves. MMM book says wider range.",
    ),

    "GBPNZD": PairProfile(
        symbol="GBPNZD",
        risk_tier="medium",
        max_risk_pct=0.008,               # 0.8% — NZD pip value ~$5.8/pip
        max_lot_size=0.5,
        max_spread_pips=5.0,              # Widest spreads of the set
        stale_minutes=90,                  # UNIVERSAL: 90 min
        stale_max_pips=0.0,
        max_duration_minutes=300,
        trail_activation_pips=35.0,        # Very wide ATR
        trail_distance_pips=25.0,
        sl_buffer_pips=5.0,
        stop_hunt_min_pips=30.0,
        stop_hunt_max_pips=65.0,           # Widest stop hunts
        expected_level_move_pips=110.0,
        asian_range_max_pips=65.0,
        notes="Widest spreads. ~$5.8/pip. Only trade London/NY. Big moves.",
    ),

    # --- EUR Crosses (MMM fractional disparity group) ---

    "EURJPY": PairProfile(
        symbol="EURJPY",
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=3.0,
        stale_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,
        trail_distance_pips=15.0,
        sl_buffer_pips=4.0,
        stop_hunt_min_pips=25.0,
        stop_hunt_max_pips=50.0,
        expected_level_move_pips=85.0,
        asian_range_max_pips=50.0,
        notes="EUR+JPY cross. ~$6.6/pip. Shows cycle disparity vs EURUSD.",
    ),

    "EURCHF": PairProfile(
        symbol="EURCHF",
        risk_tier="low",
        max_risk_pct=0.01,
        max_spread_pips=2.5,
        stale_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=10.0,        # Very low vol — small moves matter
        trail_distance_pips=8.0,
        sl_buffer_pips=3.0,
        stop_hunt_min_pips=15.0,           # Tight ranges, small hunts
        stop_hunt_max_pips=30.0,
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
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=22.0,
        trail_distance_pips=16.0,
        sl_buffer_pips=4.0,
        stop_hunt_min_pips=25.0,
        stop_hunt_max_pips=50.0,
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
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=15.0,
        trail_distance_pips=12.0,
        sl_buffer_pips=3.0,
        stop_hunt_min_pips=20.0,
        stop_hunt_max_pips=40.0,
        expected_level_move_pips=60.0,
        asian_range_max_pips=35.0,
        notes="Inverse EURUSD. ~$11/pip. Cross-validates EUR bias.",
    ),

    # --- JPY Majors ---

    "USDJPY": PairProfile(
        symbol="USDJPY",
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=2.5,
        stale_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,
        trail_distance_pips=15.0,
        sl_buffer_pips=4.0,
        stop_hunt_min_pips=25.0,
        stop_hunt_max_pips=50.0,
        expected_level_move_pips=80.0,
        asian_range_max_pips=45.0,
        notes="Most liquid JPY pair. ~$6.6/pip. Complements all JPY crosses.",
    ),

    "AUDJPY": PairProfile(
        symbol="AUDJPY",
        risk_tier="medium",
        max_risk_pct=0.008,
        max_lot_size=0.5,
        max_spread_pips=3.5,
        stale_minutes=90,
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=18.0,
        trail_distance_pips=14.0,
        sl_buffer_pips=4.0,
        stop_hunt_min_pips=20.0,
        stop_hunt_max_pips=45.0,
        expected_level_move_pips=75.0,
        asian_range_max_pips=45.0,
        notes="Commodity+JPY. ~$6.6/pip. Shows fractional disparity when AUD hits L3.",
    ),

    # --- Gold ---
    # Completely different pip value structure: 1 pip = $0.01, pip value = $1/pip per lot
    # Violent reversals, requires minimal risk and short duration

    "XAUUSD": PairProfile(
        symbol="XAUUSD",
        risk_tier="high",
        max_risk_pct=0.005,               # 0.5% — gold is brutal
        max_lot_size=0.1,                  # Hard cap
        max_spread_pips=5.0,
        stale_minutes=90,                  # UNIVERSAL: 90 min even for gold
        stale_max_pips=0.0,               # Must be in profit
        max_duration_minutes=180,          # 3h max — gold reversals are violent
        trail_activation_pips=100.0,       # Gold "pips" = cents. 100 pips = $1.00 move
        trail_distance_pips=80.0,
        t1_rr=1.0,
        partial_close_ratio=0.50,
        sl_buffer_pips=30.0,              # 30 pips = $0.30
        stop_hunt_min_pips=200.0,         # Gold stop hunts in "pips" are huge
        stop_hunt_max_pips=500.0,
        expected_level_move_pips=800.0,    # Gold level moves = $8.00
        asian_range_max_pips=400.0,        # Gold Asian range in pips
        notes="GOLD. 1 pip=$0.01. $1/pip/lot. Violent. Min risk. Short duration.",
    ),
}


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
        stale_max_pips=0.0,
        max_duration_minutes=240,
        trail_activation_pips=20.0,
        trail_distance_pips=15.0,
        sl_buffer_pips=4.0,
        notes="Unknown pair — conservative defaults.",
    )


def print_pair_profiles() -> str:
    lines = [
        "",
        "=" * 95,
        "  HELIX V3 PAIR RISK PROFILES (MMM Calibrated)",
        "  Rule: 90 min max if NOT in profit. If in profit, trail SL.",
        "=" * 95,
        "",
        f"  {'Symbol':8} {'Tier':6} {'Risk%':>6} {'MaxLot':>6} {'Spread':>6} "
        f"{'Stale':>5} {'MaxDur':>6} {'Trail':>10} {'SLBuf':>5} {'HuntRange':>10} {'LvlMove':>7}",
        "-" * 95,
    ]

    for sym, p in PAIR_PROFILES.items():
        lines.append(
            f"  {p.symbol:8} {p.risk_tier:6} {p.max_risk_pct*100:>5.1f}% "
            f"{p.max_lot_size:>6.1f} {p.max_spread_pips:>5.1f}p "
            f"{p.stale_minutes:>3}m  "
            f"{p.max_duration_minutes:>4}m "
            f"{p.trail_activation_pips:>4.0f}/{p.trail_distance_pips:.0f}p "
            f"{p.sl_buffer_pips:>4.0f}p "
            f"{p.stop_hunt_min_pips:.0f}-{p.stop_hunt_max_pips:.0f}p "
            f"{p.expected_level_move_pips:>5.0f}p"
        )

    lines.append("")
    lines.append("  Stale Rule: Exit at 90 min if pips <= 0 (universal). If pips > 0, trail SL.")
    lines.append("  Risk Tiers: low=1%, medium=0.8%, high=0.5% per trade")
    lines.append("=" * 95)
    return "\n".join(lines)
