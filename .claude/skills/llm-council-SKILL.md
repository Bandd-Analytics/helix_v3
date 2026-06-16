---
name: llm-council
description: >
  Run any question, idea, or decision through a council of 5 AI advisors who
  independently analyze it, peer-review each other anonymously, and synthesize a
  final verdict. Based on Karpathy's LLM Council methodology.
  MANDATORY TRIGGERS: 'council this', 'run the council', 'war room this',
  'pressure-test this', 'stress-test this', 'debate this'.
  STRONG TRIGGERS (use when combined with a real decision or tradeoff):
  'should I X or Y', 'which option', 'what would you do', 'is this the right move',
  'validate this', 'get multiple perspectives', "I can't decide", "I'm torn between".
  Do NOT trigger on simple yes/no questions, factual lookups, or casual 'should I'
  without a meaningful tradeoff. DO trigger when the user presents a genuine
  decision with stakes, multiple options, and context that suggests they want it
  pressure-tested from multiple angles.
---

# LLM Council

Ask one AI a question, get one answer. It might be great, it might be mid, and you
have no way to tell because you only saw one perspective.

The council fixes this. It runs your question through 5 independent advisors, each
thinking from a fundamentally different angle. They review each other's work. Then a
chairman synthesizes everything into a final recommendation that tells you where the
advisors agree, where they clash, and what to actually do.

Adapted from Andrej Karpathy's LLM Council (built by Ole Lehmann). Karpathy dispatches
queries to multiple models, has them peer-review each other anonymously, then a
chairman produces the final answer. This skill does the same thing inside Claude using
sub-agents with different thinking lenses instead of different models.

> Attribution: methodology — Andrej Karpathy; skill — Ole Lehmann
> (github.com/aiwithremy/claude-skills-llm-council). Check the repo's license before
> redistributing.

---

## When to run the council

For questions where being wrong is expensive.

Good council questions:
- "Should I launch a $97 workshop or a $497 course?"
- "Which of these 3 positioning angles is strongest?"
- "I'm thinking of pivoting from X to Y. Am I crazy?"
- "Here's my landing page copy. What's weak?"
- "Should I hire a VA or build an automation first?"

Bad council questions:
- "What's the capital of France?" (one right answer)
- "Write me a tweet" (creation task, not a decision)
- "Summarize this article" (processing task, not judgment)

The council shines when there's genuine uncertainty and the cost of a bad call is high.
If you already know the answer and just want validation, the council will likely tell
you things you don't want to hear. That's the point.

---

## The five advisors

Thinking styles, not job titles. Each leans fully into its angle and creates tension
with the others. They do not balance.

### 1. The Contrarian
Actively looks for what's wrong, what's missing, what will fail. Assumes the idea has a
fatal flaw and tries to find it. If everything looks solid, digs deeper. Not a
pessimist — the friend who saves you from a bad deal by asking the questions you're
avoiding.

### 2. The First Principles Thinker
Ignores the surface question and asks "what are we actually trying to solve here?"
Strips away assumptions. Rebuilds the problem from the ground up. Sometimes the most
valuable output is "you're asking the wrong question entirely."

### 3. The Expansionist
Looks for upside everyone else is missing. What could be bigger? What adjacent
opportunity is hiding? What's being undervalued? Doesn't care about risk (that's the
Contrarian's job) — cares about what happens if this works even better than expected.

### 4. The Outsider
Has zero context about you, your field, or your history. Responds purely to what's in
front of them. The most underrated advisor: experts develop blind spots, and the
Outsider catches the curse of knowledge — things obvious to you but confusing to
everyone else.

### 5. The Executor
Only cares about whether this can actually be done and the fastest path to doing it.
Ignores theory and big-picture thinking. Looks at every idea through "OK, but what do
you do Monday morning?" If an idea sounds brilliant but has no clear first step, says so.

**Why these five:** three natural tensions. Contrarian vs Expansionist (downside vs
upside). First Principles vs Executor (rethink everything vs just do it). The Outsider
sits in the middle, keeping everyone honest by seeing what fresh eyes see.

---

## How a council session works

### Step 1: Frame the question (with context enrichment)

When the user triggers the council, do two things before framing.

**A. Scan the workspace for context.** The user's question is usually the tip of the
iceberg. Before framing, quickly scan for and read relevant context files:
- `CLAUDE.md` / `claude.md` in the project root or workspace (business context,
  preferences, constraints)
- Any `memory/` folder (audience profiles, voice docs, business details, past decisions)
- Any files the user explicitly referenced or attached
- Recent council transcripts in this folder (avoid re-counciling the same ground)
- Any other context relevant to the specific question (e.g. for a pricing question,
  look for revenue data, past launch results, audience research)

Use quick file reads. Spend no more than ~30 seconds. You want the 2–3 files that let
advisors give specific, grounded advice instead of generic takes.

**B. Frame the question.** Take the user's raw question AND the enriched context and
rewrite it as a clear, neutral prompt all five advisors receive. Include:
1. The core decision or question
2. Key context from the user's message
3. Key context from workspace files (stage, audience, constraints, past results, numbers)
4. What's at stake (why this matters)

Don't add your own opinion. Don't steer it. But DO give each advisor enough context to
be specific rather than generic.

If the question is too vague ("council this: my business"), ask ONE clarifying question.
Just one. Then proceed. Save the framed question for the transcript.

### Step 2: Convene the council (5 sub-agents in parallel)

Spawn all 5 advisors simultaneously as sub-agents. Each gets: (1) their advisor
identity and thinking style, (2) the framed question, (3) the instruction to respond
independently, not hedge, not balance, and lean fully into their angle. 150–300 words
each — substantive but scannable.

**Sub-agent prompt template:**
```
You are [Advisor Name] on an LLM Council.

Your thinking style: [advisor description from above]

A user has brought this question to the council:

---
[framed question]
---

Respond from your perspective. Be direct and specific. Don't hedge or try to be
balanced. Lean fully into your assigned angle. The other advisors will cover the angles
you're not covering.

Keep your response between 150-300 words. No preamble. Go straight into your analysis.
```

### Step 3: Peer review (5 sub-agents in parallel)

The step that makes this more than "ask 5 times." Collect all 5 responses. Anonymize
them as Response A–E (randomize the mapping so there's no positional bias). Spawn 5 new
sub-agents; each reviewer sees all 5 anonymized responses and answers three questions.

**Reviewer prompt template:**
```
You are reviewing the outputs of an LLM Council. Five advisors independently answered
this question:

---
[framed question]
---

Here are their anonymized responses:

**Response A:**
[response]

**Response B:**
[response]

**Response C:**
[response]

**Response D:**
[response]

**Response E:**
[response]

Answer these three questions. Be specific. Reference responses by letter.

1. Which response is the strongest? Why?
2. Which response has the biggest blind spot? What is it missing?
3. What did ALL five responses miss that the council should consider?

Keep your review under 200 words. Be direct.
```

### Step 4: Chairman synthesis

One agent gets everything: the original question, all 5 advisor responses (now
de-anonymized so it can see who said what), and all 5 peer reviews.

**Chairman prompt template:**
```
You are the Chairman of an LLM Council. Your job is to synthesize the work of 5
advisors and their peer reviews into a final verdict.

The question brought to the council:
---
[framed question]
---

ADVISOR RESPONSES:

**The Contrarian:**
[response]

**The First Principles Thinker:**
[response]

**The Expansionist:**
[response]

**The Outsider:**
[response]

**The Executor:**
[response]

PEER REVIEWS:
[all 5 peer reviews]

Produce the council verdict using this exact structure:

## Where the Council Agrees
[Points multiple advisors converged on independently. High-confidence signals.]

## Where the Council Clashes
[Genuine disagreements. Present both sides. Explain why reasonable advisors disagree.]

## Blind Spots the Council Caught
[Things that only emerged through peer review. What individuals missed that others flagged.]

## The Recommendation
[A clear, direct recommendation. Not "it depends." A real answer with reasoning.
You may side with a minority advisor if their reasoning is strongest.]

## The One Thing to Do First
[A single concrete next step. Not a list. One thing.]

Be direct. Don't hedge. The whole point of the council is clarity the user couldn't get
from a single perspective.
```

### Step 5: Present the verdict in chat

Present the full verdict directly in chat as markdown. Do NOT generate an HTML report or
any files — the user reads it in the conversation. Keep it scannable; use bullets.

```
## Council Verdict: {short topic}

### Where the Council Agrees
{content}

### Where the Council Clashes
{content}

### Blind Spots the Council Caught
{content}

### The Recommendation
{content}

### The One Thing to Do First
{content}
```

### Step 6: Save the transcript (optional)

Only save a transcript if the user asks, or if the question is significant enough to
reference later. If saving, write to `council-transcript-[timestamp].md` in the
project's `active/` directory.

---

## Important notes

- **Always spawn all 5 advisors in parallel.** Sequential spawning wastes time and lets
  earlier responses bleed into later ones.
- **Always anonymize for peer review.** If reviewers know who said what, they defer to
  certain thinking styles instead of evaluating on merit.
- **The chairman can disagree with the majority.** If 4 of 5 say "do it" but the lone
  dissenter's reasoning is strongest, side with the dissenter and explain why.
- **Don't council trivial questions.** One-right-answer questions get a direct answer,
  not a council.
- **Output lives in chat, not a file.** (Resolves a contradiction in the original
  source, where the closing notes referenced an HTML report that Step 5 forbids.)
