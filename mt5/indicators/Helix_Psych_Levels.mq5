//+------------------------------------------------------------------+
//| Helix_Psych_Levels.mq5                                          |
//| Draws psychological round-number levels on the chart.            |
//| 00/50 levels (major) + 20/80 levels (minor).                    |
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

input double InpMajorStep   = 0.0100;   // Major level step (100 pips for 5-digit)
input double InpMinorStep   = 0.0050;   // Minor level step (50 pips)
input int    InpLevelCount  = 10;       // Levels above/below price
input color  InpMajorColor  = clrGold;
input color  InpMinorColor  = clrDimGray;
input color  InpQuarterColor= clrSlateGray;  // 25/75 levels
input ENUM_LINE_STYLE InpMajorStyle = STYLE_SOLID;
input ENUM_LINE_STYLE InpMinorStyle = STYLE_DOT;
input int    InpMajorWidth  = 1;
input bool   InpShowLabels  = true;
input bool   InpShowQuarter = false;     // Show 25/75 levels
input string InpPrefix      = "HX_PSY_";

//+------------------------------------------------------------------+
int OnInit()
  {
   IndicatorSetString(INDICATOR_SHORTNAME, "Helix Psych Levels");
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
   if(rates_total < 1) return 0;

   double price = close[rates_total - 1];
   int digits = (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS);

   // Auto-detect step sizes based on symbol type
   double majorStep = InpMajorStep;
   double minorStep = InpMinorStep;

   // JPY pairs
   if(digits == 3)
     {
      majorStep = 1.000;   // 100 pips for JPY
      minorStep = 0.500;   // 50 pips
     }
   // Gold
   if(StringFind(_Symbol, "XAU") >= 0)
     {
      majorStep = 50.0;
      minorStep = 10.0;
     }
   // Indices
   if(StringFind(_Symbol, "US30") >= 0 || StringFind(_Symbol, "USTEC") >= 0)
     {
      majorStep = 500.0;
      minorStep = 100.0;
     }

   // Round price down to nearest major
   double baseLevel = MathFloor(price / majorStep) * majorStep;

   // Draw levels
   ObjectsDeleteAll(0, InpPrefix);

   for(int i = -InpLevelCount; i <= InpLevelCount; i++)
     {
      // Major level (00)
      double level = baseLevel + i * majorStep;
      string nm = InpPrefix + "M_" + IntegerToString(i);
      DrawLevel(nm, level, InpMajorColor, InpMajorStyle, InpMajorWidth);
      if(InpShowLabels)
         LabelLevel(InpPrefix + "ML_" + IntegerToString(i), level, digits, InpMajorColor);

      // Minor level (50)
      double minor = level + minorStep;
      string nmm = InpPrefix + "m_" + IntegerToString(i);
      DrawLevel(nmm, minor, InpMinorColor, InpMinorStyle, 1);
      if(InpShowLabels)
         LabelLevel(InpPrefix + "mL_" + IntegerToString(i), minor, digits, InpMinorColor);

      // Quarter levels (25/75)
      if(InpShowQuarter)
        {
         double q1 = level + minorStep / 2.0;
         double q3 = level + minorStep * 1.5;
         DrawLevel(InpPrefix + "q1_" + IntegerToString(i), q1, InpQuarterColor, STYLE_DOT, 1);
         DrawLevel(InpPrefix + "q3_" + IntegerToString(i), q3, InpQuarterColor, STYLE_DOT, 1);
        }
     }

   ChartRedraw();
   return rates_total;
  }

//+------------------------------------------------------------------+
void DrawLevel(const string name, double price, color clr,
               ENUM_LINE_STYLE style, int width)
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
  }

void LabelLevel(const string name, double price, int digits, color clr)
  {
   datetime t = (datetime)SeriesInfoInteger(_Symbol, _Period, SERIES_LASTBAR_DATE);
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_TEXT, 0, t, price);
   ObjectSetInteger(0, name, OBJPROP_TIME, 0, t);
   ObjectSetDouble(0, name, OBJPROP_PRICE, 0, price);
   ObjectSetString(0, name, OBJPROP_TEXT, DoubleToString(price, digits));
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, 7);
   ObjectSetInteger(0, name, OBJPROP_ANCHOR, ANCHOR_LEFT);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
  }
//+------------------------------------------------------------------+
