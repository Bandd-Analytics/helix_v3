"""Send updated flashcards with stop hunt callouts + landscape charts to Telegram."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from dotenv import load_dotenv
load_dotenv(override=True)
from helix_v3.notifications.telegram import TelegramNotifier

tg = TelegramNotifier()
if not tg.enabled:
    print("Telegram not configured")
    sys.exit(1)

# ---- HEADER ----
tg._send_text(
    "HELIX V3 FLASHCARDS (Updated)\n"
    "2026-06-05 16:20 EAT | Friday | NYC Overlap\n"
    "Bal: $776.22 | No open positions\n"
    "\n"
    "NEW: Landscape charts, visible labels,\n"
    "stop hunt zones marked on chart.\n"
    "13 pairs. Sorted by confluence.\n"
)
print("Header sent")

# Chart timestamp for file paths
ts = "20260605_162042"

# ---- FLASHCARD 1: EURCHF ----
tg.send_with_chart(
    "EURCHF BUY | 70/100\n"
    "\n"
    "STOP HUNT: BUY 22p (5 pushes)\n"
    "Hunted below Asian low, reversed up.\n"
    "Hunt CONFIRMED and price rallying.\n"
    "\n"
    "Structure:\n"
    "  Asian: 24p (tight, valid)\n"
    "  W-bottom formed off hunt low\n"
    "  H4+H1 both BUY, LOD locked\n"
    "  Setup: THE 33 | 5 RRT | 6 spikes\n"
    "\n"
    "TDI: RSI=67 (room left) | ADR 71%\n"
    "Weekly SELL (counter) but intraday strong\n"
    "\n"
    "VERDICT: Valid entry on pullback to 0.9180\n"
    "SL below 0.9140 | Risk: 1.0%",
    f"charts/annotated/EURCHF_M15_annotated_{ts}.png",
)
print("1/13 EURCHF sent")

# ---- FLASHCARD 2: GBPCHF ----
tg.send_with_chart(
    "GBPCHF BUY | 70/100\n"
    "\n"
    "STOP HUNT: BUY 10p SOFT (5 pushes)\n"
    "Soft hunt (small breach) but W-bottom\n"
    "confirms direction. Price above Asian H.\n"
    "\n"
    "Structure:\n"
    "  Asian: 35p (valid)\n"
    "  W-bottom + THE 33 setup\n"
    "  H4+H1 both BUY | 6 RRT | 5 spikes\n"
    "\n"
    "TDI: RSI=76 OVERBOUGHT | ADR 84%\n"
    "Weekly SELL + PEAK_HIGH = danger zone\n"
    "\n"
    "VERDICT: LATE - RSI exhausted, ADR near\n"
    "limit. SKIP unless pullback to 1.0600.",
    f"charts/annotated/GBPCHF_M15_annotated_{ts}.png",
)
print("2/13 GBPCHF sent")

ts2 = ts  # same timestamp batch

# ---- FLASHCARD 3: GBPUSD ----
tg.send_with_chart(
    "GBPUSD BUY | 65/100 | TOP PICK MON\n"
    "\n"
    "STOP HUNT: BUY 51p (5 pushes)\n"
    "MASSIVE hunt below Asian low.\n"
    "Price dropped 78p from HOD - hunt\n"
    "played out, now in reversal zone.\n"
    "\n"
    "Structure:\n"
    "  Asian: 16p (very tight!)\n"
    "  W-bottom forming at current price\n"
    "  ONLY weekly-aligned BUY in portfolio\n"
    "  Setup: THE 33 | 5 RRT | 7 spikes\n"
    "\n"
    "TDI: RSI=35 OVERSOLD (bounce zone!)\n"
    "ADR: 104% EXCEEDED - done for today\n"
    "H4 SELL conflicts (short-term pressure)\n"
    "\n"
    "VERDICT: #1 PICK FOR MONDAY\n"
    "Wait for Asian base above 1.3400.\n"
    "DO NOT enter today - ADR spent.",
    f"charts/annotated/GBPUSD_M15_annotated_{ts2}.png",
)
print("3/13 GBPUSD sent")

# ---- FLASHCARD 4: USDJPY ----
tg.send_with_chart(
    "USDJPY BUY | 65/100\n"
    "\n"
    "STOP HUNT: BUY 27p (5 pushes)\n"
    "Clean hunt below Asian low with\n"
    "3+ pushes. W-bottom confirmed.\n"
    "Price rallying - SHARK FIN LONG active.\n"
    "\n"
    "Structure:\n"
    "  Asian: 14p (tightest of all pairs!)\n"
    "  Textbook accumulation -> hunt -> reversal\n"
    "  H4+H1 both BUY | THE 33\n"
    "  6 RRT | 7 spikes\n"
    "\n"
    "TDI: RSI=68 Shark Fin LONG\n"
    "ADR: 56% (MOST room to run)\n"
    "Weekly SELL + PEAK_HIGH (risky)\n"
    "\n"
    "VERDICT: Best if you trade counter-weekly.\n"
    "Entry 160.20 | SL 159.83 (37p)\n"
    "TP1 160.57 | Friday = careful.",
    f"charts/annotated/USDJPY_M15_annotated_{ts2}.png",
)
print("4/13 USDJPY sent")

# ---- FLASHCARD 5: USDCHF ----
ts3 = "20260605_162043"
tg.send_with_chart(
    "USDCHF BUY | 55/100 | MARGINAL\n"
    "\n"
    "STOP HUNT: BUY 21p (5 pushes)\n"
    "Hunt confirmed but price already\n"
    "extended. 8 RRT + 9 spikes = heavy\n"
    "rejection activity at these levels.\n"
    "\n"
    "Structure:\n"
    "  Asian: 28p (valid) | W-bottom\n"
    "  H4 BUY but H1 neutral\n"
    "\n"
    "TDI: RSI=76 OVERBOUGHT\n"
    "ADR: 107% EXCEEDED\n"
    "Weekly SELL + PEAK_HIGH\n"
    "\n"
    "VERDICT: SKIP - ADR blown, RSI maxed,\n"
    "weekly peak. Too many red flags.",
    f"charts/annotated/USDCHF_M15_annotated_{ts3}.png",
)
print("5/13 USDCHF sent")

# ---- FLASHCARD 6: EURJPY ----
tg.send_with_chart(
    "EURJPY BUY | 40/100 | REVERSED\n"
    "\n"
    "STOP HUNT: BUY 38p (5 pushes)\n"
    "Hunt played out in London session.\n"
    "Price rallied 57p then REVERSED hard.\n"
    "Now RSI=33 oversold - hunt gains erased.\n"
    "\n"
    "Structure:\n"
    "  Asian: 26p | W-bottom was valid\n"
    "  Was 70/100 at 12:00 - now 40/100\n"
    "  H4 flipped to NEUTRAL\n"
    "\n"
    "ADR: 67% (33% room if it bounces)\n"
    "Weekly SELL + PEAK_HIGH\n"
    "\n"
    "VERDICT: MONITOR for Monday.\n"
    "If bases in Asian and forms new W-bottom\n"
    "could re-enter. Classic Friday fade.",
    f"charts/annotated/EURJPY_M15_annotated_{ts3}.png",
)
print("6/13 EURJPY sent")

# ---- FLASHCARD 7: GBPJPY ----
tg.send_with_chart(
    "GBPJPY BUY | 40/100 | FADED\n"
    "\n"
    "STOP HUNT: BUY 80p (4 pushes)\n"
    "HUGE 80-pip hunt below Asian low.\n"
    "Rallied hard in London then completely\n"
    "faded in NYC. Classic Friday reversal.\n"
    "\n"
    "Structure:\n"
    "  Asian: 22p | Was THE 33 setup\n"
    "  Was 70/100 at 12:00 - now 40/100\n"
    "  102/112p ADR used = DONE\n"
    "\n"
    "TDI: RSI=40 neutral | No signals\n"
    "Weekly SELL + PEAK_HIGH\n"
    "\n"
    "VERDICT: DONE for the day.\n"
    "The stop hunt gave its move and took\n"
    "it back. No re-entry.",
    f"charts/annotated/GBPJPY_M15_annotated_{ts3}.png",
)
print("7/13 GBPJPY sent")

# ---- FLASHCARD 8: XAUUSD ----
tg.send_with_chart(
    "XAUUSD (GOLD) | 45/100 | DUMPING\n"
    "\n"
    "STOP HUNT: SELL 3817p (!)\n"
    "Massive sell-side hunt. Asian range\n"
    "invalid (4198p - way too wide).\n"
    "No MMM entry structure.\n"
    "\n"
    "Structure:\n"
    "  H4: SELL | H1: SELL | All selling\n"
    "  RSI=34 oversold + bearish divergence\n"
    "  Price 4405, down from HOD 4484\n"
    "  790-pip drop today!\n"
    "\n"
    "TDI: Oversold but no reversal signal\n"
    "Weekly SELL (L3, 7d extended)\n"
    "\n"
    "VERDICT: WATCH for W-bottom formation.\n"
    "If you short gold this is the move,\n"
    "but no valid MMM long entry yet.",
    f"charts/annotated/XAUUSD_M15_annotated_{ts3}.png",
)
print("8/13 XAUUSD sent")

# ---- FLASHCARD 9: AUDUSD ----
ts4 = "20260605_162044"
tg.send_with_chart(
    "AUDUSD BUY | 40/100 | CONFLICTED\n"
    "\n"
    "STOP HUNT: BUY 33p (1 push only)\n"
    "Hunt detected but only 1 push (need 3).\n"
    "Weak hunt confirmation.\n"
    "\n"
    "Structure:\n"
    "  Asian: 32p (valid) | M/W forming\n"
    "  Weekly SELL + H4 SELL = double conflict\n"
    "  RSI=36 oversold + bearish divergence\n"
    "  GUARD: SELL direction BANNED\n"
    "\n"
    "ADR: 74% | Risk: Low tier 1.0%\n"
    "\n"
    "VERDICT: SKIP - Everything conflicted.\n"
    "M/W says BUY, everything else says SELL.\n"
    "Guard has sell banned anyway.",
    f"charts/annotated/AUDUSD_M15_annotated_{ts4}.png",
)
print("9/13 AUDUSD sent")

# ---- FLASHCARD 10: GBPAUD ----
tg.send_with_chart(
    "GBPAUD | 45/100 | NO SIGNAL\n"
    "\n"
    "STOP HUNT: BUY 48p (5 pushes)\n"
    "Hunt confirmed with 5 pushes but\n"
    "Asian range 72p = too wide for valid\n"
    "accumulation. No clean entry.\n"
    "\n"
    "Structure:\n"
    "  H4 BUY but weekly SELL (PEAK_HIGH)\n"
    "  TDI: VB Squeeze + Bearish Divergence\n"
    "  Shark Fin Long but div = conflicting\n"
    "\n"
    "ADR: 32% (room but no setup)\n"
    "\n"
    "VERDICT: WAIT - Wide Asian killed the\n"
    "setup. Need tighter range to trade.",
    f"charts/annotated/GBPAUD_M15_annotated_{ts4}.png",
)
print("10/13 GBPAUD sent")

# ---- FLASHCARD 11: GBPNZD ----
tg.send_with_chart(
    "GBPNZD | 50/100 | FORMING\n"
    "\n"
    "STOP HUNT: BUY 58p (5 pushes)\n"
    "Good hunt with 5 pushes but Asian\n"
    "range 83p = too wide. VB Squeeze\n"
    "building (breakout imminent).\n"
    "\n"
    "Structure:\n"
    "  Weekly BUY (L3) | H4+H1 BUY\n"
    "  MBL Cross Bullish + VB Squeeze\n"
    "  RRT: 8x | THE 33 setup\n"
    "\n"
    "ADR: 36% (most room after USDJPY)\n"
    "\n"
    "VERDICT: MONDAY WATCHLIST #3\n"
    "If Asian tightens below 50p, this\n"
    "becomes a strong weekly-aligned entry.",
    f"charts/annotated/GBPNZD_M15_annotated_{ts4}.png",
)
print("11/13 GBPNZD sent")

# ---- FLASHCARD 12: EURUSD ----
tg.send_with_chart(
    "EURUSD BUY | 45/100 | REJECTED\n"
    "\n"
    "STOP HUNT: BUY 28p (5 pushes)\n"
    "Hunt played out but double timeframe\n"
    "conflict (weekly SELL + H4 SELL).\n"
    "Price dropped hard - RSI=30 deeply\n"
    "oversold.\n"
    "\n"
    "Structure:\n"
    "  Asian: 15p (tight) but conflicts kill it\n"
    "  ADR 103% EXCEEDED\n"
    "  8 RRT + 8 spikes = indecision\n"
    "\n"
    "VERDICT: SKIP - Two higher TFs say SELL\n"
    "while M15 says BUY. No edge here.",
    f"charts/annotated/EURUSD_M15_annotated_{ts4}.png",
)
print("12/13 EURUSD sent")

# ---- FLASHCARD 13: AUDJPY ----
tg.send_with_chart(
    "AUDJPY | 45/100 | DIRECTIONLESS\n"
    "\n"
    "STOP HUNT: BUY 42p (0 pushes!)\n"
    "Hunt zone detected but NO push\n"
    "confirmation. Without pushes the\n"
    "hunt is unconfirmed.\n"
    "\n"
    "Structure:\n"
    "  Asian: 52p (too wide)\n"
    "  H4 NEUTRAL | No direction\n"
    "  TDI: RSI=39, no signals at all\n"
    "\n"
    "ADR: 54% | Weekly SELL (L2)\n"
    "\n"
    "VERDICT: SKIP - No structure, no\n"
    "pushes, wide Asian, no signals. Pass.",
    f"charts/annotated/AUDJPY_M15_annotated_{ts4}.png",
)
print("13/13 AUDJPY sent")

# ---- STOP HUNT SUMMARY ----
tg._send_text(
    "STOP HUNT SUMMARY - 16:20 EAT\n"
    "=" * 35 + "\n"
    "\n"
    "CONFIRMED HUNTS (5+ pushes):\n"
    "  GBPJPY  BUY 80p  4 push  FADED\n"
    "  GBPNZD  BUY 58p  5 push  HOLDING\n"
    "  GBPUSD  BUY 51p  5 push  REVERSING\n"
    "  GBPAUD  BUY 48p  5 push  CHOPPY\n"
    "  EURJPY  BUY 38p  5 push  FADED\n"
    "  AUDUSD  BUY 33p  1 push  WEAK\n"
    "  EURUSD  BUY 28p  5 push  SOLD OFF\n"
    "  USDJPY  BUY 27p  5 push  ACTIVE\n"
    "  EURCHF  BUY 22p  5 push  ACTIVE\n"
    "  USDCHF  BUY 21p  5 push  EXTENDED\n"
    "\n"
    "ALL hunts were BUY-side (below Asian).\n"
    "London hunted lows, NYC fading the moves.\n"
    "Classic Friday pattern.\n"
    "\n"
    "STILL ACTIVE: USDJPY (Shark Fin), EURCHF\n"
    "FADED: GBPJPY, EURJPY, GBPUSD, EURUSD\n"
    "EXTENDED: GBPCHF, USDCHF (ADR blown)\n"
    "\n"
    "Monday watch: GBPUSD, EURJPY, GBPNZD\n"
    "(all oversold with room to bounce)"
)
print("\nStop hunt summary sent")
print("ALL 13 FLASHCARDS + SUMMARY DELIVERED")
