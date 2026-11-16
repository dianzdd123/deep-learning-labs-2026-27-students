# Student worksheet: add your own code beneath each # %% marker.
# This blank template does not execute a model or training loop.

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
# **Student worksheet:** Code cells are intentionally empty. Implement every task yourself. Save your own Colab or Jupyter copy before editing. Do not confuse these teaching datasets with the graded tactile coursework.
# 
# [Jupyter on GitHub](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_keras.ipynb) | [Open in Google Colab](https://colab.research.google.com/github/dianzdd123/deep-learning-labs-2026-27-students/blob/main/labs/lab1-cnn/lab1_cnn_keras.ipynb)

# %% [markdown]
# ## Framework and reproducibility
# 
# **Chosen framework:** Keras 3 with TensorFlow backend.
# 
# Before training: inspect your Python/framework version, choose CPU or available GPU, set a random seed, and write down the dataset split and intended metrics. No solution code is supplied; add your own imports and configuration below.

# %%
# Add your own implementation here.

# %% [markdown]
# ## Exercise 1. Inspect the data
# 
# Load public Fashion-MNIST, display five labelled images, scale pixel values appropriately and construct reproducible, disjoint training/validation/test splits.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
# Add your own implementation here.

# %% [markdown]
# ## Exercise 2. Plan the tensor shapes
# 
# Write down input dimensions, expected convolution output dimensions, the effect of pooling and the final output shape (batch, 10).
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
# Add your own implementation here.

# %% [markdown]
# ## Exercise 3. Implement a small CNN
# 
# Create two convolution layers, nonlinearities, a pooling stage and a classification head. Print the parameter count; verify the shape of logits.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
# Add your own implementation here.

# %% [markdown]
# ## Exercise 4. Fit a baseline
# 
# Choose appropriate loss and optimiser for integer class labels; train for a small number of epochs, record training and validation curves.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
# Add your own implementation here.

# %% [markdown]
# ## Exercise 5. Evaluate and explain
# 
# Use validation evidence for one controlled model change. Freeze your choices, then report held-out metrics, a confusion matrix and representative mistakes, if any.
# 
# **Framework hint:** Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting.
# 
# **Check before moving on:** Write down expected tensor shapes and the evidence you will collect.

# %%
# Add your own implementation here.

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
