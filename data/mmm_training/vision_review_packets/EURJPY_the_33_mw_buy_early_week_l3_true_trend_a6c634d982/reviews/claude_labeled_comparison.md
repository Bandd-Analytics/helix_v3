```json
{
  "summary": "12 EURJPY THE_33 MW BUY EARLY_WEEK L3 TRUE_TREND samples (7W/5L, 58% win rate). Winners averaged +27.3p exit / +35.7p MFE / +5.6p MAE. Losers averaged -3.9p exit / +4.4p MFE / +11.0p MAE. The dominant separator is entry timing within the London session: 6 of 7 winners entered 08:00-09:30 UTC, while 4 of 5 losers entered 10:00-11:15 UTC. Secondary separators are TDI state at entry (winners RSI ≥50 or hooking up; losers declining sub-50 or rolling from overbought) and TDR/ADR exhaustion ratio (loser C01 entered at 3.5% remaining range). Both blind models scored 5/12 (42%), consistently failing on timing-driven outcomes invisible in static structure.",
  "winner_traits": [
    "Entry between 08:00-09:30 UTC (London open window): C04=08:00, C05=08:30, C08=09:30, C09=08:30, C11=08:30, C12=08:00",
    "TDI RSI at entry ≥50 or visibly hooking up from oversold: C04=62, C05=52 recovering, C07=51, C08=50, C09=56 rising, C11=55 rising, C12=57 recovering",
    "Price at or below AR Mid at entry (buying into value, not chasing HOD): C04 at AR Mid/WK OPEN H, C05 at AR Mid, C08 near AR L, C09 near AR L, C11 near WK OPEN L, C12 near WK OPEN L",
    "EMAs stacking bullishly or converging: yellow(13) above or crossing above cyan(50), price above pink(200) or recovering toward it",
    "TDR/ADR ratio 29-67% at entry — sufficient remaining range for the move to develop",
    "Weekly BUY alignment in 5 of 7 winners (C04 had weekly BUY, C07/C08 won despite weekly SELL conflict but had structural compensation)",
    "MAE remarkably low: C07 had 0.0p MAE, C11 had 3.3p, C05 had 4.5p — early entries get cleaner fills"
  ],
  "loser_traits": [
    "Entry at 10:00-11:15 UTC (late London): C01=11:00, C03=11:15, C06=10:00, C10=11:00. The move has already played out by then.",
    "TDI declining or exhausted at entry: C01 RSI=63 rolling from 68 zone (overbought), C02 RSI=48 in deep oversold decline, C03 RSI=42 declining, C06 RSI=60 with sell arrows, C10 RSI=48 declining",
    "TDR/ADR exhausted: C01 had TDR=6p/ADR=173p (3.5%). Range fully consumed before entry.",
    "Price near HOD/AR H at entry on late setups (C01, C06) — chasing the tail end of the expansion",
    "All 5 losers exited via STALE_EXIT or BREAKEVEN_AFTER_T1 — none had profitable continuation momentum",
    "MFE capped very low: C10=0.5p, C03=1.9p, C01=4.5p — the move was already done",
    "Same-day duplicate entries (C01+C08 on Oct 14, C03+C10 on Apr 8) — the late entry on the same day always lost while the early one won"
  ],
  "filters_to_test": [
    {
      "id": "EURJPY_33MW_ENTRY_HOUR_CAP",
      "rule": "Block EURJPY THE_33 MW BUY entries after 09:45 UTC (12:45 EAT). Only accept entries in the 07:30-09:45 UTC window.",
      "threshold": "entry_hour_utc <= 9 AND entry_minute_utc <= 45",
      "evidence": "6/7 winners entered 08:00-09:30 UTC. 4/5 losers entered 10:00-11:15 UTC. Same-day proof: Oct 14 09:30 entry = +24.1p winner, Oct 14 11:00 entry = -1.5p loser.",
      "expected_impact": "Would have blocked C01, C03, C06, C10 (all losers) and C07 (winner +18.4p). Net: removes 4 losers, 1 winner. Adjusted win rate: 6/7 = 86%."
    },
    {
      "id": "EURJPY_33MW_TDI_DECLINING_BLOCK",
      "rule": "Block when TDI RSI < 48 AND TDI signal line is declining (RSI < signal, both below 50).",
      "threshold": "rsi < 48 AND sig < 50 AND rsi < sig",
      "evidence": "C02 (RSI=48/Sig=46 declining), C03 (RSI=42/Sig=40 declining), C10 (RSI=48/Sig=46 declining) — all losers with declining TDI sub-50.",
      "expected_impact": "Would block C02, C03, C10 (3 losers). No winners had RSI<48 with declining signal."
    },
    {
      "id": "EURJPY_33MW_TDR_ADR_FLOOR",
      "rule": "Block when TDR/ADR < 15%. Range exhaustion means no remaining fuel for the move.",
      "threshold": "tdr_pips / adr_pips < 0.15",
      "evidence": "C01 had TDR=6p/ADR=173p (3.5%) and was a stale exit loser. All winners had TDR/ADR ≥ 29%.",
      "expected_impact": "Would block C01 (loser). Conservative filter targeting extreme exhaustion."
    },
    {
      "id": "EURJPY_33MW_ENTRY_ABOVE_AR_MID_LATE",
      "rule": "Block when entry price > Asian Range Midpoint AND entry is after 09:30 UTC. Late entries chasing into upper range fail.",
      "threshold": "entry_price > ar_mid AND entry_hour_utc >= 10",
      "evidence": "C01 entered at HOD/AR H at 11:00 (-1.5p). C06 entered near HOD at 10:00 (-6.6p). Winners entering above AR Mid were early (C07 at 12:00 is the exception but entered at AR Mid, not AR H).",
      "expected_impact": "Would block C01, C06 (2 losers). Combines timing + price position."
    },
    {
      "id": "EURJPY_33MW_TDI_OVERBOUGHT_ROLLOVER",
      "rule": "Block when TDI RSI > 60 AND RSI is declining (RSI crossed below signal from above 62). Overbought rollover means the move peaked.",
      "threshold": "rsi > 60 AND rsi < rsi_prev_bar AND rsi_crossed_below_signal_from_62_plus",
      "evidence": "C01 had RSI=63 declining from 68 zone. Price was at HOD with TDI rolling. Exit was -1.5p stale.",
      "expected_impact": "Would block C01 (loser). Tight but precise filter for L3 exhaustion buys."
    }
  ],
  "filters_to_reject": [
    {
      "id": "REJECT_NO_CLEAN_W_BOTTOM",
      "reason": "Both Codex and Claude marked 'clean_w_bottom=false' on C05 (+26.2p winner), C08 (+24.1p winner), and C09 (+24.4p winner). The quant signature already enforces W_BOTTOM detection; visual 'cleanliness' judgment is subjective and would reject 3 high-quality winners."
    },
    {
      "id": "REJECT_WEEKLY_CONFLICT_BLOCK",
      "reason": "C07 (+18.4p, 0.0p MAE) and C08 (+24.1p) both won with Weekly SELL conflicting BUY direction. Weekly conflict alone is not a reliable blocker for this L3 TRUE_TREND signature — the intraday structure overrides."
    },
    {
      "id": "REJECT_TDR_50PCT_ADR_BLOCK",
      "reason": "Claude proposed blocking when TDR > 50% ADR. But C04 (+42.7p, best winner) had TDR=74p/ADR=143p (52%) and C07 (+18.4p) had TDR=62p/ADR=93p (67%). This filter would remove the top performer."
    },
    {
      "id": "REJECT_PRICE_BELOW_EMA200_BLOCK",
      "reason": "Claude proposed blocking BUY when price below EMA200 and declining. But C12 (+29.0p winner) showed exactly this structure — price basing near LOD below declining EMA200, then rallying through it. L3 TRUE_TREND BUYs often start below the 200."
    }
  ],
  "pair_specific_notes": [
    "EURJPY THE_33 MW BUY at L3 TRUE_TREND is a Monday London-open reversal play. The signature has a strong edge (58% raw, improvable to 86% with timing filter) but is extremely time-sensitive.",
    "Asian range 35-50p is typical for this pair on winning setups. All samples had AR < 50p (valid accumulation).",
    "Stop hunt distances are large (30-100p) reflecting EURJPY volatility. Winners averaged 60p stop hunt distance; losers averaged 47p. Larger hunts slightly favored winners, contradicting the 'oversized hunt = reject' filter proposed by Codex.",
    "Same-day re-entries at different times prove timing is the dominant variable: the SAME setup on the SAME day won at 09:30 and lost at 11:00 (Oct 14), and both late entries on Apr 8 lost.",
    "ADR range 93-173p. TDR/ADR ratio at entry matters — extreme exhaustion (< 15%) is a reliable reject, but moderate 40-65% is fine.",
    "T1 hit rate was low across all samples (only C02 and C08 hit T1). Winners relied on time-exit-profit at max duration, not T1 partial close. Consider whether T1 at 1:1 RR is set too aggressively for EURJPY on this signature."
  ],
  "uncertain_items": [
    "C07 (winner at 12:00 UTC) is the sole winner that entered late. It had 0.0p MAE and +18.4p exit. This entry survived despite late timing because price was pulling back into WK OPEN H support after a prior clean reclaim — a pullback-to-support entry rather than a chase. Need more samples to determine if a 'pullback retest after prior reclaim' exception should override the timing filter.",
    "C02 (loser, breakeven after T1 at 08:30) is the sole loser that entered in the winning time window. It had TDI deeply oversold at ~32 with no hook and price in active waterfall decline. The TDI_DECLINING_BLOCK filter would catch it, but need confirmation this doesn't also fire on recovering winners.",
    "Whether confluence score ≥ 90 can override the timing block — C09 (95/100 confluence, +24.4p) and C11 (90/100, +27.0p) were both early entries anyway, so no conflict in this dataset. Untested whether a 95+ confluence late entry would survive.",
    "Vision model blind accuracy was 42% for both Codex and Claude on this signature. The structural similarity between winners and losers makes visual classification near-random. Timing and TDI state (quantitative) are more reliable than chart-pattern judgment (visual) for this signature."
  ],
  "next_backtest_spec": {
    "pair": "EURJPY",
    "signature": "THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND",
    "test_filters": [
      {
        "filter_id": "EURJPY_33MW_ENTRY_HOUR_CAP",
        "parameter": "entry_hour_utc <= 9 AND entry_minute_utc <= 45",
        "baseline_comparison": "Run with and without filter on 365-day backtest"
      },
      {
        "filter_id": "EURJPY_33MW_TDI_DECLINING_BLOCK",
        "parameter": "rsi < 48 AND sig < 50 AND rsi < sig",
        "baseline_comparison": "Run with and without filter, measure loser rejection rate vs winner false-positive rate"
      },
      {
        "filter_id": "EURJPY_33MW_TDR_ADR_FLOOR",
        "parameter": "tdr_pips / adr_pips < 0.15",
        "baseline_comparison": "Run with and without, expect low impact (targets extreme outlier only)"
      },
      {
        "filter_id": "COMBINED_TIMING_PLUS_TDI",
        "parameter": "(entry_hour_utc <= 9 AND entry_minute_utc <= 45) OR (entry_hour_utc >= 10 AND rsi >= 55 AND rsi > sig)",
        "baseline_comparison": "Combined filter: allow early entries freely, allow late entries only if TDI is strongly bullish"
      }
    ],
    "metrics_to_report": ["win_rate", "avg_exit_pips", "avg_mfe", "avg_mae", "sharpe_ratio", "profit_factor", "max_consecutive_losses", "sample_count"],
    "minimum_samples": 30,
    "date_range": "365 days",
    "notes": "Priority is ENTRY_HOUR_CAP — if sample count after filtering drops below 20, relax to 10:00 UTC cutoff. Track whether C07-style pullback-retest entries at 12:00+ survive as an exception category."
  }
}
```
