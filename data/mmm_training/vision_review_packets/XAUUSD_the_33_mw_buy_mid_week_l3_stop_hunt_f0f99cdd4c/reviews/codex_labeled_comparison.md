{
  "summary": "Winners split into two valid branches: early floor-reversal buys near the stop-hunt/LOD extreme, and continuation buys after a real reclaim with EMA alignment. Losers were mainly weekly-neutral, stale repeat attempts, or chased moves after the stop hunt had already paid out without a fresh base.",
  "winner_traits": [
    "Weekly bias was BUY on all winners; the only Weekly NEUTRAL sample was a loser.",
    "Profitable reversals could look ugly if taken close to the liquidity floor: near current LOD, ADR low, previous LOD, or weekly-open liquidity with TDI curling up.",
    "Best continuation winners showed price holding above EMA50 with EMA5 > EMA13 and widening, often after reclaiming Asian range or current LOD.",
    "High ADR% and large stop-hunt pips did not disqualify XAUUSD winners; C01, C03, C04, and C09 all won despite visually extended conditions.",
    "First or second same-hunt attempts performed better than later repeat signals from the same daily sweep."
  ],
  "loser_traits": [
    "Weekly NEUTRAL plus very large Asian range/ADR expansion was unfavorable.",
    "Late repeat buys after the same stop hunt degraded: C06 lost after C01 and C04 had already fired on the same XAUUSD day.",
    "Weak crash rebounds failed when price was below EMA50, had no higher-low retest, and TDI was still below or near the 50 line.",
    "Straight-line rallies into HOD without a pullback/base were risky, especially when TDI had already rolled over from the upper band.",
    "Large stop hunt alone was not enough; C02 and C07 had large hunts but lacked clean reclaim/base quality."
  ],
  "filters_to_test": [
    {
      "name": "weekly_buy_required",
      "rule": "For BUY setups, reject if weekly_bias != BUY.",
      "thresholds": "weekly_bias must equal BUY"
    },
    {
      "name": "same_hunt_attempt_decay",
      "rule": "For same symbol+direction+EAT date, group signals sharing a stop-hunt low within 0.15 * asian_range_pips. Reject signal_index >= 3 unless a new LOD is made by at least 0.25 * asian_range_pips or price closes above prior HOD.",
      "thresholds": "same_hunt_low_tolerance <= 15% Asian range; reject third+ attempt"
    },
    {
      "name": "early_floor_reversal_branch",
      "rule": "Accept a messy reversal only if close is within 0.25 * current_day_range of current LOD, the stop-hunt low occurred within the last 8 M15 candles, and TDI green slope is positive for 2 candles.",
      "thresholds": "distance_from_LOD <= 25% TDR; candles_since_low <= 8; TDI green slope > 0 for 2 bars"
    },
    {
      "name": "confirmed_reclaim_branch",
      "rule": "Accept continuation only after at least 2 consecutive closes above EMA13, EMA5 > EMA13, EMA13 slope positive, and either close > EMA50 or close back inside Asian range.",
      "thresholds": "2 closes above EMA13; EMA5 > EMA13; EMA13 slope > 0"
    },
    {
      "name": "hod_chase_requires_pullback",
      "rule": "If close is in the top 15% of current day range and distance from stop-hunt low is greater than 0.75 * current_day_range, require at least one pullback candle touching EMA13 or EMA50 followed by a bullish close above EMA13.",
      "thresholds": "range_position >= 85%; distance_from_hunt_low >= 75% TDR; pullback touch required"
    },
    {
      "name": "weak_crash_rebound_reject",
      "rule": "Reject if close < EMA50, close is more than 0.35 * current_day_range above LOD, no higher-low retest exists within last 12 candles, and TDI green <= red.",
      "thresholds": "close < EMA50; distance_from_LOD > 35% TDR; no HL retest in 12 bars; TDI green <= red"
    }
  ],
  "filters_to_reject": [
    "Do not reject solely because price has not returned inside Asian range; C01 and C04 were winners.",
    "Do not reject solely on ADR% > 100; several XAUUSD winners were above 100% ADR.",
    "Do not reject solely on stop_hunt_pips > 1500; both winners and losers had large hunts.",
    "Do not require a textbook clean W-bottom; profitable XAUUSD floor reversals can be visually messy.",
    "Do not reject all HOD-area buys; C03, C09, and C10 were profitable despite HOD proximity."
  ],
  "pair_specific_notes": [
    "Use normalized thresholds for XAUUSD; raw pip size is too volatile across sessions.",
    "XAUUSD can continue after extreme ADR expansion, so ADR should be contextual rather than a hard cap.",
    "Weekly BUY appears important for this signature, but entry quality still depends on whether the signal is early at the floor or confirmed after reclaim.",
    "Repeated same-day THE_33 buy signals should be treated as decaying unless a fresh liquidity event occurs."
  ],
  "uncertain_items": [
    "C01 and C04 won despite weak visual W structure, so the model should preserve an early-floor exception.",
    "C05 and C10 conflict visually: both are HOD-area buys, but C05 lost and C10 won, so HOD rejection must be conditional on pullback/base quality.",
    "C07 had high max favorable pips but closed stale negative, so some failures may be trade-management exits rather than pure entry-filter failures."
  ],
  "next_backtest_spec": {
    "scope": "XAUUSD only, exact signature THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS",
    "labels": "winner if exit_pips > 0 or t1_hit true; loser if exit_pips <= 0",
    "features": [
      "weekly_bias",
      "EAT date and same-day signal index",
      "same-hunt group by LOD proximity",
      "asian_range_pips",
      "current_day_range_pips",
      "ADR_percent",
      "stop_hunt_pips",
      "close_position_in_day_range",
      "distance_from_LOD",
      "distance_from_stop_hunt_low",
      "candles_since_stop_hunt_low",
      "return_inside_asian_range",
      "EMA5/EMA13/EMA50 order and slopes",
      "TDI green/red levels, cross, and 2-bar slopes",
      "higher_low_retest within 12 candles",
      "pullback touch of EMA13 or EMA50 after HOD break"
    ],
    "tests": "Run single-filter and combined-branch ablations, report N, win rate, avg exit pips, avg MFE, avg MAE, and rejected-winner count with walk-forward split by snapshot_at."
  }
}