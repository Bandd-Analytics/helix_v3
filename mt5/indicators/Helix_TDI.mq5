//+------------------------------------------------------------------+
//| Helix_TDI.mq5                                                   |
//| Traders Dynamic Index with Shark Fin color changes.              |
//| Matches JTDI Shark Fins PineScript behavior:                     |
//|   - Fast MA (Green) turns RED when outside VB (shark fin)        |
//|   - Slow MA (Black) turns ORANGE when outside VB (shark fin)     |
//|   - VB band fill between upper and lower                         |
//|   - OB/OS reference levels                                       |
//| V2-verified parameters from helix_v3/core/tdi.py                 |
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "2.00"
#property indicator_separate_window
#property indicator_buffers 9
#property indicator_plots   5
#property indicator_minimum 10
#property indicator_maximum 90

// Plot 1: Fast MA (Green/Red on shark fin) — DRAW_COLOR_LINE
#property indicator_label1  "Fast MA"
#property indicator_type1   DRAW_COLOR_LINE
#property indicator_color1  clrLime, clrRed
#property indicator_width1  2

// Plot 2: Slow MA (DimGray/Orange on shark fin) — DRAW_COLOR_LINE
#property indicator_label2  "Slow MA"
#property indicator_type2   DRAW_COLOR_LINE
#property indicator_color2  clrDimGray, clrOrange
#property indicator_width2  2

// Plot 3: Market Base Line (Yellow)
#property indicator_label3  "MBL"
#property indicator_type3   DRAW_LINE
#property indicator_color3  clrYellow
#property indicator_width3  2

// Plot 4: Upper VB
#property indicator_label4  "Upper VB"
#property indicator_type4   DRAW_LINE
#property indicator_color4  clrDodgerBlue
#property indicator_width4  2

// Plot 5: Lower VB
#property indicator_label5  "Lower VB"
#property indicator_type5   DRAW_LINE
#property indicator_color5  clrDodgerBlue
#property indicator_width5  2

//--- Inputs — V2-Verified Parameters
input group "TDI"
input int    InpRSIPeriod   = 21;       // RSI period (Wilder)
input int    InpFastMA      = 2;        // Fast MA period (Green line)
input int    InpSlowMA      = 7;        // Slow MA period (Trade Signal)
input int    InpBandLength  = 34;       // Band / MBL period
input double InpBandMult    = 1.6185;   // Volatility Band multiplier
input bool   InpShowMBL     = true;     // Show Market Base Line

input group "Levels"
input int    InpOBLevel     = 63;       // Overbought (Shark Fin upper)
input int    InpMidLevel    = 50;       // Midline
input int    InpOSLevel     = 37;       // Oversold (Shark Fin lower)

input group "Colors"
input color  InpFastNormal  = clrLime;      // Fast MA normal
input color  InpFastFin     = clrRed;       // Fast MA shark fin
input color  InpSlowNormal  = clrDimGray;   // Slow MA normal
input color  InpSlowFin     = clrOrange;    // Slow MA shark fin
input color  InpBandColor   = clrDodgerBlue; // Volatility Bands
input color  InpMBLColor    = clrYellow;     // Market Base Line

//--- Buffers
double FastBuf[], FastClrBuf[];   // Fast MA + color index
double SlowBuf[], SlowClrBuf[];   // Slow MA + color index
double MBLBuf[];                   // Market Base Line
double UpperBuf[], LowerBuf[];     // VB bands
double RSIBuf[];                   // Raw RSI (internal, not plotted)
double StdBuf[];                   // StdDev (internal)

int hRSI = INVALID_HANDLE;

//+------------------------------------------------------------------+
int OnInit()
  {
   // Plot 1: Fast MA (color line)
   SetIndexBuffer(0, FastBuf,    INDICATOR_DATA);
   SetIndexBuffer(1, FastClrBuf, INDICATOR_COLOR_INDEX);
   PlotIndexSetInteger(0, PLOT_COLOR_INDEXES, 2);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 0, InpFastNormal);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 1, InpFastFin);

   // Plot 2: Slow MA (color line)
   SetIndexBuffer(2, SlowBuf,    INDICATOR_DATA);
   SetIndexBuffer(3, SlowClrBuf, INDICATOR_COLOR_INDEX);
   PlotIndexSetInteger(1, PLOT_COLOR_INDEXES, 2);
   PlotIndexSetInteger(1, PLOT_LINE_COLOR, 0, InpSlowNormal);
   PlotIndexSetInteger(1, PLOT_LINE_COLOR, 1, InpSlowFin);

   // Plot 3: MBL
   SetIndexBuffer(4, MBLBuf, INDICATOR_DATA);
   PlotIndexSetInteger(2, PLOT_LINE_COLOR, 0, InpMBLColor);

   // Plot 4-5: VB bands
   SetIndexBuffer(5, UpperBuf, INDICATOR_DATA);
   SetIndexBuffer(6, LowerBuf, INDICATOR_DATA);
   PlotIndexSetInteger(3, PLOT_LINE_COLOR, 0, InpBandColor);
   PlotIndexSetInteger(4, PLOT_LINE_COLOR, 0, InpBandColor);

   // Internal buffers (not plotted)
   SetIndexBuffer(7, RSIBuf, INDICATOR_CALCULATIONS);
   SetIndexBuffer(8, StdBuf, INDICATOR_CALCULATIONS);

   for(int i = 0; i < 7; i++)
      PlotIndexSetDouble(i, PLOT_EMPTY_VALUE, EMPTY_VALUE);

   hRSI = iRSI(_Symbol, _Period, InpRSIPeriod, PRICE_CLOSE);
   if(hRSI == INVALID_HANDLE)
      return INIT_FAILED;

   // Reference levels
   IndicatorSetInteger(INDICATOR_LEVELS, 3);
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 0, InpOBLevel);
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 1, InpMidLevel);
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 2, InpOSLevel);
   IndicatorSetInteger(INDICATOR_LEVELCOLOR, 0, clrOrangeRed);
   IndicatorSetInteger(INDICATOR_LEVELCOLOR, 1, clrRoyalBlue);
   IndicatorSetInteger(INDICATOR_LEVELCOLOR, 2, clrGreen);
   IndicatorSetInteger(INDICATOR_LEVELSTYLE, 0, STYLE_DASH);
   IndicatorSetInteger(INDICATOR_LEVELSTYLE, 1, STYLE_DASH);
   IndicatorSetInteger(INDICATOR_LEVELSTYLE, 2, STYLE_DASH);

   IndicatorSetString(INDICATOR_SHORTNAME,
      "Helix TDI Shark Fins (RSI=" + IntegerToString(InpRSIPeriod) + ")");
   return INIT_SUCCEEDED;
  }

void OnDeinit(const int reason)
  {
   if(hRSI != INVALID_HANDLE) IndicatorRelease(hRSI);
  }

//+------------------------------------------------------------------+
int OnCalculate(const int rates_total, const int prev_calculated,
                const datetime &time[], const double &open[],
                const double &high[], const double &low[],
                const double &close[], const long &tick_volume[],
                const long &volume[], const int &spread[])
  {
   // Copy RSI
   int copied = CopyBuffer(hRSI, 0, 0, rates_total, RSIBuf);
   if(copied <= 0) return 0;

   int minBars = InpBandLength + InpRSIPeriod + 1;
   int start = MathMax(prev_calculated - 1, minBars);
   if(start < minBars) start = minBars;

   for(int i = start; i < rates_total; i++)
     {
      // --- Fast MA: SMA(RSI, FastMA period) ---
      double sumF = 0;
      for(int j = 0; j < InpFastMA && (i - j) >= 0; j++)
         sumF += RSIBuf[i - j];
      FastBuf[i] = sumF / InpFastMA;

      // --- Slow MA: SMA(RSI, SlowMA period) ---
      double sumS = 0;
      for(int j = 0; j < InpSlowMA && (i - j) >= 0; j++)
         sumS += RSIBuf[i - j];
      SlowBuf[i] = sumS / InpSlowMA;

      // --- MBL: SMA(RSI, BandLength) = Bollinger basis ---
      double sumB = 0;
      for(int j = 0; j < InpBandLength && (i - j) >= 0; j++)
         sumB += RSIBuf[i - j];
      double basis = sumB / InpBandLength;
      MBLBuf[i] = InpShowMBL ? basis : EMPTY_VALUE;

      // --- VB: Bollinger bands on RSI (population stddev) ---
      double sumSq = 0;
      for(int j = 0; j < InpBandLength && (i - j) >= 0; j++)
        {
         double d = RSIBuf[i - j] - basis;
         sumSq += d * d;
        }
      double sigma = MathSqrt(sumSq / InpBandLength);
      UpperBuf[i] = basis + InpBandMult * sigma;
      LowerBuf[i] = basis - InpBandMult * sigma;

      // --- Shark Fin color: line outside VB = fin active ---
      bool fastFin = FastBuf[i] > UpperBuf[i] || FastBuf[i] < LowerBuf[i];
      bool slowFin = SlowBuf[i] > UpperBuf[i] || SlowBuf[i] < LowerBuf[i];

      FastClrBuf[i] = fastFin ? 1 : 0;  // 0=normal(green), 1=fin(red)
      SlowClrBuf[i] = slowFin ? 1 : 0;  // 0=normal(gray),  1=fin(orange)
     }

   return rates_total;
  }
//+------------------------------------------------------------------+
