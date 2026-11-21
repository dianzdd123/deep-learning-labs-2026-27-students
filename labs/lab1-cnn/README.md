# Lab 1: Convolutional Neural Networks

[Student home](../../README.md) · [Lab workflow](../../docs/LAB_WORKFLOW.md) · [Get help](../../docs/GETTING_HELP.md)

**Unmarked practice · Dr Dandan Zhang · Imperial I-X MSc AIAI**

Understand local convolution, pooling, weight sharing and image classification.

**Data:** Fashion-MNIST, 28 x 28 grayscale images and ten classes. Choose one framework for your first attempt.

| Framework | Notebook | Run online | Python worksheet |
|---|---|---|---|
| Keras 3 / TensorFlow | [View / download](lab1_cnn_keras.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_keras.ipynb) | [.py with VS Code cells](lab1_cnn_keras.py) |
| PyTorch | [View / download](lab1_cnn_pytorch.ipynb) | [Open in Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_pytorch.ipynb) | [.py with VS Code cells](lab1_cnn_pytorch.py) |

## Follow this order

1. Save a personal copy and check its kernel/framework.
2. Read all the tasks, then complete one guided cell at a time.
3. Check shapes on a tiny batch before training.
4. Use validation evidence to choose settings; freeze choices before the final held-out evaluation.
5. Restart and run from the top, then save your work and learning record.

Replace each `...` and complete the TODOs. The Python worksheet contains the same prompts and starter code as the notebook.

## Learning checkpoints

- Load public Fashion-MNIST, display five labelled images, scale pixel values appropriately and construct reproducible, disjoint training/validation/test splits.
- Write down input dimensions, expected convolution output dimensions, the effect of pooling and the final output shape (batch, 10).
- Create two convolution layers, nonlinearities, a pooling stage and a classification head. Print the parameter count; verify the shape of logits.
- Choose appropriate loss and optimiser for integer class labels; train for a small number of epochs, record training and validation curves.
- Use validation evidence for one controlled model change. Freeze your choices, then report held-out metrics, a confusion matrix and representative mistakes, if any.

## After the lab

Use the [learning log](../../docs/LEARNING_LOG.md) to explain measured results, representative errors and one limitation. Keep your implementation in your own files. This lab is not a coursework submission.
