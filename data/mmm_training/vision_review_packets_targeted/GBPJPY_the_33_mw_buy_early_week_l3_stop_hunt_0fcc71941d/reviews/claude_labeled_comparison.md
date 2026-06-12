```json
{
  "summary": "For GBPJPY THE_33 / W-bottom BUY / early-week / L3 / stop-hunt setups, the answer key shows this signature is strongly favorable: 8 of 9 examples are winners (5 hit T1/TARGET_2) and only C03 lost. Both blind reviewers were badly miscalibrated, labeling most true winners as losers; their proposed 'require clean W + reclaim inside Asian range + bullish TDI turn' filters would have rejected several real winners (C04, C05, C07, C08, C09) and must NOT be hard-coded. The only loser (C03) is an early-trigger variant of the same session as winners C01 (+30 min) and C05 (+2h15m): it fired at the first 05:00 print before reclaim confirmed, went 13.3p adverse vs only 4.0p favorable, and never developed. The real winner/loser separator here is post-entry follow-through quality (low immediate adverse excursion, prompt reclaim toward AR mid), not the presence/absence of a textbook W — most winners already satisfy the signature gates.",
  "winner_traits": [
    "Prompt follow-through after entry: big winners (C04, C05, C08, C09) held max_adverse < 3.5 pips while reaching 30-39 pips favorable (MFE/MAE > 8).",
    "Entry placed AFTER an initial confirming bar rather than on the first session print (C01 05:30 and C05 07:15 won on the same day C03 05:00 lost).",
    "T1/TARGET_2 winners (C04, C05, C07, C08, C09) showed a V-reclaim that pushed back toward/through Asian-range mid within the first few M15 bars.",
    "Hunt sweep of LOD followed by immediate reclaim and continuation, not stalling at the hunt low.",
    "TDI bullish recovery from the lower zone visible on most winners (signal cross up / blood-in-water)."
  ],
  "loser_traits": [
    "C03: earliest trigger of the session (05:00) before reclaim/second leg confirmed.",
    "MFE capped at ~4 pips with MAE ~13 pips — immediately underwater and never developed (poor MFE/MAE ratio < 0.4).",
    "Entry pinned near LOD after a HOD rejection with no higher-low yet formed; structure still incomplete at entry.",
    "Choppy, overlapping candles around entry rather than a clean impulsive reclaim leg."
  ],
  "filters_to_test": [
    "Confirmation-bar delay: do not enter on the first M15 trigger of the session; require >=1 closed M15 bar reclaiming above the hunt low before entry (C03 05:00 lost; same-session entries 30+ min later won).",
    "Early adverse-excursion abort: if price runs > 10 pips against entry within the first 2 M15 bars (3 for XAU-class), treat structure as invalid (loser MAE 13.3p vs winners' 1.3-3.5p on T1 trades).",
    "Reclaim-depth gate: require price to recover to >= Asian-range mid within 3 M15 bars of entry; reject if still below AR low.",
    "MFE/MAE shape proxy: require favorable move >= adverse move within first 3 bars (loser had favorable 4.0p < adverse 13.3p).",
    "Higher-low requirement after the hunt: at least one M15 higher-low above the stop-hunt low before BUY confirmation."
  ],
  "filters_to_reject": [
    "Hard 'clean W-bottom required' block — multiple winners (C01, C06 per reviewers) lacked a textbook W yet still profited.",
    "Hard 'return_inside_asian_range required' block — winners C01 and C04 do not all satisfy it; would cut hit rate.",
    "Block on bullish run / parabolic spike into range high — C05 and C08 were winners despite extension.",
    "Block BUY on a bearish TDI signal cross at entry — C07 carried that read yet hit TARGET_2 (+32.75p).",
    "Adopting the blind reviewers' majority 'loser' verdicts as labels — they were inverted vs the answer key."
  ],
  "pair_specific_notes": [
    "GBPJPY THE_33 BUY at this signature has a high base favorable rate; bias filters toward timing/follow-through quality, not toward adding more structural veto gates.",
    "Pip scales here are ~10-40p MFE; use GBPJPY hunt range 30-60p and min SL ~25p when encoding adverse-excursion thresholds.",
    "Same-session re-trigger risk: a too-early entry (C03) and a confirmed entry (C01/C05) can share an identical signature — timing/confirmation is the discriminator, so encode a per-session confirmation delay rather than a one-shot signature match."
  ],
  "uncertain_items": [
    "Whether C03 is truly structurally different from C01/C05 or simply unlucky timing within the same wave — only the 30-min lead and weak MFE/MAE distinguish it.",
    "Exact TDI states are hard to read from the static panels; 'bullish recovery' inference is approximate and not reliably separable between winners and the loser.",
    "Single loser (n=1) limits statistical confidence; proposed filters are hypotheses to backtest, not validated edges."
  ],
  "next_backtest_spec": {
    "signature": "THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74",
    "pair": "GBPJPY",
    "objective": "Test whether timing/follow-through filters raise win rate and MFE/MAE without rejecting the existing winners.",
    "variants": [
      "baseline (current gates)",
      "baseline + confirmation-bar delay (>=1 closed M15 reclaim above hunt low)",
      "baseline + early adverse-excursion abort (>10p against within 2 bars)",
      "baseline + reclaim-to-AR-mid within 3 bars",
      "baseline + higher-low-after-hunt requirement",
      "baseline + all timing filters combined"
    ],
    "metrics": ["win_rate", "avg_exit_pips", "mfe_mae_ratio", "t1_hit_rate", "trades_retained_vs_baseline", "winners_incorrectly_filtered"],
    "acceptance_criteria": "Filter set must retain >=7 of the 8 known winners while removing the C03-type early/underwater entries; reject any filter that drops more than one historical winner.",
    "sample_window": "Multi-year GBPJPY M15 covering 2024-2026, early-week sessions only, minimum 30 signature instances before drawing conclusions."
  }
}
```
