# Lab 4: Transformer Encoder and Self-Attention

[Student home](../../README.md) · [Lab workflow](../../docs/LAB_WORKFLOW.md) · [Get help](../../docs/GETTING_HELP.md)

**Unmarked practice · Dr Dandan Zhang · Imperial I-X MSc AIAI**

Trace patch tokens, positional embeddings and scaled dot-product attention.

**Data:** Fashion-MNIST, 28 x 28 grayscale images. Choose one framework for your first attempt.

| Framework | Notebook | Run online | Python worksheet |
|---|---|---|---|
| Keras 3 / TensorFlow | [View / download](lab4_transformer_keras.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab4-transformer/lab4_transformer_keras.ipynb) | [.py with VS Code cells](lab4_transformer_keras.py) |
| PyTorch | [View / download](lab4_transformer_pytorch.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab4-transformer/lab4_transformer_pytorch.ipynb) | [.py with VS Code cells](lab4_transformer_pytorch.py) |

## Follow this order

1. Save a personal copy and check its kernel/framework.
2. Read all the tasks, then complete one guided cell at a time.
3. Check shapes on a tiny batch before training.
4. Use validation evidence to choose settings; freeze choices before the final held-out evaluation.
5. Restart and run from the top, then save your work and learning record.

Replace each `...` and complete the TODOs. The Python worksheet contains the same prompts and starter code as the notebook.

## Learning checkpoints

- Divide each 28 x 28 image into non-overlapping 7 x 7 patches; derive 16 patch tokens containing 49 pixel values each.
- Project each token into 32 features and add learnable position embeddings. Check that the position weights belong to the model and receive updates. Explain why position information is important.
- Implement four-head scaled dot-product self-attention, a residual connection and feed-forward layers. Assert attention shape (batch, 4, 16, 16).
- Pool encoder representations and predict ten class logits. Plot train and validation curves using a small, fixed budget.
- Use validation for one controlled modification, freeze your choices, then inspect held-out errors. Explain why the encoder is not a complete Seq2Seq translator or generative LLM.

## After the lab

Use the [learning log](../../docs/LEARNING_LOG.md) to explain measured results, representative errors and one limitation. Keep your implementation in your own files. This lab is not a coursework submission.
