# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Lab 4: Transformer Encoder and Self-Attention | Keras
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
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab4-transformer/lab4_transformer_keras.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab4-transformer/lab4_transformer_keras.ipynb)

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
# ## Exercise 1. Inspect image patches
# 
# Divide each 28 x 28 image into non-overlapping 7 x 7 patches; derive 16 patch tokens containing 49 pixel values each.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
(images, labels), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
images = images.astype("float32")[..., None] / 255
x_test = x_test.astype("float32")[..., None] / 255
# TODO: split images and labels into x_train, y_train, x_val, y_val.
def patchify(images):
    patches = tf.image.extract_patches(images, [1,7,7,1], [1,7,7,1], [1,1,1,1], "VALID")
    return ...  # reshape to (batch, 16, 49)
print(patchify(images[:2]).shape)

# %% [markdown]
# ## Exercise 2. Implement token embeddings
# 
# Project each token into 32 features and add learnable position embeddings. Check that the position weights belong to the model and receive updates. Explain why position information is important.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
class Tokens(layers.Layer):
    def __init__(self):
        super().__init__()
        self.project = layers.Dense(32)
        self.position = ...  # TODO: register 16 trainable position vectors.

    def call(self, images):
        projected = self.project(patchify(images))
        return ...  # combine projected tokens and position vectors

# %% [markdown]
# ## Exercise 3. Build encoder attention
# 
# Implement four-head scaled dot-product self-attention, a residual connection and feed-forward layers. Assert attention shape (batch, 4, 16, 16).
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
inputs = keras.Input(shape=(28, 28, 1))
tokens = Tokens()(inputs)
attention = layers.MultiHeadAttention(num_heads=4, key_dim=8)
context, weights = attention(tokens, tokens, return_attention_scores=True)
encoded = ...  # TODO: residual addition, feed-forward block and second skip.
assert tuple(weights.shape[1:]) == (4, 16, 16)

# %% [markdown]
# ## Exercise 4. Train a simple classifier
# 
# Pool encoder representations and predict ten class logits. Plot train and validation curves using a small, fixed budget.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
pooled = layers.GlobalAveragePooling1D()(encoded)
logits = ...  # TODO: classify pooled tokens into ten classes.
model = keras.Model(inputs, logits)
epochs = 3
model.compile(optimizer="adam", loss=..., metrics=["accuracy"])  # TODO: integer labels and logits.
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=epochs)
plt.plot(history.history["val_accuracy"])
# Add a labelled training curve and inspect the gap.

# %% [markdown]
# ## Exercise 5. Evaluate and critique
# 
# Use validation for one controlled modification, freeze your choices, then inspect held-out errors. Explain why the encoder is not a complete Seq2Seq translator or generative LLM.
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
# - Why can't a token's original position be inferred from its contents alone?
# - Why is an attention heatmap not automatically an explanation of a prediction?
# 
# Submit no solutions to this public repository. Save a private copy of your experiment with framework versions, split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.
