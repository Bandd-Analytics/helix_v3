//+------------------------------------------------------------------+
//| Helix_AR_NY_LDN_EMA_ADR_Gann.mq5                                  |
//| Port of "AR Box, NY/LDN, EMA, ADR, Gann 2.0" Pine indicator.      |
//| Draws Asian range box + pip label, London/NY opening-range boxes, |
//| Gann 0/0.5/1 levels carried from the prior Asian session,         |
//| EMAs 5/13/50/200/800, weekly separators, and an ADR(14) table.    |
//| Times are expressed in GMT minutes (matches Helix V3 sessions.py).|
//+------------------------------------------------------------------+
#property copyright "Helix V3"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 5
#property indicator_plots   5

#property indicator_label1  "EMA 5"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrYellow
#property indicator_width1  1
#property indicator_label2  "EMA 13"
#property indicator_type2   DRAW_LINE
#property indicator_color2  clrRed
#property indicator_width2  1
#property indicator_label3  "EMA 50"
#property indicator_type3   DRAW_LINE
#property indicator_color3  clrAqua
#property indicator_width3  1
#property indicator_label4  "EMA 200"
#property indicator_type4   DRAW_LINE
#property indicator_color4  clrWhite
#property indicator_width4  1
#property indicator_label5  "EMA 800"
#property indicator_type5   DRAW_LINE
#property indicator_color5  clrNavy
#property indicator_width5  1

//--- inputs: sessions (all in GMT minutes-from-midnight)
input group "Sessions (GMT minutes from midnight)"
input int InpAsiaStart    = 30;    // Asia start (00:30 GMT)
input int InpAsiaEnd      = 450;   // Asia end   (07:30 GMT)
input int InpLondonStart  = 450;   // London open (07:30 GMT)
input int InpLondonBoxLen = 75;    // London box length, minutes
input int InpNYStart      = 810;   // NY open    (13:30 GMT)
input int InpNYBoxLen     = 75;    // NY box length, minutes
input int InpAdrLength    = 14;    // ADR lookback (daily SMA of H-L)
input int InpAsiaAvgWin   = 20;    // Rolling Asian-range average window

input group "Display toggles"
input bool InpShowAsiaBoxes    = true;
input bool InpShowAsiaPips     = true;
input bool InpShowLondonBox    = true;
input bool InpShowNYBox        = true;
input bool InpShowGann         = true;
input bool InpShowAdrTable     = true;
input bool InpShowWeeklySep    = true;
input bool InpShowEMA5         = true;
input bool InpShowEMA13        = true;
input bool InpShowEMA50        = true;
input bool InpShowEMA200       = true;
input bool InpShowEMA800       = true;

input group "Style"
input color InpAsiaColor   = clrAqua;
input color InpLondonColor = clrDodgerBlue;
input color InpNYColor     = clrTomato;
input color InpGannColor   = clrLightGray;
input color InpWeekColor   = clrOrange;
input int   InpBoxAlpha    = 50;          // 0..255 transparency (lower = lighter)
input string InpObjPrefix  = "HX_";       // chart-object name prefix

//--- EMA buffers
double EMA5Buf[], EMA13Buf[], EMA50Buf[], EMA200Buf[], EMA800Buf[];
int    hEMA5 = INVALID_HANDLE, hEMA13 = INVALID_HANDLE, hEMA50 = INVALID_HANDLE;
int    hEMA200 = INVALID_HANDLE, hEMA800 = INVALID_HANDLE;

//--- rolling Asian-pip ring for the avg
double AsiaPipRing[];
int    AsiaPipCount = 0;

//--- bookkeeping
datetime LastAsiaStartTime = 0;
datetime LastLondonBoxTime = 0;
datetime LastNYBoxTime     = 0;
datetime LastWeekSepTime   = 0;
double   PipSize           = 0.0;

//+------------------------------------------------------------------+
int OnInit()
  {
   SetIndexBuffer(0, EMA5Buf,   INDICATOR_DATA);
   SetIndexBuffer(1, EMA13Buf,  INDICATOR_DATA);
   SetIndexBuffer(2, EMA50Buf,  INDICATOR_DATA);
   SetIndexBuffer(3, EMA200Buf, INDICATOR_DATA);
   SetIndexBuffer(4, EMA800Buf, INDICATOR_DATA);

   PlotIndexSetDouble(0, PLOT_EMPTY_VALUE, EMPTY_VALUE);
   PlotIndexSetDouble(1, PLOT_EMPTY_VALUE, EMPTY_VALUE);
   PlotIndexSetDouble(2, PLOT_EMPTY_VALUE, EMPTY_VALUE);
   PlotIndexSetDouble(3, PLOT_EMPTY_VALUE, EMPTY_VALUE);
   PlotIndexSetDouble(4, PLOT_EMPTY_VALUE, EMPTY_VALUE);

   hEMA5   = iMA(_Symbol, _Period, 5,   0, MODE_EMA, PRICE_CLOSE);
   hEMA13  = iMA(_Symbol, _Period, 13,  0, MODE_EMA, PRICE_CLOSE);
   hEMA50  = iMA(_Symbol, _Period, 50,  0, MODE_EMA, PRICE_CLOSE);
   hEMA200 = iMA(_Symbol, _Period, 200, 0, MODE_EMA, PRICE_CLOSE);
   hEMA800 = iMA(_Symbol, _Period, 800, 0, MODE_EMA, PRICE_CLOSE);

   PipSize = PipValue();
   ArrayResize(AsiaPipRing, InpAsiaAvgWin);
   ArrayInitialize(AsiaPipRing, 0.0);
   AsiaPipCount = 0;

   IndicatorSetString(INDICATOR_SHORTNAME, "Helix AR/LDN/NY/Gann/EMA/ADR");
   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   if(hEMA5   != INVALID_HANDLE) IndicatorRelease(hEMA5);
   if(hEMA13  != INVALID_HANDLE) IndicatorRelease(hEMA13);
   if(hEMA50  != INVALID_HANDLE) IndicatorRelease(hEMA50);
   if(hEMA200 != INVALID_HANDLE) IndicatorRelease(hEMA200);
   if(hEMA800 != INVALID_HANDLE) IndicatorRelease(hEMA800);

   // Remove all our chart objects on detach (clean uninstall).
   ObjectsDeleteAll(0, InpObjPrefix);
   ChartRedraw();
  }

//+------------------------------------------------------------------+
double PipValue()
  {
   // 5/3-digit forex: 1 pip = 10 points. 2/4-digit: 1 pip = 1 point. Metals: tick size.
   int digits = (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS);
   double point = SymbolInfoDouble(_Symbol, SYMBOL_POINT);
   if(digits == 3 || digits == 5)
      return point * 10.0;
   return point;
  }

//+------------------------------------------------------------------+
int MinuteOfDayGMT(const datetime t)
  {
   MqlDateTime dt;
   TimeToStruct(t, dt);     // server time
   // Convert to GMT: server_time - (TimeCurrent() - TimeGMT())
   datetime gmt = t - (TimeCurrent() - TimeGMT());
   TimeToStruct(gmt, dt);
   return dt.hour * 60 + dt.min;
  }

//+------------------------------------------------------------------+
datetime GmtDateOfBar(const datetime t)
  {
   datetime gmt = t - (TimeCurrent() - TimeGMT());
   MqlDateTime dt;
   TimeToStruct(gmt, dt);
   dt.hour = 0; dt.min = 0; dt.sec = 0;
   return StructToTime(dt);
  }

//+------------------------------------------------------------------+
string MakeName(const string tag, const datetime when)
  {
   return InpObjPrefix + tag + "_" + IntegerToString((long)when);
  }

//+------------------------------------------------------------------+
void DrawRect(const string name, datetime t1, double p1, datetime t2, double p2,
              color clr, int alpha)
  {
   // ARGB stored via ObjectSetInteger; OBJPROP_COLOR uses RGB.
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_RECTANGLE, 0, t1, p1, t2, p2);
   ObjectSetInteger(0, name, OBJPROP_TIME, 0, t1);
   ObjectSetDouble (0, name, OBJPROP_PRICE, 0, p1);
   ObjectSetInteger(0, name, OBJPROP_TIME, 1, t2);
   ObjectSetDouble (0, name, OBJPROP_PRICE, 1, p2);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_BACK, true);
   ObjectSetInteger(0, name, OBJPROP_FILL, true);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 1);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
  }

//+------------------------------------------------------------------+
void DrawTrend(const string name, datetime t1, double p1, datetime t2, double p2,
               color clr, ENUM_LINE_STYLE style, int width)
  {
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_TREND, 0, t1, p1, t2, p2);
   ObjectSetInteger(0, name, OBJPROP_TIME, 0, t1);
   ObjectSetDouble (0, name, OBJPROP_PRICE, 0, p1);
   ObjectSetInteger(0, name, OBJPROP_TIME, 1, t2);
   ObjectSetDouble (0, name, OBJPROP_PRICE, 1, p2);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_STYLE, style);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, width);
   ObjectSetInteger(0, name, OBJPROP_RAY_RIGHT, false);
   ObjectSetInteger(0, name, OBJPROP_RAY_LEFT, false);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
  }

//+------------------------------------------------------------------+
void DrawText(const string name, datetime t, double p, const string txt,
              color clr, int size)
  {
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_TEXT, 0, t, p);
   ObjectSetInteger(0, name, OBJPROP_TIME, 0, t);
   ObjectSetDouble (0, name, OBJPROP_PRICE, 0, p);
   ObjectSetString (0, name, OBJPROP_TEXT, txt);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, size);
   ObjectSetInteger(0, name, OBJPROP_ANCHOR, ANCHOR_LEFT);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
  }

//+------------------------------------------------------------------+
void DrawHudLabel(const string name, int xOffset, int yOffset, const string txt,
                  color clr, int size)
  {
   if(ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_CORNER,   CORNER_RIGHT_UPPER);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE, xOffset);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE, yOffset);
   ObjectSetString (0, name, OBJPROP_TEXT, txt);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, size);
   ObjectSetInteger(0, name, OBJPROP_ANCHOR, ANCHOR_RIGHT_UPPER);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
  }

//+------------------------------------------------------------------+
double ADR(const int length)
  {
   // 14-day SMA of (High - Low) on the daily timeframe of the symbol.
   MqlRates d[];
   ArraySetAsSeries(d, true);
   int copied = CopyRates(_Symbol, PERIOD_D1, 0, length + 1, d);
   if(copied <= 1) return 0.0;
   double sum = 0.0;
   int n = 0;
   // d[0] is the still-forming day; start at d[1].
   for(int i = 1; i <= length && i < copied; i++)
     {
      sum += (d[i].high - d[i].low);
      n++;
     }
   return (n > 0) ? sum / n : 0.0;
  }

//+------------------------------------------------------------------+
void UpdateAsiaRing(const double pips)
  {
   int slot = AsiaPipCount % InpAsiaAvgWin;
   AsiaPipRing[slot] = pips;
   AsiaPipCount++;
  }

double AsiaAvgPips()
  {
   if(AsiaPipCount == 0) return 0.0;
   int n = MathMin(AsiaPipCount, InpAsiaAvgWin);
   double sum = 0.0;
   for(int i = 0; i < n; i++) sum += AsiaPipRing[i];
   return sum / n;
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
   //--- EMAs into buffers
   int to_copy = rates_total - prev_calculated;
   if(prev_calculated > 0) to_copy++;
   if(to_copy > rates_total) to_copy = rates_total;
   if(to_copy <= 0) to_copy = rates_total;

   FillEma(hEMA5,   EMA5Buf,   rates_total, prev_calculated, InpShowEMA5);
   FillEma(hEMA13,  EMA13Buf,  rates_total, prev_calculated, InpShowEMA13);
   FillEma(hEMA50,  EMA50Buf,  rates_total, prev_calculated, InpShowEMA50);
   FillEma(hEMA200, EMA200Buf, rates_total, prev_calculated, InpShowEMA200);
   FillEma(hEMA800, EMA800Buf, rates_total, prev_calculated, InpShowEMA800);

   //--- session overlays: incremental scan from prev_calculated forward
   int start = MathMax(prev_calculated - 1, 1);
   for(int i = start; i < rates_total; i++)
     {
      int   m_now  = MinuteOfDayGMT(time[i]);
      int   m_prev = MinuteOfDayGMT(time[i - 1]);
      datetime day = GmtDateOfBar(time[i]);

      //--- Asia start
      bool asiaStartNow = (m_now >= InpAsiaStart && m_now < InpAsiaEnd) &&
                          !(m_prev >= InpAsiaStart && m_prev < InpAsiaEnd);
      if(asiaStartNow && InpShowAsiaBoxes)
        {
         string nm = MakeName("ASIA_BOX", day);
         DrawRect(nm, time[i], high[i], time[i], low[i], InpAsiaColor, InpBoxAlpha);
         LastAsiaStartTime = day;
        }

      //--- update active Asia box (extend right edge, expand H/L)
      if(InpShowAsiaBoxes && (m_now >= InpAsiaStart && m_now < InpAsiaEnd))
        {
         string nm = MakeName("ASIA_BOX", day);
         if(ObjectFind(0, nm) >= 0)
           {
            datetime t1 = (datetime)ObjectGetInteger(0, nm, OBJPROP_TIME, 0);
            double   p1 = ObjectGetDouble (0, nm, OBJPROP_PRICE, 0);
            double   p2 = ObjectGetDouble (0, nm, OBJPROP_PRICE, 1);
            double   hi = MathMax(p1, high[i]);
            double   lo = MathMin(p2, low[i]);
            DrawRect(nm, t1, hi, time[i], lo, InpAsiaColor, InpBoxAlpha);
           }
        }

      //--- Asia end -> finalize: pip label, ring update, Gann freeze for the just-closed day
      bool asiaEndNow = !(m_now >= InpAsiaStart && m_now < InpAsiaEnd) &&
                          (m_prev >= InpAsiaStart && m_prev < InpAsiaEnd);
      if(asiaEndNow)
        {
         string nm = MakeName("ASIA_BOX", day);
         if(ObjectFind(0, nm) >= 0)
           {
            double hi = ObjectGetDouble(0, nm, OBJPROP_PRICE, 0);
            double lo = ObjectGetDouble(0, nm, OBJPROP_PRICE, 1);
            double pips = (hi - lo) / PipSize;
            UpdateAsiaRing(pips);
            if(InpShowAsiaPips)
              {
               datetime t1 = (datetime)ObjectGetInteger(0, nm, OBJPROP_TIME, 0);
               datetime midT = t1 + (time[i] - t1) / 2;
               DrawText(MakeName("ASIA_PIPS", day), midT, lo,
                        StringFormat("Asia: %.1f pips", pips),
                        clrWhite, 8);
              }
            if(InpShowGann)
              {
               double mid = (hi + lo) / 2.0;
               datetime tStart = time[i];
               datetime tEnd   = time[i] + PeriodSeconds(PERIOD_D1); // ray forward 1 day; next Asia start will overwrite
               DrawTrend(MakeName("GANN_LOW",  day), tStart, lo,  tEnd, lo,  InpGannColor, STYLE_DASH, 1);
               DrawTrend(MakeName("GANN_MID",  day), tStart, mid, tEnd, mid, InpGannColor, STYLE_DASH, 1);
               DrawTrend(MakeName("GANN_HIGH", day), tStart, hi,  tEnd, hi,  InpGannColor, STYLE_DASH, 1);
               DrawText(MakeName("GANN_LBL0",  day), tStart, lo,  "0",   InpGannColor, 7);
               DrawText(MakeName("GANN_LBL05", day), tStart, mid, "0.5", InpGannColor, 7);
               DrawText(MakeName("GANN_LBL1",  day), tStart, hi,  "1",   InpGannColor, 7);
              }
           }
        }

      //--- London box (07:30-08:45)
      if(InpShowLondonBox)
        {
         int boxEnd = InpLondonStart + InpLondonBoxLen;
         bool inBox  = (m_now >= InpLondonStart && m_now < boxEnd);
         bool wasIn  = (m_prev >= InpLondonStart && m_prev < boxEnd);
         string nm = MakeName("LDN_BOX", day);
         if(inBox && !wasIn)
            DrawRect(nm, time[i], high[i], time[i], low[i], InpLondonColor, InpBoxAlpha);
         if(inBox && ObjectFind(0, nm) >= 0)
           {
            datetime t1 = (datetime)ObjectGetInteger(0, nm, OBJPROP_TIME, 0);
            double   p1 = ObjectGetDouble (0, nm, OBJPROP_PRICE, 0);
            double   p2 = ObjectGetDouble (0, nm, OBJPROP_PRICE, 1);
            double   hi = MathMax(p1, high[i]);
            double   lo = MathMin(p2, low[i]);
            DrawRect(nm, t1, hi, time[i], lo, InpLondonColor, InpBoxAlpha);
           }
        }

      //--- NY box (13:30-14:45)
      if(InpShowNYBox)
        {
         int boxEnd = InpNYStart + InpNYBoxLen;
         bool inBox  = (m_now >= InpNYStart && m_now < boxEnd);
         bool wasIn  = (m_prev >= InpNYStart && m_prev < boxEnd);
         string nm = MakeName("NY_BOX", day);
         if(inBox && !wasIn)
            DrawRect(nm, time[i], high[i], time[i], low[i], InpNYColor, InpBoxAlpha);
         if(inBox && ObjectFind(0, nm) >= 0)
           {
            datetime t1 = (datetime)ObjectGetInteger(0, nm, OBJPROP_TIME, 0);
            double   p1 = ObjectGetDouble (0, nm, OBJPROP_PRICE, 0);
            double   p2 = ObjectGetDouble (0, nm, OBJPROP_PRICE, 1);
            double   hi = MathMax(p1, high[i]);
            double   lo = MathMin(p2, low[i]);
            DrawRect(nm, t1, hi, time[i], lo, InpNYColor, InpBoxAlpha);
           }
        }

      //--- Weekly separator (Monday open)
      if(InpShowWeeklySep)
        {
         MqlDateTime dt;
         TimeToStruct(time[i], dt);
         MqlDateTime dtPrev;
         TimeToStruct(time[i - 1], dtPrev);
         if(dt.day_of_week == 1 && dtPrev.day_of_week != 1)
           {
            string nm = MakeName("WK_SEP", time[i]);
            if(ObjectFind(0, nm) < 0)
               ObjectCreate(0, nm, OBJ_VLINE, 0, time[i], 0);
            ObjectSetInteger(0, nm, OBJPROP_TIME,  0, time[i]);
            ObjectSetInteger(0, nm, OBJPROP_COLOR, InpWeekColor);
            ObjectSetInteger(0, nm, OBJPROP_STYLE, STYLE_SOLID);
            ObjectSetInteger(0, nm, OBJPROP_WIDTH, 1);
            ObjectSetInteger(0, nm, OBJPROP_BACK, true);
            ObjectSetInteger(0, nm, OBJPROP_SELECTABLE, false);
            ObjectSetInteger(0, nm, OBJPROP_HIDDEN, true);
           }
        }
     }

   //--- ADR table (top-right HUD)
   if(InpShowAdrTable)
     {
      double adr = ADR(InpAdrLength);
      double adrPips = (PipSize > 0.0) ? adr / PipSize : 0.0;

      // Today's range: scan back to last Monday-style daily open
      datetime now = time[rates_total - 1];
      MqlDateTime ndt; TimeToStruct(now, ndt);
      double tdHi = -DBL_MAX, tdLo = DBL_MAX;
      for(int j = rates_total - 1; j >= 0; j--)
        {
         MqlDateTime jdt; TimeToStruct(time[j], jdt);
         if(jdt.day != ndt.day || jdt.mon != ndt.mon || jdt.year != ndt.year) break;
         if(high[j] > tdHi) tdHi = high[j];
         if(low[j]  < tdLo) tdLo = low[j];
        }
      double todayPips = (tdHi > -DBL_MAX) ? (tdHi - tdLo) / PipSize : 0.0;
      double usedPct   = (adrPips > 0.0) ? (todayPips / adrPips) * 100.0 : 0.0;
      double avgAsia   = AsiaAvgPips();

      DrawHudLabel(InpObjPrefix + "HUD_ADR",   10, 20,  StringFormat("ADR:     %.1f p", adrPips),       clrWhite, 9);
      DrawHudLabel(InpObjPrefix + "HUD_ADR3",  10, 36,  StringFormat("3xADR:   %.1f p", adrPips * 3.0), clrWhite, 9);
      DrawHudLabel(InpObjPrefix + "HUD_TDR",   10, 52,  StringFormat("Today:   %.1f p", todayPips),     clrWhite, 9);
      DrawHudLabel(InpObjPrefix + "HUD_USED",  10, 68,  StringFormat("ADR%%:    %.1f%%", usedPct),      clrWhite, 9);
      DrawHudLabel(InpObjPrefix + "HUD_AVGA",  10, 84,  StringFormat("AvgAsia: %.1f p", avgAsia),       clrWhite, 9);
     }

   return rates_total;
  }

//+------------------------------------------------------------------+
void FillEma(const int handle, double &buf[], const int total, const int prev, const bool show)
  {
   if(!show || handle == INVALID_HANDLE)
     {
      for(int i = MathMax(prev - 1, 0); i < total; i++) buf[i] = EMPTY_VALUE;
      return;
     }
   int copied = CopyBuffer(handle, 0, 0, total, buf);
   if(copied <= 0)
      for(int i = MathMax(prev - 1, 0); i < total; i++) buf[i] = EMPTY_VALUE;
  }
//+------------------------------------------------------------------+
