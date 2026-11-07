# Prepare your Python environment

**Deep Learning 2026–2027 | Imperial College London | Dr Dandan Zhang**

**Start here before the first lab.** All four major lab exercises are supplied as Jupyter `.ipynb` files. Each lab offers a **Keras 3 / TensorFlow** option and a **PyTorch** option. You need only one to complete a guided first attempt.

## Choose your environment

| | Google Colab: recommended | Local Jupyter or VS Code |
|---|---|---|
| Install Python? | No: use a hosted runtime | Yes: install Python and packages |
| Install a GPU? | No: CPU works; GPU may be requested | No: a CPU environment is sufficient |
| Open the notebook | Click **Open in Google Colab** after release | Download `.ipynb` from GitHub |
| Save work | **File > Save a copy in Drive** | Save the file in your own project directory |
| Temporary files | Runtime storage can be reset | Stored on your own computer |
| Suitable for | First run and easy setup | Learning editors, projects and version control |

## Route A: Google Colab in a browser

1. Sign in to [Google Colab](https://colab.research.google.com/) with a Google account.
2. When the week's lab is released, use its **Open in Google Colab** link from the [student homepage](../README.md).
3. Choose **File > Save a copy in Drive**. Edit your own copy, not the instructor's original.
4. Read the Markdown instructions first. Add your code to the **blank coding cells**, in order.
5. Select **Runtime > Run all** only after your code is ready; for debugging, run cells one at a time.
6. A CPU runtime is valid for the small introductory exercises. To request a GPU, use **Runtime > Change runtime type**, if available. GPU access is not guaranteed.
7. Save the notebook, record your Python/framework versions and keep your experiment outputs. Runtime files under `/content` may disappear after a reset.

A released lab is **not** a complete solution notebook. You are expected to write imports, data preparation, model architecture, training and evaluation code yourself.

## Route B: Jupyter Notebook or VS Code locally

1. Install a supported [Python](https://www.python.org/downloads/) version. **Python 3.12** is a suitable course reference; check package compatibility on your operating system.
2. Install [VS Code](https://code.visualstudio.com/) with the **Python** and **Jupyter** extensions, or install [JupyterLab](https://jupyter.org/).
3. Download the released `.ipynb` from GitHub: open it and choose the **Download raw file** control.
4. Create and activate a Python virtual environment in a personal project directory. Use that environment as the notebook kernel.
5. Install **only the framework for your chosen lab**, with NumPy, Matplotlib, scikit-learn and notebook dependencies.

**Windows PowerShell:**
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install jupyterlab numpy matplotlib scikit-learn
# Choose one framework:
.\.venv\Scripts\python.exe -m pip install keras tensorflow
# OR: follow https://pytorch.org/get-started/locally/ for PyTorch/torchvision
```

**macOS or Linux terminal:**
```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install jupyterlab numpy matplotlib scikit-learn
# Choose one framework:
.venv/bin/python -m pip install keras tensorflow
# OR: follow https://pytorch.org/get-started/locally/ for PyTorch/torchvision
```

For PyTorch, choose the installer appropriate to your platform from the [official selector](https://pytorch.org/get-started/locally/). It is normal for the Keras and PyTorch notebook versions to use different input axis conventions. TensorFlow/Keras usually expects `(N,H,W,C)` image arrays while PyTorch commonly uses `(N,C,H,W)`.

The folder `.venv/` must not be committed to GitHub. Do not copy your personal environment or credentials into a public repository.

## Pre-lab readiness check

Before attempting a model, verify all of the following:

- You can open a released notebook and save a personal copy.
- You can select a Python kernel/runtime and execute a simple Python expression.
- You understand the difference between a **Markdown cell** and a **code cell**.
- You can import the framework you chose and inspect its version.
- You can create a small array/tensor, inspect `shape`, and print the result.
- You can make a basic plot and save your notebook.
- You know where the notebook, downloaded data and outputs will be stored.

The required lab work does **not** depend on a local CUDA installation or paid Colab service.

## Common problems

| Problem | First check |
|---|---|
| Notebook opens but cannot run | Select a running kernel/runtime; check Python version and imports |
| `ModuleNotFoundError` | Install the missing package into the **same** interpreter used by the notebook |
| No GPU appears | Use CPU for the first run; GPU access depends on the environment |
| Colab files disappear | Runtime storage is temporary; save notebooks and download important results |
| Notebook works locally but not in Colab | Compare Python/framework versions, dataset paths and device settings |
| Shape mismatch | Print every intermediate tensor's shape; check channels-last vs channels-first |
| `CUDA out of memory` | Reduce batch size, choose a smaller training subset or use CPU |
| GitHub notebook cannot be edited | GitHub is a viewer; download it or open in Colab |

**Further reference:** [Keras documentation](https://keras.io/), [TensorFlow tutorials](https://www.tensorflow.org/tutorials), [PyTorch installation](https://pytorch.org/get-started/locally/), [VS Code Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [Colab FAQ](https://research.google.com/colaboratory/faq.html).
