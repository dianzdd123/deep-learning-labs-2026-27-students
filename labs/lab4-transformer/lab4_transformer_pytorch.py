# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 4: Transformer Encoder and Self-Attention | Pytorch
# 
# **Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**
# 
# **Lecturer:** Dr Dandan Zhang | **Formative, unmarked**
# 
# **Dataset:** Fashion-MNIST, 28 x 28 grayscale images
# 
# **Learning aim:** Trace patch tokens, positional embeddings and scaled dot-product attention.
# 
# **Student worksheet:** Replace each `...` and complete the TODOs before running that cell. Shape checks help you verify each step. Save your own Colab or Jupyter copy before editing. Do not confuse these teaching datasets with the graded tactile coursework.
# 
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab4-transformer/lab4_transformer_pytorch.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab4-transformer/lab4_transformer_pytorch.ipynb)

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
# ## Exercise 1. Inspect image patches
# 
# Divide each 28 x 28 image into non-overlapping 7 x 7 patches; derive 16 patch tokens containing 49 pixel values each.
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
def patchify(images):
    tiles = nn.functional.unfold(images, kernel_size=7, stride=7)
    return ...  # TODO: reorder (batch, 49, 16) to (batch, 16, 49).

# %% [markdown]
# ## Exercise 2. Implement token embeddings
# 
# Project each token into 32 features and add learnable position embeddings. Check that the position weights belong to the model and receive updates. Explain why position information is important.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
class Tokens(nn.Module):
    def __init__(self):
        super().__init__()
        self.project = nn.Linear(49, 32)
        self.position = ...  # TODO: register trainable (1, 16, 32) positions.

    def forward(self, images):
        projected = self.project(patchify(images))
        return ...  # combine projected tokens and positions

# %% [markdown]
# ## Exercise 3. Build encoder attention
# 
# Implement four-head scaled dot-product self-attention, a residual connection and feed-forward layers. Assert attention shape (batch, 4, 16, 16).
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = nn.MultiheadAttention(32, 4, batch_first=True)
        self.ff = ...  # TODO: feed-forward layers ending in 32 features

    def forward(self, tokens):
        context, weights = self.attn(tokens, tokens, tokens, average_attn_weights=False)
        assert weights.shape[1:] == (4, 16, 16)
        return ...  # add both residual connections

# %% [markdown]
# ## Exercise 4. Train a simple classifier
# 
# Pool encoder representations and predict ten class logits. Plot train and validation curves using a small, fixed budget.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
class PoolTokens(nn.Module):
    def forward(self, tokens):
        return ...  # TODO: pool the token axis and keep the features.

model = nn.Sequential(Tokens(), Encoder(), PoolTokens(), nn.Linear(32, 10))
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
# ## Exercise 5. Evaluate and critique
# 
# Use validation for one controlled modification, freeze your choices, then inspect held-out errors. Explain why the encoder is not a complete Seq2Seq translator or generative LLM.
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
# - Why can't a token's original position be inferred from its contents alone?
# - Why is an attention heatmap not automatically an explanation of a prediction?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
