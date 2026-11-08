#!/usr/bin/env python3
"""Validate released blank worksheets and the absence of unreleased lab folders."""
import ast
import json
from pathlib import Path
from release_week import WEEKS, LABS, python_worksheet


def validate(root):
    manifest = json.loads((root / "release_manifest.json").read_text())
    released = manifest["released"]
    assert len(released) == len(set(released)), "Duplicate release state"
    assert set(released).issubset({week[0] for week in WEEKS}), "Unknown release"
    expected = set()
    for slug, _, _, labs in WEEKS:
        if slug == "orientation":
            folder = root / "orientation"
            if slug not in released:
                assert not folder.exists(), "Orientation prematurely released"
            else:
                expected.add(folder / "environment_check.ipynb")
        for key in labs:
            number = LABS[key]["number"]
            folder = root / f"labs/lab{number}-{key}"
            if slug not in released:
                assert not folder.exists(), f"Unreleased lab visible: {key}"
            else:
                for framework in ("keras", "pytorch"):
                    expected.add(folder / f"lab{number}_{key}_{framework}.ipynb")
    found = set(root.rglob("*.ipynb"))
    assert found == expected, "Missing or unexpected student notebooks"
    for path in sorted(expected):
        book = json.loads(path.read_text())
        assert book["nbformat"] == 4
        codes = [cell for cell in book["cells"] if cell["cell_type"] == "code"]
        assert len(codes) >= 3, path
        for cell in codes:
            assert not "".join(cell["source"]).strip(), f"Prefilled student code: {path}"
            assert cell.get("execution_count") is None and not cell.get("outputs"), path
        script = path.with_suffix(".py")
        assert script.is_file(), f"Missing Python worksheet: {script}"
        content = script.read_text()
        assert not ast.parse(content).body, f"Executable solution code in {script}"
        assert content == python_worksheet(book), f"Notebook/Python instructions differ: {script}"
    return len(expected), len(released)


if __name__ == "__main__":
    notebooks, weeks = validate(Path(__file__).resolve().parents[1])
    print(f"Validation passed: {notebooks} blank notebook/Python pairs, {weeks} published week(s).")
