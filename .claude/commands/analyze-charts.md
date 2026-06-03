# /analyze-charts

Generate fresh charts for all pairs and provide vision analysis. Writes verdict JSONs to `verdicts/` directory for local consensus mode.

## Usage
```
/analyze-charts
/analyze-charts GBPJPY
/analyze-charts EURUSD GBPJPY XAUUSD
```

## What it does
1. Connects to MT5 and fetches latest data
2. Exports 1024x1024 vision charts for specified pairs (or all)
3. Claude reads each chart and produces MMM structural analysis
4. Writes verdict JSON files to `verdicts/`
5. Reports consensus readiness for each pair
