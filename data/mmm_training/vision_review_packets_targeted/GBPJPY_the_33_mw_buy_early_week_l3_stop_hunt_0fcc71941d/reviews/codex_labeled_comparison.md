{
  "summary": "The packet is 8 winners vs 1 loser, so the separator is weak statistically. The clearest hypothesis is timing/confirmation: C03 was the early shark-fin-only trigger, while later same-cluster examples became profitable. Do not promote any filter from this packet alone.",
  "winner_traits": [
    "Most stronger winners had explicit TDI support: SIGNAL_CROSS_BULLISH, MBL_CROSS_BULLISH, or bullish divergence.",
    "Winners tolerated GBPJPY extension and large hunts: stop hunts ranged about 38-63p and Asian ranges about 25-49p.",
    "Confluence >=65 or advisory >=77.0 was high precision in this packet, but lower-score examples also won.",
    "Later same-setup confirmations after the first stop-hunt read performed better than the earliest read."
  ],
  "loser_traits": [
    "Only C03 failed, making loser traits low confidence.",
    "C03 was shark-fin-only with no bullish TDI cross, no bullish divergence, confluence 60, and theme score 0.44.",
    "C03 is visually and structurally close to C01/C05, so the likely failure factor is early timing before confirmation, not the setup family itself."
  ],
  "filters_to_test": [
    {
      "name": "shark_fin_cluster_wait",
      "rule": "Group same symbol+direction+normalized_key candidates within 150 minutes. For BUY candidates with tdi_shark_fin=true, tdi_crossed_signal='none', and tdi_divergence='none', reject cluster_index=1 unless a closed M15 candle closes above previous_high+2p and above asian_low+max(5p,0.15*asian_range_pips)."
    },
    {
      "name": "tdi_quality_tier",
      "rule": "Assign tdi_quality=2 for SIGNAL_CROSS_BULLISH or MBL_CROSS_BULLISH, 1 for bullish divergence, 0 for shark-fin-long only, -1 for bearish cross without bullish divergence. Test tdi_quality>=1 as strict, and tdi_quality>=0 plus price confirmation as permissive."
    },
    {
      "name": "post_hunt_reclaim",
      "rule": "For BUY, within 1-6 M15 bars after the hunt low, require one closed candle with close>=asian_low+max(5p,0.15*asian_range_pips) and close>=hunt_low+0.35*stop_hunt_pips."
    },
    {
      "name": "higher_low_w_confirmation",
      "rule": "After the hunt low, require at least one M15 higher-low candle where low>=hunt_low+2p, close>open, and close>ema_fast before accepting shark-fin-only entries."
    },
    {
      "name": "context_strength_subbucket",
      "rule": "Tag high-grade when confluence_score>=65 or advisory_confidence_score>=77.0 or single_setup_theme_score>=0.46. Compare this as a scoring boost, not an immediate rejection rule."
    },
    {
      "name": "upper_range_exception",
      "rule": "If entry_position_pct=(close-asian_low)/asian_range_pips >0.85, allow only when tdi_quality>=1 and close>ema_fast; otherwise reject upper-range BUY continuation attempts."
    }
  ],
  "filters_to_reject": [
    "Reject blanket bans on shark-fin-only entries; C01 and C04 were winners.",
    "Reject blanket bans on bearish TDI cross when bullish divergence is present; C07 hit TARGET_2.",
    "Reject blanket bans on upper-third or vertical-extension BUYs; C08 won despite that visual profile.",
    "Reject requiring weekly BUY alignment; this setup can work with weekly_trend=SELL in the stored context.",
    "Reject using Asian range size or stop-hunt size alone; C03 shared the same AR/hunt values as winning C01/C05."
  ],
  "pair_specific_notes": [
    "GBPJPY needs pip-scaled thresholds; 5-11p MAE can still be normal for this setup.",
    "GBP_STRENGTH plus JPY_WEAKNESS appears supportive and should remain in the feature set.",
    "The C03 to C01 to C05 cluster occurred around 08:00, 08:30, and 10:15 EAT, suggesting delayed confirmation may matter."
  ],
  "uncertain_items": [
    "Only one loser is present, so no filter is promotion-ready.",
    "C01 and C03 have nearly identical stored context, so chart-only separation is unreliable.",
    "Reviewer labels like return_inside_asian_range were inconsistent; replace them with numeric OHLC-derived fields."
  ],
  "next_backtest_spec": {
    "cohort": "GBPJPY M15 normalized_key=THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74",
    "derive_features": [
      "cluster_index within 150 minutes",
      "tdi_quality",
      "entry_position_pct",
      "close distance above asian_low",
      "close distance above hunt_low",
      "higher_low_after_hunt",
      "close_vs_ema_fast",
      "bars_since_hunt_low"
    ],
    "compare": [
      "baseline signature",
      "shark_fin_cluster_wait",
      "tdi_quality_tier",
      "post_hunt_reclaim",
      "higher_low_w_confirmation",
      "context_strength_subbucket"
    ],
    "metrics": [
      "total",
      "favorable_rate",
      "avg_exit_pips",
      "avg_mfe",
      "avg_mae",
      "t1_rate",
      "target2_rate",
      "train_validation_out_of_sample_split"
    ]
  }
}