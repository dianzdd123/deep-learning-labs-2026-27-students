# Lab 3: Recurrent Neural Networks, GRU and LSTM

[Student home](../../README.md) · [Lab workflow](../../docs/LAB_WORKFLOW.md) · [Get help](../../docs/GETTING_HELP.md)

**Unmarked practice · Dr Dandan Zhang · Imperial I-X MSc AIAI**

Explain recurrent state, gating and why sequence order matters.

**Data:** Synthetic increasing sequences and their reversed counterparts. Choose one framework for your first attempt.

| Framework | Notebook | Run online | Python worksheet |
|---|---|---|---|
| Keras 3 / TensorFlow | [View / download](lab3_rnn_keras.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab3-rnn/lab3_rnn_keras.ipynb) | [.py with VS Code cells](lab3_rnn_keras.py) |
| PyTorch | [View / download](lab3_rnn_pytorch.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab3-rnn/lab3_rnn_pytorch.ipynb) | [.py with VS Code cells](lab3_rnn_pytorch.py) |

## Follow this order

1. Save a personal copy and check its kernel/framework.
2. Read all the tasks, then complete one guided cell at a time.
3. Check shapes on a tiny batch before training.
4. Use validation evidence to choose settings; freeze choices before the final held-out evaluation.
5. Restart and run from the top, then save your work and learning record.

Replace each `...` and complete the TODOs. The Python worksheet contains the same prompts and starter code as the notebook.

## Learning checkpoints

- Generate paired ordered and reversed sequences using the same values; plot an example and verify both have the same mean.
- Assign entire source-sequence pairs to train/validation/test splits; document why splitting individual sequence copies would be misleading.
- Implement RNN, GRU and LSTM classifiers with matching hidden sizes and two-class logits. Trace shapes at every timestep.
- Use the same split, optimiser and training budget; report parameters and validation evidence. Consider a simple order-sensitive baseline before claiming a need for long-term memory.
- Select using validation results belonging to the saved weights you will evaluate; inspect held-out errors and explain padding/masking for variable length.

## After the lab

Use the [learning log](../../docs/LEARNING_LOG.md) to explain measured results, representative errors and one limitation. Keep your implementation in your own files. This lab is not a coursework submission.
