{
  "summary": "Winners were mainly confirmed high-side reversals or post-raid continuation sells; losers clustered around unconfirmed spike entries, low-side exhaustion sells, or H1 BUY recovery structure. TDI conflict alone did not separate outcomes.",
  "winner_traits": [
    "HOD/Asian-high raid followed by price closing back inside the range or below fast averages.",
    "Bearish displacement after the raid: multiple red M15 closes or one large sell candle before entry.",
    "Shark-fin-long and bullish signal-cross were often acceptable when price had already rejected HOD.",
    "Best entries retained downside room or had strong post-HOD continuation momentum."
  ],
  "loser_traits": [
    "First sell into a parabolic bullish HOD spike before confirmation, especially C11 versus later winner C12.",
    "Sell after LOD/low-side sweep with bullish TDI divergence, MBL cross, or hook-up from oversold.",
    "H1 BUY recovery structure without a clean close below AR mid/EMA stack.",
    "Failed losers quickly expanded against entry by roughly 400-545p."
  ],
  "filters_to_test": [
    {
      "name": "confirmed_high_side_raid_return",
      "rule": "For SELL, require a sweep above HOD or Asian high by max(50p, 0.05 * asian_range_pips), then at least 1 M15 close back below that swept level by max(25p, 0.03 * asian_range_pips)."
    },
    {
      "name": "bearish_displacement_after_raid",
      "rule": "Within 8 M15 candles after the high-side raid, require either 2 bearish closes or total bearish body >= max(150p, 0.20 * asian_range_pips), with latest close below EMA8 and EMA13."
    },
    {
      "name": "spike_cooldown",
      "rule": "If last 6 candles include a bullish candle body >= max(250p, 0.25 * asian_range_pips) through HOD/Asian high, block SELL until 2 consecutive M15 closes are below that candle midpoint and no new high prints."
    },
    {
      "name": "low_side_exhaustion_block",
      "rule": "Block SELL if close is within max(150p, 0.15 * asian_range_pips) of current LOD or below Asian low after a LOD sweep in last 8 candles AND TDI shows bullish divergence, MBL cross bullish, or green line rising 2 bars."
    },
    {
      "name": "h1_buy_requires_breakdown",
      "rule": "If h1_trend == BUY, allow SELL only after close is below AR mid or EMA50 by max(75p, 0.08 * asian_range_pips) and last 6 candles show a lower high."
    },
    {
      "name": "continuation_short_quality",
      "rule": "For entries not near HOD, require close below EMA8/13/50, EMA8 slope down for 3 bars, pullback high not closing above EMA13, and distance to LOD >= max(250p, 0.25 * asian_range_pips)."
    }
  ],
  "filters_to_reject": [
    "Hard-blocking all TDI_CONFLICT signals; many winners had shark-fin-long or bullish signal-cross.",
    "Hard-blocking ADR% above 80; C10 was a strong winner despite high ADR usage.",
    "Using Asian range size alone; winners and losers both appear in tight and wide ranges.",
    "Using stop_hunt_pips or push_count alone; both failed to separate this packet.",
    "Rejecting all sells near HOD; HOD rejection was often the profitable source."
  ],
  "pair_specific_notes": [
    "For XAUUSD M15, use both absolute pips and Asian-range ratios because candle sizes vary heavily.",
    "High-side HOD failure mattered more than TDI agreement.",
    "Later confirmation after a spike was materially better than the first spike sell.",
    "Low-side exhaustion with bullish TDI is the clearest avoid pattern."
  ],
  "uncertain_items": [
    "Small sample: 13 reviewed examples from this packet.",
    "C01 hit T1 then breakeven, so treating it as a loser may over-penalize fast partial wins.",
    "C09 warns against blocking all low-position sells; the block should target low-side exhaustion plus bullish TDI.",
    "Visual AR/EMA/TDI states need OHLC-derived proxies before full validation."
  ],
  "next_backtest_spec": {
    "scope": "All XAUUSD matches for this exact normalized signature, then adjacent XAUUSD SELL RRT THE_33 mid-week variants.",
    "features": [
      "bars_since_high_side_raid",
      "raid_pips_above_hod_or_asian_high",
      "closes_back_inside_after_raid",
      "bearish_body_pips_1_3_6_bars",
      "entry_position_in_asian_range",
      "distance_to_hod_lod_pips",
      "largest_bullish_impulse_last_6",
      "tdi_conflict_subtype",
      "tdi_green_slope_2_bars",
      "h1_trend",
      "close_vs_ema8_13_50_200"
    ],
    "ablations": [
      "confirmed_high_side_raid_return",
      "bearish_displacement_after_raid",
      "spike_cooldown",
      "low_side_exhaustion_block",
      "h1_buy_requires_breakdown",
      "continuation_short_quality"
    ],
    "metrics": [
      "favorable_rate",
      "avg_exit_pips",
      "avg_mae",
      "t1_rate",
      "blocked_losers",
      "missed_winners",
      "year_split_passes"
    ],
    "keep_rule_if": "At least 20 samples, improves avg_exit_pips and avg_mae, blocks more losers than winners, and passes at least 2 temporal splits."
  }
}