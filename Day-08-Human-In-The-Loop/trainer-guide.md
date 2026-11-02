# Session 8 Trainer Guide — Human in the Loop

## Outcome

By the end of the session, a learner can run one file and explain how it helps them pause for a simple human decision.

## Files to Use

- `example.py` — the only required learner code file
- `slides.pptx` — the classroom deck
- `README.md` — the participant handout (objectives, concepts, code walkthrough, lab steps, and assignment)

Do not create a test folder or extra helper modules for this introductory lesson. Learners work only in `example.py`; the `bonus\` folder (chatbots with/without HITL, notebooks) is optional.

## Setup in Windows Command Prompt

From the repository root:

```cmd
uv sync
uv run python Day-08-Human-In-The-Loop\example.py
```

This example is deterministic and does not need a live model call. It still teaches a LangGraph building block.

## Day 8 Specific Notes

- Every run pauses: the graph always hits `interrupt` and waits. There is no risk classification and no low-risk bypass in this example.
- The learner types `yes` or `no` at the Command Prompt `input` prompt; any answer other than `yes` counts as rejection.
- After the pause, the second `invoke` resumes the same `thread_id` (`approval-1`) with `Command(resume=True/False)`. Changing the thread ID would lose the paused state.
- Run it twice, once with `yes` (prints `Action completed.`) and once with `no` (prints `Action cancelled.`).

## Suggested 120-Minute Flow

1. **10 minutes — Predict:** Show the graph picture and ask learners what will happen.
2. **25 minutes — Teach:** Explain the one session concept in plain language.
3. **30 minutes — Read:** Walk through `example.py` from top to bottom.
4. **25 minutes — Run:** Execute the file in Windows Command Prompt and trace the state.
5. **20 minutes — Change:** Let learners change one sample input near the bottom of the file.
6. **10 minutes — Explain:** Ask learners to describe the input, nodes, route, and output.

## Code Walkthrough Questions

1. What value enters the graph?
2. What does each node return?
3. Is the next step fixed, rule-based, or model-selected?
4. What value is printed at the end?
5. What one safe input change can we try?

## Common Mistakes

- Running the command from the wrong folder
- Reading every line at once instead of following the graph order
- Changing the graph and the input at the same time
- Confusing a normal Python function with a model decision
- Adding framework helpers that are not used in `example.py`

## Exit Check

The learner should be able to point to the start, each node, the route, the end, and the printed result. For Session 6 and later agent examples, also ask who chooses the next action and how that choice is limited.
