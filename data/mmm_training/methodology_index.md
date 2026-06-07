# Steve Mauro MMM Methodology Extraction Index

Purpose: convert training videos into timestamped, testable MMM rules.

Content boundary: notes should paraphrase methodology and preserve timestamps, screenshots, and evidence references. Avoid rebuilding the course as a full verbatim transcript.

## Workflow

1. Extract audio and keyframes.
2. Build timestamped notes per video.
3. Convert notes into rule cards.
4. Map rule cards to flashcard fields and MMM replay signatures.
5. Validate each rule against historical market behavior.
6. Promote only validated rules into Claude/Codex skill documents.

## Source Videos

- `video_001`: MMM 8-2-2011 Day 1 (`videos\MMM 8-2-2011 Day 1 .mp4`)
- `video_002`: MMM 8-3-2011 Day 2 (`videos\MMM 8-3-2011 Day 2 .mp4`)
- `video_003`: MMM 8-4-2011 Day 3 (`videos\MMM 8-4-2011 Day 3 .mp4`)
- `video_004`: MMM 8-4-2011 Day 4 (`videos\MMM 8-4-2011 Day 4.mp4`)

## Rule Status

- `source_only`: observed in training, not converted into rule.
- `candidate`: converted into setup/exit/management parameters.
- `backtested`: replayed against market data.
- `validated`: statistically useful enough to enter the validation library.
- `rejected`: taught pattern did not correlate with market behavior under current tests.
