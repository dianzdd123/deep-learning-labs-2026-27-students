# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 2: Residual Networks and Controlled Comparison | Keras
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
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab2-resnet/lab2_resnet_keras.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab2-resnet/lab2_resnet_keras.ipynb)

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
# ## Exercise 1. Explore RGB images
# 
# Load CIFAR-10, inspect the image dimensions in your framework's axis order, normalise inputs and set up a fixed train/validation/test split.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
(x_pool, y_pool), (x_test, y_test) = keras.datasets.cifar10.load_data()
print(x_pool.shape, y_pool.shape, x_pool.min(), x_pool.max())
order = np.random.default_rng(seed).permutation(len(x_pool))
train_ids, val_ids = ...  # TODO: partition order into two disjoint index arrays.
# Scale all images consistently and add a channel axis for grayscale images.
x_train, y_train = ...
x_val, y_val = ...

# %% [markdown]
# ## Exercise 2. Plan a residual block
# 
# Draw the identity and residual paths. Specify when tensor shapes agree for addition and when a projection would be needed.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
x = keras.Input(shape=(32, 32, 16))
branch = layers.Conv2D(16, 3, padding="same")(x)
shortcut = ...  # TODO: choose a shape-compatible identity path.
print(branch.shape, shortcut.shape)

# %% [markdown]
# ## Exercise 3. Implement paired models
# 
# Create a compact plain block and matching residual block with identical convolution branches. Check parameter counts and dummy-batch output shapes.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
def make_model(use_skip):
    inputs = keras.Input(shape=(32, 32, 3))
    x = layers.Conv2D(16, 3, padding="same")(inputs)
    residual = ...  # TODO: apply the same convolution branch in both models.
    merged = ...  # condition addition on use_skip
    pooled = layers.GlobalAveragePooling2D()(merged)
    return keras.Model(inputs, layers.Dense(10)(pooled))

plain, residual = make_model(False), make_model(True)
print(plain.count_params(), residual.count_params())

# %% [markdown]
# ## Exercise 4. Train both fairly
# 
# Use the same split, optimiser, learning rate and epoch budget. Match compatible initial branch weights and batch order where possible. Plot validation performance; document remaining differences.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
results = {}
for name, net in [("plain", plain), ("residual", residual)]:
    # TODO: match initial branch weights and reset batch order before each fit.
    net.compile(optimizer="adam", loss=..., metrics=["accuracy"])
    results[name] = net.fit(x_train, y_train, epochs=3, validation_data=(x_val, y_val))
# Plot both validation curves with the same axes.

# %% [markdown]
# ## Exercise 5. Assess the evidence
# 
# Choose a model based on validation evidence; evaluate on the held-out set, inspect failures and discuss what extra seeds/depth would establish.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
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
# - Why is a shortcut impossible if channel counts differ without an additional projection?
# - Can a short single-seed run establish the superiority of a residual architecture?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
