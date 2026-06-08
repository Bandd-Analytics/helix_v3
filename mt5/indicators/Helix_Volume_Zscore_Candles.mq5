//+------------------------------------------------------------------+
//| Helix_Volume_Zscore_Candles.mq5                                  |
//| Port of "Candle Colored by Volume Z-score [Morty]" PineScript.   |
//| Colors candles by volume/body Z-score: normal, large, extreme.   |
//| Low-volume candles highlighted for accumulation detection.        |
//+------------------------------------------------------------------+
#property copyright "Helix V3 — ported from Morty PineScript"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 5
#property indicator_plots   1

#property indicator_label1  "Volume Z"
#property indicator_type1   DRAW_COLOR_CANDLES
#property indicator_color1  clrWhite, clrBlue, clrGreen, clrBlack, clrPurple, clrRed, clrYellow
#property indicator_width1  2

//--- inputs
input group "Z-Score Settings"
input ENUM_APPLIED_VOLUME InpVolumeType = VOLUME_TICK;  // Volume source
input int    InpLength   = 20;    // Z-Score lookback
input double InpZ1       = 1.5;   // Large threshold (z1)
input double InpZ2       = 2.5;   // Extreme threshold (z2)
input double InpLowVolZ  = -1.0;  // Low volume threshold

input group "Source Mode"
input int InpSourceMode  = 0;     // 0=Volume, 1=Body, 2=Any(max), 3=All(min)

input group "Display"
input bool InpShowLowVol = true;  // Highlight low-volume candles

//--- buffers
double OpenBuf[], HighBuf[], LowBuf[], CloseBuf[], ColorBuf[];

//+------------------------------------------------------------------+
int OnInit()
  {
   SetIndexBuffer(0, OpenBuf,  INDICATOR_DATA);
   SetIndexBuffer(1, HighBuf,  INDICATOR_DATA);
   SetIndexBuffer(2, LowBuf,   INDICATOR_DATA);
   SetIndexBuffer(3, CloseBuf, INDICATOR_DATA);
   SetIndexBuffer(4, ColorBuf, INDICATOR_COLOR_INDEX);

   PlotIndexSetInteger(0, PLOT_COLOR_INDEXES, 7);
   // 0=white(up normal), 1=blue(up large), 2=green(up extreme)
   // 3=black(dn normal), 4=purple(dn large), 5=red(dn extreme)
   // 6=yellow(low volume)
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 0, clrWhite);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 1, clrDodgerBlue);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 2, clrGreen);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 3, clrDimGray);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 4, clrPurple);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 5, clrRed);
   PlotIndexSetInteger(0, PLOT_LINE_COLOR, 6, clrYellow);

   IndicatorSetString(INDICATOR_SHORTNAME, "Helix Vol Z-Score Candles");
   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
int OnCalculate(const int        rates_total,
                const int        prev_calculated,
                const datetime  &time[],
                const double    &open[],
                const double    &high[],
                const double    &low[],
                const double    &close[],
                const long      &tick_volume[],
                const long      &volume[],
                const int       &spread[])
  {
   int start = MathMax(prev_calculated - 1, InpLength);
   if(start < InpLength) start = InpLength;

   for(int i = start; i < rates_total; i++)
     {
      OpenBuf[i]  = open[i];
      HighBuf[i]  = high[i];
      LowBuf[i]   = low[i];
      CloseBuf[i] = close[i];

      //--- compute volume z-score
      double vol_mean = 0, vol_std = 0;
      double body_mean = 0, body_std = 0;

      for(int j = 0; j < InpLength; j++)
        {
         int idx = i - j;
         if(idx < 0) break;
         double v = (InpVolumeType == VOLUME_TICK) ? (double)tick_volume[idx] : (double)volume[idx];
         double b = MathAbs(close[idx] - open[idx]);
         vol_mean  += v;
         body_mean += b;
        }
      vol_mean  /= InpLength;
      body_mean /= InpLength;

      for(int j = 0; j < InpLength; j++)
        {
         int idx = i - j;
         if(idx < 0) break;
         double v = (InpVolumeType == VOLUME_TICK) ? (double)tick_volume[idx] : (double)volume[idx];
         double b = MathAbs(close[idx] - open[idx]);
         vol_std  += (v - vol_mean) * (v - vol_mean);
         body_std += (b - body_mean) * (b - body_mean);
        }
      vol_std  = MathSqrt(vol_std / InpLength);
      body_std = MathSqrt(body_std / InpLength);

      double cur_vol = (InpVolumeType == VOLUME_TICK) ? (double)tick_volume[i] : (double)volume[i];
      double cur_body = MathAbs(close[i] - open[i]);

      double z_vol  = (vol_std  > 0) ? (cur_vol  - vol_mean)  / vol_std  : 0;
      double z_body = (body_std > 0) ? (cur_body - body_mean) / body_std : 0;

      //--- composite z based on mode
      double z = 0;
      switch(InpSourceMode)
        {
         case 0: z = z_vol;  break;                        // Volume only
         case 1: z = z_body; break;                        // Body only
         case 2: z = MathMax(z_vol, z_body); break;        // Any
         case 3: z = MathMin(z_vol, z_body); break;        // All
        }

      //--- classify
      bool is_up = close[i] >= open[i];
      bool low_vol = InpShowLowVol && (z_vol <= InpLowVolZ);

      if(low_vol)
        {
         ColorBuf[i] = 6;  // yellow — accumulation / low volume
        }
      else if(z >= InpZ2)
        {
         ColorBuf[i] = is_up ? 2 : 5;  // extreme: green up, red down
        }
      else if(z >= InpZ1)
        {
         ColorBuf[i] = is_up ? 1 : 4;  // large: blue up, purple down
        }
      else
        {
         ColorBuf[i] = is_up ? 0 : 3;  // normal: white up, gray down
        }
     }

   return rates_total;
  }
//+------------------------------------------------------------------+
