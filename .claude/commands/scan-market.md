# /scan-market

Run a full market scan across all configured pairs and timeframes. Displays the market dashboard with readiness scores and sends WhatsApp alert for high-readiness setups.

## Usage
```
/scan-market
```

## What it does
1. Connects to MT5
2. Runs quant engine on all 7 pairs x 2 timeframes
3. Computes readiness scores
4. Displays formatted dashboard
5. Sends WhatsApp market update (if high readiness found)
