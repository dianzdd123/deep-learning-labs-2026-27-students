# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 3: Recurrent Neural Networks, GRU and LSTM | Pytorch
# 
# **Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**
# 
# **Lecturer:** Dr Dandan Zhang | **Formative, unmarked**
# 
# **Dataset:** Synthetic increasing sequences and their reversed counterparts
# 
# **Learning aim:** Explain recurrent state, gating and why sequence order matters.
# 
# **Student worksheet:** Replace each `...` and complete the TODOs before running that cell. Shape checks help you verify each step. Save your own Colab or Jupyter copy before editing. Do not confuse these teaching datasets with the graded tactile coursework.
# 
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab3-rnn/lab3_rnn_pytorch.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab3-rnn/lab3_rnn_pytorch.ipynb)

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
# ## Exercise 1. Create an order-sensitive task
# 
# Generate paired ordered and reversed sequences using the same values; plot an example and verify both have the same mean.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Use batch_first=True where appropriate; hidden-state layout is a separate contract.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
rng = np.random.default_rng(seed)
ordered = np.sort(rng.normal(size=(1000, 12)), axis=1).astype("float32")
reversed_sequences = ...  # TODO: reverse the time axis within each row.
pair_ids = np.arange(len(ordered))
assert np.allclose(ordered.mean(axis=1), reversed_sequences.mean(axis=1))
# Plot both sequences for a single pair ID.

# %% [markdown]
# ## Exercise 2. Prevent paired leakage
# 
# Assign entire source-sequence pairs to train/validation/test splits; document why splitting individual sequence copies would be misleading.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Use batch_first=True where appropriate; hidden-state layout is a separate contract.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
ids = rng.permutation(pair_ids)
train_ids, val_ids, test_ids = ...  # TODO: split IDs before expanding pairs.
assert not (set(train_ids) & set(val_ids))

def expand(ids):
    sequences = np.concatenate([ordered[ids], reversed_sequences[ids]])
    labels = ...  # align one integer label with each sequence
    return sequences[..., None], labels

x_train, y_train = expand(train_ids)
x_val, y_val = expand(val_ids)
x_test, y_test = expand(test_ids)

# %% [markdown]
# ## Exercise 3. Implement three recurrent models
# 
# Implement RNN, GRU and LSTM classifiers with matching hidden sizes and two-class logits. Trace shapes at every timestep.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Use batch_first=True where appropriate; hidden-state layout is a separate contract.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
class SequenceClassifier(nn.Module):
    def __init__(self, cell):
        super().__init__()
        self.encoder = cell(1, 32, batch_first=True)
        self.head = nn.Linear(32, 2)

    def forward(self, x):
        outputs, state = self.encoder(x)
        last = ...  # TODO: select final timestep from outputs (batch, time, hidden).
        return self.head(last)

models = {cell.__name__: SequenceClassifier(cell) for cell in [nn.RNN, nn.GRU, nn.LSTM]}

# %% [markdown]
# ## Exercise 4. Compare training behaviour
# 
# Use the same split, optimiser and training budget; report parameters and validation evidence. Consider a simple order-sensitive baseline before claiming a need for long-term memory.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Use batch_first=True where appropriate; hidden-state layout is a separate contract.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
from torch.utils.data import TensorDataset
def loader(x, y, shuffle=False):
    dataset = TensorDataset(torch.as_tensor(x).float(), torch.as_tensor(y).long())
    return DataLoader(dataset, batch_size=32, shuffle=shuffle)

test_loader = loader(x_test, y_test)
scores = {}
for name, net in models.items():
    # TODO: train on loader(x_train, y_train, True); evaluate on loader(x_val, y_val).
    scores[name] = ...  # record validation accuracy for the saved weights
# Compare against an endpoint-difference baseline.

# %% [markdown]
# ## Exercise 5. Check failure modes
# 
# Select using validation results belonging to the saved weights you will evaluate; inspect held-out errors and explain padding/masking for variable length.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Use batch_first=True where appropriate; hidden-state layout is a separate contract.
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
# - Why is an order-blind average insufficient for this task?
# - How do recurrent gates influence retention of state?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
