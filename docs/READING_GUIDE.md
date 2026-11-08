# Reading guide: one useful question at a time

[Student home](../README.md) · [Glossary](GLOSSARY.md) · [Study guidance](STUDY_GUIDANCE.md)

Read a targeted section before a lab, then return to it with a question from your
experiment. You do not need to read every book or both frameworks' documentation.
The sequence and prompts below are teaching suggestions; the linked explanations
and original research belong to their respective authors.

## Core books

| Resource | Use it for |
|---|---|
| Simon J. D. Prince, [Understanding Deep Learning](https://udlbook.github.io/udlbook/) | Visual and conceptual explanations across model families |
| Zhang, Lipton, Li and Smola, [Dive into Deep Learning](https://d2l.ai/) | Worked mathematics and executable examples; focus on the relevant chapter |
| Goodfellow, Bengio and Courville, [Deep Learning](https://www.deeplearningbook.org/) | Deeper foundations and theoretical context |
| Deisenroth, Faisal and Ong, [Mathematics for Machine Learning](https://mml-book.github.io/) | Linear algebra, derivatives and probability preparation |

## Before and after each lab

| Stage | Start with | Read to answer | After your experiment |
|---|---|---|---|
| Preparation | [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) or [Keras guides](https://keras.io/guides/); relevant MML sections | What are a tensor, a gradient and a training loop? | Explain the interpreter, tensor axes and target dtype you used |
| CNN | D2L [convolutions for images](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html), plus padding/stride and pooling sections | How do local filters change output size? | Recalculate one layer's output shape and parameter count |
| ResNet | He et al., [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385); D2L [ResNet](https://d2l.ai/chapter_convolutional-modern/resnet.html) | What does the shortcut add to the computation? | Separate your observed result from the paper's much larger experiments |
| RNN | D2L [RNNs](https://d2l.ai/chapter_recurrent-neural-networks/rnn.html), [GRU](https://d2l.ai/chapter_recurrent-modern/gru.html), [LSTM](https://d2l.ai/chapter_recurrent-modern/lstm.html) | How do state updates and gates retain information? | Explain whether your task actually needs long-term memory |
| Transformer | Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762); D2L attention chapters | What do queries, keys, values, positions and masks do? | Explain why an image encoder is not a complete language generator |

Use the library API for implementation details, not a paper's notation alone:
[Keras layers](https://keras.io/api/layers/), [PyTorch neural-network modules](https://docs.pytorch.org/docs/stable/nn.html),
and [TensorFlow tutorials](https://www.tensorflow.org/tutorials).

## How to read a paper without getting lost

First identify its question and main claim. Then inspect the model/data diagram and
one experiment: what is controlled, what is measured, and what comparison supports
the claim? Finally trace the mathematics relevant to your lab. Write down one limit
on transferring the paper's conclusion to your own small experiment.

Do not copy a reported accuracy into your learning record as if you measured it.
Record which source helped, what you reused and what you independently checked.

**Next:** [Apply the lab workflow](LAB_WORKFLOW.md).
