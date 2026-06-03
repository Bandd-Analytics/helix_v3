# MT5 Connector Plugin

## Description
Handles all MetaTrader 5 terminal interactions.

## Capabilities
- Connect/disconnect to MT5 terminal
- Fetch OHLCV data (any symbol, any timeframe)
- Get account info (balance, equity, margin)
- Get symbol info (pip value, tick value, spread)
- Send market orders with SL/TP
- Modify SL/TP on open positions
- Partial close positions
- Query deal history

## Configuration
Set in `.env`:
```
MT5_LOGIN=your_login
MT5_PASSWORD=your_password
MT5_SERVER=your_server
MT5_PATH=path/to/terminal64.exe
```

## Requirements
- MetaTrader 5 terminal must be running
- AutoTrading must be enabled (Ctrl+E)
- Python MetaTrader5 package installed
