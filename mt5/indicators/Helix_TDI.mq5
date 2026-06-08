//+------------------------------------------------------------------+
//| Helix_TDI.mq5                                                   |
//| Traders Dynamic Index — V2-verified parameters.                  |
//| Separate window: RSI Price Line (Green), Trade Signal (Red),     |
//| Market Base Line (Yellow), Volatility Bands, Shark Fin zones.    |
//| Ported from helix_v3/core/tdi.py                                 |
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "1.00"
#property indicator_separate_window
#property indicator_buffers 5
#property indicator_plots   5
#property indicator_minimum 10
#property indicator_maximum 90

// Green: RSI Price Line
#property indicator_label1  "RSI Price (Green)"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrLime
#property indicator_width1  2

// Red: Trade Signal Line
#property indicator_label2  "Trade Signal (Red)"
#property indicator_type2   DRAW_LINE
#property indicator_color2  clrRed
#property indicator_width2  1

// Yellow: Market Base Line
#property indicator_label3  "Market Base (Yellow)"
#property indicator_type3   DRAW_LINE
#property indicator_color3  clrYellow
#property indicator_width3  1

// Upper VB
#property indicator_label4  "Upper VB"
#property indicator_type4   DRAW_LINE
#property indicator_color4  clrDodgerBlue
#property indicator_style4  STYLE_DASH
#property indicator_width4  1

// Lower VB
#property indicator_label5  "Lower VB"
#property indicator_type5   DRAW_LINE
#property indicator_color5  clrDodgerBlue
#property indicator_style5  STYLE_DASH
#property indicator_width5  1

//--- V2-Verified Parameters (2026-04-27)
input int    InpRSIPeriod   = 21;       // RSI period (Wilder)
input int    InpPriceLine   = 2;        // RSI Price Line SMA
input int    InpSignalLine  = 7;        // Trade Signal Line SMA
input int    InpBaseLine    = 34;       // Market Base Line SMA
input double InpVBStdDev    = 1.6185;   // VB Bollinger StdDev
input int    InpVBPeriod    = 34;       // VB Bollinger period

//--- Shark Fin thresholds
input double InpSharkUpper  = 63.0;     // Shark Fin upper (overbought)
input double InpSharkLower  = 37.0;     // Shark Fin lower (oversold)

//--- Buffers
double GreenBuf[], RedBuf[], YellowBuf[], UpperBuf[], LowerBuf[];

// Internal RSI handle
int hRSI = INVALID_HANDLE;

//+------------------------------------------------------------------+
int OnInit()
  {
   SetIndexBuffer(0, GreenBuf,  INDICATOR_DATA);
   SetIndexBuffer(1, RedBuf,    INDICATOR_DATA);
   SetIndexBuffer(2, YellowBuf, INDICATOR_DATA);
   SetIndexBuffer(3, UpperBuf,  INDICATOR_DATA);
   SetIndexBuffer(4, LowerBuf,  INDICATOR_DATA);

   for(int i = 0; i < 5; i++)
      PlotIndexSetDouble(i, PLOT_EMPTY_VALUE, EMPTY_VALUE);

   hRSI = iRSI(_Symbol, _Period, InpRSIPeriod, PRICE_CLOSE);
   if(hRSI == INVALID_HANDLE)
      return INIT_FAILED;

   // Shark Fin zone levels
   IndicatorSetInteger(INDICATOR_LEVELS, 4);
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 0, InpSharkUpper);
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 1, InpSharkLower);
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 2, 50.0);  // midline
   IndicatorSetDouble(INDICATOR_LEVELVALUE, 3, 50.0);
   IndicatorSetInteger(INDICATOR_LEVELCOLOR, 0, clrOrangeRed);
   IndicatorSetInteger(INDICATOR_LEVELCOLOR, 1, clrOrangeRed);
   IndicatorSetInteger(INDICATOR_LEVELCOLOR, 2, clrGray);
   IndicatorSetInteger(INDICATOR_LEVELSTYLE, 0, STYLE_DOT);
   IndicatorSetInteger(INDICATOR_LEVELSTYLE, 1, STYLE_DOT);
   IndicatorSetInteger(INDICATOR_LEVELSTYLE, 2, STYLE_DOT);

   IndicatorSetString(INDICATOR_SHORTNAME, "Helix TDI (RSI=" + IntegerToString(InpRSIPeriod) + ")");
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
   // Copy RSI values
   double rsi[];
   ArraySetAsSeries(rsi, false);
   int copied = CopyBuffer(hRSI, 0, 0, rates_total, rsi);
   if(copied <= 0) return 0;

   int start = MathMax(prev_calculated - 1, InpBaseLine + InpRSIPeriod);
   if(start < InpBaseLine + InpRSIPeriod) start = InpBaseLine + InpRSIPeriod;

   for(int i = start; i < rates_total; i++)
     {
      // Green: SMA(RSI, PriceLine period)
      double sumG = 0;
      for(int j = 0; j < InpPriceLine && (i - j) >= 0; j++)
         sumG += rsi[i - j];
      GreenBuf[i] = sumG / InpPriceLine;

      // Red: SMA(RSI, SignalLine period)
      double sumR = 0;
      for(int j = 0; j < InpSignalLine && (i - j) >= 0; j++)
         sumR += rsi[i - j];
      RedBuf[i] = sumR / InpSignalLine;

      // Yellow: SMA(RSI, BaseLine period)
      double sumY = 0;
      for(int j = 0; j < InpBaseLine && (i - j) >= 0; j++)
         sumY += rsi[i - j];
      YellowBuf[i] = sumY / InpBaseLine;

      // VB: Bollinger on RSI (population stddev)
      double sumVB = 0, sumSq = 0;
      for(int j = 0; j < InpVBPeriod && (i - j) >= 0; j++)
        {
         sumVB += rsi[i - j];
        }
      double meanVB = sumVB / InpVBPeriod;
      for(int j = 0; j < InpVBPeriod && (i - j) >= 0; j++)
        {
         double d = rsi[i - j] - meanVB;
         sumSq += d * d;
        }
      double sigma = MathSqrt(sumSq / InpVBPeriod);

      UpperBuf[i] = YellowBuf[i] + InpVBStdDev * sigma;
      LowerBuf[i] = YellowBuf[i] - InpVBStdDev * sigma;
     }

   return rates_total;
  }
//+------------------------------------------------------------------+
