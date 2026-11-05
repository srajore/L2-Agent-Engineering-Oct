# Session 9 Trainer Guide — RAG Engineering

## Outcome

By the end of the session, a learner can run one file and explain how it helps them retrieve one local fact before model generation.

## Files to Use

- `example.py` — the only required learner code file
- `slides.pptx` — the classroom deck
- `README.md` — the participant handout (objectives, concepts, code walkthrough, lab steps, and assignment)

Do not create a test folder or extra helper modules for this introductory lesson. Learners work only in `example.py`; the notebooks and docs in `bonus\` are optional.

## Setup in Windows Command Prompt

From the repository root (run `ollama signin` once first; this day calls the model):

```cmd
uv sync
ollama signin
uv run python Day-09-RAG-Engineering\example.py
```

This example calls `ollama.chat` with the fixed model `gpt-oss:120b-cloud`, so `ollama signin` is required. Keep that model name unchanged. Note: on a keyword miss the context is `No matching article found.` and the model is still called; there are no citations.

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
