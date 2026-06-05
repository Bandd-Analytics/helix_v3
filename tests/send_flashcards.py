"""Send detailed flashcard analysis per pair to Telegram."""
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
header = (
    "HELIX V3 FLASHCARD SCAN\n"
    "2026-06-05 16:00 EAT | Friday | NYC Overlap\n"
    "Bal: $776.22 | Eq: $776.22 | No open positions\n"
    "Guard: AUDUSD_SELL banned | GBPJPY_SELL cooldown\n"
    "\n"
    "13 pairs scanned. 5 entry-grade. 0 trades open.\n"
    "Flashcards sorted by confluence score.\n"
)
tg._send_text(header)
print("Header sent")

# ---- ENTRY-GRADE FLASHCARDS ----

cards = [
    {
        "symbol": "EURCHF",
        "chart": "charts/annotated/EURCHF_M15_annotated_20260605_155956.png",
        "text": (
            "EURCHF BUY | 70/100 | ENTRY\n"
            "\n"
            "WEEKLY: SELL (Late Week) | L2 | 2d from peak\n"
            "H4: Level 3 BUY (strong intraday momentum)\n"
            "H1: TRUE_TREND BUY | LOD locked 0.91397\n"
            "15M: Asian 24p (valid) | Hunt BUY 22p | 5 push\n"
            "M/W: Yes -> BUY | Setup: THE_33\n"
            "\n"
            "TDI: RSI=67 Sig=58 Base=50 | Overbought\n"
            "ADR: 50/42p (71% but TDR>ADR = extended)\n"
            "Price: 0.91894 | Spread: 0.3p\n"
            "\n"
            "CAUTION: Weekly SELL conflicts\n"
            "EDGE: H4+H1 aligned BUY, W-bottom, tight Asian\n"
            "RISK: Low tier | 1.0% | Trail 10/8p\n"
            "\n"
            "VERDICT: Solid intraday BUY but counter-weekly. "
            "TDI=67 still has room. Best on pullback to 0.9180 "
            "with SL below 0.9140."
        ),
    },
    {
        "symbol": "GBPCHF",
        "chart": "charts/annotated/GBPCHF_M15_annotated_20260605_155956.png",
        "text": (
            "GBPCHF BUY | 70/100 | ENTRY\n"
            "\n"
            "WEEKLY: SELL (Late Week) | PEAK_HIGH | 0d\n"
            "H4: Level 3 BUY\n"
            "H1: TRUE_TREND BUY | LOD locked 1.05788\n"
            "15M: Asian 35p (valid) | Hunt BUY 10p (soft) | 5 push\n"
            "M/W: Yes -> BUY | Setup: THE_33\n"
            "\n"
            "TDI: RSI=76 Sig=68 Base=56 | Overbought\n"
            "ADR: 55/53p used (84%)\n"
            "Price: 1.06311 | Spread: 0.4p\n"
            "\n"
            "CAUTION: Weekly SELL + PEAK_HIGH = reversal zone!\n"
            "TDI RSI=76 very overbought. ADR 84% used.\n"
            "EDGE: H4/H1 both BUY, strong momentum\n"
            "RISK: Medium tier | 0.8% | Trail 22/16p\n"
            "\n"
            "VERDICT: LATE. RSI=76, ADR 84%, weekly peak. "
            "High risk of snap-back. SKIP unless pullback to "
            "1.0600 with TDI reset."
        ),
    },
    {
        "symbol": "GBPUSD",
        "chart": "charts/annotated/GBPUSD_M15_annotated_20260605_155955.png",
        "text": (
            "GBPUSD BUY | 65/100 | ENTRY\n"
            "\n"
            "WEEKLY: BUY (Late Week) | PEAK_LOW | 8d from peak\n"
            "H4: Level 3 SELL (conflict!)\n"
            "H1: TRUE_TREND NEUTRAL\n"
            "15M: Asian 16p (tight!) | Hunt BUY 51p | 5 push\n"
            "M/W: Yes -> BUY | Setup: THE_33\n"
            "\n"
            "TDI: RSI=35 Sig=56 Base=64 | OVERSOLD\n"
            "ADR: 79/76p used (104% - EXCEEDED)\n"
            "Price: 1.34048 | Spread: 0.2p\n"
            "\n"
            "CAUTION: ADR exceeded (104%). H4 SELL conflicts.\n"
            "Dropped 78p from HOD 1.3483 to 1.3405\n"
            "EDGE: ONLY weekly-aligned BUY in portfolio!\n"
            "RSI=35 deeply oversold = bounce zone.\n"
            "RISK: Low tier | 1.0% | Trail 20/15p\n"
            "\n"
            "VERDICT: TOP PICK FOR MONDAY. ADR spent today. "
            "Weekly BUY + oversold = strong bounce candidate. "
            "If holds 1.3400 into Asian, Monday setup likely. "
            "DO NOT enter today."
        ),
    },
    {
        "symbol": "USDJPY",
        "chart": "charts/annotated/USDJPY_M15_annotated_20260605_155956.png",
        "text": (
            "USDJPY BUY | 65/100 | ENTRY\n"
            "\n"
            "WEEKLY: SELL (Late Week) | PEAK_HIGH | 0d\n"
            "H4: Level 3 BUY\n"
            "H1: TRUE_TREND BUY\n"
            "15M: Asian 14p (very tight!) | Hunt BUY 27p | 5 push\n"
            "M/W: Yes -> BUY | Setup: THE_33\n"
            "\n"
            "TDI: RSI=68 Sig=47 Base=46 | SHARK FIN LONG\n"
            "ADR: 39/70p used (56%) - MOST ROOM TO RUN\n"
            "Price: 160.216 | Spread: 0.1p\n"
            "\n"
            "CAUTION: Weekly SELL + PEAK_HIGH = danger\n"
            "EDGE: Shark Fin LONG + 56% ADR (best room)\n"
            "Tight 14p Asian = textbook accumulation\n"
            "RISK: Medium tier | 0.8% | Trail 20/15p\n"
            "\n"
            "VERDICT: Best remaining if you accept counter-weekly. "
            "Shark Fin + room + tight accum. Entry 160.20, "
            "SL below 159.83 (37p). TP1 160.57. "
            "Friday peak = tread carefully."
        ),
    },
    {
        "symbol": "USDCHF",
        "chart": "charts/annotated/USDCHF_M15_annotated_20260605_155956.png",
        "text": (
            "USDCHF BUY | 55/100 | MARGINAL\n"
            "\n"
            "WEEKLY: SELL (Late Week) | PEAK_HIGH | 0d\n"
            "H4: Level 3 BUY | H1: NEUTRAL\n"
            "15M: Asian 28p (valid) | Hunt BUY 21p | 5 push\n"
            "M/W: Yes -> BUY | Setup: THE_33\n"
            "\n"
            "TDI: RSI=76 Sig=56 Base=42 | Overbought\n"
            "ADR: 59/55p used (107% - EXCEEDED)\n"
            "Price: 0.79311 | Spread: 0.0p\n"
            "8 RRTs + 9 spikes = heavy rejection activity\n"
            "\n"
            "VERDICT: SKIP. ADR blown, RSI exhausted, "
            "weekly peak. Too many red flags."
        ),
    },
]

for i, card in enumerate(cards):
    tg.send_with_chart(card["text"], card["chart"])
    print(f"Sent {card['symbol']} flashcard ({i+1}/5)")

# ---- WATCH LIST ----

watch_cards = [
    (
        "GBPNZD | 50/100 | NOT VALID\n"
        "Wkly: BUY (L3, 7d) | H4: L3 BUY | H1: BUY\n"
        "Asian: 83p (TOO WIDE) | VB Squeeze + MBL Cross Bull\n"
        "ADR: 36% used | Room but no valid entry signal.\n"
        "If Asian tightens Monday, could be top pick."
    ),
    (
        "EURUSD | 45/100 | NOT VALID\n"
        "Wkly: SELL (L3) | H4: SELL | RSI=30 oversold\n"
        "ADR: 103% exceeded. Dropped hard today.\n"
        "Double TF conflict (wkly+H4 SELL vs M15 BUY). SKIP."
    ),
    (
        "GBPAUD | 45/100 | NOT VALID\n"
        "Wkly: SELL (PEAK_HIGH) | H4: L3 BUY | Asian 72p wide\n"
        "TDI: VB Squeeze + Bearish Divergence (conflicting!)\n"
        "Shark Fin Long but divergence = risky. WAIT."
    ),
    (
        "AUDJPY | 45/100 | NOT VALID\n"
        "Wkly: SELL (L2, 3d) | H4: NEUTRAL | Asian 52p wide\n"
        "TDI: RSI=39. No signals. Directionless. SKIP."
    ),
    (
        "XAUUSD (GOLD) | 45/100 | NOT VALID\n"
        "Wkly: SELL (L3) | H4: SELL | H1: SELL\n"
        "RSI=34 oversold + Bearish Divergence. Dumping.\n"
        "Price 4405, down from HOD 4484 (790p drop!)\n"
        "No valid MMM entry. MONITOR for W-bottom formation."
    ),
    (
        "AUDUSD | 40/100 | NOT VALID\n"
        "Wkly: SELL | H4: SELL | RSI=36 + bearish divergence\n"
        "GUARD: SELL banned. Everything conflicted. SKIP."
    ),
    (
        "GBPJPY | 40/100 | NOT VALID\n"
        "Wkly: SELL (PEAK_HIGH) | H4: NEUTRAL | RSI=40\n"
        "Was 70/100 earlier. Gave back the move.\n"
        "102/112p ADR used. DONE for the day."
    ),
    (
        "EURJPY | 40/100 | NOT VALID\n"
        "Wkly: SELL (PEAK_HIGH) | H4: NEUTRAL | RSI=33 oversold\n"
        "Was 70/100 earlier. Completely reversed.\n"
        "57/85p ADR (67%). Could bounce Monday if bases. MONITOR."
    ),
]

watch_text = "WATCH LIST FLASHCARDS\n" + "=" * 30 + "\n\n"
watch_text += "\n\n".join(watch_cards)
tg._send_text(watch_text)
print("Watch list sent")

# ---- SUMMARY ----
summary = (
    "MARKET SUMMARY - Fri 5 Jun 16:00 EAT\n"
    "=" * 35 + "\n"
    "\n"
    "BIAS: USD selling reversed into NYC.\n"
    "JPY pairs rallied London, faded NYC. Classic Friday.\n"
    "CHF pairs strongest intraday but all at weekly peaks.\n"
    "\n"
    "TOP PICKS FOR MONDAY:\n"
    "1. GBPUSD BUY - Weekly aligned, RSI=35 oversold\n"
    "   If holds 1.3400 into Asian session\n"
    "2. EURJPY - If bases in Asian, new W-bottom\n"
    "3. GBPNZD - If Asian range tightens (<50p)\n"
    "\n"
    "AVOID: CHF longs (at weekly peaks), XAUUSD (dumping)\n"
    "\n"
    "NO TRADES TODAY (Friday late session).\n"
    "All setups either extended or reversing."
)
tg._send_text(summary)
print("Summary sent")
print("\nALL 13 FLASHCARDS DELIVERED TO TELEGRAM")
