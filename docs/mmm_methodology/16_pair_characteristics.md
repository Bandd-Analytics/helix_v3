# 16 — Pair Characteristics

## Overview

Each pair in the 13-pair portfolio has distinct volatility, pip value, spread
characteristics, and optimal trading sessions. These differences require
pair-specific calibration of all MMM parameters.

## Full Pair Portfolio

### Low Tier (Standard Risk, 1.0%)

#### EURUSD
- **Pip value**: ~$10/pip per lot
- **Character**: Most liquid. Tight spreads. Textbook MMM patterns.
- **Asian range**: Typically < 40 pips (tight)
- **Stop hunt**: 20-40 pips. Hunts are tighter than GBP.
- **Level move**: ~70 pips
- **Best sessions**: London, early NYC
- **Notes**: Primary pair for learning MMM. Clean patterns.

#### GBPUSD
- **Pip value**: ~$10/pip per lot
- **Character**: Higher volatility than EUR. Wider swings. Core MMM pair.
- **Asian range**: Up to 50 pips
- **Stop hunt**: 25-50 pips. Standard MMM range.
- **Level move**: ~80 pips
- **Best sessions**: London (most active for GBP)
- **Notes**: Steve Mauro's go-to pair in training.

#### AUDUSD
- **Pip value**: ~$10/pip per lot
- **Character**: Slower, commodity-linked. Smaller ADR.
- **Asian range**: < 35 pips (tighter due to Asian timezone activity)
- **Stop hunt**: 15-35 pips. Smaller hunts.
- **Level move**: ~55 pips
- **Best sessions**: Asian/London overlap
- **Notes**: Good for Asian session observation. Active during AUD time.

#### EURCHF
- **Pip value**: ~$11/pip per lot
- **Character**: Ultra-low volatility. Tightest ranges.
- **Asian range**: < 25 pips (often < 20)
- **Stop hunt**: 15-30 pips
- **Level move**: ~45 pips (smallest in portfolio)
- **Best sessions**: London
- **Notes**: Clean accumulation detection. Small but reliable moves.

#### USDCHF
- **Pip value**: ~$11/pip per lot
- **Character**: Inverse of EURUSD. Cross-validates EUR bias.
- **Asian range**: < 35 pips
- **Stop hunt**: 20-40 pips
- **Level move**: ~60 pips
- **Best sessions**: London, NYC
- **Notes**: Use alongside EURUSD for confirmation.

### Medium Tier (Reduced Risk, 0.8%)

#### GBPAUD
- **Pip value**: ~$7.3/pip per lot
- **Character**: Volatile cross. Spiky. Wider everything.
- **Asian range**: Up to 60 pips
- **Stop hunt**: 30-60 pips
- **Level move**: ~100 pips (big moves)
- **Best sessions**: London/NYC overlap
- **Notes**: Requires wider SL buffer (5 pips). Spiky candles.

#### GBPJPY
- **Pip value**: ~$6.6/pip per lot
- **Character**: High volatility JPY cross. Fast, aggressive moves.
- **Asian range**: Up to 50 pips
- **Stop hunt**: 30-60 pips. Aggressive hunts.
- **Level move**: ~100 pips. Can run 150+ pips on trend days.
- **Best sessions**: London (GBP active) and early NYC
- **Notes**: MMM book says wider range for volatile JPY crosses.

#### GBPNZD
- **Pip value**: ~$5.8/pip per lot
- **Character**: Widest spreads. Only trade London/NYC.
- **Asian range**: Up to 65 pips (widest in FX portfolio)
- **Stop hunt**: 30-65 pips
- **Level move**: ~110 pips
- **Best sessions**: London/NYC only
- **Notes**: Big moves but wide spreads. Avoid Asian session entirely.

#### EURJPY
- **Pip value**: ~$6.6/pip per lot
- **Character**: EUR+JPY cross. Shows cycle disparity vs EURUSD.
- **Asian range**: Up to 50 pips
- **Stop hunt**: 25-50 pips
- **Level move**: ~85 pips
- **Notes**: When EURUSD is at L3 but EURJPY is at L1, trade EURJPY.

#### GBPCHF
- **Pip value**: ~$11/pip per lot
- **Character**: GBP volatility + CHF safe-haven dynamics.
- **Asian range**: Up to 50 pips
- **Stop hunt**: 25-50 pips
- **Level move**: ~85 pips
- **Notes**: Cleaner M/W patterns than GBPNZD.

#### USDJPY
- **Pip value**: ~$6.6/pip per lot
- **Character**: Most liquid JPY pair. Complements all JPY crosses.
- **Asian range**: Up to 45 pips
- **Stop hunt**: 25-50 pips
- **Level move**: ~80 pips
- **Notes**: Active during Asian session due to JPY.

#### AUDJPY
- **Pip value**: ~$6.6/pip per lot
- **Character**: Commodity + JPY. Shows fractional disparity.
- **Asian range**: Up to 45 pips
- **Stop hunt**: 20-45 pips
- **Level move**: ~75 pips
- **Notes**: When AUD hits L3, AUDJPY may show disparity.

### High Tier (Minimal Risk, 0.5%)

#### XAUUSD (Gold)
- **Pip value**: $1/pip per lot (1 pip = $0.01)
- **Character**: Violent. Brutal reversals. Completely different dynamics.
- **Asian range**: Up to 400 pips ($4.00)
- **Stop hunt**: 200-500 pips ($2-5)
- **Level move**: ~800 pips ($8.00)
- **Best sessions**: London/NYC (most active)
- **Constraints**: Max 0.1 lots, 3h max duration, 0.5% risk
- **Notes**: Treat as separate instrument. All parameters in "gold pips" ($0.01).

## Fractional Disparity

Per MMM book: When one pair in a correlated group is at L3 (extended/choppy)
but another is at L1 (fresh move), trade the L1 pair. Examples:
- EURUSD at L3, EURJPY at L1 → Trade EURJPY
- AUDUSD at L3, AUDJPY at L1 → Trade AUDJPY
- GBPUSD at L3, GBPCHF at L1 → Trade GBPCHF

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Per-pair stop hunt ranges | UNTESTED | Actual breach distribution by pair |
| Level move sizes are accurate | UNTESTED | Measured level distances by pair |
| Pip value affects risk sizing | UNTESTED | Verify lot sizing across pairs |
| Fractional disparity is tradeable | UNTESTED | Compare L1 trades when correlated pair at L3 |
| Optimal sessions per pair | UNTESTED | Win rate by session per pair |
