# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 2: Residual Networks and Controlled Comparison | Pytorch
# 
# **Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**
# 
# **Lecturer:** Dr Dandan Zhang | **Formative, unmarked**
# 
# **Dataset:** CIFAR-10, 32 x 32 RGB images and ten classes
# 
# **Learning aim:** Understand y = F(x) + x and the effect of an identity shortcut.
# 
# **Student worksheet:** Replace each `...` and complete the TODOs before running that cell. Shape checks help you verify each step. Save your own Colab or Jupyter copy before editing. Do not confuse these teaching datasets with the graded tactile coursework.
# 
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab2-resnet/lab2_resnet_pytorch.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab2-resnet/lab2_resnet_pytorch.ipynb)

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
# ## Exercise 1. Explore RGB images
# 
# Load CIFAR-10, inspect the image dimensions in your framework's axis order, normalise inputs and set up a fixed train/validation/test split.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
from torchvision import datasets, transforms
transform = transforms.ToTensor()
pool = datasets.CIFAR10("data", train=True, download=True, transform=transform)
test = datasets.CIFAR10("data", train=False, download=True, transform=transform)
print(pool[0][0].shape, pool[0][1])
split_lengths = ...  # TODO: reserve validation examples from pool.
train, val = random_split(pool, split_lengths, generator=torch.Generator().manual_seed(seed))
# Build train_loader, val_loader and test_loader. Shuffle only training examples.

# %% [markdown]
# ## Exercise 2. Plan a residual block
# 
# Draw the identity and residual paths. Specify when tensor shapes agree for addition and when a projection would be needed.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
x = torch.zeros(2, 16, 32, 32)
branch = nn.Conv2d(16, 16, 3, padding=1)(x)
shortcut = ...  # TODO: choose the identity tensor; predict what stride 2 changes.
assert branch.shape == shortcut.shape

# %% [markdown]
# ## Exercise 3. Implement paired models
# 
# Create a compact plain block and matching residual block with identical convolution branches. Check parameter counts and dummy-batch output shapes.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
class Block(nn.Module):
    def __init__(self, use_skip):
        super().__init__()
        self.use_skip = use_skip
        self.branch = ...  # TODO: shape-preserving convolution branch

    def forward(self, x):
        residual = self.branch(x)
        return ...  # condition addition on self.use_skip

def make_model(use_skip):
    return nn.Sequential(nn.Conv2d(3, 16, 3, padding=1), Block(use_skip),
                         nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(16, 10))
plain, residual = make_model(False), make_model(True)
# Compare parameter counts and run a dummy RGB batch.

# %% [markdown]
# ## Exercise 4. Train both fairly
# 
# Use the same split, optimiser, learning rate and epoch budget. Match compatible initial branch weights and batch order where possible. Plot validation performance; document remaining differences.
# 
# **Framework hint:** Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
results = {}
for name, net in [("plain", plain), ("residual", residual)]:
    net = net.to(device)
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
    # TODO: match initial weights and reset loader order before each run.
    results[name] = ...  # train for three epochs; store validation curves and weights
# Compare validation accuracy at matched epochs.

# %% [markdown]
# ## Exercise 5. Assess the evidence
# 
# Choose a model based on validation evidence; evaluate on the held-out set, inspect failures and discuss what extra seeds/depth would establish.
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
# - Why is a shortcut impossible if channel counts differ without an additional projection?
# - Can a short single-seed run establish the superiority of a residual architecture?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
