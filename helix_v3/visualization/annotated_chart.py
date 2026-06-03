"""Annotated Chart Generator for WhatsApp Flashcards.

Extends the base chart exporter with visual markup annotations showing:
- Asian range bounding box (labeled)
- Stop hunt zone (shaded region above/below Asian range)
- M/W peak markers
- Entry zone arrow
- EMA interaction points (circles)
- HOD/LOD markers
- Confluence zone highlighting
- Direction arrow with label

Output is a standalone PNG that can be:
1. Attached to WhatsApp via Twilio MMS (MediaUrl)
2. Saved as a flashcard in the database
3. Uploaded to a temporary hosting service for URL access
"""

from __future__ import annotations

import base64
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import mplfinance as mpf
import numpy as np
import pandas as pd

from config.pair_profiles import PairProfile, get_pair_profile
from config.settings import settings
from helix_v3.utils.logger import get_logger

matplotlib.use("Agg")
logger = get_logger("annotated_chart")

EAT = timezone(timedelta(hours=3))


class AnnotatedChartGenerator:
    """Generates charts with visual confluence markings for flashcards."""

    def __init__(self) -> None:
        self._cfg = settings.chart
        self._output_dir = Path(self._cfg.output_dir) / "annotated"
        self._output_dir.mkdir(parents=True, exist_ok=True)

    def generate(
        self,
        df: pd.DataFrame,
        symbol: str,
        timeframe: str,
        annotations: Dict,
    ) -> Tuple[str, Path]:
        """Generate an annotated chart with confluence markings.

        Args:
            df: OHLCV DataFrame with DatetimeIndex.
            symbol: Trading pair.
            timeframe: Chart timeframe.
            annotations: Dict with keys like:
                - direction: "BUY" or "SELL"
                - confidence: 0.0-1.0
                - confluence_score: 0-100
                - asian_high, asian_low: float
                - stop_hunt_high, stop_hunt_low: float (hunt zone bounds)
                - entry_price: float
                - stop_loss: float
                - tp1, tp2: float
                - hod, lod: float
                - m_w_peaks: list of (index, price) tuples
                - ema_interactions: list of (index, price) tuples
                - cycle_level: int
                - session: str
                - weekly_trend: str
                - notes: list of str

        Returns:
            Tuple of (base64_image, file_path).
        """
        pp = get_pair_profile(symbol)
        bar_count = min(self._cfg.bar_count, len(df))
        subset = df.iloc[-bar_count:].copy()

        bg = self._cfg.background_color

        # EMA overlays
        closes = df["Close"]
        ema_addplots = []
        for period in settings.trading.ema_periods:
            ema = closes.ewm(span=period, adjust=False).mean().iloc[-bar_count:]
            color = self._cfg.ema_colors.get(period, "#FFFFFF")
            width = {5: 0.8, 13: 0.8, 50: 1.2, 200: 1.5, 800: 2.0}.get(period, 1.0)
            ema_addplots.append(
                mpf.make_addplot(ema, color=color, width=width, secondary_y=False)
            )

        # Build style
        style = mpf.make_mpf_style(
            base_mpf_style="nightclouds",
            marketcolors=mpf.make_marketcolors(
                up="#26a69a", down="#ef5350", edge="inherit", wick="inherit", volume="in",
            ),
            facecolor=bg, figcolor=bg, gridstyle="", gridcolor=bg,
            rc={"axes.edgecolor": bg, "axes.labelcolor": bg,
                "xtick.color": bg, "ytick.color": bg},
        )

        res = self._cfg.resolution

        fig, axes = mpf.plot(
            subset, type="candle", style=style,
            addplot=ema_addplots if ema_addplots else None,
            volume=False,
            figsize=(res / self._cfg.dpi, res / self._cfg.dpi),
            returnfig=True, tight_layout=True,
            xrotation=0, datetime_format="", show_nontrading=False,
        )

        ax = axes[0]

        # Strip default ticks
        for a in fig.get_axes():
            a.set_xticklabels([])
            a.set_yticklabels([])
            a.tick_params(left=False, right=False, bottom=False, top=False,
                          labelleft=False, labelright=False,
                          labelbottom=False, labeltop=False)
            for spine in a.spines.values():
                spine.set_visible(False)

        # === DRAW ANNOTATIONS ===
        y_min = subset["Low"].min()
        y_max = subset["High"].max()
        y_range = y_max - y_min
        x_len = len(subset)

        # 1. Asian Range Box
        asian_h = annotations.get("asian_high")
        asian_l = annotations.get("asian_low")
        if asian_h and asian_l:
            rect = mpatches.Rectangle(
                (0, asian_l), x_len * 0.4, asian_h - asian_l,
                linewidth=1, edgecolor="#888888", facecolor="#888888",
                alpha=0.12, zorder=1,
            )
            ax.add_patch(rect)
            ax.text(
                x_len * 0.02, asian_h + y_range * 0.01,
                "ASIAN RANGE", color="#888888", fontsize=7, fontweight="bold",
                zorder=10,
            )

        # 2. Stop Hunt Zone (shaded red/green above/below Asian range)
        hunt_h = annotations.get("stop_hunt_high")
        hunt_l = annotations.get("stop_hunt_low")
        if hunt_h and asian_h:
            rect = mpatches.Rectangle(
                (0, asian_h), x_len * 0.6, hunt_h - asian_h,
                linewidth=0, facecolor="#FF4444", alpha=0.08, zorder=1,
            )
            ax.add_patch(rect)
            ax.text(
                x_len * 0.02, hunt_h + y_range * 0.005,
                "STOP HUNT ZONE", color="#FF6666", fontsize=6, zorder=10,
            )
        if hunt_l and asian_l:
            rect = mpatches.Rectangle(
                (0, hunt_l), x_len * 0.6, asian_l - hunt_l,
                linewidth=0, facecolor="#FF4444", alpha=0.08, zorder=1,
            )
            ax.add_patch(rect)

        # 3. HOD / LOD horizontal lines
        hod = annotations.get("hod")
        lod = annotations.get("lod")
        if hod:
            ax.axhline(y=hod, color="#FF9800", linewidth=0.7, linestyle="--", alpha=0.6, zorder=2)
            ax.text(x_len * 0.85, hod + y_range * 0.005, "HOD", color="#FF9800", fontsize=6, zorder=10)
        if lod:
            ax.axhline(y=lod, color="#2196F3", linewidth=0.7, linestyle="--", alpha=0.6, zorder=2)
            ax.text(x_len * 0.85, lod - y_range * 0.015, "LOD", color="#2196F3", fontsize=6, zorder=10)

        # 4. Entry zone + SL + TP markers
        entry = annotations.get("entry_price")
        sl = annotations.get("stop_loss")
        tp1 = annotations.get("tp1")
        tp2 = annotations.get("tp2")
        direction = annotations.get("direction", "")

        if entry:
            entry_color = "#00E676" if direction == "BUY" else "#FF5252"
            ax.axhline(y=entry, color=entry_color, linewidth=1.2, linestyle="-", alpha=0.8, zorder=5)
            # Entry arrow
            arrow_y_offset = y_range * 0.03 if direction == "BUY" else -y_range * 0.03
            ax.annotate(
                f"ENTRY {direction}",
                xy=(x_len - 5, entry), xytext=(x_len - 20, entry + arrow_y_offset),
                color=entry_color, fontsize=7, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=entry_color, lw=1.5),
                zorder=10,
            )

        if sl:
            ax.axhline(y=sl, color="#FF1744", linewidth=0.8, linestyle="-.", alpha=0.7, zorder=4)
            ax.text(x_len * 0.7, sl - y_range * 0.015, "SL", color="#FF1744", fontsize=6, fontweight="bold", zorder=10)
        if tp1:
            ax.axhline(y=tp1, color="#00C853", linewidth=0.6, linestyle=":", alpha=0.5, zorder=3)
            ax.text(x_len * 0.7, tp1 + y_range * 0.005, "TP1 (1:1)", color="#00C853", fontsize=5, zorder=10)
        if tp2:
            ax.axhline(y=tp2, color="#00C853", linewidth=0.6, linestyle=":", alpha=0.5, zorder=3)
            ax.text(x_len * 0.7, tp2 + y_range * 0.005, "TP2", color="#00C853", fontsize=5, zorder=10)

        # 5. M/W peak markers
        m_w_peaks = annotations.get("m_w_peaks", [])
        for idx, price in m_w_peaks:
            if 0 <= idx < x_len:
                ax.plot(idx, price, marker="v" if direction == "SELL" else "^",
                        color="#FFD600", markersize=8, zorder=8)

        # 6. EMA interaction circles
        ema_interactions = annotations.get("ema_interactions", [])
        for idx, price in ema_interactions:
            if 0 <= idx < x_len:
                ax.plot(idx, price, marker="o", color="#E040FB",
                        markersize=6, markerfacecolor="none", markeredgewidth=1.5, zorder=7)

        # 7. Info box (top-left)
        conf = annotations.get("confidence", 0)
        confluence = annotations.get("confluence_score", 0)
        cycle = annotations.get("cycle_level", 0)
        session = annotations.get("session", "")
        weekly = annotations.get("weekly_trend", "")

        info_lines = [
            f"{symbol} {timeframe}",
            f"Dir: {direction} | Conf: {conf:.0%}",
            f"Confluence: {confluence}/100 | L{cycle}",
        ]
        if session:
            info_lines.append(f"Session: {session}")
        if weekly:
            info_lines.append(f"Weekly: {weekly}")

        # Notes
        notes = annotations.get("notes", [])
        for n in notes[:3]:
            info_lines.append(n[:40])

        info_text = "\n".join(info_lines)
        ax.text(
            0.02, 0.98, info_text,
            transform=ax.transAxes, fontsize=6, color="#CCCCCC",
            verticalalignment="top", fontfamily="monospace",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a2e", alpha=0.85, edgecolor="#333333"),
            zorder=20,
        )

        # 8. Timestamp (bottom-right)
        ts = datetime.now(EAT).strftime("%Y-%m-%d %H:%M EAT")
        ax.text(
            0.98, 0.02, ts,
            transform=ax.transAxes, fontsize=5, color="#666666",
            horizontalalignment="right", verticalalignment="bottom",
            zorder=20,
        )

        # Export
        buf = BytesIO()
        fig.savefig(
            buf, format="png", dpi=self._cfg.dpi,
            bbox_inches="tight", pad_inches=0.02,
            facecolor=bg,
        )
        plt.close(fig)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode("utf-8")

        ts_file = datetime.now(EAT).strftime("%Y%m%d_%H%M%S")
        filename = f"{symbol}_{timeframe}_annotated_{ts_file}.png"
        file_path = self._output_dir / filename
        buf.seek(0)
        file_path.write_bytes(buf.read())

        logger.info("Annotated chart exported: %s", file_path)
        return b64, file_path

    def generate_from_mtf(
        self,
        df: pd.DataFrame,
        symbol: str,
        timeframe: str,
        mtf_analysis,
    ) -> Tuple[str, Path]:
        """Generate annotated chart directly from an MTFAnalysis result."""
        pp = get_pair_profile(symbol)
        pip_size = pp.stop_hunt_min_pips  # for computing hunt zone bounds

        a = mtf_analysis
        m15 = a.fifteen_min
        h1 = a.one_hour

        # Build annotation dict from MTF analysis
        annotations = {
            "direction": a.trade_direction.value,
            "confidence": a.trade_confidence,
            "confluence_score": a.confluence_score,
            "cycle_level": a.four_hour.level_count,
            "session": h1.session_phase.value if h1 else "",
            "weekly_trend": a.weekly.trend_direction.value,
            "asian_high": m15.asian_range_high,
            "asian_low": m15.asian_range_low,
            "hod": h1.hod,
            "lod": h1.lod,
            "notes": [],
        }

        # Stop hunt zone
        if m15.stop_hunt_detected:
            if m15.stop_hunt_direction.value == "SELL":
                annotations["stop_hunt_high"] = m15.asian_range_high + m15.stop_hunt_pips * pp.sl_buffer_pips
            else:
                annotations["stop_hunt_low"] = m15.asian_range_low - m15.stop_hunt_pips * pp.sl_buffer_pips
            annotations["notes"].append(f"Stop hunt: {m15.stop_hunt_direction.value} {m15.stop_hunt_pips:.1f}p")

        if m15.m_w_forming:
            annotations["notes"].append("M/W formation detected")
        if m15.rrt_detected:
            annotations["notes"].append("Railroad Tracks detected")
        if m15.push_count >= 3:
            annotations["notes"].append(f"{m15.push_count} pushes (target: 3)")

        # Rejection reasons
        for r in a.rejection_reasons[:2]:
            annotations["notes"].append(f"WARN: {r[:35]}")

        return self.generate(df, symbol, timeframe, annotations)
