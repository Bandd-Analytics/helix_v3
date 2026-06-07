# 01 — Market Maker Theory

## Core Premise

Market makers (MMs) are large institutional players who provide liquidity and
profit from the bid-ask spread. Per Steve Mauro, they also actively manipulate
price to accumulate positions at favorable levels before driving price in their
intended direction.

## The MM Cycle

The entire MMM methodology rests on this repeating cycle:

```
ACCUMULATE → STOP HUNT → TRUE TREND → DISTRIBUTION
```

1. **Accumulation** (Asian session): MMs build positions within a tight range.
   Price moves in a narrow channel. Retail traders set stops just outside this range.

2. **Stop Hunt** (London Gap / early London): MMs spike price through the
   accumulation zone boundary to trigger retail stop losses and limit orders,
   creating liquidity for their real position.

3. **True Trend** (London / early NYC): After the stop hunt completes, MMs drive
   price in the opposite direction — the real move. This is where you enter.

4. **Distribution** (Late NYC / pre-Asian): MMs take profit. Price returns toward
   the accumulation zone. No new entries.

## Key Concepts

### Levels (L1, L2, L3)

Each cycle move is measured in "levels" — the distance from one consolidation
to the next:

- **L1**: First major move from peak. Most predictable. ~60-80 pips on majors.
- **L2**: Second consolidation and move. Slightly less predictable.
- **L3**: Third level. Price is extended. Choppy, dangerous. Avoid trading L3 unless
  you have strong confluence.

### Peak Formation

A peak forms at the extreme of a cycle (high or low). Identified by:
- Price reaching L2/L3 extension from previous cycle
- Multiple rejections at the level (M-top or W-bottom)
- TDI showing overbought/oversold divergence

### The 3-Day Cycle

MMs typically run a 3-day cycle:
- Day 1: Accumulation and initial stop hunt
- Day 2: True trend run (biggest move)
- Day 3: Distribution, potential reversal setup for next cycle

See [02_3_day_cycle.md](02_3_day_cycle.md) for detailed rules.

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| MM cycle structure | UNTESTED | Requires session-level replay analysis |
| L1/L2/L3 level distances | UNTESTED | Need to measure actual level moves per pair |
| 3-day cycle duration | UNTESTED | Statistical analysis of cycle length distribution |
| Peak formation reliability | UNTESTED | Count M/W at actual cycle extremes vs mid-cycle |
