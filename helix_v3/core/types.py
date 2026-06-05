from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Direction(Enum):
    BUY = "BUY"
    SELL = "SELL"
    NEUTRAL = "NEUTRAL"


class CycleLevel(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3


class SignalStrength(Enum):
    WEAK = "WEAK"
    MODERATE = "MODERATE"
    STRONG = "STRONG"


@dataclass
class SessionBounds:
    high: float
    low: float
    range_pips: float
    volatility_compression: float
    is_accumulation: bool
    timestamp: datetime


@dataclass
class StopHuntSignal:
    direction: Direction
    breach_pips: float
    z_score: float
    is_absorption: bool
    timestamp: datetime


@dataclass
class EMAVector:
    ema_5_angle: float
    ema_13_angle: float
    ema_50_angle: float
    ema_200_angle: float
    ema_800_angle: float
    fast_slow_divergence: float
    trend_alignment: Direction


@dataclass
class QuantSignal:
    symbol: str
    timeframe: str
    timestamp: datetime
    session_bounds: Optional[SessionBounds]
    stop_hunt: Optional[StopHuntSignal]
    ema_vector: EMAVector
    accumulation_active: bool
    stop_hunt_detected: bool
    pre_filter_passed: bool


@dataclass
class VisionVerdict:
    model_name: str
    direction: Direction
    confidence: float
    cycle_level: Optional[CycleLevel]
    m_w_detected: bool
    rrt_detected: bool
    pin_bar_detected: bool
    setup_class: str = "UNKNOWN"
    entry_quality: int = 0
    risk_flags: list[str] = field(default_factory=list)
    expected_path: str = ""
    invalidation: str = ""
    reasoning: str = ""
    raw_json: dict = field(default_factory=dict)


@dataclass
class ConsensusResult:
    agreed: bool
    direction: Direction
    avg_confidence: float
    verdicts: list[VisionVerdict] = field(default_factory=list)
    divergence_notes: str = ""


@dataclass
class ExecutionOrder:
    symbol: str
    direction: Direction
    lot_size: float
    entry_price: float
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    sl_pips: float
    risk_reward: float
    ticket: Optional[int] = None
    status: str = "PENDING"
