# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 3: Recurrent Neural Networks, GRU and LSTM | Keras
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
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab3-rnn/lab3_rnn_keras.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab3-rnn/lab3_rnn_keras.ipynb)

# %% [markdown]
# ## Framework and reproducibility
# 
# **Chosen framework:** Keras 3 with TensorFlow backend.
# 
# Before training: inspect your Python/framework version, choose CPU or available GPU, set a random seed, and write down the dataset split and intended metrics. Run the starter imports and record your settings below.

# %%
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

seed = 42
keras.utils.set_random_seed(seed)
print(tf.__version__, tf.config.list_physical_devices("GPU"))
# TODO: record your device and choose the validation metric.
validation_metric = ...

# %% [markdown]
# ## Exercise 1. Create an order-sensitive task
# 
# Generate paired ordered and reversed sequences using the same values; plot an example and verify both have the same mean.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Read the Keras recurrent-layer return options.
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
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Read the Keras recurrent-layer return options.
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
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Read the Keras recurrent-layer return options.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
def build(cell):
    inputs = keras.Input(shape=x_train.shape[1:])
    hidden = ...  # TODO: apply cell with 32 hidden units; keep the last output.
    return keras.Model(inputs, layers.Dense(2)(hidden))

models = {cell.__name__: build(cell) for cell in [layers.SimpleRNN, layers.GRU, layers.LSTM]}
# Check each model on two samples.

# %% [markdown]
# ## Exercise 4. Compare training behaviour
# 
# Use the same split, optimiser and training budget; report parameters and validation evidence. Consider a simple order-sensitive baseline before claiming a need for long-term memory.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Read the Keras recurrent-layer return options.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
scores = {}
for name, model in models.items():
    model.compile(optimizer="adam", loss=..., metrics=["accuracy"])  # TODO: configure logits loss.
    history = model.fit(x_train, y_train, epochs=3, validation_data=(x_val, y_val))
    scores[name] = history.history["val_accuracy"][-1]
# Compare final weights at the same epoch and an endpoint-difference baseline.

# %% [markdown]
# ## Exercise 5. Check failure modes
# 
# Select using validation results belonging to the saved weights you will evaluate; inspect held-out errors and explain padding/masking for variable length.
# 
# **Framework hint:** Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. Read the Keras recurrent-layer return options.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
# TODO: choose weights using validation results, then freeze the model.
final_model = ...
logits = final_model.predict(x_test, verbose=0)
predicted = ...  # Pick one class per example.
truth = np.asarray(y_test).reshape(-1)
print(tf.math.confusion_matrix(truth, predicted))
# Locate misclassified indices and inspect examples.

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
