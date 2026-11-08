# A practical workflow for every lab

[Student home](../README.md) · [Notebook basics](NOTEBOOK_BASICS.md) · [Learning log](LEARNING_LOG.md)

Use this page alongside the released worksheet. Suggested timings below organise a
first study session; they are not the official session length or assessment criteria.

## Before coding: know the question

Allow about 10 minutes to read the aim, inspect the task and write a prediction.
Identify what goes into the model, what it should produce and what evidence would
support your claim. Select one framework and read one targeted source from the
[reading guide](READING_GUIDE.md).

| Lab | Main idea | Be able to explain |
|---|---|---|
| CNN | Local filters and shared weights | How a layer changes image dimensions and parameter count |
| ResNet | A residual branch plus a shortcut | Why shapes must agree for addition, and what a fair comparison holds fixed |
| RNN | Recurrent state and gating | How time order changes the information available to a model |
| Transformer | Tokens, positions and attention | What the query, key and value dimensions mean |

## Work through five checkpoints

### 1. Data — about 10 minutes

Inspect several samples and labels. Record source, scale, class meanings and split
sizes. Keep correlated examples in the same split. Do not decide settings from test
results. For the RNN task, whole source-sequence pairs belong in one split.

**Check:** you can explain one example and why the split is appropriate.

### 2. Shapes — about 10 minutes

Write the input, intermediate and output dimensions before training. Use a tiny
batch and print shapes. For images, verify whether the channel axis is first or
last. For sequences, identify batch, time and feature axes.

**Check:** the model output and target representation match the chosen loss.

### 3. Baseline — about 15–25 minutes

Start with a small data subset and short training budget. Record seed, optimiser,
learning rate, batch size, epoch count and parameter count. Observe loss/validation
trends. A failed run is useful evidence when its cause is understood.

**Check:** parameters actually update, losses are finite and validation does not
update model weights. Explain what train/evaluation mode changes in your framework.

### 4. Controlled investigation — about 15–25 minutes

Write one question and change one factor. Hold the data split and training budget
fixed where possible. Compare validation behaviour and computational cost. Report
when architectures differ in parameter count or optimisation details.

Select the candidate using validation evidence. If using an earlier epoch's score,
restore the corresponding saved weights before evaluating it. Otherwise use the
score belonging to the final weights you actually kept.

**Check:** you can say what changed, what stayed fixed and what limits the comparison.

### 5. Final evaluation and reflection — about 10–15 minutes

Freeze the choices before the held-out evaluation. Report the metric and inspect
representative failures. Do not tune again in response to the test score and then
present that same set as untouched evidence. Save the notebook, results and a short
[learning log](LEARNING_LOG.md).

**Check:** you can explain an observed outcome, a limitation and a sensible next investigation.

## What counts as a useful completed practice session?

- [ ] My own code runs from the top after a kernel restart.
- [ ] I can explain the important tensor dimensions and loss/target pairing.
- [ ] My data split and model-selection procedure are written down.
- [ ] I recorded measured results, not example numbers from a guide or AI output.
- [ ] I investigated one controlled question and explained the limits of the evidence.
- [ ] My files are saved and I know which questions still need help.

These are **learning checkpoints**, not a marking rubric or a submission requirement.
If you cannot finish, record the last checkpoint reached and a focused question.

## Avoid three misleading conclusions

A short run on a small subset does not rank architectures universally. A higher
score can come from a changed split, budget or preprocessing. A visually appealing
plot does not establish reliability: include failed runs and uncertainty where relevant.

For the sequence direction task, consider a simple order-sensitive baseline before
concluding that long-term memory is necessary. For attention, explain the axes of a
heatmap before interpreting its colours as meaningful evidence.

**Next:** [Save a learning record](LEARNING_LOG.md) or [ask for help](GETTING_HELP.md).
