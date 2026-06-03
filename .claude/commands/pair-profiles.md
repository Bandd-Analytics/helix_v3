# /pair-profiles

Display all pair risk profiles showing per-pair trade management rules.

## Usage
```
/pair-profiles
/pair-profiles GBPJPY
```

## What it does
1. Loads pair profiles from `config/pair_profiles.py`
2. Displays risk tier, max risk %, lot caps, spread limits
3. Shows stale thresholds, trailing parameters, duration limits
4. Explains why each pair has its specific rules
