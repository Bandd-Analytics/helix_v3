# MMM Rule Cards

Each card should be a concise, testable rule. Example schema:

Candidate cards extracted from the training transcripts live in
`candidate_rule_cards.md`. They must remain `candidate` until historical replay
validates the setup behavior.

```json
{
  "rule_id": "MMM-001",
  "title": "Example M/W stop-hunt reversal",
  "source_video": "video_001",
  "start_time": "00:00:00",
  "end_time": "00:00:00",
  "summary": "Paraphrased teaching goes here.",
  "timeframes": [
    "D1",
    "H4",
    "H1",
    "M15"
  ],
  "entry_conditions": [
    "Pair-specific Asian range is valid",
    "Stop hunt occurs beyond Asian range",
    "M/W formation confirms direction"
  ],
  "exit_conditions": [
    "T1 at 1R",
    "Trail after breakeven"
  ],
  "invalidation": [
    "Structural stop beyond setup"
  ],
  "visual_evidence": [],
  "validation_status": "candidate"
}
```
