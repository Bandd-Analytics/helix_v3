# 13 — Multi-Timeframe Analysis Sequence

## Overview

MMM requires a strict top-down analysis sequence. You NEVER enter on M15 without
knowing where you are on H1, H4, and Weekly. Each timeframe feeds context DOWN
to the next.

## Analysis Sequence

```
WEEKLY (D1/H4) → 4-HOUR (H4) → 1-HOUR (H1) → 15-MINUTE (M15)
```

### Step 1: Weekly Structure
**Questions to answer:**
- Where are we in the 3-day/weekly cycle?
- Has a peak high or peak low been made?
- Is a mid-week reversal due?
- What is the weekly EMA bias?

**Data used**: D1 bars (30 days), H4 bars (120 bars)

**Output**: Weekly trend direction, cycle position, week phase

### Step 2: 4-Hour Context
**Questions to answer:**
- What level are we at (L1/L2/L3)?
- Is a peak formation detected on H4?
- Is the market choppy (L3 indicator)?
- What is the H4 EMA alignment?

**Data used**: H4 bars (120 bars), last 18 H4 bars (3 days)

**Output**: Level count, choppiness flag, H4 trend direction

### Step 3: 1-Hour Confirmation
**Questions to answer:**
- What session are we in?
- Where is HOD/LOD? Are they locked?
- Has EMA 50 crossed EMA 200?
- What is the intraday level count?

**Data used**: H1 bars (100 bars), today's H1 bars

**Output**: Session phase, HOD/LOD status, intraday trend

### Step 4: 15-Minute Entry
**Questions to answer:**
- Is the Asian range valid (accumulation)?
- Has a stop hunt occurred?
- What direction does the M/W indicate?
- How many pushes? Is RRT detected?

**Data used**: M15 bars (200 bars), post-Asian M15 bars

**Output**: Entry signal, direction, confidence score

## Confluence Scoring (0-100)

From `mtf_analyzer.py`:

| Factor | Points |
|--------|--------|
| **Weekly** | |
| Weekly trend matches entry direction | +20 |
| Mid-week reversal expected | +10 |
| **4-Hour** | |
| H4 at Level 3 | +15 |
| H4 at Level 2 | +10 |
| H4 trend matches entry | +10 |
| **1-Hour** | |
| H1 trend matches entry | +10 |
| HOD or LOD locked | +5 |
| In TRUE_TREND or STOP_HUNT session | +5 |
| **15-Minute** | |
| Accumulation valid | +5 |
| Stop hunt detected | +10 |
| 3+ pushes | +5 |
| M/W forming | +5 |
| RRT detected | +5 |

**Maximum**: 100 points

### Trade Validity
A trade is valid when:
- Confluence score >= 50
- Entry direction is not NEUTRAL
- Maximum 1 rejection reason (allows minor conflicts)

### Rejection Reasons
- Weekly trend conflicts with entry direction
- H4 choppy but not at L3
- H4 trend conflicts with entry direction
- Session winding down (RETURN_TO_ACCUM)
- Asian range too wide

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Top-down alignment improves win rate | UNTESTED | Win rate at different confluence scores |
| Confluence >= 50 is correct threshold | UNTESTED | Optimize threshold from backtest data |
| Weekly alignment is most important | UNTESTED | Weight analysis of each factor |
| 1 rejection reason is acceptable | UNTESTED | Outcomes with 0 vs 1 vs 2 rejections |
