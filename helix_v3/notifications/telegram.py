"""Telegram Notification Module via Bot API.

Drop-in replacement for WhatsAppNotifier. Free, no message limits,
supports images with captions (chart + analysis in one message).

Setup:
1. Message @BotFather on Telegram -> /newbot -> get bot token
2. Create a channel/group, add your bot as admin
3. Get chat_id: send a message to the bot, then visit
   https://api.telegram.org/bot<TOKEN>/getUpdates
4. Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from helix_v3.notifications.dispatch import fire_and_forget
from helix_v3.utils.logger import get_logger

logger = get_logger("telegram_notify")

EAT = timezone(timedelta(hours=3))

# Telegram caption limit
_CAPTION_LIMIT = 1024


def _eat_now() -> str:
    return datetime.now(EAT).strftime("%H:%M EAT")


def _eat_datetime() -> str:
    return datetime.now(EAT).strftime("%Y-%m-%d %H:%M EAT")


def _to_eat(iso_or_str: str) -> str:
    try:
        if "T" in iso_or_str:
            dt = datetime.fromisoformat(iso_or_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(EAT).strftime("%Y-%m-%d %H:%M EAT")
        return iso_or_str
    except Exception:
        return iso_or_str


def _format_duration(minutes: float) -> str:
    if minutes < 60:
        return f"{minutes:.0f}min"
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    return f"{hours}h {mins}min"


class TelegramNotifier:
    """Telegram Bot API notification service.

    Same public interface as WhatsAppNotifier so the orchestrator
    can switch between them without code changes.
    """

    BASE_URL = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self) -> None:
        import os

        self._token = os.getenv("TELEGRAM_BOT_TOKEN", "")
        self._chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
        self._enabled = bool(self._token and self._chat_id)

        if self._enabled:
            logger.info("Telegram notifications ENABLED -> chat_id=%s", self._chat_id)
        else:
            logger.warning(
                "Telegram notifications DISABLED - set TELEGRAM_BOT_TOKEN "
                "and TELEGRAM_CHAT_ID in .env"
            )

    @property
    def enabled(self) -> bool:
        return self._enabled

    def _api_url(self, method: str) -> str:
        return self.BASE_URL.format(token=self._token, method=method)

    def _send(self, message: str, image_path: Optional[str] = None) -> bool:
        """Send a Telegram message, optionally with an image.

        If image_path is provided and the message fits in the caption limit,
        sends as a single photo+caption. Otherwise sends text then photo.
        """
        if not self._enabled:
            logger.debug("Telegram disabled, skipping: %s", message[:80])
            return False

        if image_path:
            return self.send_with_chart(message, image_path)

        return self._send_text(message)

    def _send_text(self, message: str) -> bool:
        """Queue a text message — fire-and-forget (audit Tier 3.2)."""
        if not self._enabled:
            return False
        fire_and_forget(self._send_text_sync, message, description="Telegram text")
        return True

    def _send_text_sync(self, message: str) -> bool:
        """Blocking text send — runs on the notify worker, never the trade path."""
        import httpx

        try:
            resp = httpx.post(
                self._api_url("sendMessage"),
                json={
                    "chat_id": self._chat_id,
                    "text": message,
                    "parse_mode": "HTML",
                },
                timeout=30.0,
            )

            if resp.status_code == 200 and resp.json().get("ok"):
                msg_id = resp.json()["result"]["message_id"]
                logger.info("Telegram sent: %s (msg_id=%s)", message[:60], msg_id)
                return True
            else:
                # Retry without parse_mode in case HTML is malformed
                resp2 = httpx.post(
                    self._api_url("sendMessage"),
                    json={
                        "chat_id": self._chat_id,
                        "text": message,
                    },
                    timeout=30.0,
                )
                if resp2.status_code == 200 and resp2.json().get("ok"):
                    return True
                logger.error("Telegram send failed: %d %s", resp.status_code, resp.text[:200])
                return False

        except Exception as e:
            logger.error("Telegram send error: %s", e)
            return False

    def send_with_chart(self, message: str, chart_path: str) -> bool:
        """Queue chart image + analysis text — fire-and-forget (Tier 3.2)."""
        if not self._enabled:
            return False
        fire_and_forget(
            self._send_with_chart_sync, message, chart_path,
            description="Telegram chart",
        )
        return True

    def _send_with_chart_sync(self, message: str, chart_path: str) -> bool:
        """Blocking photo+caption send — runs on the notify worker.

        Strategy:
        - If message <= 1024 chars: single sendPhoto with caption
        - If message > 1024 chars: sendPhoto with truncated caption,
          then full text as reply
        """
        import httpx

        img = Path(chart_path)
        if not img.exists():
            logger.warning("Chart not found: %s, sending text only", chart_path)
            return self._send_text_sync(message)

        try:
            if len(message) <= _CAPTION_LIMIT:
                # Single message: photo + full caption
                with open(img, "rb") as f:
                    resp = httpx.post(
                        self._api_url("sendPhoto"),
                        data={"chat_id": self._chat_id},
                        files={"photo": (img.name, f, "image/png")},
                        params={"caption": message},
                        timeout=30.0,
                    )

                if resp.status_code == 200 and resp.json().get("ok"):
                    logger.info("Telegram photo+caption sent: %s", img.name)
                    return True
                else:
                    logger.error("Telegram photo send failed: %s", resp.text[:200])
                    return self._send_text_sync(message)
            else:
                # Long message: send photo with short caption, then full text as reply
                short_caption = message[:_CAPTION_LIMIT - 20] + "\n..."

                with open(img, "rb") as f:
                    resp = httpx.post(
                        self._api_url("sendPhoto"),
                        data={"chat_id": self._chat_id},
                        files={"photo": (img.name, f, "image/png")},
                        params={"caption": short_caption},
                        timeout=30.0,
                    )

                photo_ok = resp.status_code == 200 and resp.json().get("ok")
                if photo_ok:
                    photo_msg_id = resp.json()["result"]["message_id"]
                    # Send full text as reply to the photo
                    httpx.post(
                        self._api_url("sendMessage"),
                        json={
                            "chat_id": self._chat_id,
                            "text": message,
                            "reply_to_message_id": photo_msg_id,
                        },
                        timeout=30.0,
                    )
                    logger.info("Telegram photo+reply sent: %s", img.name)
                    return True
                else:
                    logger.error("Telegram photo failed: %s", resp.text[:200])
                    return self._send_text_sync(message)

        except Exception as e:
            logger.error("Telegram chart send error: %s", e)
            return self._send_text_sync(message)

    # ------------------------------------------------------------------
    # Trade Setup Alert
    # ------------------------------------------------------------------

    def notify_trade_setup(
        self,
        symbol: str,
        timeframe: str,
        direction: str,
        confidence: float,
        cycle_level: int,
        readiness: int,
        notes: str = "",
    ) -> bool:
        msg = (
            f"HELIX V3 SETUP ALERT\n"
            f"{'='*30}\n"
            f"Symbol: {symbol} {timeframe}\n"
            f"Direction: {direction}\n"
            f"Confidence: {confidence:.0%}\n"
            f"Cycle Level: L{cycle_level}\n"
            f"Readiness: {readiness}/100\n"
        )
        if notes:
            msg += f"Notes: {notes}\n"
        msg += f"\n{_eat_datetime()}"
        return self._send(msg)

    # ------------------------------------------------------------------
    # Trade Entry Alert
    # ------------------------------------------------------------------

    def notify_trade_entry(
        self,
        symbol: str,
        direction: str,
        lot_size: float,
        entry_price: float,
        stop_loss: float,
        tp1: float,
        tp2: float,
        sl_pips: float,
        risk_reward: float,
        ticket: int,
        equity: float = 0,
        risk_amount: float = 0,
        bias: str = "",
        cycle_level: int = 0,
        confidence: float = 0,
    ) -> bool:
        msg = (
            f"HELIX V3 TRADE ENTERED\n"
            f"{'='*30}\n"
            f"Ticket: {ticket}\n"
            f"{direction} {symbol} | {lot_size} lots\n"
            f"\n"
            f"Entry:   {entry_price:.5f}\n"
            f"SL:      {stop_loss:.5f} ({sl_pips:.0f} pips)\n"
            f"TP1:     {tp1:.5f} (1:1 RR)\n"
            f"TP2:     {tp2:.5f} ({risk_reward:.1f}:1 RR)\n"
        )
        if bias:
            msg += f"\nBias: {bias}"
        if cycle_level:
            msg += f" | Cycle: L{cycle_level}"
        if confidence:
            msg += f" | Conf: {confidence:.0%}"
        if equity:
            msg += f"\nEquity: ${equity:.2f}"
        if risk_amount:
            from config.settings import settings
            msg += f" | Risk: ${risk_amount:.2f} ({settings.risk.max_risk_per_trade*100:.0f}%)"
        msg += f"\n\n{_eat_datetime()}"
        return self._send(msg)

    # ------------------------------------------------------------------
    # T1 Partial Close
    # ------------------------------------------------------------------

    def notify_t1_hit(
        self,
        symbol: str,
        ticket: int,
        pips: float,
        profit: float,
        close_lots: float,
    ) -> bool:
        msg = (
            f"HELIX V3 T1 HIT\n"
            f"{'='*30}\n"
            f"Ticket: {ticket} ({symbol})\n"
            f"Partial Close: {close_lots} lots\n"
            f"Pips: +{pips:.1f}\n"
            f"Profit: ${profit:.2f}\n"
            f"SL moved to breakeven\n"
            f"Trailing SL now active\n"
            f"\n{_eat_datetime()}"
        )
        return self._send(msg)

    # ------------------------------------------------------------------
    # Full Trade Close Report
    # ------------------------------------------------------------------

    def notify_trade_exit(
        self,
        symbol: str,
        direction: str,
        ticket: int,
        exit_reason: str,
        pips: float,
        net_profit: float,
        duration_min: float,
        outcome: str,
        entry_price: float = 0,
        exit_price: float = 0,
        lot_size: float = 0,
        sl_pips: float = 0,
        risk_reward: float = 0,
        bias: str = "",
        cycle_level: int = 0,
        confidence: float = 0,
        equity_before: float = 0,
        equity_after: float = 0,
        gross_profit: float = 0,
        commission: float = 0,
        swap: float = 0,
        t1_hit: bool = False,
        t1_pips: float = 0,
        t1_profit: float = 0,
        opened_at: str = "",
        closed_at: str = "",
        timeframe: str = "",
        pip_value: float = 0,
    ) -> bool:
        tag = "WIN" if outcome == "WIN" else "LOSS" if outcome == "LOSS" else "BE"

        msg = (
            f"HELIX V3 TRADE REPORT [{tag}]\n"
            f"{'='*30}\n"
            f"\n"
            f"Ticket:    {ticket}\n"
            f"Pair:      {direction} {symbol}"
        )
        if timeframe:
            msg += f" ({timeframe})"
        msg += "\n"

        if lot_size:
            msg += f"Lots:      {lot_size}\n"

        msg += "\n--- Prices ---\n"
        if entry_price:
            msg += f"Entry:     {entry_price:.5f}\n"
        if exit_price:
            msg += f"Exit:      {exit_price:.5f}\n"
        msg += f"Pips:      {pips:+.1f}\n"
        if sl_pips:
            msg += f"SL was:    {sl_pips:.0f} pips\n"
        if risk_reward:
            msg += f"RR Target: {risk_reward:.1f}:1\n"
        if pip_value:
            msg += f"Pip Value: ${pip_value:.4f}\n"

        if bias or cycle_level or confidence:
            msg += "\n--- Setup ---\n"
            if bias:
                msg += f"Bias:      {bias}\n"
            if cycle_level:
                msg += f"Cycle:     Level {cycle_level}\n"
            if confidence:
                msg += f"Confidence:{confidence:.0%}\n"

        msg += "\n--- P&L ---\n"
        if gross_profit:
            msg += f"Gross:     ${gross_profit:+.2f}\n"
        if commission:
            msg += f"Commission:${commission:.2f}\n"
        if swap:
            msg += f"Swap:      ${swap:+.2f}\n"
        msg += f"Net P&L:   ${net_profit:+.2f}\n"

        if t1_hit:
            msg += "\n--- Partial Close ---\n"
            msg += f"T1 Hit:    Yes (+{t1_pips:.1f} pips)\n"
            msg += f"T1 Profit: ${t1_profit:.2f}\n"

        if equity_before or equity_after:
            msg += "\n--- Account ---\n"
            if equity_before:
                msg += f"Before:    ${equity_before:.2f}\n"
            if equity_after:
                msg += f"After:     ${equity_after:.2f}\n"
                if equity_before:
                    change = equity_after - equity_before
                    pct = (change / equity_before) * 100 if equity_before else 0
                    msg += f"Change:    ${change:+.2f} ({pct:+.2f}%)\n"

        msg += "\n--- Timing ---\n"
        msg += f"Exit Reason: {exit_reason}\n"
        msg += f"Duration:    {_format_duration(duration_min)}\n"
        if opened_at:
            msg += f"Opened:      {_to_eat(opened_at)}\n"
        if closed_at:
            msg += f"Closed:      {_to_eat(closed_at)}\n"

        msg += f"\n{_eat_datetime()}"
        return self._send(msg)

    # ------------------------------------------------------------------
    # Market Conditions
    # ------------------------------------------------------------------

    def notify_market_conditions(
        self,
        dashboard: str,
        high_readiness: List[Dict[str, Any]],
    ) -> bool:
        if not high_readiness:
            return False

        # Session phase in human terms
        from datetime import timezone as _tz
        h = datetime.now(_tz.utc).hour
        if 1 <= h < 5:
            phase = "ACCUMULATION"
            phase_note = "Asian range forming. Watch for tight compression."
        elif 5 <= h < 8:
            phase = "STOP HUNT"
            phase_note = "London breaking Asian range. Watch for fake breakouts."
        elif 8 <= h < 13:
            phase = "TRUE TREND"
            phase_note = "Real move underway. Entries valid if structure confirms."
        elif 13 <= h < 17:
            phase = "NYC REVERSAL"
            phase_note = "Late session. Only high-conviction setups."
        else:
            phase = "DEAD TIME"
            phase_note = "Session closed. No entries."

        # Day context
        dow = datetime.now(EAT).strftime("%A")
        day_num = datetime.now(EAT).weekday()
        if day_num in (6, 0):
            week = "Early week — fresh cycle, watch for initial stop hunts"
        elif day_num in (1, 2):
            week = "Mid week — reversal zone, highest probability window"
        else:
            week = "Late week — manage existing trades, reduce new exposure"

        # Deduplicate: keep only M15 (skip H1 duplicates)
        seen = set()
        filtered = []
        for s in high_readiness:
            if s["symbol"] not in seen:
                seen.add(s["symbol"])
                filtered.append(s)

        msg = (
            f"HELIX V3 MARKET SCAN\n"
            f"{'='*30}\n"
            f"{dow} | {phase}\n"
            f"{week}\n"
            f"{phase_note}\n"
        )

        for s in filtered[:5]:
            symbol = s["symbol"]
            bias = s.get("bias", "NEUTRAL")
            readiness = s.get("trade_readiness", 0)
            spread = s.get("spread_pips", 0) or 0

            # Build MMM narrative per pair
            hunt_active = s.get("stop_hunt_active", False)
            hunt_dir = s.get("stop_hunt_direction", "")
            hunt_pips = s.get("stop_hunt_breach_pips", 0) or 0
            is_accum = s.get("is_accumulation", False)
            sess_range = s.get("session_range", 0) or 0
            vol_comp = s.get("vol_compression", 0) or 0

            # Trend from EMA stack
            trend = s.get("trend", "NEUTRAL")

            # Readiness bar
            bar_len = readiness // 10
            bar = ">" * bar_len + "-" * (10 - bar_len)

            lines = [f"\n{symbol} {'BUY' if bias == 'BUY' else 'SELL' if bias == 'SELL' else 'NEUTRAL'}"]
            lines.append(f"  [{bar}] {readiness}/100")

            # What's happening on this pair
            if hunt_active and hunt_pips > 0:
                real_dir = "SELL" if hunt_dir == "BUY" else "BUY"
                lines.append(
                    f"  Stop hunt {hunt_dir} {hunt_pips:.0f} pips "
                    f"— expect {real_dir} reversal"
                )
            elif is_accum:
                lines.append(
                    f"  Accumulating (range {sess_range:.0f}p, "
                    f"compression {vol_comp:.2f})"
                )
            elif bias != "NEUTRAL":
                lines.append(f"  EMA trend: {trend}, bias {bias}")

            if spread > 3:
                lines.append(f"  Spread wide: {spread:.1f}p")

            msg += "\n".join(lines) + "\n"

        msg += f"\n{_eat_datetime()}"
        return self._send(msg)

    def notify_scanner_watchlist(self, report: str) -> bool:
        """Send the alert-only scanner watchlist report."""
        return self._send_text(report)

    # ------------------------------------------------------------------
    # Period Reports (Session / EOD / Weekly / Monthly)
    # ------------------------------------------------------------------

    def notify_period_report(
        self,
        period_name: str,
        period_range: str,
        total_trades: int,
        wins: int,
        losses: int,
        breakevens: int,
        total_pips: float,
        net_profit: float,
        win_rate: float,
        profit_factor: float,
        best_trade: Optional[Dict[str, Any]] = None,
        worst_trade: Optional[Dict[str, Any]] = None,
        by_symbol: Optional[Dict[str, Any]] = None,
        winning_setups: Optional[List[Dict[str, Any]]] = None,
        equity_start: float = 0,
        equity_end: float = 0,
        max_drawdown_pips: float = 0,
        avg_duration_min: float = 0,
        t1_hit_count: int = 0,
    ) -> bool:
        if total_trades == 0:
            msg = (
                f"HELIX V3 {period_name.upper()} REPORT\n"
                f"{'='*30}\n"
                f"Period: {period_range}\n"
                f"\nNo trades during this period.\n"
                f"\n{_eat_datetime()}"
            )
            return self._send(msg)

        msg = (
            f"HELIX V3 {period_name.upper()} REPORT\n"
            f"{'='*30}\n"
            f"Period: {period_range}\n"
            f"\n--- Overview ---\n"
            f"Trades:      {total_trades}\n"
            f"W / L / BE:  {wins} / {losses} / {breakevens}\n"
            f"Win Rate:    {win_rate:.0f}%\n"
            f"T1 Hit Rate: {t1_hit_count}/{total_trades}\n"
            f"\n--- Performance ---\n"
            f"Total Pips:  {total_pips:+.1f}\n"
            f"Net P&L:     ${net_profit:+.2f}\n"
            f"Profit Factor:{profit_factor:.2f}\n"
            f"Max DD:      {max_drawdown_pips:.1f} pips\n"
            f"Avg Duration:{_format_duration(avg_duration_min)}\n"
        )

        if equity_start or equity_end:
            msg += "\n--- Account ---\n"
            if equity_start:
                msg += f"Start:       ${equity_start:.2f}\n"
            if equity_end:
                msg += f"End:         ${equity_end:.2f}\n"
                if equity_start:
                    gain = equity_end - equity_start
                    pct = (gain / equity_start) * 100 if equity_start else 0
                    msg += f"Gain/Loss:   ${gain:+.2f} ({pct:+.2f}%)\n"

        if best_trade:
            msg += "\n--- Best Trade ---\n"
            msg += (
                f"{best_trade.get('direction','')} {best_trade.get('symbol','')} "
                f"{best_trade.get('pips_gained',0):+.1f} pips "
                f"${best_trade.get('net_profit',0):+.2f}\n"
            )
        if worst_trade:
            msg += "\n--- Worst Trade ---\n"
            msg += (
                f"{worst_trade.get('direction','')} {worst_trade.get('symbol','')} "
                f"{worst_trade.get('pips_gained',0):+.1f} pips "
                f"${worst_trade.get('net_profit',0):+.2f}\n"
            )

        if by_symbol:
            is_long_period = period_name.upper() in ("WEEKLY", "MONTHLY")
            if is_long_period and len(by_symbol) > 2:
                msg += "\n--- Top & Bottom Pairs ---\n"
                sorted_syms = sorted(by_symbol.items(), key=lambda x: x[1]["net_profit"], reverse=True)
                sym, data = sorted_syms[0]
                msg += (
                    f"Best:  {sym} {data['trades']}T "
                    f"WR={data['win_rate']:.0f}% "
                    f"{data['total_pips']:+.1f}p "
                    f"${data['net_profit']:+.2f}\n"
                )
                sym, data = sorted_syms[-1]
                msg += (
                    f"Worst: {sym} {data['trades']}T "
                    f"WR={data['win_rate']:.0f}% "
                    f"{data['total_pips']:+.1f}p "
                    f"${data['net_profit']:+.2f}\n"
                )
                msg += f"({len(by_symbol)} pairs traded total)\n"
            else:
                msg += "\n--- By Symbol ---\n"
                for sym, data in by_symbol.items():
                    msg += (
                        f"{sym}: {data['trades']}T "
                        f"WR={data['win_rate']:.0f}% "
                        f"{data['total_pips']:+.1f}p "
                        f"${data['net_profit']:+.2f}\n"
                    )

        if winning_setups:
            msg += "\n--- Top Setups ---\n"
            for s in winning_setups[:3]:
                msg += (
                    f"L{s.get('cycle_level', '?')} {s.get('bias', '?')}: "
                    f"{s.get('wins',0)}W/{s.get('total',0)}T "
                    f"WR={s.get('win_rate',0):.0f}%\n"
                )

        msg += f"\n{_eat_datetime()}"
        return self._send(msg)

    # ------------------------------------------------------------------
    # Flashcard Setup Alert (with annotated chart)
    # ------------------------------------------------------------------

    def notify_setup_with_chart(
        self,
        symbol: str,
        timeframe: str,
        direction: str,
        confidence: float,
        confluence_score: int,
        cycle_level: int,
        session: str,
        weekly_trend: str,
        asian_range_pips: float,
        stop_hunt_pips: float,
        m_w: bool,
        rrt: bool,
        push_count: int,
        chart_path: str,
        entry_price: float = 0,
        stop_loss: float = 0,
        tp1: float = 0,
        tp2: float = 0,
        sl_pips: float = 0,
        risk_reward: float = 0,
        notes: str = "",
    ) -> bool:
        msg = (
            f"HELIX V3 SETUP FLASHCARD\n"
            f"{'='*30}\n"
            f"\n"
            f"Pair:       {symbol} {timeframe}\n"
            f"Direction:  {direction}\n"
            f"Confidence: {confidence:.0%}\n"
            f"Confluence: {confluence_score}/100\n"
            f"\n"
            f"--- MTF Context ---\n"
            f"Weekly:     {weekly_trend}\n"
            f"Cycle:      Level {cycle_level}\n"
            f"Session:    {session}\n"
            f"\n"
            f"--- 15M Signals ---\n"
            f"Asian Rng:  {asian_range_pips:.0f} pips\n"
            f"Stop Hunt:  {stop_hunt_pips:.1f} pips\n"
            f"M/W:        {'Yes' if m_w else 'No'}\n"
            f"RRT:        {'Yes' if rrt else 'No'}\n"
            f"Pushes:     {push_count}/3\n"
        )

        if entry_price:
            msg += (
                f"\n--- Order ---\n"
                f"Entry:      {entry_price:.5f}\n"
                f"SL:         {stop_loss:.5f} ({sl_pips:.0f}p)\n"
                f"TP1:        {tp1:.5f} (1:1)\n"
                f"TP2:        {tp2:.5f} ({risk_reward:.1f}:1)\n"
            )

        if notes:
            msg += f"\nNotes: {notes}\n"

        msg += f"\n{_eat_datetime()}"

        return self.send_with_chart(msg, chart_path)

    # ------------------------------------------------------------------
    # Drawdown Warning
    # ------------------------------------------------------------------

    def notify_drawdown_warning(
        self, current_dd_pct: float, limit_pct: float
    ) -> bool:
        msg = (
            f"HELIX V3 DRAWDOWN WARNING\n"
            f"{'='*30}\n"
            f"Current DD: {current_dd_pct:.1f}%\n"
            f"Limit: {limit_pct:.0f}%\n"
            f"Action: New trades may be blocked\n"
            f"\n{_eat_datetime()}"
        )
        return self._send(msg)

    # ------------------------------------------------------------------
    # Market Scan Analysis (detailed narrative for automated scans)
    # ------------------------------------------------------------------

    def notify_market_scan(
        self,
        analysis_text: str,
        top_charts: Optional[List[str]] = None,
    ) -> bool:
        """Send a full market scan analysis with optional top charts.

        Sends the text analysis first, then each chart as a separate photo.
        """
        ok = self._send_text(analysis_text)

        if top_charts:
            for chart_path in top_charts[:3]:
                p = Path(chart_path)
                if p.exists():
                    self._send_photo_only(chart_path)

        return ok

    def _send_photo_only(self, chart_path: str) -> bool:
        """Queue a captionless photo — fire-and-forget (Tier 3.2)."""
        if not self._enabled:
            return False
        fire_and_forget(
            self._send_photo_only_sync, chart_path, description="Telegram photo"
        )
        return True

    def _send_photo_only_sync(self, chart_path: str) -> bool:
        """Blocking photo send — runs on the notify worker."""
        import httpx

        try:
            with open(chart_path, "rb") as f:
                resp = httpx.post(
                    self._api_url("sendPhoto"),
                    data={"chat_id": self._chat_id},
                    files={"photo": (Path(chart_path).name, f, "image/png")},
                    timeout=30.0,
                )
            return resp.status_code == 200 and resp.json().get("ok", False)
        except Exception as e:
            logger.error("Telegram photo-only send error: %s", e)
            return False
