#!/usr/bin/env python3
"""Check a student Python environment without downloading data or training a model.

Examples:
    python scripts/check_environment.py --framework none
    python scripts/check_environment.py --framework pytorch
    python scripts/check_environment.py --framework keras
"""
import argparse
import importlib
import os
import platform
import sys
import tempfile
from pathlib import Path


def check_framework(name):
    """Run the same small, predictable tensor operation in either framework."""
    if name == "pytorch":
        import torch
        import torchvision

        print("PyTorch:", torch.__version__)
        print("torchvision:", torchvision.__version__)
        values = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        shape = tuple(values.shape)
        mean = values.mean().item()
        print("CUDA available:", torch.cuda.is_available(), "(CPU is sufficient)")
    else:
        # Select the backend before importing Keras. This helper uses a fresh process.
        os.environ["KERAS_BACKEND"] = "tensorflow"
        import keras
        import tensorflow as tf
        from keras import ops

        print("Keras:", keras.__version__, "Backend:", keras.backend.backend())
        print("TensorFlow:", tf.__version__)
        values = ops.convert_to_tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        shape = tuple(values.shape)
        mean = float(ops.convert_to_numpy(ops.mean(values)))

    print("Tensor shape:", shape, "Expected: (2, 3)")
    print("Tensor mean:", mean, "Expected: 3.5")
    if shape != (2, 3) or abs(mean - 3.5) > 1e-6:
        raise RuntimeError("The small tensor check did not return the expected result.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--framework", choices=["none", "pytorch", "keras"], default="none")
    args = parser.parse_args()

    print("Python:", sys.version.split()[0])
    print("Interpreter:", sys.executable)
    print("System:", platform.system(), platform.machine())
    print("Working folder:", Path.cwd())
    print("Course reference Python: 3.12; this check does not enforce a version pin.")

    stage = "writing a temporary file"
    try:
        # The temporary file is removed automatically. Your work is not modified.
        with tempfile.TemporaryDirectory(prefix="dl-readiness-") as directory:
            probe = Path(directory) / "check.txt"
            probe.write_text("ready", encoding="utf-8")
            if probe.read_text(encoding="utf-8") != "ready":
                raise RuntimeError("The temporary file could not be read back.")
        print("Temporary file check passed.")

        if args.framework != "none":
            # Check supporting imports separately so the failing package is named.
            for module_name in ["numpy", "matplotlib", "sklearn", "ipykernel"]:
                stage = "importing " + module_name
                module = importlib.import_module(module_name)
                print(module_name + ":", getattr(module, "__version__", "imported"))
            stage = "checking " + args.framework
            check_framework(args.framework)
        else:
            print("Framework check skipped; choose --framework pytorch or --framework keras when installed.")
    except Exception as error:
        print("CHECK FAILED while", stage, file=sys.stderr)
        print(type(error).__name__ + ": " + str(error), file=sys.stderr)
        print("See docs/ENVIRONMENT_SETUP.md and docs/TROUBLESHOOTING.md.", file=sys.stderr)
        return 1

    print("Environment check passed.")
    print("This verifies the selected setup checks, not dataset access, training or GPU execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
