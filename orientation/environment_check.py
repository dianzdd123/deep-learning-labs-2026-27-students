# Student worksheet: add your own code beneath each # %% marker.
# Replace each ellipsis and complete the TODOs before running its cell.

# %% [markdown]
# # Preparation: Getting started with Google Colab
# 
# **Environment check and coursework data exploration | 10 November 2026**
# 
# This is an optional guided preparation worksheet, separate from the four main labs. Open in Colab or download for Jupyter/VS Code. Check Python and your chosen framework, then follow the separate [Part A coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A) for the released tactile dataset. This worksheet does not contain that dataset. Use the current handbook and announcements on Canvas for assessed work.

# %% [markdown]
# ## 1. Check your environment
# 
# Write code to report Python version, selected Keras or PyTorch version and the available CPU/GPU. Do not paste access tokens.

# %%
import platform
from importlib.metadata import version
print(platform.python_version())
package = ...  # TODO: enter "torch" or "tensorflow" and inspect available devices.
print(version(package))

# %% [markdown]
# ## 2. Explore the data responsibly
# 
# Follow the current official Final Coursework data instructions, identify sample shapes and labels, and record your own observations. Keep test data separate from model selection.

# %%
from pathlib import Path
data_dir = ...  # TODO: enter the local folder from the official data instructions.
print([p.name for p in Path(data_dir).iterdir()][:5])
# Open one sample and record its shape and label.

# %% [markdown]
# ## 3. Questions for the teaching session
# 
# Write one dataset question and one training or evaluation question to discuss in the Q&A.

# %%
questions = {
    "dataset": ...,  # TODO: ask about a property of the sample you inspected.
    "evaluation": ...,  # Which split or metric needs clarification?
}
print(questions)
