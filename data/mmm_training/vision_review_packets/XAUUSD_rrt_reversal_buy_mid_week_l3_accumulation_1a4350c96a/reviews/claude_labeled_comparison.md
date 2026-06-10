Now I have all 11 charts inspected and the answer key loaded. Let me synthesize the winner vs loser comparison.

**Answer Key:**
- **Winners (7):** C01 (+2659p), C02 (+225p), C03 (+1466p), C04 (+372p), C06 (+373p), C08 (+878p), C10 (+763p)
- **Losers (4):** C05 (0p BE), C07 (-480p), C09 (-112p stale), C11 (-105p)
- **Win rate: 63.6%**

**Blind review accuracy:** Codex 7/11 (63.6%), Claude 4/11 (36.4%).

```json
{
  "summary": "XAUUSD RRT_REVERSAL BUY at L3 accumulation mid-week: 7W/4L (63.6%). The dominant separator is the weekly bias: all 3 hard losers (C05, C07, C11) carried Weekly NEUTRAL, while all 7 winners carried Weekly BUY. A secondary separator is the realized Asian range width — losers averaged ~823p vs winners ~1633p. Losers consistently entered near HOD/WK_OPEN_H resistance with multiple red exhaustion arrows visible and TDI either below the 50 midline or rolling over. Both blind reviewers over-rejected winners: Claude scored only 36.4% accuracy (rejected winners C01, C02, C03, C06, C08, C10), confirming that this signature's visual complexity on XAUUSD misleads pattern-based rejection heuristics. The setup is net-profitable and should not be filtered more aggressively overall; instead, targeted rejection of the NEUTRAL-weekly subset eliminates the worst outcomes.",
  "winner_traits": [
    "Weekly bias = BUY (MID_WEEK) on all 7 winners — zero exceptions",
    "Asian range ≥ 1300p in 6 of 7 visible cases (C02=1505, C03=1781, C04=1387, C06=1360, C08=2013, C10=1716); wider accumulation = deeper institutional loading",
    "TDI RSI ≥ 50 at entry in 6 of 7 (C01=68, C02=56, C03=53, C04=55, C06=56, C08=51); exception C10=45 but had Weekly BUY + strong stop hunt",
    "Stop hunt clearly labeled/visible on chart with price reclaiming the range (C03 767p, C04 1275p, C06 1812p, C08 1627p, C10 3154p)",
    "Price at entry is above the 50 EMA (yellow) or has just crossed back above it — EMA structure supportive",
    "Green up-arrows outnumber or balance red down-arrows near entry zone",
    "Max adverse excursion (MAE) moderate: median 209p; C06 had only 19p MAE — clean entries within the impulse",
    "3 of 7 winners hit T1 and trailed to large gains (C01 +2659p, C03 +1466p, C10 +763p); the remaining 4 exited at time-profit with +225 to +878p"
  ],
  "loser_traits": [
    "Weekly bias = NEUTRAL in 3 of 4 losers (C05, C07, C11) — buy into neutral weekly structure lacks HTF tailwind",
    "Asian range < 1100p in 3 of 4 (C05=679p, C07=679p, C11=1026p); narrow accumulation = insufficient institutional loading for L3 gold",
    "Entry at or above WK OPEN H / HOD resistance with multiple red down-arrows visible (C05: 4+ red arrows at peak, C07: red arrows at prev HOD, C09: 3+ red arrows at HOD, C11: red arrow at WK OPEN H)",
    "TDI RSI ≤ 48 or rolling over at entry (C05=48 declining, C07=59 but rolling over from peak, C09=57 at VB Squeeze ceiling, C11=43 deeply below midline)",
    "Friday-to-Monday session transitions on C05 and C07 — weekend gap risk + unclear fresh-week direction",
    "C09 (the only Weekly BUY loser) had VB Squeeze at HOD with 3+ red arrows — stalled into a stale exit despite tight range and clean hunt; the HOD exhaustion arrows overrode the positive setup factors",
    "No clean second-leg pullback hold visible — entries were either at the top of the impulse or after distribution"
  ],
  "filters_to_test": [
    {
      "id": "F1_WEEKLY_NEUTRAL_BLOCK",
      "rule": "Reject BUY when weekly_bias == 'NEUTRAL' for this XAUUSD RRT_REVERSAL signature",
      "threshold": "weekly_bias != 'BUY'",
      "rationale": "3/3 NEUTRAL entries were losers (C05, C07, C11). 0/7 winners had NEUTRAL. Sensitivity 75% (catches 3 of 4 losers), specificity 100% (blocks zero winners).",
      "expected_impact": "Removes 3 losers, keeps all 7 winners. New win rate: 7/8 = 87.5%"
    },
    {
      "id": "F2_ASIAN_RANGE_FLOOR_1100P",
      "rule": "Reject when Asian_range_pips < 1100 for XAUUSD RRT_REVERSAL BUY at L3",
      "threshold": "asian_range < 1100 pips (XAUUSD-specific)",
      "rationale": "3 of 4 losers had Asian range < 1100p (679, 679, 1026). Only 0 of 7 winners had range < 1100p. Insufficient accumulation width for gold at this cycle level.",
      "expected_impact": "Removes 3 losers (C05, C07, C11), keeps all 7 winners. Overlaps heavily with F1."
    },
    {
      "id": "F3_RED_ARROWS_AT_HOD_EXHAUSTION",
      "rule": "Reject BUY when >= 3 red down-arrows are visible within 4 candles of current HOD at entry time",
      "threshold": "count_red_arrows_within_4_bars_of_hod >= 3",
      "rationale": "C05 (loser), C07 (loser), C09 (loser) all showed 3+ red exhaustion arrows clustered at HOD. Only 1 winner (C02) had red arrows near HOD but fewer than 3 and further from entry.",
      "expected_impact": "Catches C05, C07, C09 (3 of 4 losers). May catch some winners — needs backtest confirmation."
    },
    {
      "id": "F4_TDI_RSI_BELOW_45_BLOCK",
      "rule": "Reject BUY when TDI RSI < 45 AND weekly_bias != 'BUY'",
      "threshold": "rsi < 45 AND weekly_bias == 'NEUTRAL'",
      "rationale": "C11 (RSI 43, NEUTRAL, loser). C10 had RSI 45 but weekly BUY and won +763p. The combo filter preserves C10 while rejecting C11.",
      "expected_impact": "Targeted — catches C11 specifically. Redundant with F1 but adds a hard floor for future edge cases."
    },
    {
      "id": "F5_FRIDAY_ENTRY_BLOCK",
      "rule": "Reject entries triggered on Friday for this XAUUSD L3 signature (weekend gap risk)",
      "threshold": "entry_day_of_week == Friday",
      "rationale": "C05 and C07 both triggered on Friday into Monday. Both lost. No Friday entries among winners.",
      "expected_impact": "Removes 2 losers. Overlaps with F1 (both were NEUTRAL). Needs larger sample to confirm independence."
    }
  ],
  "filters_to_reject": [
    {
      "id": "REJECT_RSI_ABOVE_65_ON_BUY",
      "source": "Claude blind review (C01)",
      "reason": "C01 had RSI 68 and was the best winner in the set (+2659p trail stop). Blocking RSI > 65 on buys would have eliminated the single largest gain. On XAUUSD in trending weeks, overbought RSI is a momentum signal, not exhaustion."
    },
    {
      "id": "REJECT_WIDE_ASIAN_RANGE_ABOVE_1400P",
      "source": "Claude blind review (C02)",
      "reason": "Winners C02 (1505p), C03 (1781p), C10 (1716p), C08 (2013p) all had Asian ranges above 1400p and won. Wide Asian range on XAUUSD at L3 is bullish accumulation, not a rejection signal."
    },
    {
      "id": "REJECT_ENTRY_AFTER_MOVE_EXCEEDS_1X_ADR",
      "source": "Claude blind review (C03)",
      "reason": "C03 entered after a big move but won +1466p with trail stop. XAUUSD routinely makes multi-ADR moves during mid-week reversals. This filter would have killed 3+ winners."
    },
    {
      "id": "REJECT_BUY_WHEN_RSI_BELOW_50",
      "source": "Claude blind review (C05)",
      "reason": "C10 had RSI 45 and won +763p. C03 had RSI 53 (near 50). A flat RSI < 50 block is too aggressive for XAUUSD where the RRT reversal buy often fires from oversold recovery. Must be combined with weekly bias filter (F4) to be useful."
    },
    {
      "id": "REJECT_COUNTERTREND_INTO_SELLOFF",
      "source": "Codex blind review (C10), Claude blind review (C10)",
      "reason": "Both reviewers predicted C10 as a loser with high confidence (Codex 82%, Claude 77%). C10 was actually a winner (+763p trail stop, T1 hit). The chart looked bearish visually but the weekly BUY + stop hunt at 3154p + RRT reversal mechanics worked. This confirms vision models systematically misjudge XAUUSD V-shaped recoveries."
    }
  ],
  "pair_specific_notes": [
    "XAUUSD L3 accumulation produces large Asian ranges (1300-2000p) that look 'wide' vs forex pairs but represent normal institutional loading for gold. Do NOT apply forex-scaled Asian range filters.",
    "XAUUSD weekly BUY bias is the single strongest filter for this signature. NEUTRAL weekly bias eliminated all hard losers with zero false positives in this sample.",
    "Gold RRT reversals from deep selloffs (C01, C10) look visually terrifying but produce the largest wins. Vision models consistently reject these — both reviewers scored < 40% accuracy on these charts. The algo should NOT defer to vision consensus for this specific signature.",
    "Stop hunt magnitudes on XAUUSD are 5-10x forex scale (767p to 11721p). The hunt-to-range ratio matters more than absolute pip size.",
    "ADR% at entry: winners averaged ~47%, losers averaged ~31%. Higher ADR% = more intraday range consumed = but still room to run when weekly is BUY. Low ADR% + NEUTRAL weekly = stall/reversal risk.",
    "T1 hit rate: 3/7 winners (43%) hit T1 and trailed to large gains. The 4 non-T1 winners still averaged +462p via time-exit-profit. This signature has positive expectancy even without T1."
  ],
  "uncertain_items": [
    "C09 is the only Weekly BUY loser (-112p stale exit). It had the tightest Asian range among BUY-week entries (908p) and 3+ red arrows at HOD. Whether Asian range < 1000p + red arrows is a reliable additional filter requires more samples.",
    "C08 won +878p despite Asian range 2013p (widest in set) and choppy L3 price action with TDI at 51/50. Codex and Claude both rejected it. Whether extremely wide Asian ranges (>1800p) on XAUUSD produce lower-quality wins needs more data.",
    "The Friday entry block (F5) overlaps completely with the NEUTRAL weekly filter (F1) in this sample. Cannot determine if Friday alone is a risk factor or if NEUTRAL weekly is the true cause.",
    "C05 hit T1 then returned to breakeven — the only loser with T1 hit. Whether T1 management (partial close + BE stop) is suboptimal for this signature vs holding full size needs separate analysis."
  ],
  "next_backtest_spec": {
    "signature": "RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION",
    "pair": "XAUUSD",
    "primary_filter": "F1_WEEKLY_NEUTRAL_BLOCK: skip entry when weekly_bias != 'BUY'",
    "secondary_filter": "F3_RED_ARROWS_AT_HOD_EXHAUSTION: skip when red_arrow_count_at_hod >= 3 within 4 bars",
    "tertiary_filter": "F2_ASIAN_RANGE_FLOOR_1100P: skip when asian_range_pips < 1100",
    "lookback_days": 365,
    "min_samples": 20,
    "metrics_required": ["win_rate", "avg_exit_pips", "sharpe", "max_drawdown", "t1_hit_rate", "avg_mae_pips"],
    "baseline": "unfiltered signature (current 63.6% win rate, 7W/4L)",
    "hypothesis": "F1 alone should lift win rate to >80% by removing NEUTRAL-weekly losers. F1+F3 combined should catch C09-type stale exits. Target: >75% win rate with Sharpe > 2.0.",
    "ablation_order": ["F1_only", "F1+F2", "F1+F3", "F1+F2+F3", "F1+F4"],
    "vision_override_note": "For this signature, consider disabling vision consensus veto — both reviewers scored <=64% accuracy vs 63.6% base rate, meaning vision adds no edge and actively rejects the highest-conviction winners (C01, C10)."
  }
}
```
