# MMM Session Cycle Guide

This document explains the Market Maker Method (Steve Mauro) daily session cycle — the core
framework that drives every entry decision in Helix V3.

## The Core Idea

Institutional market makers follow a predictable daily cycle to accumulate positions, trap
retail traders with fake breakouts, then drive price in the real direction for profit. The
session phases describe where we are in that cycle.

## Daily Session Phases

| Phase               | UTC Time      | Kenyan Time (EAT) | What Is Happening                                                                                                                                                                                                                   | Entry Quality                                                                      |
|---------------------|---------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **ACCUMULATION**    | 01:00 - 05:00 | 04:00 - 08:00     | Asia session. Price ranges tight. Market makers quietly build positions. The "Asian range" (box) forms here. Low volume, small candles.                                                                                             | NO ENTRY — range is forming                                                        |
| **STOP_HUNT**       | 05:00 - 08:00 | 08:00 - 11:00     | London pre-market / early London. Price BREAKS above or below the Asian range. This triggers retail stop losses. **This is the FAKE move** — retail traders get stopped out, market makers fill their real orders at better prices. | BEST ENTRY WINDOW. Enter after the fake breakout reverses.                         |
| **TRUE_TREND**      | 08:00 - 13:00 | 11:00 - 16:00     | London main session. After the fake stop hunt, price reverses and moves in the REAL direction. This is where profits run. The M/W pattern confirms the reversal.                                                                    | GOOD for entries if you missed the stop hunt. This is where the real move happens. |
| **NYC_REVERSAL**    | 13:00 - 17:00 | 16:00 - 20:00     | New York overlap. Late-day potential reversal. Can get a secondary entry here but it's less reliable than London. Often price retraces part of the London move.                                                                     | SECONDARY window. Less reliable.                                                   |
| **RETURN_TO_ACCUM** | 17:00 - 01:00 | 20:00 - 04:00     | Session winding down. Price drifts back toward the center. Volume dies. Nothing useful happens here.                                                                                                                                | NO ENTRY — dead time. System blocks all entries.                                   |

## Visual: The Daily Price Cycle

```
Price
  |
  |          STOP HUNT (fake breakout above Asian High)
  |         /
  |    ----/---- Asian High ---------------------------
  |   |  /  |
  |   |/    |   ACCUMULATION
  |   |     |   (tight range, low volume)
  |   |     |
  |   --------- Asian Low ----------------------------
  |         |
  |         |    TRUE TREND starts here
  |         |    (real move, opposite to the fake hunt)
  |         |         \
  |         |          \
  |         |           \   <-- This is where profit happens
  |         |            \
  |         |             \
  +----+----+------+-------+------+---> Time
     Asia  London  London  NYC   Dead
     04:00  08:00  11:00  16:00  20:00  (Kenyan time)
     01:00  05:00  08:00  13:00  17:00  (UTC)
```

## How the Entry Actually Works

1. **Asian session (04:00-08:00 EAT):** Watch the range form. Note the High and Low.

2. **Stop hunt (08:00-11:00 EAT):** Price breaks ABOVE the Asian High (or BELOW the Asian Low).
   Retail traders think "breakout!" and go long (or short). Their stop losses are now exposed.

3. **The reversal:** Price reverses sharply. Those retail stops get hit. Market makers now
   have filled their real positions at the prices they wanted.

4. **Entry signal:** The system detects:
   - Asian range formed (accumulation valid)
   - Price broke the range (stop hunt detected, X pips of breach)
   - M/W pattern forming (W-bottom = BUY, M-top = SELL)
   - At least 3 pushes in the structure
   - TDI confirmation (momentum aligning)

5. **True trend (11:00-16:00 EAT):** Price moves in the real direction. Our trade is in profit.
   T1 partial close at 1:1 RR, then trail the stop.

## The Weekly Cycle

The daily cycle sits inside a weekly cycle:

| Weekly Phase | Days | Kenyan Reference | What's Happening |
|---|---|---|---|
| **EARLY_WEEK** | Sunday-Monday | Sun night - Mon | Cycle starts. First accumulation + stop hunt. Often the strongest setups. |
| **MID_WEEK** | Tuesday-Wednesday | Tue - Wed | Mid-week reversal zone. If early-week pushed one direction, the reversal often happens here. Wednesday accumulation on GBPJPY has 70.5% win rate. |
| **LATE_WEEK** | Thursday-Friday | Thu - Fri | Final push or exhaustion. Friday exits before weekend. Less reliable for new entries. |

## H4 Level Count

The H4 level count tracks how many "pushes" or legs the market has made on the 4-hour timeframe:

| Level | Meaning | Entry Quality |
|---|---|---|
| **L0** | No clear structure yet | Neutral — needs other confluence |
| **L1** | First push | Early in the cycle, good for with-trend entries |
| **L2** | Second push | Building momentum, still room to run |
| **L3** | Third push | **Peak/reversal expected.** This is where the best counter-trend setups form. All R_RUNNER setups are L3. |

## What R_RUNNER Setups Look Like

All 3 R_RUNNER setups share this exact profile:

```
THE_33_MW | BUY | EARLY_WEEK | L3 | STOP_HUNT
```

Translation in plain language:
- **THE_33_MW:** Pattern type "The 33" with M/W confirmation
- **BUY:** W-bottom pattern detected (the reversal signal)
- **EARLY_WEEK:** Monday (cycle just started)
- **L3:** H4 has made 3 pushes down (exhaustion)
- **STOP_HUNT:** London just broke below Asian Low (the fake move)

So the trade is: Market pushed down 3 times on H4, Asia accumulated, London broke below
to stop out longs, then a W-bottom forms signaling the reversal. Enter BUY.

This happens on GBPJPY on Mondays during the 08:00-11:00 EAT window with 85-90% success rate.

## Kenyan Time Quick Reference

For quick reference during live trading:

| Time (EAT) | What To Do |
|---|---|
| 04:00 - 08:00 | Watch Asian range form. Note the box. Do NOT trade. |
| 08:00 - 09:00 | Watch for stop hunt. Price should break Asian H or L. |
| 09:00 - 11:00 | PRIME ENTRY WINDOW. If stop hunt + M/W + 3 pushes, the system enters. |
| 11:00 - 16:00 | Manage open trades. Still valid for new entries if conditions met. |
| 16:00 - 20:00 | NYC reversal. Secondary window only. Tighter targets. |
| 20:00 - 04:00 | DONE. Close anything not in profit. Wait for next day. |

## Filter Signals (from Codex Ablation Research)

These filters improve win rate when applied on top of the session cycle:

| Filter | What It Checks | Effect |
|---|---|---|
| **TDI RSI > Signal** | Momentum already turning in entry direction | GBPJPY: 60% -> 100% win rate |
| **Asian Range >= 30 pips** | Accumulation was substantial, not just noise | EURJPY: 50% -> 75% win rate |
| **Hunt within pair expected range** | Stop hunt wasn't abnormally deep | GBPJPY true-trend: 64% -> 82% win rate |

## RRS Performance Grades

| Grade | Favorable Rate | Meaning | Action |
|---|---|---|---|
| **R_RUNNER** | >= 75% | Elite setup. Historically wins 3 out of 4 times. | Highest conviction. Full risk allocation. |
| **R_REPEATER** | >= 50%, < 75% | Solid repeatable edge. Wins more than it loses. | Standard risk. The volume is here (90 setups). |
| **S_STRANGER** | < 50% | Loses more than it wins. Only interesting if payoff is asymmetric. | Watch only unless avg exit is strongly positive. |