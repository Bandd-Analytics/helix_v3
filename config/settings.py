from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class MT5Config:
    login: int = int(os.getenv("MT5_LOGIN", "0"))
    password: str = os.getenv("MT5_PASSWORD", "")
    server: str = os.getenv("MT5_SERVER", "")
    path: str = os.getenv("MT5_PATH", "")


@dataclass(frozen=True)
class APIConfig:
    anthropic_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    openai_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_model: str = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")
    anthropic_fast_model: str = os.getenv("ANTHROPIC_FAST_MODEL", "claude-sonnet-4-6")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-5.5")
    openai_embedding_model: str = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    model_routing_policy: str = os.getenv("MODEL_ROUTING_POLICY", "dual_provider")
    consensus_confidence_threshold: float = 0.88


@dataclass(frozen=True)
class RiskConfig:
    max_risk_per_trade: float = float(os.getenv("MAX_RISK_PER_TRADE", "0.01"))
    max_drawdown_pct: float = float(os.getenv("MAX_DRAWDOWN_PCT", "0.08"))
    max_concurrent_positions: int = int(os.getenv("MAX_CONCURRENT_POSITIONS", "3"))
    sl_buffer_pips: float = 3.0
    partial_close_ratio: float = 0.50
    partial_close_rr: float = 1.0
    # Trade management
    max_trade_duration_minutes: int = int(os.getenv("MAX_TRADE_DURATION_MIN", "240"))
    stale_trade_minutes: int = int(os.getenv("STALE_TRADE_MIN", "90"))
    stale_trade_max_pips: float = float(os.getenv("STALE_TRADE_MAX_PIPS", "5.0"))
    trailing_stop_enabled: bool = os.getenv("TRAILING_STOP", "true").lower() == "true"
    trailing_stop_activation_pips: float = float(os.getenv("TRAIL_ACTIVATION_PIPS", "20.0"))
    trailing_stop_distance_pips: float = float(os.getenv("TRAIL_DISTANCE_PIPS", "15.0"))
    close_before_session: str = os.getenv("CLOSE_BEFORE_SESSION", "ASIAN_EARLY")
    reentry_guard_ban_scope: str = os.getenv("REENTRY_GUARD_BAN_SCOPE", "direction").lower()


@dataclass(frozen=True)
class ChartConfig:
    output_dir: Path = Path(os.getenv("CHART_OUTPUT_DIR", str(BASE_DIR / "charts")))
    resolution: int = int(os.getenv("CHART_RESOLUTION", "1024"))
    bar_count: int = int(os.getenv("CHART_BAR_COUNT", "120"))
    dpi: int = 150
    background_color: str = "#0d1117"
    ema_colors: dict = field(default_factory=lambda: {
        5: "#FF0000",
        13: "#FFD700",
        50: "#00FFFF",
        200: "#FF00FF",
        800: "#FFFFFF",
    })
    session_box_color: str = "#AAAAAA"
    session_box_alpha: float = 0.1


@dataclass(frozen=True)
class TradingConfig:
    symbols: List[str] = field(
        default_factory=lambda: os.getenv("DEFAULT_PAIRS", "EURUSD,GBPUSD,AUDUSD").split(",")
    )
    ema_periods: List[int] = field(default_factory=lambda: [5, 13, 50, 200, 800])
    asian_session_start: int = 21  # EST hour
    asian_session_end: int = 2     # EST hour
    accumulation_percentile: float = 0.15  # 15th percentile
    accumulation_lookback_days: int = 20
    stop_hunt_min_pips: float = 15.0
    stop_hunt_max_pips: float = 30.0
    atr_multiplier_low: float = 1.5
    atr_multiplier_high: float = 2.5
    timeframes: dict = field(default_factory=lambda: {
        "M15": 15,
        "H1": 60,
    })


@dataclass(frozen=True)
class Settings:
    mt5: MT5Config = field(default_factory=MT5Config)
    api: APIConfig = field(default_factory=APIConfig)
    risk: RiskConfig = field(default_factory=RiskConfig)
    chart: ChartConfig = field(default_factory=ChartConfig)
    trading: TradingConfig = field(default_factory=TradingConfig)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_dir: Path = Path(os.getenv("LOG_DIR", str(BASE_DIR / "logs")))


settings = Settings()
