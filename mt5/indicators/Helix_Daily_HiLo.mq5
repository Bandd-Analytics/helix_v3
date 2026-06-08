//+------------------------------------------------------------------+
//| Helix_Daily_HiLo.mq5                                            |
//| Previous day HOD/LOD with N-day snake history.                   |
//| Ported from helix_v3/core/tdi.py compute_daily_hilo()            |
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

input int    InpDaysBack    = 14;       // Days of history to show
input color  InpHighColor   = clrDodgerBlue;
input color  InpLowColor    = clrTomato;
input color  InpPHODColor   = clrAqua;   // Previous HOD (most important)
input color  InpPLODColor   = clrOrange;  // Previous LOD
input int    InpLineWidth   = 1;
input ENUM_LINE_STYLE InpSnakeStyle = STYLE_DOT;
input ENUM_LINE_STYLE InpPrevStyle  = STYLE_DASH;
input string InpPrefix      = "HX_HILO_";

//+------------------------------------------------------------------+
int OnInit()
  {
   IndicatorSetString(INDICATOR_SHORTNAME, "Helix Daily HiLo");
   return INIT_SUCCEEDED;
  }
void OnDeinit(const int reason) { ObjectsDeleteAll(0, InpPrefix); ChartRedraw(); }

//+------------------------------------------------------------------+
int OnCalculate(const int rates_total, const int prev_calculated,
                const datetime &time[], const double &open[],
                const double &high[], const double &low[],
                const double &close[], const long &tick_volume[],
                const long &volume[], const int &spread[])
  {
   MqlRates d[];
   ArraySetAsSeries(d, true);
   int copied = CopyRates(_Symbol, PERIOD_D1, 0, InpDaysBack + 2, d);
   if(copied < 3) return rates_total;

   // PHOD / PLOD (yesterday)
   double phod = d[1].high;
   double plod = d[1].low;

   // Draw PHOD/PLOD as prominent horizontal lines
   datetime now = time[rates_total - 1];
   datetime dayStart = time[rates_total - 1] - PeriodSeconds(PERIOD_D1);

   string nmPHOD = InpPrefix + "PHOD";
   string nmPLOD = InpPrefix + "PLOD";

   DrawHLine(nmPHOD, phod, InpPHODColor, InpPrevStyle, 2, "PHOD " + DoubleToString(phod, (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS)));
   DrawHLine(nmPLOD, plod, InpPLODColor, InpPrevStyle, 2, "PLOD " + DoubleToString(plod, (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS)));

   // Snake: N-day highs and lows as dotted lines
   for(int i = 2; i < copied && i <= InpDaysBack + 1; i++)
     {
      string nmH = InpPrefix + "H_" + IntegerToString(i);
      string nmL = InpPrefix + "L_" + IntegerToString(i);
      int alpha = 255 - (i * 15);
      if(alpha < 50) alpha = 50;

      DrawHLine(nmH, d[i].high, InpHighColor, InpSnakeStyle, InpLineWidth, "");
      DrawHLine(nmL, d[i].low,  InpLowColor,  InpSnakeStyle, InpLineWidth, "");
     }

   ChartRedraw();
   return rates_total;
  }

//+------------------------------------------------------------------+
void DrawHLine(const string name, double price, color clr,
               ENUM_LINE_STYLE style, int width, const string label)
  {
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_HLINE, 0, 0, price);
   ObjectSetDouble(0, name, OBJPROP_PRICE, price);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_STYLE, style);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, width);
   ObjectSetInteger(0, name, OBJPROP_BACK, true);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
   if(label != "")
      ObjectSetString(0, name, OBJPROP_TEXT, label);
  }
//+------------------------------------------------------------------+
