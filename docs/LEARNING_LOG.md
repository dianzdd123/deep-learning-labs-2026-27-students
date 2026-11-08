# My lab learning record

[Student home](../README.md) · [Lab workflow](LAB_WORKFLOW.md)

Copy this template into your personal notes. Replace bracketed prompts with your
own observations. This is a practice aid, not an assessed report template.

## Question and prediction

- Lab / date: [ ]
- My question: [one testable question]
- Before running, I expect: [prediction and reasoning]

## Reproducible settings

| Item | My actual setting |
|---|---|
| Framework / version / Python | [ ] |
| Environment and device | [Colab or local; CPU or GPU] |
| Dataset and preprocessing | [source, scale, transformations] |
| Split sizes and grouping rule | [train / validation / test; correlated samples] |
| Seed | [ ] |
| Model and trainable parameter count | [ ] |
| Loss and target representation | [ ] |
| Optimiser and learning rate | [ ] |
| Epochs and batch size | [ ] |
| Model-selection rule and saved weights | [final epoch, or restored checkpoint] |

## Shape explanation

Input: [ ]. Important intermediate tensor: [ ]. Output: [ ]. Target: [ ].
One reason these dimensions are appropriate: [ ].

## Controlled comparison

| Run | The one factor changed | Validation evidence | Training time / other cost |
|---|---|---|---|
| Baseline | — | [measured value or observation] | [ ] |
| Comparison | [ ] | [ ] | [ ] |

What I held fixed: [ ]. Remaining differences or confounders: [ ].

## Final evaluation

Choices were frozen before test evaluation: [describe].
Held-out result, if evaluated: [metric, sample count and selected weights].
Representative mistakes, if any: [example, prediction, target and possible explanation].
If none were observed, state the sample count and that result; do not invent errors.
A result I did not expect: [ ].

## Reflection and files

- What the evidence supports: [ ]
- What it does not establish: [ ]
- One concept I can now explain: [ ]
- One unresolved question / next experiment: [ ]
- Saved notebook/script and result filenames: [ ]
- Sources or AI assistance used, and how I checked them: [ ]

Keep failed runs when they inform your explanation. Do not invent a result to fill
an empty table. For assessed work, use the official Canvas requirements instead.
