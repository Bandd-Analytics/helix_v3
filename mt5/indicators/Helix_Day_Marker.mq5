//+------------------------------------------------------------------+
//| Helix_Day_Marker.mq5                                            |
//| Draws day separators with day-of-week labels.                    |
//| Color-codes days: Mon=green, Tue-Wed=yellow (reversal zone),     |
//| Thu-Fri=orange (late week).                                      |
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

input color  InpMonColor    = clrLime;       // Monday (early week)
input color  InpTueWedColor = clrYellow;     // Tue-Wed (mid-week reversal)
input color  InpThuFriColor = clrOrange;     // Thu-Fri (late week)
input color  InpSunColor    = clrGray;       // Sunday
input ENUM_LINE_STYLE InpStyle = STYLE_DOT;
input int    InpWidth       = 1;
input bool   InpShowLabels  = true;
input int    InpMaxDays     = 30;            // Max days to draw
input string InpPrefix      = "HX_DAY_";

string DayNames[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
string MMMPhase[] = {"", "Early Week", "Mid-Week Reversal", "Mid-Week Reversal", "Late Week", "Late Week", ""};

//+------------------------------------------------------------------+
int OnInit()
  {
   IndicatorSetString(INDICATOR_SHORTNAME, "Helix Day Marker");
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
   if(rates_total < 2) return 0;

   int count = 0;
   MqlDateTime prev_dt, curr_dt;

   for(int i = rates_total - 1; i >= 1 && count < InpMaxDays; i--)
     {
      TimeToStruct(time[i], curr_dt);
      TimeToStruct(time[i - 1], prev_dt);

      // Day change
      if(curr_dt.day != prev_dt.day || curr_dt.mon != prev_dt.mon)
        {
         count++;
         int dow = curr_dt.day_of_week;

         color clr;
         if(dow == 0)      clr = InpSunColor;
         else if(dow == 1) clr = InpMonColor;
         else if(dow <= 3) clr = InpTueWedColor;
         else              clr = InpThuFriColor;

         // Vertical separator
         string nm = InpPrefix + "V_" + IntegerToString((long)time[i]);
         if(ObjectFind(0, nm) < 0)
            ObjectCreate(0, nm, OBJ_VLINE, 0, time[i], 0);
         ObjectSetInteger(0, nm, OBJPROP_TIME, 0, time[i]);
         ObjectSetInteger(0, nm, OBJPROP_COLOR, clr);
         ObjectSetInteger(0, nm, OBJPROP_STYLE, InpStyle);
         ObjectSetInteger(0, nm, OBJPROP_WIDTH, InpWidth);
         ObjectSetInteger(0, nm, OBJPROP_BACK, true);
         ObjectSetInteger(0, nm, OBJPROP_HIDDEN, true);
         ObjectSetInteger(0, nm, OBJPROP_SELECTABLE, false);

         // Day label
         if(InpShowLabels)
           {
            string label = DayNames[dow];
            if(dow >= 1 && dow <= 5)
               label += " (" + MMMPhase[dow] + ")";

            string nmL = InpPrefix + "L_" + IntegerToString((long)time[i]);
            if(ObjectFind(0, nmL) < 0)
               ObjectCreate(0, nmL, OBJ_TEXT, 0, time[i], high[i]);
            ObjectSetInteger(0, nmL, OBJPROP_TIME, 0, time[i]);
            ObjectSetDouble(0, nmL, OBJPROP_PRICE, 0, high[i]);
            ObjectSetString(0, nmL, OBJPROP_TEXT, label);
            ObjectSetInteger(0, nmL, OBJPROP_COLOR, clr);
            ObjectSetInteger(0, nmL, OBJPROP_FONTSIZE, 8);
            ObjectSetInteger(0, nmL, OBJPROP_ANCHOR, ANCHOR_LEFT_LOWER);
            ObjectSetInteger(0, nmL, OBJPROP_HIDDEN, true);
            ObjectSetInteger(0, nmL, OBJPROP_SELECTABLE, false);
           }
        }
     }

   return rates_total;
  }
//+------------------------------------------------------------------+
