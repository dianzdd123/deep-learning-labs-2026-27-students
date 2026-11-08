# Troubleshooting: start with the first failing step

[Student home](../README.md) · [Environment](ENVIRONMENT_SETUP.md) · [Get help](GETTING_HELP.md)

Save your work, read the **first relevant traceback**, and change one thing at a
time. Repeatedly reinstalling packages or rerunning later cells can hide the cause.

| Symptom | First check | Next action |
|---|---|---|
| GitHub shows a notebook but no Run button | You are in the preview | Open Colab or download the `.ipynb` for a local kernel |
| Worksheet code cells are empty | The page says student worksheet | This is intentional; implement the task above each cell |
| Lab link is not available yet | Homepage release status | Use preparation guides; check Canvas if the date has passed |
| Download has nested folders or cannot save | ZIP has not been extracted | Extract it and open the folder containing `README.md` |
| `python3.12` / `py -3.12` is not found | Python installation and version | Install/select Python 3.12, or use Colab |
| `ModuleNotFoundError` | `sys.executable` in the failing kernel | Install into that environment with its `python -m pip`; notebook `%pip` targets the active kernel |
| Terminal imports work, notebook imports fail | Terminal and kernel paths differ | Select the project `.venv` in the notebook's kernel picker |
| No matching package distribution | Python version, OS and processor | Check the official framework installer; use Colab if the reference wheel is unavailable |
| Keras uses a different backend | Keras was imported before backend selection | Restart; set `KERAS_BACKEND` before the first Keras import |
| No GPU / `False` availability | A CPU runtime is selected | Continue with a small CPU experiment; do not treat this as a setup failure |
| `NameError` after running a later cell | Earlier definitions were not executed | Restart and run from the top after saving |
| A changed model seems to have no effect | An old model object remains in memory | Recreate the model and optimiser; restart if the state is unclear |
| Tensor shape mismatch | Input layout and the failing layer | Print a tiny batch's shape before and after the layer; check channel/time axes |
| Classification loss rejects labels | Target shape and dtype | Check whether the chosen loss expects integer class IDs or encoded targets |
| Loss becomes NaN/inf | Inputs, labels and learning rate | Inspect one small batch and finite values before a longer run |
| Training is slow or memory runs out | Batch size, subset and model size | Reduce the starting experiment; preserve the protocol when comparing models |
| Dataset download fails | Network and official host | Keep the error; retry later or ask for the approved course route |
| Colab disconnects / files disappear | Runtime storage is temporary | Reconnect, rerun setup and restore your saved work/results |
| A `.py` worksheet prints nothing | The template contains only comments | Add your own implementation; blank templates are not completed programs |
| Script appears to pause at a figure | `plt.show()` is displaying a window | Close the plot when ready to continue; save wanted figures first |

## Three checks to include in a help request

In the failing notebook:

```python
import sys
from pathlib import Path
print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("Working folder:", Path.cwd())
```

Then report your chosen framework and version, the relevant failing line and the
first error message. Redact usernames or paths if they reveal personal information.
For a local checkout, the [environment helper](../scripts/check_environment.py) can
check imports and a small tensor without starting training.

## What a successful run does not prove

A program can run while using an inappropriate split, comparing different budgets,
or selecting settings from test data. Return to the [lab workflow](LAB_WORKFLOW.md)
when the problem is experimental reasoning rather than a Python exception.

**Still blocked?** Follow [Get help](GETTING_HELP.md). Use Canvas for assessed work.
