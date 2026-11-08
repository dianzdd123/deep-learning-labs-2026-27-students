# Environment setup: Colab, VS Code or JupyterLab

[Student home](../README.md) · [Start here](STUDENT_START_HERE.md) · [Troubleshooting](TROUBLESHOOTING.md)

Choose **one environment and one framework** for your first lab. The course has
Keras 3 with TensorFlow, and PyTorch with torchvision. Both can start on CPU.

## Route A: Google Colab

1. Open [Colab](https://colab.research.google.com/) and create a new notebook for
   preparation, or open a released worksheet using its Colab link.
2. For a course worksheet, choose **File → Save a copy in Drive**. Give the copy a
   useful name. Check that your copy is the one you are editing.
3. Connect to a Python runtime. Run the following in a code cell:

```python
import sys
print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("My notebook is running")
```

4. Run **one** of the framework checks below. Colab's installed versions can change;
   record the versions printed rather than assuming they match the local pins.
5. If an import fails, read the error and install the missing package in that
   runtime. Use `%pip` in a notebook cell, and restart if the installation asks you
   to. Avoid replacing a working environment merely to match a different machine.
6. Keep CPU for preparation. For later experiments, **Runtime → Change runtime
   type** may offer a GPU. Availability and runtime duration are not guaranteed.
7. Save the notebook. Download important plots/results from the runtime files panel
   before disconnecting; saving a notebook does not save every file under `/content`.

### Small PyTorch check

```python
import torch
print("PyTorch:", torch.__version__)
values = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print("Shape:", tuple(values.shape))  # two rows, three columns
print("Mean:", values.mean().item())
```

Expected: shape **`(2, 3)`**, mean **`3.5`**. This checks basic tensor operations,
not training accuracy or GPU operation.

### Small Keras/TensorFlow check

Use this as the first framework cell in a fresh kernel:

```python
import os
os.environ["KERAS_BACKEND"] = "tensorflow"  # choose before importing Keras
import keras
from keras import ops
print("Keras:", keras.__version__, "Backend:", keras.backend.backend())
values = ops.convert_to_tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print("Shape:", tuple(values.shape))
print("Mean:", float(ops.convert_to_numpy(ops.mean(values))))
```

Expected: backend **`tensorflow`**, shape **`(2, 3)`**, mean **`3.5`**. If Keras was
already imported with another backend, restart the kernel before changing it.

## Route B: local VS Code or JupyterLab

These commands use the course's **Python 3.12 reference stack**. The pins match the
Linux CPU reference used for the teaching materials; they are not a guarantee for
every operating system or processor. If your platform has no matching wheel, use
Colab or ask for a suitable institutional environment.

### 1. Get a working folder

Install Python 3.12 and, for VS Code, the official **Python** and **Jupyter**
extensions. On the [repository homepage](../README.md), choose **Code → Download
ZIP**, extract it fully, and open the extracted folder in VS Code. Do not work
inside the ZIP preview. No Git installation is needed for this route.

Open a terminal in the folder containing `README.md`, `requirements-notebooks.txt`
and `scripts/`. If you have Git and prefer a clone, use:

```bash
git clone https://github.com/dianzdd123/deep-learning-labs-2026-27-students.git
cd deep-learning-labs-2026-27-students
```

### 2. Create the environment

**Windows PowerShell** — use the explicit interpreter, so activation-policy changes
are unnecessary:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements-notebooks.txt
```

**macOS / Linux terminal:**

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements-notebooks.txt
```

If `py -3.12` or `python3.12` is not found, check your Python installation before
continuing. Do not silently use a different interpreter.

### 3. Install one framework

**PyTorch, Windows or Linux CPU:**

```powershell
# Windows PowerShell
.\.venv\Scripts\python.exe -m pip install -r requirements-pytorch-cpu.txt
```

```bash
# Linux terminal
.venv/bin/python -m pip install -r requirements-pytorch-cpu.txt
```

The CPU file uses the official PyTorch wheel index and the matched
`torch==2.8.0` / `torchvision==0.23.0` pair. Install the common notebook file first.

**PyTorch, macOS:** after the common notebook installation, use:

```bash
.venv/bin/python -m pip install torch==2.8.0 torchvision==0.23.0
```

For other processors or accelerator configurations, consult the
[official installation selector](https://pytorch.org/get-started/locally/) and
[version pairing instructions](https://pytorch.org/get-started/previous-versions/).

**Keras/TensorFlow alternative:**

```powershell
# Windows PowerShell
.\.venv\Scripts\python.exe -m pip install -r requirements-keras.txt
```

```bash
# macOS / Linux terminal
.venv/bin/python -m pip install -r requirements-keras.txt
```

The reference is TensorFlow 2.20.0 with Keras 3.11.3. Native Windows uses CPU for
this route. Intel macOS does not have the pinned TensorFlow wheel; use Colab.
Check the [TensorFlow installation guide](https://www.tensorflow.org/install/pip)
for platform support. GPU configuration is outside this first setup exercise.

### 4. Check the environment

The helper checks the interpreter, imports, a small tensor and a writable temporary
folder. It does not download a dataset, train a model or install anything.

```powershell
# Windows; replace pytorch with keras if that is your chosen framework
.\.venv\Scripts\python.exe scripts/check_environment.py --framework pytorch
```

```bash
# macOS / Linux
.venv/bin/python scripts/check_environment.py --framework pytorch
```

A successful run ends with **`Environment check passed.`** CPU operation is expected.
You can run `--framework none` for the Python/file check before installing a framework.
If a check fails, read its named component and the original error in the output.

### 5. Select the kernel and run a cell

In VS Code:

1. Open your `.ipynb` file.
2. Use **Select Kernel** at the top right; select the Python environment in this
   project's `.venv`. The exact menu labels may vary by extension version.
3. Run the Python version cell above. `sys.executable` should point into `.venv`.
4. Run your chosen tensor check, save, restart the kernel and rerun from the top.

Selecting **Python: Select Interpreter** for terminal scripts does not by itself
prove that the notebook selected the same kernel. Check the printed path.

To use JupyterLab instead, start it from the project environment:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab
```

```bash
.venv/bin/python -m jupyterlab
```

Keep that terminal open while using JupyterLab.

## Pre-lab readiness check

- [ ] I can save my notebook in a location I recognise.
- [ ] I can select a kernel and print its Python executable.
- [ ] My chosen framework reports its version and completes the tensor check.
- [ ] I can run cells in order after a kernel restart.
- [ ] I can distinguish Markdown instructions from executable code cells.
- [ ] I know that the released worksheet's blank code cells are intentional.
- [ ] I know where to keep results and how to ask for help.

## Common problems

Use the [troubleshooting guide](TROUBLESHOOTING.md) for missing packages, kernels,
shape errors, slow runs and lost Colab files. **Next:** [Notebook basics](NOTEBOOK_BASICS.md).

## Sources

Setup guidance is based on the official [Colab FAQ](https://research.google.com/colaboratory/faq.html),
[VS Code notebook documentation](https://code.visualstudio.com/docs/datascience/jupyter-notebooks),
[Python virtual-environment guide](https://docs.python.org/3.12/library/venv.html),
[PyTorch version instructions](https://pytorch.org/get-started/previous-versions/) and
[TensorFlow installation guide](https://www.tensorflow.org/install/pip), checked
8 November 2026. The preparation sequence and readiness checklist are teaching guidance.
