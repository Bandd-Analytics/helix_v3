//+------------------------------------------------------------------+
//| Helix_ADR_Marker.mq5                                            |
//| ADR marker using Wilder ATR(14) — matches V2 SM_ADR_Marker.     |
//| Shows expected daily range boundaries from today's open.          |
//| Ported from helix_v3/core/tdi.py compute_adr_marker()            |
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

input int    InpAdrPeriod   = 14;        // ATR lookback
input color  InpHighColor   = clrLime;
input color  InpMidColor    = clrYellow;
input color  InpLowColor    = clrRed;
input ENUM_LINE_STYLE InpStyle = STYLE_DASHDOTDOT;
input int    InpWidth       = 1;
input bool   InpShowHUD     = true;      // Show ADR stats in corner
input string InpPrefix      = "HX_ADR_";

double PipSize;

//+------------------------------------------------------------------+
int OnInit()
  {
   PipSize = PipVal();
   IndicatorSetString(INDICATOR_SHORTNAME, "Helix ADR Marker");
   return INIT_SUCCEEDED;
  }
void OnDeinit(const int reason) { ObjectsDeleteAll(0, InpPrefix); ChartRedraw(); }

double PipVal()
  {
   int digits = (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS);
   double point = SymbolInfoDouble(_Symbol, SYMBOL_POINT);
   return (digits == 3 || digits == 5) ? point * 10.0 : point;
  }

//+------------------------------------------------------------------+
int OnCalculate(const int rates_total, const int prev_calculated,
                const datetime &time[], const double &open[],
                const double &high[], const double &low[],
                const double &close[], const long &tick_volume[],
                const long &volume[], const int &spread[])
  {
   MqlRates d[];
   ArraySetAsSeries(d, true);
   int copied = CopyRates(_Symbol, PERIOD_D1, 0, InpAdrPeriod + 2, d);
   if(copied < InpAdrPeriod + 1) return rates_total;

   // Wilder ATR(14) — using EMA with alpha=1/period
   double atr = 0;
   // Simple seed
   double sum = 0;
   for(int i = 1; i <= InpAdrPeriod && i < copied; i++)
      sum += d[i].high - d[i].low;
   atr = sum / InpAdrPeriod;

   // Wilder smooth over remaining
   for(int i = InpAdrPeriod + 1; i < copied; i++)
     {
      double tr = d[i].high - d[i].low;
      atr = atr + (tr - atr) / InpAdrPeriod;
     }

   double todayOpen = d[0].open;
   double markerHigh = todayOpen + atr / 2.0;
   double markerMid  = todayOpen;
   double markerLow  = todayOpen - atr / 2.0;
   double adrPips = (PipSize > 0) ? atr / PipSize : 0;

   // Today's actual range
   double todayRange = (d[0].high - d[0].low);
   double todayPips = (PipSize > 0) ? todayRange / PipSize : 0;
   double usedPct = (atr > 0) ? (todayRange / atr) * 100.0 : 0;

   // Draw lines
   DrawHLine(InpPrefix + "HIGH", markerHigh, InpHighColor, InpStyle, InpWidth, "ADR High");
   DrawHLine(InpPrefix + "MID",  markerMid,  InpMidColor,  InpStyle, InpWidth, "ADR Mid (Open)");
   DrawHLine(InpPrefix + "LOW",  markerLow,  InpLowColor,  InpStyle, InpWidth, "ADR Low");

   // HUD
   if(InpShowHUD)
     {
      DrawLabel(InpPrefix + "HUD1", 10, 120, StringFormat("ADR(14): %.0f p", adrPips), clrWhite, 9);
      color usedClr = clrWhite;
      if(usedPct > 100) usedClr = clrRed;
      else if(usedPct > 80) usedClr = clrOrange;
      DrawLabel(InpPrefix + "HUD2", 10, 136, StringFormat("Today:   %.0f p (%.0f%%)", todayPips, usedPct), usedClr, 9);
      DrawLabel(InpPrefix + "HUD3", 10, 152, StringFormat("3xADR:   %.0f p", adrPips * 3.0), clrGray, 9);
     }

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
   if(label != "") ObjectSetString(0, name, OBJPROP_TEXT, label);
  }

void DrawLabel(const string name, int x, int y, const string txt, color clr, int sz)
  {
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_CORNER, CORNER_RIGHT_UPPER);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE, x);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE, y);
   ObjectSetString(0, name, OBJPROP_TEXT, txt);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, sz);
   ObjectSetInteger(0, name, OBJPROP_ANCHOR, ANCHOR_RIGHT_UPPER);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
  }
//+------------------------------------------------------------------+
