# /trade-report

Generate and send trade performance reports via WhatsApp.

## Usage
```
/trade-report session    # Current session stats
/trade-report daily      # Today's stats
/trade-report weekly     # This week's stats
/trade-report monthly    # This month's stats
/trade-report all        # All-time performance summary
```

## What it does
1. Queries the trade journal SQLite database
2. Computes performance metrics (win rate, pips, P&L, profit factor, etc.)
3. Formats and sends WhatsApp report
4. Session/daily: full symbol breakdown
5. Weekly/monthly: best and worst pair only
