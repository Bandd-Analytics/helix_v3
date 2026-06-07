# MMM Candidate Rule Cards From Training Transcripts

Status: candidate extraction. These cards are paraphrased from timestamped local training sources
and must be backtested before promotion into `CODEX_MMM_STRATEGY.md` or `CLAUDE_MMM_STRATEGY.md`.

## MMM-TRAIN-001: Default Execution Chart Is M15

- Source windows: `video_003` `00:12:25-00:15:26`
- Visual evidence: `frames/video_003/frame_000026.jpg`
- Teaching summary: Unless a higher timeframe is explicitly being used for context or level checks,
  the working execution chart is M15. The setup should not be chased; wait for the market maker
  pattern to complete inside the expected working window.
- Timeframes: M15 execution; higher timeframes for levels/context only.
- Candidate conditions:
  - Use M15 as the entry/management chart for intraday MMM setups.
  - Use H1/H4/D1 only to locate larger levels, cycle phase, and directional context.
  - Avoid changing timeframes to justify a late entry after the setup has moved.
- Validation mapping:
  - Compare M15 replay entries against the same signal detected on M5/M30/H1.
  - Track whether M15 entries produce better MAE/MFE and more consistent T1 hits.
- Validation status: `candidate`

## MMM-TRAIN-002: Three-Hit Liquidity Reversal Into W Formation

- Source windows: `video_002` `00:27:53-00:30:57`
- Visual evidence: `frames/video_002/frame_000057.jpg`
- Teaching summary: A stronger long reversal can form when price attacks the low area three times,
  especially when later swipes do not materially take out the prior low. This behavior implies
  liquidity has been collected and trapped shorts may be held into the reversal.
- Timeframes: M15 execution.
- Candidate long conditions:
  - Price is in the last quarter to last third of the active box/range.
  - Price makes three pushes/swipes into the low area.
  - Later low swipes fail to meaningfully break the prior low or immediately reject.
  - W formation is visible or developing.
  - Entry is considered on a confirming close, not during an unfinished candle.
  - First target is the high of day or next mapped intraday level.
- Invalidation:
  - Fresh clean breakdown through the low after the third swipe.
  - No confirming close after the W structure.
  - Target distance is too small relative to structural stop.
- Validation mapping:
  - Detect three-push lows, failed marginal breaks, W_BOTTOM, and entry close.
  - Compare first target at HOD versus 1R/T1 and next level target.
- Validation status: `candidate`

## MMM-TRAIN-003: Stop-Hunt High False Break Into M Formation

- Source windows: `video_003` `00:39:45-00:42:48`, `video_004` `03:03:07-03:06:11`
- Visual evidence: `frames/video_003/frame_000081.jpg`, `frames/video_004/frame_000367.jpg`
- Teaching summary: A short reversal setup can form when price trades above a prior high or HOD,
  opens/spikes into liquidity, then fails to hold above that breakout area. The high can be worked
  for roughly 30 to 90 minutes, so the rule should wait for confirmation instead of chasing the
  first spike.
- Timeframes: M15 execution.
- Candidate short conditions:
  - Price extends above HOD, yesterday high, or another visible level.
  - Breakout closes fail to hold above the level or close back below the breakout entry zone.
  - M formation, railroad track, or second-leg confirmation appears.
  - HOD/light-blue tracer remains relevant to the setup.
  - Entry waits for close/zone shift confirmation.
- Invalidation:
  - Strong continuation closes hold above the breakout level.
  - No M formation, no railroad track, and no zone shift inside the working window.
  - Entry occurs after the move has already left acceptable stop distance.
- Validation mapping:
  - Detect HOD/yesterday-high breach, failed closes, M_TOP, railroad tracks, and elapsed time
    from first breach.
  - Test 30, 45, 60, and 90 minute setup windows.
- Validation status: `candidate`

## MMM-TRAIN-004: Asian/Tokyo Range Stop Hunt With TDI Shark Fin

- Source windows: `video_004` `03:00:07-03:03:07`, `video_004` `03:06:11-03:09:12`
- Visual evidence: `frames/video_004/frame_000361.jpg`, `frames/video_004/frame_000373.jpg`
- Teaching summary: When price remains inside the Tokyo/Asian channel and then runs a stop hunt
  beyond the range, a TDI/RSI band break can flag an imminent reversal. Entry is not the band break
  alone; the setup needs price to return inside and print MMM confirmation.
- Timeframes: M15 execution with session/range context.
- Candidate conditions:
  - Asian/Tokyo channel is mapped and within pair-specific acceptable range.
  - Price breaks outside the channel into a stop hunt.
  - TDI/RSI line breaks outside the bands, forming a shark-fin type condition.
  - Price breaks back inside or confirms with an MMM reversal signal.
  - Stop is structural beyond HOD/LOD or the stop-hunt extreme.
- Candidate management:
  - Add only when trend acceleration confirms, such as market baseline break with angle/separation
    or volatility band break.
  - Do not add just because a band was touched; add only when direction and context agree.
  - Exit or reduce when volatility calms and price enters consolidation.
- Validation mapping:
  - Combine Asian range, stop-hunt direction, TDI band excursion, return-inside event, and
    M/W pattern.
  - Test add-on rules separately from initial entry rules.
- Validation status: `candidate`

## MMM-TRAIN-005: Pivot Projection Day Map M3/M1

- Source windows: `video_004` `02:20:35-02:23:40`
- Visual evidence: `frames/video_004/frame_000282.jpg`
- Teaching summary: Prior-day direction and pivot projection can define the expected daily map.
  For a down-cycle/red-candle context, a projected high near M3 can become the stop-hunt area
  before price seeks M1 and later pulls back into consolidation.
- Timeframes: D1/H1 context, M15 execution.
- Candidate sell-day conditions:
  - Prior day or cycle context supports a down-cycle expectation.
  - Daily/pivot map projects HOD around M3 and lower objective around M1.
  - Stop hunt runs roughly into the upper projection area.
  - M formation, yesterday tracer, pivot level, or session timing aligns.
  - Asian/Tokyo range is approximately 25 to 50 pips, adjusted by pair profile.
  - Pattern works for roughly 30 to 90 minutes before directional release.
- Candidate target logic:
  - Primary objective is movement toward M1/three levels lower.
  - Late-day pullback/consolidation should be expected after the objective is reached.
- Validation mapping:
  - Add pivot projection fields to replay signatures.
  - Test projected M3 to M1 movement by pair and day context.
- Validation status: `candidate`

## MMM-TRAIN-006: HOD/LOD Tracer And Moving Average Confirmation

- Source windows: `video_002` `01:25:49-01:28:49`
- Visual evidence: `frames/video_002/frame_000173.jpg`
- Teaching summary: HOD/LOD markers are major context references. Moving-average crossovers are
  confirmation only after the stop hunt and M/W structure; they are not standalone entry signals,
  especially in sideways or Asian-session chop.
- Timeframes: M15 execution.
- Candidate conditions:
  - HOD/LOD and prior-day high/low are visible and correct.
  - A 5/13 or similar moving-average cross confirms a market-maker zone shift.
  - Crossover is valid only after stop hunt and M/W context.
  - Crossover in sideways Asian chop is ignored.
- Validation mapping:
  - Compare MA cross signals before versus after confirmed stop hunt/MW structure.
  - Track false positive rate in Asian chop versus post-stop-hunt release.
- Validation status: `candidate`

## MMM-TRAIN-007: Friday/US Session Swing Exit Logic

- Source windows: `video_001` `00:39:47-00:42:48`
- Visual evidence: `frames/video_001/frame_000081.jpg`
- Teaching summary: For a larger swing position, Friday US session can be an exit context when
  price has completed levels, spikes into a low/high, and moves toward end-of-week consolidation.
- Timeframes: Weekly/D1/H4/H1 context, M15 management.
- Candidate exit conditions:
  - It is Friday and the trade has already moved through multiple levels.
  - US session timing approaches the expected reversal/consolidation window.
  - Price spikes into LOD/HOD or completes a repeated spike.
  - Price begins consolidating after the level move.
- Validation mapping:
  - Test Friday session exit versus trailing-stop-only and fixed target exits.
  - Segment swing-management tests separately from intraday scalp tests.
- Validation status: `candidate`

## MMM-TRAIN-008: Session-Specific Homework And Bidirectional Pattern Trading

- Source windows: `video_002` `03:48:46-03:51:46`
- Visual evidence: `frames/video_002/frame_000459.jpg`
- Teaching summary: The trader should focus homework and execution on the session they actually
  trade. M and W patterns can create opportunities in both directions, but only when the trader
  has mapped the session levels and understands the pattern sequence.
- Timeframes: M15 execution, session-specific preparation.
- Candidate conditions:
  - Mark levels for the session being traded.
  - Avoid taking reversal trades in sessions not actively watched or prepared.
  - Recognize intraday "pushes" separately from multi-day "levels."
  - A large M can provide short opportunity; later W/two-pin behavior can justify switching bias
    only after confirmation.
- Validation mapping:
  - Add session-focus field to flashcards.
  - Compare London-focused setups versus New York-focused setups by pair.
  - Mine transitions where M_TOP completion is followed by W_BOTTOM reversal in the same session.
- Validation status: `candidate`
