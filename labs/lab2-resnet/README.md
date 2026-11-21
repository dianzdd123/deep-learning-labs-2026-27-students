# Lab 2: Residual Networks and Controlled Comparison

[Student home](../../README.md) · [Lab workflow](../../docs/LAB_WORKFLOW.md) · [Get help](../../docs/GETTING_HELP.md)

**Unmarked practice · Dr Dandan Zhang · Imperial I-X MSc AIAI**

Understand y = F(x) + x and the effect of an identity shortcut.

**Data:** CIFAR-10, 32 x 32 RGB images and ten classes. Choose one framework for your first attempt.

| Framework | Notebook | Run online | Python worksheet |
|---|---|---|---|
| Keras 3 / TensorFlow | [View / download](lab2_resnet_keras.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab2-resnet/lab2_resnet_keras.ipynb) | [.py with VS Code cells](lab2_resnet_keras.py) |
| PyTorch | [View / download](lab2_resnet_pytorch.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab2-resnet/lab2_resnet_pytorch.ipynb) | [.py with VS Code cells](lab2_resnet_pytorch.py) |

## Follow this order

1. Save a personal copy and check its kernel/framework.
2. Read all the tasks, then complete one guided cell at a time.
3. Check shapes on a tiny batch before training.
4. Use validation evidence to choose settings; freeze choices before the final held-out evaluation.
5. Restart and run from the top, then save your work and learning record.

Replace each `...` and complete the TODOs. The Python worksheet contains the same prompts and starter code as the notebook.

## Learning checkpoints

- Load CIFAR-10, inspect the image dimensions in your framework's axis order, normalise inputs and set up a fixed train/validation/test split.
- Draw the identity and residual paths. Specify when tensor shapes agree for addition and when a projection would be needed.
- Create a compact plain block and matching residual block with identical convolution branches. Check parameter counts and dummy-batch output shapes.
- Use the same split, optimiser, learning rate and epoch budget. Match compatible initial branch weights and batch order where possible. Plot validation performance; document remaining differences.
- Choose a model based on validation evidence; evaluate on the held-out set, inspect failures and discuss what extra seeds/depth would establish.

## After the lab

Use the [learning log](../../docs/LEARNING_LOG.md) to explain measured results, representative errors and one limitation. Keep your implementation in your own files. This lab is not a coursework submission.
