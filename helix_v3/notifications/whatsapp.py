"""WhatsApp Notification Module via Twilio.

Sends automated WhatsApp messages for:
- Valid trade setups detected (high readiness)
- Trade entries (order filled)
- T1 partial close hit
- Full trade close reports (entry/exit, prices, P&L, bias, reason)
- Market condition alerts
- Period reports: per-session, EOD, weekly, monthly summaries
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("whatsapp_notify")

# East Africa Time (UTC+3)
EAT = timezone(timedelta(hours=3))


def _eat_now() -> str:
    return datetime.now(EAT).strftime("%H:%M EAT")


def _eat_datetime() -> str:
    return datetime.now(EAT).strftime("%Y-%m-%d %H:%M EAT")


def _to_eat(iso_or_str: str) -> str:
    """Convert an ISO timestamp or arbitrary string to EAT display."""
    try:
        if "T" in iso_or_str:
            dt = datetime.fromisoformat(iso_or_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(EAT).strftime("%Y-%m-%d %H:%M EAT")
        return iso_or_str  # Already formatted
    except Exception:
        return iso_or_str


def _format_duration(minutes: float) -> str:
    if minutes < 60:
        return f"{minutes:.0f}min"
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    return f"{hours}h {mins}min"


class WhatsAppNotifier:
    """Twilio-based WhatsApp notification service."""

    def __init__(self) -> None:
        import os

        self._account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
        self._auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")
        self._from_number = os.getenv("TWILIO_WHATSAPP_FROM", "")
        self._to_number = os.getenv("WHATSAPP_TO", "")
        self._enabled = bool(
            self._account_sid and self._auth_token
            and self._from_number and self._to_number
        )

        if self._enabled:
            logger.info("WhatsApp notifications ENABLED -> %s", self._to_number)
        else:
            logger.warning(
                "WhatsApp notifications DISABLED - set TWILIO_ACCOUNT_SID, "
                "TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_FROM, WHATSAPP_TO in .env"
            )

    @property
    def enabled(self) -> bool:
        return self._enabled

    def _send(self, message: str, image_path: Optional[str] = None) -> bool:
        """Send a WhatsApp message, optionally with an attached image.

        For image attachments, the file is uploaded to Twilio's media hosting
        first, then the media URL is included in the message.
        """
        if not self._enabled:
            logger.debug("WhatsApp disabled, skipping: %s", message[:80])
            return False

        import httpx

        url = (
            f"https://api.twilio.com/2010-04-01/Accounts/"
            f"{self._account_sid}/Messages.json"
        )

        try:
            data = {
                "From": f"whatsapp:{self._from_number}",
                "To": f"whatsapp:{self._to_number}",
                "Body": message,
            }

            response = httpx.post(
                url,
                auth=(self._account_sid, self._auth_token),
                data=data,
                timeout=30.0,
            )

            if response.status_code in (200, 201):
                sid = response.json().get("sid", "")
                logger.info("WhatsApp sent: %s (SID: %s)", message[:60], sid)
                return True
            else:
                logger.error(
                    "WhatsApp send failed: %d %s",
                    response.status_code, response.text[:200],
                )
                return False

        except Exception as e:
            logger.error("WhatsApp send error: %s", e)
            return False

    def send_with_chart(self, message: str, chart_path: str) -> bool:
        """Send the message text-only on WhatsApp.

        Charts previously went through tmpfiles.org — a public,
        unauthenticated host — exposing annotated entry/SL/TP levels to
        anyone (audit Tier 0.8). Twilio sandbox cannot take inline media, so
        until a private media bucket exists WhatsApp is text-only; Telegram's
        native photo upload remains the channel for chart images.
        """
        if not self._enabled:
            return False

        from pathlib import Path

        if Path(chart_path).exists():
            logger.info(
                "WhatsApp chart suppressed (no private media host): %s — sending text only",
                chart_path,
            )
            message = f"{message}\n[Chart available via Telegram]"
        else:
            logger.warning("Chart not found for WhatsApp: %s, sending text only", chart_path)
        return self._send(message)

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

        # Prices
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

        # Bias & Setup
        if bias or cycle_level or confidence:
            msg += "\n--- Setup ---\n"
            if bias:
                msg += f"Bias:      {bias}\n"
            if cycle_level:
                msg += f"Cycle:     Level {cycle_level}\n"
            if confidence:
                msg += f"Confidence:{confidence:.0%}\n"

        # P&L
        msg += "\n--- P&L ---\n"
        if gross_profit:
            msg += f"Gross:     ${gross_profit:+.2f}\n"
        if commission:
            msg += f"Commission:${commission:.2f}\n"
        if swap:
            msg += f"Swap:      ${swap:+.2f}\n"
        msg += f"Net P&L:   ${net_profit:+.2f}\n"

        # T1 info
        if t1_hit:
            msg += "\n--- Partial Close ---\n"
            msg += f"T1 Hit:    Yes (+{t1_pips:.1f} pips)\n"
            msg += f"T1 Profit: ${t1_profit:.2f}\n"

        # Account
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

        # Timing
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

        from datetime import timezone as _tz
        h = datetime.now(_tz.utc).hour
        if 1 <= h < 5:
            phase, note = "ACCUMULATION", "Asian range forming"
        elif 5 <= h < 8:
            phase, note = "STOP HUNT", "London breaking Asian range"
        elif 8 <= h < 13:
            phase, note = "TRUE TREND", "Real move underway"
        elif 13 <= h < 17:
            phase, note = "NYC REVERSAL", "Late session, high conviction only"
        else:
            phase, note = "DEAD TIME", "No entries"

        dow = datetime.now(EAT).strftime("%A")
        seen = set()
        filtered = [s for s in high_readiness if s["symbol"] not in seen and not seen.add(s["symbol"])]

        msg = f"HELIX V3 MARKET SCAN\n{'='*30}\n{dow} | {phase}\n{note}\n"
        for s in filtered[:5]:
            bias = s.get("bias", "NEUTRAL")
            readiness = s.get("trade_readiness", 0)
            hunt_active = s.get("stop_hunt_active", False)
            hunt_dir = s.get("stop_hunt_direction", "")
            hunt_pips = s.get("stop_hunt_breach_pips", 0) or 0
            bar = ">" * (readiness // 10) + "-" * (10 - readiness // 10)
            msg += f"\n{s['symbol']} {bias}\n  [{bar}] {readiness}/100\n"
            if hunt_active and hunt_pips > 0:
                real_dir = "SELL" if hunt_dir == "BUY" else "BUY"
                msg += f"  Stop hunt {hunt_dir} {hunt_pips:.0f}p — expect {real_dir}\n"
        msg += f"\n{_eat_datetime()}"
        return self._send(msg)

    def notify_scanner_watchlist(self, report: str) -> bool:
        """Send the alert-only scanner watchlist report."""
        return self._send(report)

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

        # Account
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

        # Best / Worst
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

        # By symbol (full for session/daily, best+worst only for weekly/monthly)
        if by_symbol:
            is_long_period = period_name.upper() in ("WEEKLY", "MONTHLY")
            if is_long_period and len(by_symbol) > 2:
                msg += "\n--- Top & Bottom Pairs ---\n"
                sorted_syms = sorted(by_symbol.items(), key=lambda x: x[1]["net_profit"], reverse=True)
                # Best
                sym, data = sorted_syms[0]
                msg += (
                    f"Best:  {sym} {data['trades']}T "
                    f"WR={data['win_rate']:.0f}% "
                    f"{data['total_pips']:+.1f}p "
                    f"${data['net_profit']:+.2f}\n"
                )
                # Worst
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

        # Winning setups
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
        """Send a full setup flashcard with annotated chart attached."""
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

        msg += f"\nSee attached chart for visual confluence.\n{_eat_datetime()}"

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
