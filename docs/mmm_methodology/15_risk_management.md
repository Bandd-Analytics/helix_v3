# 15 — Risk Management

## Overview

MMM risk management is multi-layered: per-trade, per-pair, per-session, and
account-wide. The system uses a persistent re-entry guard to prevent revenge
trading.

## Per-Trade Risk

| Tier | Risk % | Max Lot |
|------|--------|---------|
| Low (EURUSD, GBPUSD, AUDUSD, EURCHF, USDCHF) | 1.0% | 1.0 |
| Medium (GBPAUD, GBPJPY, GBPNZD, EURJPY, GBPCHF, USDJPY, AUDJPY) | 0.8% | 0.5 |
| High (XAUUSD) | 0.5% | 0.1 |

## Drawdown Circuit Breaker

From `gatekeeper.py`:
```
drawdown = (balance - equity) / balance
if drawdown >= 8%: HALT ALL TRADING
```

Maximum drawdown target: < 8% of account balance.

## Re-Entry Guard (Persistent, SQLite-Backed)

From `reentry_guard.py`:

### Rules
1. **After ANY exit** on a symbol → 2-hour cooldown (prevents same-setup churn)
2. **1 loss** on symbol+direction → Blocked until session transition
3. **2+ losses** on symbol+direction same day → BANNED for the day
4. **New trading day** (22:00 UTC reset) → All bans/cooldowns clear
5. **Startup** → Rebuild state from DB + MT5 history

### Why Persistent?
All state is written to SQLite immediately. If the orchestrator restarts, the
re-entry guard state survives. This prevents:
- Re-entering a losing setup after a crash/restart
- Losing track of daily loss counts
- Revenge trading after restart

### Database Schema
```sql
CREATE TABLE loss_events (
    id, symbol, direction, ticket, loss_pips, loss_usd,
    recorded_at, trading_day
);
CREATE TABLE bans (
    id, symbol, direction, ban_type, reason,
    created_at, trading_day
);
```

## Exposure Check

Before any new entry:
1. Check if there's already an open position on the same pair
2. If yes → BLOCK (no doubling up)
3. Check total open positions vs account limit

## Spread Protection

Each pair has a `max_spread_pips` threshold:
- If current spread > max_spread → BLOCK entry
- Protects against news spikes, illiquid hours, broker widening

| Pair | Max Spread |
|------|-----------|
| EURUSD | 2.0 pips |
| GBPUSD | 2.5 pips |
| AUDUSD | 2.0 pips |
| GBPAUD | 4.0 pips |
| GBPJPY | 4.0 pips |
| GBPNZD | 5.0 pips |
| XAUUSD | 5.0 pips |

## Slippage Protection

From `gatekeeper.py`:
- Maximum acceptable slippage configured per order
- If fill price deviates too much from expected → flag in journal

## Account Targets

- **Sharpe Ratio**: > 1.5
- **Max Drawdown**: < 8%
- **Per-trade risk**: 0.5-1.0% depending on tier

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Re-entry guard prevents revenge trading | UNTESTED | Compare outcomes with/without guard |
| 2-hour cooldown is appropriate | UNTESTED | Optimize cooldown duration |
| Day ban after 2 losses is correct | UNTESTED | Test 2 vs 3 loss threshold |
| 8% drawdown limit is appropriate | UNTESTED | Historical drawdown distribution |
| Spread thresholds block bad entries | UNTESTED | Entry quality at different spreads |
