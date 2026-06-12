"""MMMChartVisualizer - High-fidelity chart exporter for vision model ingestion.

Renders clean, vector-geometry candlestick charts with EMA overlays and session
boxes optimized for GPT-5.5 and Claude Opus vision analysis.
"""

from __future__ import annotations

import base64
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path
from typing import Dict, Optional

import matplotlib
import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import pandas as pd

from config.settings import settings
from helix_v3.utils.logger import get_logger

matplotlib.use("Agg")

logger = get_logger("chart_visualizer")


class MMMChartVisualizer:
    """Transforms raw financial data into optimal visual inputs for vision models.

    Produces 1024x1024 clean candlestick charts with:
    - Color-coded EMA overlays (5/13/50/200/800)
    - Asian session bounding boxes
    - Day High/Low horizontal markers
    - No text labels, gridlines, or axis clutter
    """

    def __init__(self) -> None:
        self._cfg = settings.chart
        self._trading_cfg = settings.trading
        self._output_dir = Path(self._cfg.output_dir)
        self._output_dir.mkdir(parents=True, exist_ok=True)

        self._ema_colors: Dict[int, str] = dict(self._cfg.ema_colors)
        self._ema_widths: Dict[int, float] = {
            5: 0.8,
            13: 0.8,
            50: 1.2,
            200: 1.5,
            800: 2.0,
        }

    def _compute_emas(self, df: pd.DataFrame) -> Dict[int, pd.Series]:
        emas: Dict[int, pd.Series] = {}
        for period in self._trading_cfg.ema_periods:
            emas[period] = df["Close"].ewm(span=period, adjust=False).mean()
        return emas

    def _build_ema_addplots(
        self, emas: Dict[int, pd.Series], bar_count: int
    ) -> list:
        addplots = []
        for period, series in emas.items():
            color = self._ema_colors.get(period, "#FFFFFF")
            width = self._ema_widths.get(period, 1.0)
            addplots.append(
                mpf.make_addplot(
                    series.iloc[-bar_count:],
                    color=color,
                    width=width,
                    secondary_y=False,
                )
            )
        return addplots

    def _build_session_box(
        self, df: pd.DataFrame, bar_count: int
    ) -> list:
        """Create Asian session highlight as vertical spans."""
        subset = df.iloc[-bar_count:]
        est_offset = timedelta(hours=-5)

        session_start = self._trading_cfg.asian_session_start
        session_end = self._trading_cfg.asian_session_end

        session_mask = pd.Series(False, index=subset.index)
        hours_est = (subset.index + est_offset).hour

        if session_start > session_end:
            session_mask = (hours_est >= session_start) | (hours_est < session_end)
        else:
            session_mask = (hours_est >= session_start) & (hours_est < session_end)

        if not session_mask.any():
            return []

        # Create a fill between plot for the session region
        y_min = subset["Low"].min()
        y_max = subset["High"].max()
        session_series = pd.Series(np.nan, index=subset.index)
        session_series[session_mask] = y_max

        session_base = pd.Series(np.nan, index=subset.index)
        session_base[session_mask] = y_min

        plots = [
            mpf.make_addplot(
                session_series,
                type="scatter",
                marker="|",
                markersize=0.5,
                color=self._cfg.session_box_color,
                alpha=self._cfg.session_box_alpha,
                secondary_y=False,
            )
        ]
        return plots

    def _build_day_levels(
        self, df: pd.DataFrame, bar_count: int
    ) -> list:
        """Thin horizontal lines for day high/low."""
        subset = df.iloc[-bar_count:]
        day_high = subset["High"].max()
        day_low = subset["Low"].min()

        high_line = pd.Series(day_high, index=subset.index)
        low_line = pd.Series(day_low, index=subset.index)

        return [
            mpf.make_addplot(
                high_line,
                color="#555555",
                width=0.5,
                linestyle="dashed",
                secondary_y=False,
            ),
            mpf.make_addplot(
                low_line,
                color="#555555",
                width=0.5,
                linestyle="dashed",
                secondary_y=False,
            ),
        ]

    def _get_style(self) -> dict:
        bg = self._cfg.background_color
        return mpf.make_mpf_style(
            base_mpf_style="nightclouds",
            marketcolors=mpf.make_marketcolors(
                up="#26a69a",
                down="#ef5350",
                edge="inherit",
                wick="inherit",
                volume="in",
            ),
            facecolor=bg,
            figcolor=bg,
            gridstyle="",
            gridcolor=bg,
            rc={
                "axes.edgecolor": bg,
                "axes.labelcolor": bg,
                "xtick.color": bg,
                "ytick.color": bg,
            },
        )

    def export_vision_matrix(
        self,
        df: pd.DataFrame,
        symbol: str,
        timeframe: str,
        save_to_disk: bool = True,
    ) -> tuple[str, Optional[Path]]:
        """Export a clean chart image optimized for vision model consumption.

        Args:
            df: OHLCV DataFrame with DatetimeIndex.
            symbol: Trading pair symbol.
            timeframe: Chart timeframe label.
            save_to_disk: Whether to also save the PNG file.

        Returns:
            Tuple of (base64_encoded_image, file_path_or_None).
        """
        bar_count = min(self._cfg.bar_count, len(df))
        subset = df.iloc[-bar_count:].copy()

        emas = self._compute_emas(df)

        addplots = []
        addplots.extend(self._build_ema_addplots(emas, bar_count))
        addplots.extend(self._build_day_levels(df, bar_count))

        session_plots = self._build_session_box(df, bar_count)
        addplots.extend(session_plots)

        style = self._get_style()
        res = self._cfg.resolution

        fig, axes = mpf.plot(
            subset,
            type="candle",
            style=style,
            addplot=addplots if addplots else None,
            volume=False,
            figsize=(res / self._cfg.dpi, res / self._cfg.dpi),
            returnfig=True,
            tight_layout=True,
            xrotation=0,
            datetime_format="",
            show_nontrading=False,
        )

        # Strip all text, ticks, labels
        for ax in fig.get_axes():
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.tick_params(
                left=False, right=False, bottom=False, top=False,
                labelleft=False, labelright=False,
                labelbottom=False, labeltop=False,
            )
            ax.set_xlabel("")
            ax.set_ylabel("")
            for spine in ax.spines.values():
                spine.set_visible(False)

        # Export to base64
        buf = BytesIO()
        fig.savefig(
            buf,
            format="png",
            dpi=self._cfg.dpi,
            bbox_inches="tight",
            pad_inches=0,
            facecolor=self._cfg.background_color,
        )
        plt.close(fig)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode("utf-8")

        file_path: Optional[Path] = None
        if save_to_disk:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            filename = f"{symbol}_{timeframe}_{ts}.png"
            file_path = self._output_dir / filename
            buf.seek(0)
            file_path.write_bytes(buf.read())
            logger.info("Chart exported: %s", file_path)

        return b64, file_path
