# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 1: Convolutional Neural Networks | Keras
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
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_keras.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_keras.ipynb)

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
# ## Exercise 1. Inspect the data
# 
# Load public Fashion-MNIST, display five labelled images, scale pixel values appropriately and construct reproducible, disjoint training/validation/test splits.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
(x_pool, y_pool), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
print(x_pool.shape, y_pool.shape, x_pool.min(), x_pool.max())
order = np.random.default_rng(seed).permutation(len(x_pool))
train_ids, val_ids = ...  # TODO: partition order into two disjoint index arrays.
# Scale all images consistently and add a channel axis for grayscale images.
x_train, y_train = ...
x_val, y_val = ...

# %% [markdown]
# ## Exercise 2. Plan the tensor shapes
# 
# Write down input dimensions, expected convolution output dimensions, the effect of pooling and the final output shape (batch, 10).
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
sample_shape = x_train.shape[1:]
probe = layers.Conv2D(16, 3, padding="same")
features = probe(x_train[:2])
pooled = ...  # TODO: apply 2 x 2 pooling and predict the resulting dimensions.
print(sample_shape, features.shape, pooled.shape)

# %% [markdown]
# ## Exercise 3. Implement a small CNN
# 
# Create two convolution layers, nonlinearities, a pooling stage and a classification head. Print the parameter count; verify the shape of logits.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
model = keras.Sequential([
    keras.Input(shape=sample_shape),
    layers.Conv2D(16, 3, padding="same", activation="relu"),
    ...,  # TODO: pooling and a second convolution with activation
    layers.Flatten(),
    ...,  # ten raw class scores
])
model.summary()
assert model(x_train[:2]).shape == (2, 10)

# %% [markdown]
# ## Exercise 4. Fit a baseline
# 
# Choose appropriate loss and optimiser for integer class labels; train for a small number of epochs, record training and validation curves.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
epochs = 3
model.compile(optimizer="adam", loss=..., metrics=["accuracy"])  # TODO: integer labels and logits.
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=epochs)
plt.plot(history.history["val_accuracy"])
# Add a labelled training curve and inspect the gap.

# %% [markdown]
# ## Exercise 5. Evaluate and explain
# 
# Use validation evidence for one controlled model change. Freeze your choices, then report held-out metrics, a confusion matrix and representative mistakes, if any.
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
# - Why do shared local filters require fewer parameters than an equally expressive dense mapping?
# - Why should the test set not be used to select an architecture?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
