# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 1: Convolutional Neural Networks | Pytorch
# 
# **Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**
# 
# **Lecturer:** Dr Dandan Zhang | **Formative, unmarked**
# 
# **Dataset:** Fashion-MNIST, 28 x 28 grayscale images and ten classes
# 
# **Learning aim:** Understand local convolution, pooling, weight sharing and image classification.
# 
# **Student worksheet:** Replace each `...` and complete the TODOs before running that cell. Shape checks help you verify each step. Save your own Colab or Jupyter copy before editing. Do not confuse these teaching datasets with the graded tactile coursework.
# 
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_pytorch.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_pytorch.ipynb)

# %% [markdown]
# ## Framework and reproducibility
# 
# **Chosen framework:** PyTorch and torchvision (where relevant).
# 
# Before training: inspect your Python/framework version, choose CPU or available GPU, set a random seed, and write down the dataset split and intended metrics. Run the starter imports and record your settings below.

# %%
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader, random_split

seed = 42
torch.manual_seed(seed)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(torch.__version__, device)
# TODO: record your device and choose the validation metric.
validation_metric = ...

# %% [markdown]
# ## Exercise 1. Inspect the data
# 
# Load public Fashion-MNIST, display five labelled images, scale pixel values appropriately and construct reproducible, disjoint training/validation/test splits.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
from torchvision import datasets, transforms
transform = transforms.ToTensor()
pool = datasets.FashionMNIST("data", train=True, download=True, transform=transform)
test = datasets.FashionMNIST("data", train=False, download=True, transform=transform)
print(pool[0][0].shape, pool[0][1])
split_lengths = ...  # TODO: reserve validation examples from pool.
train, val = random_split(pool, split_lengths, generator=torch.Generator().manual_seed(seed))
# Build train_loader, val_loader and test_loader. Shuffle only training examples.

# %% [markdown]
# ## Exercise 2. Plan the tensor shapes
# 
# Write down input dimensions, expected convolution output dimensions, the effect of pooling and the final output shape (batch, 10).
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
batch, _ = next(iter(train_loader))
features = nn.Conv2d(1, 16, 3, padding=1)(batch)
pooled = ...  # TODO: apply 2 x 2 pooling.
print(batch.shape, features.shape, pooled.shape)

# %% [markdown]
# ## Exercise 3. Implement a small CNN
# 
# Create two convolution layers, nonlinearities, a pooling stage and a classification head. Print the parameter count; verify the shape of logits.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
model = nn.Sequential(
    nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(),
    ...,  # TODO: pooling, second convolution and nonlinearity
    nn.Flatten(),
    ...,  # map flattened features to ten logits
)
assert model(batch[:2]).shape == (2, 10)
print(sum(p.numel() for p in model.parameters()))

# %% [markdown]
# ## Exercise 4. Fit a baseline
# 
# Choose appropriate loss and optimiser for integer class labels; train for a small number of epochs, record training and validation curves.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
epochs = 3
model = model.to(device)
optimizer = torch.optim.Adam(model.parameters())
criterion = ...  # TODO: choose a loss for integer labels and raw logits.
for epoch in range(epochs):
    model.train()
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        logits = model(inputs)
        loss = ...
        # TODO: backpropagate and update parameters.
    # Evaluate val_loader with model.eval() and no_grad(); record both curves.

# %% [markdown]
# ## Exercise 5. Evaluate and explain
# 
# Use validation evidence for one controlled model change. Freeze your choices, then report held-out metrics, a confusion matrix and representative mistakes, if any.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
final_model = ...  # TODO: load the weights chosen on validation data.
final_model.eval()
predicted, truth = [], []
with torch.no_grad():
    for inputs, labels in test_loader:
        logits = final_model(inputs.to(device))
        batch_classes = ...  # Pick one class index per example.
        predicted.extend(batch_classes.cpu().tolist())
        truth.extend(labels.tolist())
# Compute accuracy, build a confusion matrix and inspect mistakes.

# %% [markdown]
# ## Help while you work
# 
# [Lab workflow](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/LAB_WORKFLOW.md) · [Troubleshooting](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/TROUBLESHOOTING.md) · [Learning-log template](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/LEARNING_LOG.md)

# %% [markdown]
# ## Reflection and learning record
# 
# - Why do shared local filters require fewer parameters than an equally expressive dense mapping?
# - Why should the test set not be used to select an architecture?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
