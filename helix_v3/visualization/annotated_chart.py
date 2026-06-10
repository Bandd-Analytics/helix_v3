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
from typing import Dict, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import mplfinance as mpf
import pandas as pd

from config.settings import settings
from helix_v3.core.instruments import fallback_pip_size
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
                - prev_hod, prev_lod: float (previous day's HOD/LOD)
                - pivots: dict with PP, R1, R2, S1, S2, M1-M4
                - adr_high, adr_low: float (ADR projected levels)
                - tdi: TDIResult object (for TDI subplot)
                - patterns: list of DetectedPattern objects
                - session_boxes: list of (start_idx, end_idx, label) tuples
                - trade_type: str (MMM trade classification)
                - rrt_bars: list of bar indices with RRT patterns

        Returns:
            Tuple of (base64_image, file_path).
        """
        bar_count = min(self._cfg.bar_count, len(df))
        subset = df.iloc[-bar_count:].copy()

        bg = self._cfg.background_color
        tdi_data = annotations.get("tdi")
        has_tdi = tdi_data is not None

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

        # TDI addplots (rendered as panel 1 — the first subplot below price)
        if has_tdi:
            tdi_rsi = tdi_data.rsi_line.iloc[-bar_count:]
            tdi_signal = tdi_data.signal_line.iloc[-bar_count:]
            tdi_base = tdi_data.market_base.iloc[-bar_count:]
            tdi_upper = tdi_data.upper_vb.iloc[-bar_count:]
            tdi_lower = tdi_data.lower_vb.iloc[-bar_count:]

            ema_addplots.extend([
                mpf.make_addplot(tdi_rsi, panel=1, color="#00E676", width=1.0, ylabel="TDI"),
                mpf.make_addplot(tdi_signal, panel=1, color="#FF5252", width=0.8),
                mpf.make_addplot(tdi_base, panel=1, color="#FFD600", width=0.8),
                mpf.make_addplot(tdi_upper, panel=1, color="#42A5F5", width=0.5, linestyle="--"),
                mpf.make_addplot(tdi_lower, panel=1, color="#42A5F5", width=0.5, linestyle="--"),
            ])

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
        dpi = self._cfg.dpi
        # Landscape: 16:9 aspect ratio for mobile readability
        fig_w = res / dpi * 1.6
        fig_height = min(fig_w * 0.65, 12.0) if has_tdi else fig_w * 0.55
        panel_ratios = (4, 1.5) if has_tdi else (1,)

        fig, axes = mpf.plot(
            subset, type="candle", style=style,
            addplot=ema_addplots if ema_addplots else None,
            volume=False,
            figsize=(fig_w, fig_height),
            panel_ratios=panel_ratios,
            returnfig=True, tight_layout=True,
            xrotation=0, datetime_format="", show_nontrading=False,
        )

        ax = axes[0]

        # Strip default ticks on price panel
        for a in fig.get_axes():
            a.set_xticklabels([])
            a.set_yticklabels([])
            a.tick_params(left=False, right=False, bottom=False, top=False,
                          labelleft=False, labelright=False,
                          labelbottom=False, labeltop=False)
            for spine in a.spines.values():
                spine.set_visible(False)

        # Add TDI reference lines (68/50/32) on TDI panel
        if has_tdi:
            tdi_ax = None
            all_axes = fig.get_axes()
            if len(all_axes) > 1:
                tdi_ax = all_axes[-1]
            if tdi_ax is not None:
                for level, color, label in [
                    (68, "#FF5252", "68"), (50, "#888888", "50"), (32, "#42A5F5", "32")
                ]:
                    tdi_ax.axhline(y=level, color=color, linewidth=0.5, linestyle="--", alpha=0.4, zorder=1)
                    tdi_ax.text(
                        len(subset) * 0.98, level + 1, label,
                        color=color, fontsize=5, alpha=0.6, ha="right", zorder=10,
                    )

        # === DRAW ANNOTATIONS ===
        y_min = subset["Low"].min()
        y_max = subset["High"].max()
        y_range = y_max - y_min
        x_len = len(subset)

        # 1. Asian Range Boxes — draw on EVERY Asian session visible in chart
        #    Per MMM worktime ribbon: light blue box for each day's Asian session
        subset_offset = len(df) - len(subset)
        all_asian_ranges = annotations.get("all_asian_ranges", {})
        today_ar_date = annotations.get("today_asian_date", "")

        if all_asian_ranges:
            for date_str, ar in all_asian_ranges.items():
                ar_s = max(0, ar["start_idx"] - subset_offset)
                ar_e = min(x_len, ar["end_idx"] - subset_offset + 1)
                if ar_e <= 0 or ar_s >= x_len:
                    continue  # Not visible in chart subset
                ar_w = max(ar_e - ar_s, 1)
                ar_h_val = ar["high"]
                ar_l_val = ar["low"]

                # Box spanning full price range (session column shading)
                rect = mpatches.Rectangle(
                    (ar_s, y_min), ar_w, y_range,
                    linewidth=0, facecolor="#4FC3F7", alpha=0.05, zorder=0,
                )
                ax.add_patch(rect)

                # Tighter box at the actual Asian H/L range
                rect2 = mpatches.Rectangle(
                    (ar_s, ar_l_val), ar_w, ar_h_val - ar_l_val,
                    linewidth=1, edgecolor="#4FC3F7", facecolor="#4FC3F7",
                    alpha=0.12, zorder=1,
                )
                ax.add_patch(rect2)

                # Label only today's Asian range with pips
                if date_str == today_ar_date:
                    ar_pips = ar.get("pips", 0)
                    ar_label = f"ASIAN RANGE ({ar_pips:.0f}p)"
                    ax.text(
                        ar_s + 1, ar_h_val + y_range * 0.01,
                        ar_label, color="#4FC3F7", fontsize=9, fontweight="bold",
                        zorder=10,
                    )
        else:
            # Fallback: single Asian range from MTF analysis
            asian_h = annotations.get("asian_high")
            asian_l = annotations.get("asian_low")
            ar_start = annotations.get("asian_start_idx", 0)
            ar_end = annotations.get("asian_end_idx", 0)
            ar_s = max(0, ar_start - subset_offset)
            ar_e = min(x_len, ar_end - subset_offset + 1)
            if asian_h and asian_l and ar_e > 0:
                rect = mpatches.Rectangle(
                    (ar_s, asian_l), max(ar_e - ar_s, 1), asian_h - asian_l,
                    linewidth=1, edgecolor="#4FC3F7", facecolor="#4FC3F7",
                    alpha=0.10, zorder=1,
                )
                ax.add_patch(rect)

        # Today's Asian H/L for reference lines
        asian_h = annotations.get("asian_high")
        asian_l = annotations.get("asian_low")

        # 1b. Asian H/L/Mid dotted lines extending across full chart width
        if asian_h and asian_l:
            ar_line_labels = [
                (asian_h, "AR H", "#4FC3F7"),
                (asian_l, "AR L", "#4FC3F7"),
                (annotations.get("asian_mid", (asian_h + asian_l) / 2), "AR Mid", "#4FC3F7"),
            ]
            for level, label, color in ar_line_labels:
                ax.axhline(y=level, color=color, linewidth=0.5, linestyle=":", alpha=0.35, zorder=2)
                ax.text(x_len * 0.97, level + y_range * 0.003, label,
                        color=color, fontsize=5, alpha=0.6, ha="right", zorder=10)

        # 1c. Weekly open range (psychological S/R — first 4h of week)
        wk_high = annotations.get("weekly_open_high")
        wk_low = annotations.get("weekly_open_low")
        wk_pips = annotations.get("weekly_open_pips", 0)
        if wk_high and wk_low:
            for wk_level, wk_label in [
                (wk_high, "WK OPEN H"),
                (wk_low, "WK OPEN L"),
            ]:
                if y_min <= wk_level <= y_max:
                    ax.axhline(y=wk_level, color="#FFD600", linewidth=1.0, linestyle="-", alpha=0.45, zorder=2)
                    pip_suffix = f" ({wk_pips:.0f}p)" if wk_pips else ""
                    ax.text(x_len * 0.6, wk_level + y_range * 0.005,
                            f"{wk_label}{pip_suffix}",
                            color="#FFD600", fontsize=6, fontweight="bold", alpha=0.75, zorder=10)

        # 1d. Session boundary vertical separators
        session_bounds = annotations.get("session_boundaries", [])
        session_colors_vline = {
            "ASIA": "#4FC3F7", "LONDON": "#FF9800", "LONDON_GAP": "#FF9800",
            "US": "#E040FB", "NY_GAP": "#E040FB", "OFFHOURS": "#666666",
        }
        for (bound_idx, bound_label) in session_bounds:
            rx = bound_idx - (len(df) - len(subset))
            if 0 <= rx < x_len:
                vc = session_colors_vline.get(bound_label, "#666666")
                ax.axvline(x=rx, color=vc, linewidth=0.4, linestyle="--", alpha=0.4, zorder=1)

        # 1e. Session color shading (subtle background per session)
        session_shade_colors = {
            "ASIA": "#4FC3F7",        # light blue
            "LONDON_GAP": "#FF9800",  # light orange
            "LONDON": "#66BB6A",      # light green
            "NY_GAP": "#CE93D8",      # light purple
            "US": "#CE93D8",          # light purple
        }
        if session_bounds and len(session_bounds) >= 2:
            for i in range(len(session_bounds)):
                bound_idx, bound_label = session_bounds[i]
                rx_start = bound_idx - (len(df) - len(subset))
                # End at next boundary or chart end
                if i + 1 < len(session_bounds):
                    rx_end = session_bounds[i + 1][0] - (len(df) - len(subset))
                else:
                    rx_end = x_len
                rx_start = max(0, rx_start)
                rx_end = min(x_len, rx_end)
                if rx_start < rx_end and bound_label in session_shade_colors:
                    shade_color = session_shade_colors[bound_label]
                    shade_rect = mpatches.Rectangle(
                        (rx_start, y_min), rx_end - rx_start, y_range,
                        linewidth=0, facecolor=shade_color, alpha=0.03, zorder=0,
                    )
                    ax.add_patch(shade_rect)

        # 1f. London Open boxes (blue) — first 75 min of London session per day
        london_boxes = annotations.get("london_open_boxes", {})
        for date_str, box in london_boxes.items():
            bs = box["start_idx"] - subset_offset
            be = box["end_idx"] - subset_offset + 1
            if be <= 0 or bs >= x_len:
                continue
            bs = max(0, bs)
            be = min(x_len, be)
            rect = mpatches.Rectangle(
                (bs, box["low"]), max(be - bs, 1), box["high"] - box["low"],
                linewidth=1, edgecolor="#2196F3", facecolor="#2196F3",
                alpha=0.18, zorder=2,
            )
            ax.add_patch(rect)

        # 1g. NY Open boxes (red) — first 75 min of NYC session per day
        ny_boxes = annotations.get("ny_open_boxes", {})
        for date_str, box in ny_boxes.items():
            bs = box["start_idx"] - subset_offset
            be = box["end_idx"] - subset_offset + 1
            if be <= 0 or bs >= x_len:
                continue
            bs = max(0, bs)
            be = min(x_len, be)
            rect = mpatches.Rectangle(
                (bs, box["low"]), max(be - bs, 1), box["high"] - box["low"],
                linewidth=1, edgecolor="#EF5350", facecolor="#EF5350",
                alpha=0.18, zorder=2,
            )
            ax.add_patch(rect)

        # 1h. Gann 0/0.5/1 segments — frozen Asian H/Mid/L carried to next Asian
        gann_segments = annotations.get("gann_segments", [])
        gann_color = "#BDBDBD"
        for seg in gann_segments:
            gs = seg["start_idx"] - subset_offset
            ge = seg["end_idx"] - subset_offset
            if ge <= 0 or gs >= x_len:
                continue
            gs = max(0, gs)
            ge = min(x_len - 1, ge)
            for level_val, level_label in (
                (seg["low"], "0"),
                (seg["mid"], "0.5"),
                (seg["high"], "1"),
            ):
                if not (y_min <= level_val <= y_max):
                    continue
                ax.plot(
                    [gs, ge], [level_val, level_val],
                    color=gann_color, linewidth=1.0, linestyle="--",
                    alpha=0.55, zorder=3,
                )
                # Label just past the segment start
                label_x = min(gs + 3, ge)
                ax.text(
                    label_x, level_val, level_label,
                    color=gann_color, fontsize=6, alpha=0.7,
                    ha="left", va="center", zorder=10,
                )

        # 2. Stop Hunt Zone (prominent red/pink per MMM flashcard style)
        hunt_h = annotations.get("stop_hunt_high")
        hunt_l = annotations.get("stop_hunt_low")
        hunt_pips = annotations.get("stop_hunt_pips", 0)
        hunt_active = annotations.get("stop_hunt_active", False)

        if hunt_h and asian_h:
            rect = mpatches.Rectangle(
                (0, asian_h), x_len * 0.7, hunt_h - asian_h,
                linewidth=1.5, edgecolor="#E91E63", facecolor="#E91E63", alpha=0.15, zorder=1,
            )
            ax.add_patch(rect)
            hunt_label = f"STOP HUNT {hunt_pips:.0f}p" if hunt_pips else "STOP HUNT"
            if hunt_active:
                hunt_label = ">>> " + hunt_label + " LIVE <<<"
            ax.text(
                x_len * 0.02, hunt_h + y_range * 0.008,
                hunt_label, color="#E91E63", fontsize=9, fontweight="bold", zorder=10,
            )
            # Horizontal line at hunt extreme
            ax.axhline(y=hunt_h, color="#E91E63", linewidth=1.0, linestyle="--", alpha=0.5, zorder=2)

        if hunt_l and asian_l:
            rect = mpatches.Rectangle(
                (0, hunt_l), x_len * 0.7, asian_l - hunt_l,
                linewidth=1.5, edgecolor="#E91E63", facecolor="#E91E63", alpha=0.15, zorder=1,
            )
            ax.add_patch(rect)
            hunt_label_low = f"STOP HUNT {hunt_pips:.0f}p" if hunt_pips else "STOP HUNT"
            if hunt_active:
                hunt_label_low = ">>> " + hunt_label_low + " LIVE <<<"
            ax.text(
                x_len * 0.02, hunt_l - y_range * 0.025,
                hunt_label_low, color="#E91E63", fontsize=9, fontweight="bold", zorder=10,
            )
            ax.axhline(y=hunt_l, color="#E91E63", linewidth=1.0, linestyle="--", alpha=0.5, zorder=2)

        # 3. HOD / LOD horizontal lines
        hod = annotations.get("hod")
        lod = annotations.get("lod")
        if hod:
            ax.axhline(y=hod, color="#FF9800", linewidth=1.0, linestyle="--", alpha=0.7, zorder=2)
            ax.text(x_len * 0.85, hod + y_range * 0.005, "HOD", color="#FF9800", fontsize=8, fontweight="bold", zorder=10)
        if lod:
            ax.axhline(y=lod, color="#2196F3", linewidth=1.0, linestyle="--", alpha=0.7, zorder=2)
            ax.text(x_len * 0.85, lod - y_range * 0.018, "LOD", color="#2196F3", fontsize=8, fontweight="bold", zorder=10)

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

        # 7. Previous day HOD/LOD (distinct from current HOD/LOD)
        prev_hod = annotations.get("prev_hod")
        prev_lod = annotations.get("prev_lod")
        if prev_hod:
            ax.axhline(y=prev_hod, color="#FF6D00", linewidth=0.5, linestyle=":", alpha=0.4, zorder=2)
            ax.text(x_len * 0.7, prev_hod + y_range * 0.005,
                    f"Prev HOD {prev_hod:.5f}", color="#FF6D00", fontsize=6, alpha=0.8, zorder=10)
        if prev_lod:
            ax.axhline(y=prev_lod, color="#448AFF", linewidth=0.5, linestyle=":", alpha=0.4, zorder=2)
            ax.text(x_len * 0.7, prev_lod - y_range * 0.015,
                    f"Prev LOD {prev_lod:.5f}", color="#448AFF", fontsize=6, alpha=0.8, zorder=10)

        # 7b. Current day HOD/LOD (distinct colors from prev)
        curr_hod = annotations.get("curr_hod")
        curr_lod = annotations.get("curr_lod")
        if curr_hod:
            ax.axhline(y=curr_hod, color="#76FF03", linewidth=0.7, linestyle="--", alpha=0.5, zorder=2)
            ax.text(x_len * 0.7, curr_hod + y_range * 0.005,
                    f"Curr HOD {curr_hod:.5f}", color="#76FF03", fontsize=6, alpha=0.8, zorder=10)
        if curr_lod:
            ax.axhline(y=curr_lod, color="#40C4FF", linewidth=0.7, linestyle="--", alpha=0.5, zorder=2)
            ax.text(x_len * 0.7, curr_lod - y_range * 0.015,
                    f"Curr LOD {curr_lod:.5f}", color="#40C4FF", fontsize=6, alpha=0.8, zorder=10)

        # 8. Pivot levels (if provided)
        pivots = annotations.get("pivots")
        if pivots:
            pivot_colors = {"PP": "#FFFFFF", "R1": "#FF8A80", "S1": "#82B1FF", "M3": "#FFAB91", "M1": "#90CAF9"}
            for key in ["PP", "R1", "S1", "M3", "M1"]:
                val = pivots.get(key)
                if val and y_min <= val <= y_max:
                    color = pivot_colors.get(key, "#666666")
                    ax.axhline(y=val, color=color, linewidth=0.4, linestyle=":", alpha=0.3, zorder=1)
                    ax.text(x_len * 0.92, val + y_range * 0.003, key, color=color, fontsize=4, alpha=0.6, zorder=10)

        # 9. ADR projected levels
        adr_high = annotations.get("adr_high")
        adr_low = annotations.get("adr_low")
        if adr_high and y_min <= adr_high <= y_max:
            ax.axhline(y=adr_high, color="#E040FB", linewidth=0.5, linestyle="-.", alpha=0.3, zorder=1)
            ax.text(x_len * 0.88, adr_high + y_range * 0.005, "ADR H", color="#E040FB", fontsize=5, alpha=0.6, zorder=10)
        if adr_low and y_min <= adr_low <= y_max:
            ax.axhline(y=adr_low, color="#E040FB", linewidth=0.5, linestyle="-.", alpha=0.3, zorder=1)
            ax.text(x_len * 0.88, adr_low - y_range * 0.015, "ADR L", color="#E040FB", fontsize=5, alpha=0.6, zorder=10)

        # 10. Pattern markers (RRT, pin bars, spikes, etc.) — with text labels
        detected_patterns = annotations.get("patterns", [])
        pattern_markers = {
            "RRT": ("s", "#FFD600", 10, "RRT"),
            "PIN_BAR_BULL": ("^", "#00E676", 10, "PIN"),
            "PIN_BAR_BEAR": ("v", "#FF5252", 10, "PIN"),
            "SPIKE_CANDLE": ("x", "#FF9100", 11, "SPIKE"),
            "HAMMER": ("^", "#76FF03", 9, "HAM"),
            "INVERTED_HAMMER": ("v", "#FF1744", 9, "INV.H"),
            "EVENING_STAR": ("*", "#FF5252", 11, "EVE*"),
            "MORNING_STAR": ("*", "#00E676", 11, "MRN*"),
            "M_TOP": ("v", "#FF6D00", 12, "M-TOP"),
            "W_BOTTOM": ("^", "#00B0FF", 12, "W-BTM"),
            "HALF_BATMAN": ("D", "#E040FB", 10, "BATMAN"),
            "HIGH_TEST": ("_", "#FF6D00", 12, "HI-TEST"),
            "LOW_TEST": ("_", "#448AFF", 12, "LO-TEST"),
        }
        _labeled_positions = set()  # Avoid overlapping labels
        for pat in detected_patterns:
            pat_name = pat.pattern.value if hasattr(pat, "pattern") else str(pat.get("pattern", ""))
            pat_idx = pat.bar_index if hasattr(pat, "bar_index") else pat.get("bar_index", 0)
            pat_price = pat.price if hasattr(pat, "price") else pat.get("price", 0)
            rel_idx = pat_idx - (len(df) - len(subset))
            if 0 <= rel_idx < x_len and pat_name in pattern_markers:
                marker, color, size, label = pattern_markers[pat_name]
                ax.plot(rel_idx, pat_price, marker=marker, color=color,
                        markersize=size, markerfacecolor="none" if marker in ("o", "s") else color,
                        markeredgewidth=1.5, zorder=9, alpha=0.9)
                # Add text label above/below marker (avoid duplicates nearby)
                bucket = (rel_idx // 3, pat_name)
                if bucket not in _labeled_positions:
                    is_bearish = pat_name in ("PIN_BAR_BEAR", "INVERTED_HAMMER", "EVENING_STAR", "M_TOP", "HIGH_TEST")
                    label_y = pat_price + y_range * (- 0.03 if is_bearish else 0.02)
                    ax.text(rel_idx, label_y, label, color=color, fontsize=7,
                            fontweight="bold", ha="center", alpha=0.9, zorder=11)
                    _labeled_positions.add(bucket)

        # 11. Session box overlay (Asian range as colored region)
        session_boxes = annotations.get("session_boxes", [])
        session_colors = {"ASIAN": "#888888", "NYC": "#FF9800"}
        for start_idx, end_idx, label in session_boxes:
            s = max(0, start_idx - (len(df) - len(subset)))
            e = min(x_len, end_idx - (len(df) - len(subset)))
            if s < e:
                box_color = session_colors.get(label, "#666666")
                rect = mpatches.Rectangle(
                    (s, y_min), e - s, y_range,
                    linewidth=0, facecolor=box_color, alpha=0.04, zorder=0,
                )
                ax.add_patch(rect)

        # 12. Range pip labels between swing highs/lows
        swing_ranges = annotations.get("swing_ranges", [])
        for (x1, y1, x2, y2, pips) in swing_ranges:
            rx1 = x1 - (len(df) - len(subset))
            rx2 = x2 - (len(df) - len(subset))
            if 0 <= rx1 < x_len and 0 <= rx2 < x_len:
                mid_x = (rx1 + rx2) / 2
                mid_y = (y1 + y2) / 2
                ax.plot([rx1, rx2], [y1, y2], color="#FFFFFF", linewidth=0.6,
                        linestyle="--", alpha=0.5, zorder=6)
                ax.text(mid_x, mid_y + y_range * 0.01, f"R = {pips:.1f}",
                        color="#FFFFFF", fontsize=6, fontweight="bold",
                        ha="center", alpha=0.8, zorder=10)

        # 13. Day-of-week labels at session transitions
        day_labels = annotations.get("day_labels", [])
        for (x_idx, day_name) in day_labels:
            rx = x_idx - (len(df) - len(subset))
            if 0 <= rx < x_len:
                ax.axvline(x=rx, color="#666666", linewidth=0.3, linestyle=":",
                           alpha=0.3, zorder=1)
                ax.text(rx, y_max + y_range * 0.02, day_name,
                        color="#AAAAAA", fontsize=6, fontweight="bold",
                        ha="center", zorder=10)

        # 14. Level count numbers on price (1, 2, 3 — MMM cycle counts)
        level_counts = annotations.get("level_counts", [])
        for (x_idx, y_pos, level_num) in level_counts:
            rx = x_idx - (len(df) - len(subset))
            if 0 <= rx < x_len:
                ax.text(rx, y_pos, f"L{level_num}",
                        color="#FFD600", fontsize=18, fontweight="bold",
                        ha="center", va="center", alpha=0.85, zorder=12,
                        bbox=dict(boxstyle="round,pad=0.15", facecolor="#1a1a2e",
                                  alpha=0.6, edgecolor="#FFD600"))

        # 15. Entry/exit signal arrows (red down, green up per MMM flashcards)
        signal_arrows = annotations.get("signal_arrows", [])
        for (x_idx, y_pos, direction_str) in signal_arrows:
            rx = x_idx - (len(df) - len(subset))
            if 0 <= rx < x_len:
                if direction_str == "SELL":
                    ax.annotate("", xy=(rx, y_pos - y_range * 0.01),
                                xytext=(rx, y_pos + y_range * 0.03),
                                arrowprops=dict(arrowstyle="-|>", color="#FF1744",
                                                lw=2, mutation_scale=15),
                                zorder=11)
                else:
                    ax.annotate("", xy=(rx, y_pos + y_range * 0.01),
                                xytext=(rx, y_pos - y_range * 0.03),
                                arrowprops=dict(arrowstyle="-|>", color="#00E676",
                                                lw=2, mutation_scale=15),
                                zorder=11)

        # 16. ADR dashboard (top-right stats box per MMM flashcard style)
        adr_stats = annotations.get("adr_stats")
        if adr_stats:
            stat_lines = []
            # Full Pine-style table order: ADR / 3xADR / Today / ADR Used% / Avg Asia,
            # plus legacy HOD/LOD/TDR/WADR/MADR if caller provided them.
            for key in ["HOD", "LOD", "TDR", "ADR", "ADR_3X", "ADR_USED", "AVG_ASIA", "WADR", "MADR"]:
                val = adr_stats.get(key)
                if val is not None:
                    label = {"ADR_3X": "3xADR", "ADR_USED": "ADR%", "AVG_ASIA": "AvgAsia"}.get(key, key)
                    stat_lines.append(f"{label}: {val}")
            if stat_lines:
                stat_text = "\n".join(stat_lines)
                ax.text(
                    0.98, 0.65, stat_text,
                    transform=ax.transAxes, fontsize=7, color="#EEEEEE",
                    verticalalignment="top", horizontalalignment="right",
                    fontfamily="monospace",
                    bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1a2e",
                              alpha=0.85, edgecolor="#555555", linewidth=1.0),
                    zorder=20,
                )

        # 17. Trade type label (THE 33, etc.) — prominent
        trade_type = annotations.get("trade_type", "")
        if trade_type and trade_type != "NONE":
            ax.text(
                0.98, 0.98, trade_type.replace("_", " "),
                transform=ax.transAxes, fontsize=12, color="#FFD600",
                horizontalalignment="right", verticalalignment="top",
                fontweight="bold", alpha=0.95,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a2e", alpha=0.85, edgecolor="#FFD600", linewidth=1.5),
                zorder=20,
            )

        # 13. TDI signal annotation (on TDI panel if present)
        if has_tdi and len(axes) > 1:
            tdi_ax = axes[-1] if len(axes) > 2 else None
            # Find the TDI panel axis
            for a in fig.get_axes():
                # TDI panel has ylabel "TDI" or is the last non-empty axis
                pass  # TDI lines already plotted via addplot; signals shown in info box

        # 14. TDI signals in info box
        tdi_info = []
        if has_tdi:
            tdi_info.append(f"RSI: {tdi_data.rsi:.0f} | Sig: {tdi_data.signal:.0f}")
            for sig in tdi_data.signals:
                if sig.value != "NONE":
                    tdi_info.append(f"TDI: {sig.value.replace('_', ' ')}")
            if tdi_data.divergence != "none":
                tdi_info.append(f"Divergence: {tdi_data.divergence}")

        # Info box (top-left)
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
        if trade_type and trade_type != "NONE":
            info_lines.append(f"Setup: {trade_type.replace('_', ' ')}")

        # TDI signals
        for ti in tdi_info[:3]:
            info_lines.append(ti)

        # Notes
        notes = annotations.get("notes", [])
        for n in notes[:3]:
            info_lines.append(n[:40])

        info_text = "\n".join(info_lines)
        ax.text(
            0.02, 0.98, info_text,
            transform=ax.transAxes, fontsize=8, color="#EEEEEE",
            verticalalignment="top", fontfamily="monospace",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1a2e", alpha=0.9, edgecolor="#555555", linewidth=1.0),
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

        # Clamp figure size to prevent rendering explosion from annotations
        fig.set_size_inches(fig_w, fig_height)

        # Export
        buf = BytesIO()
        fig.savefig(
            buf, format="png", dpi=dpi,
            pad_inches=0.02,
            facecolor=bg,
        )
        plt.close(fig)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode("utf-8")

        ts_file = datetime.now(EAT).strftime("%Y%m%d_%H%M%S_%f")
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
        tdi_result=None,
        pattern_scan=None,
        pivots: Optional[Dict] = None,
        adr: float = 0,
        prev_hod: float = 0,
        prev_lod: float = 0,
        pip_size: Optional[float] = None,
    ) -> Tuple[str, Path]:
        """Generate annotated chart directly from an MTFAnalysis result.

        Optionally includes TDI subplot, pattern markers, pivots, and ADR.
        """
        a = mtf_analysis
        m15 = a.fifteen_min
        h1 = a.one_hour

        # Use session infrastructure for date-precise Asian range
        from helix_v3.core.sessions import classify_sessions, get_today_asian_range

        pip_val = pip_size if pip_size and pip_size > 0 else fallback_pip_size(symbol)
        session_info = classify_sessions(df, pip_val)

        # Get TODAY's Asian range (date-precise, not stale)
        today_asian = get_today_asian_range(session_info, df)
        if today_asian:
            asian_h = today_asian["high"]
            asian_l = today_asian["low"]
            asian_pips = today_asian["pips"]
        else:
            asian_h = m15.asian_range_high
            asian_l = m15.asian_range_low
            asian_pips = m15.asian_range_pips

        annotations = {
            "direction": a.trade_direction.value,
            "confidence": a.trade_confidence,
            "confluence_score": a.confluence_score,
            "cycle_level": a.four_hour.level_count,
            "session": h1.session_phase.value if h1 else "",
            "weekly_trend": f"{a.weekly.trend_direction.value} ({a.weekly.week_phase.value})",
            "asian_high": asian_h,
            "asian_low": asian_l,
            "asian_range_pips": asian_pips,
            "hod": h1.hod,
            "lod": h1.lod,
            "notes": [],
        }

        # Asian H/L/Mid dotted lines extending across full chart
        annotations["asian_mid"] = (asian_h + asian_l) / 2.0

        # All Asian ranges for worktime ribbon boxes (every day visible)
        annotations["all_asian_ranges"] = session_info.asian_ranges
        if today_asian:
            latest_date = max(session_info.asian_ranges.keys())
            annotations["today_asian_date"] = latest_date
            annotations["asian_start_idx"] = today_asian.get("start_idx", 0)
            annotations["asian_end_idx"] = today_asian.get("end_idx", 0)

        # Stop hunt zone
        if m15.stop_hunt_detected:
            annotations["stop_hunt_pips"] = m15.stop_hunt_pips
            annotations["stop_hunt_direction"] = m15.stop_hunt_direction.value
            annotations["stop_hunt_active"] = True  # Mark as live/confirmed
            if m15.stop_hunt_direction.value == "SELL":
                annotations["stop_hunt_high"] = asian_h + m15.stop_hunt_pips * pip_val
            else:
                annotations["stop_hunt_low"] = asian_l - m15.stop_hunt_pips * pip_val
            annotations["notes"].append(f"STOP HUNT: {m15.stop_hunt_direction.value} {m15.stop_hunt_pips:.1f}p ({m15.push_count} pushes)")

        if m15.m_w_forming:
            annotations["notes"].append("M/W formation detected")
        if m15.rrt_detected:
            annotations["notes"].append("Railroad Tracks detected")
        if m15.push_count >= 3:
            annotations["notes"].append(f"{m15.push_count} pushes (target: 3)")

        # TDI
        if tdi_result is not None:
            annotations["tdi"] = tdi_result

        # Pattern markers
        if pattern_scan is not None:
            annotations["patterns"] = pattern_scan.patterns
            if pattern_scan.trade_type.value != "NONE":
                annotations["trade_type"] = pattern_scan.trade_type.value
            if pattern_scan.half_batman:
                annotations["notes"].append("Half Batman pattern")
            if pattern_scan.spike_count > 0:
                annotations["notes"].append(f"{pattern_scan.spike_count} spike candle(s)")

        # Pivots
        if pivots:
            annotations["pivots"] = pivots

        # ADR levels
        if adr > 0:
            mid_price = (h1.hod + h1.lod) / 2 if h1 else float(df["Close"].iloc[-1])
            annotations["adr_high"] = mid_price + adr / 2
            annotations["adr_low"] = mid_price - adr / 2

        # Previous AND current day HOD/LOD
        if prev_hod > 0:
            annotations["prev_hod"] = prev_hod
        if prev_lod > 0:
            annotations["prev_lod"] = prev_lod
        annotations["curr_hod"] = h1.hod
        annotations["curr_lod"] = h1.lod

        # Session boundaries as vertical separators with labels
        annotations["session_boundaries"] = session_info.session_boundaries

        # London / NY open boxes and Gann segments (Pine indicator port)
        annotations["london_open_boxes"] = session_info.london_open_boxes
        annotations["ny_open_boxes"] = session_info.ny_open_boxes
        annotations["gann_segments"] = session_info.gann_segments

        # Day-of-week labels from session infrastructure (not manual)
        annotations["day_labels"] = session_info.day_labels

        # Weekly open range (psychological S/R — first 4h of trading week)
        if session_info.weekly_open_range:
            wr = session_info.weekly_open_range
            annotations["weekly_open_high"] = wr["high"]
            annotations["weekly_open_low"] = wr["low"]
            annotations["weekly_open_mid"] = wr["mid"]
            annotations["weekly_open_pips"] = wr["pips"]

        # Level count
        if a.four_hour.level_count > 0:
            mid_idx = len(df) - len(df) // 4
            y_est = float(df["High"].max() - df["Low"].min())
            level_y = float(df["High"].iloc[mid_idx]) + y_est * 0.05
            annotations["level_counts"] = [(mid_idx, level_y, a.four_hour.level_count)]

        # HUD dashboard — pip_mult converts raw price to pip count
        if adr > 0:
            pip_mult = 1.0 / pip_val
            tdr_pips = (h1.hod - h1.lod) * pip_mult
            adr_pips = adr * pip_mult
            adr_used_pct = (tdr_pips / adr_pips * 100.0) if adr_pips > 0 else 0.0
            # WADR/MADR from session_info if available
            wadr_pips = getattr(session_info, "wadr", 0) * pip_mult if hasattr(session_info, "wadr") else 0
            madr_pips = getattr(session_info, "madr", 0) * pip_mult if hasattr(session_info, "madr") else 0
            adr_stats_dict = {
                "HOD": f"{h1.hod:.5f}",
                "LOD": f"{h1.lod:.5f}",
                "TDR": f"{tdr_pips:.1f}p",
                "ADR": f"{adr_pips:.1f}p",
                "ADR_3X": f"{adr_pips * 3:.1f}p",
                "ADR_USED": f"{adr_used_pct:.1f}%",
            }
            if session_info.asian_avg_pips > 0:
                adr_stats_dict["AVG_ASIA"] = f"{session_info.asian_avg_pips:.1f}p"
            if wadr_pips > 0:
                adr_stats_dict["WADR"] = f"{wadr_pips:.0f}p"
            if madr_pips > 0:
                adr_stats_dict["MADR"] = f"{madr_pips:.0f}p"
            annotations["adr_stats"] = adr_stats_dict

        # Signal arrows
        if pattern_scan is not None:
            signal_arrows = []
            for pat in pattern_scan.patterns:
                if pat.significance >= 0.8:
                    if pat.pattern.value in ("PIN_BAR_BEAR", "INVERTED_HAMMER", "EVENING_STAR", "M_TOP"):
                        signal_arrows.append((pat.bar_index + (len(df) - 50), pat.price, "SELL"))
                    elif pat.pattern.value in ("PIN_BAR_BULL", "HAMMER", "MORNING_STAR", "W_BOTTOM"):
                        signal_arrows.append((pat.bar_index + (len(df) - 50), pat.price, "BUY"))
            annotations["signal_arrows"] = signal_arrows[:8]

        # Rejections
        for r in a.rejection_reasons[:2]:
            annotations["notes"].append(f"WARN: {r[:35]}")

        return self.generate(df, symbol, timeframe, annotations)
