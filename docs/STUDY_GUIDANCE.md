# How to learn effectively in the four deep learning labs

**Deep Learning 2026–2027 | Dr Dandan Zhang**

The point of a laboratory session is not simply to make a notebook run. It is to understand why a model is structured as it is, what evidence its behaviour provides and how to diagnose an unreliable result.

## A repeatable learning cycle

1. **Predict:** Write down the input and output shapes, the learning task, the proposed loss and one potential failure mode **before** executing your code.
2. **Implement:** Complete the blank cells yourself. Work through the model one layer or operation at a time; inspect shapes and parameters.
3. **Test:** Establish a small baseline. Use a fixed seed, train/validation/test separation and a controlled training budget.
4. **Diagnose:** Examine training curves and class-specific or task-specific errors. A single high accuracy number is rarely sufficient.
5. **Explain and improve:** Change one factor, justify the change and describe what your results do and do not establish.

## What each lab adds

| Lab | Main question | Evidence to collect |
|---|---|---|
| CNN | How do local filters exploit image structure? | Convolution shape trace, learning curves and confusion matrix |
| ResNet | What changes when an identity shortcut is added? | Matched plain-versus-residual comparison, parameters and validation trends |
| RNN | What can a recurrent state capture that an average cannot? | Ordering experiment, RNN/GRU/LSTM comparison and error analysis |
| Transformer | How do tokens exchange information through attention? | Patch count, Q/K/V and attention dimensions, encoder output and validation evidence |

**Mind the limits of the exercises:** small datasets and short runs help you learn a technique. They do not support claims of state-of-the-art performance, superior generalisation under other conditions or successful deployment to a real tactile sensor.

## Using AI to learn rather than bypass learning

AI tools may help you interpret an error, locate relevant documentation or identify a flawed assumption. They can also produce plausible-looking code or explanations that do not match your actual experiment.

Before accepting an AI suggestion, ask yourself:

- Can I explain each important tensor shape and model decision without the tool?
- Does the proposed loss function match the target representation?
- Have I checked the suggested API against current Keras or PyTorch documentation?
- Did I actually run the code and obtain the metrics shown?
- Are training, validation and test data properly separated?
- Can I explain a failure case, rather than only showing a successful example?

For **assessed coursework**, the official module AI-use policy applies. Do not use this formative guidance as permission to delegate assessed work to AI. Consult Canvas for required declarations and restrictions.

## Your lab notes: a useful one-page record

Write a short record after each session containing: **objective; framework and versions; dataset; split and seed; model and parameter count; training budget; validation results; held-out results; observed errors; what you learned; what remains uncertain**.

Readings: [Keras Guides](https://keras.io/guides/), [PyTorch Tutorials](https://pytorch.org/tutorials/), [Dive into Deep Learning](https://d2l.ai/), [Attention Is All You Need](https://arxiv.org/abs/1706.03762).


## Continue with a practical guide

[Lab workflow](LAB_WORKFLOW.md) · [Learning-log template](LEARNING_LOG.md) · [Reading guide](READING_GUIDE.md) · [Glossary](GLOSSARY.md) · [Get help](GETTING_HELP.md).
