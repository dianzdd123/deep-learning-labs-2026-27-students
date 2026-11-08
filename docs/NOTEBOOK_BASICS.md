# Notebook and GitHub basics

[Student home](../README.md) · [Start here](STUDENT_START_HERE.md) · [Environment](ENVIRONMENT_SETUP.md)

## What the file types mean

| File | What it contains | Where to use it |
|---|---|---|
| `README.md` or another `.md` | Instructions and links | Read on GitHub or in an editor |
| `.ipynb` | Ordered Markdown and code cells, plus saved outputs | Colab, JupyterLab or VS Code |
| `.py` | Ordinary Python text | Python terminal or VS Code |
| `requirements-*.txt` | Package names and pinned versions | Pass to the stated `python -m pip install -r ...` command |
| `.zip` | A compressed collection of files | Extract before opening the project |

GitHub's notebook preview is a viewer. If you see instructions but no Run button,
open the Colab link or download the notebook for a local kernel. A preview error
does not necessarily mean the downloaded notebook is invalid.

## Read, implement, run, inspect

A **Markdown cell** explains the task or records reasoning. A **code cell** executes
Python. In a student worksheet the code cells start empty; write your own code there.

1. Read the instruction directly above the cell.
2. Predict what variables, shapes and outputs you expect.
3. Write a small part of the implementation.
4. Run the cell with its run control or **Shift+Enter**.
5. Inspect the output before moving on. Running successfully is not proof that the
   result answers the intended question.

For notebook practice before a lab, try this in a new personal notebook:

```python
sample_count = 3
print("Samples:", sample_count)
```

Expected output: `Samples: 3`. Add a Markdown cell explaining what the variable means.
This preparation example is not a solution to a lab model or training loop.

## The kernel remembers earlier cells

The kernel is the running Python process. It stores variables until restarted or
disconnected. Execution numbers show the order in which cells ran, which may differ
from their order on the page.

If you run a later cell before defining its variables, you may see `NameError`.
If you change a model definition but keep using an older model object, your result
may not reflect the code now visible. Restart and run from the top to resolve hidden
state; save your work first because a restart clears variables from memory.

**Before calling a notebook reproducible:** save it, restart the kernel, run cells
from top to bottom, and confirm that the expected outputs are produced again.
Random training outcomes can still vary by seed, device and framework.

## Save the right things

Save your edited notebook frequently. Notebook saving can retain cell outputs, but
it does not automatically preserve every downloaded dataset, checkpoint or figure
in the runtime's filesystem. Save important figures explicitly and keep result files
in a known folder. In Colab, download or copy needed files before the session ends.

A useful personal layout is:

| Location | Contents |
|---|---|
| `my_work/lab1/` | Your completed notebook or Python worksheet |
| `my_work/lab1/results/` | Figures and a small CSV/JSON of measured results |
| `my_work/lab1/learning_log.md` | Your question, settings, observations and reflection |

The repository ignores `my_work/` to reduce accidental commits. **Ignoring a folder
is not access control** and does not make a previously published file private.
Keep assessed work in an authorised private location.

## Using the Python worksheet

A released `.py` worksheet mirrors the notebook's instructions as comments. VS Code
recognises `# %%` as a code-cell boundary and `# %% [markdown]` as commentary. Fill in
one task at a time. The supplied blank template has no executable solution.

When your code is ready, run it with your environment's Python. A plain script starts
with a fresh namespace each time; unlike a notebook, it cannot rely on an old cell
still being in memory. Plot windows may need closing before the script continues.

## Downloading updates without losing your work

The download-and-extract route needs no Git commands. Keep your own work outside the
untouched course download, then download a fresh copy when a week is released.

If you cloned the repository, use `git status` first. Save or commit your own changes
appropriately before updating. `git pull --ff-only` updates a clean checkout without
creating a merge commit; if Git refuses, stop and ask for help. Avoid `reset --hard`,
force pushes or deleting folders as a routine update method.

You do not need to open a pull request or push your solutions to complete a lab.

**Next:** [Use the lab workflow](LAB_WORKFLOW.md).
