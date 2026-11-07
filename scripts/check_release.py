#!/usr/bin/env python3
"""Fail when a student notebook contains prefilled code or future labs are exposed."""
import json
from pathlib import Path
from release_week import WEEKS, LABS

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/"release_manifest.json").read_text())
released=manifest["released"]
assert len(released)==len(set(released)),"Duplicate release state"
assert set(released).issubset({w[0] for w in WEEKS})
for slug,dt,title,labs in WEEKS:
    if slug not in released:
        if slug=="orientation":
            assert not (root/"orientation/environment_check.ipynb").exists(),"Orientation prematurely released"
        for key in labs:
            n=LABS[key]["number"]
            assert not (root/f"labs/lab{n}-{key}").exists(), f"Unreleased lab visible: {key}"
    else:
        for key in labs:
            n=LABS[key]["number"]
            for fw in ("keras","pytorch"):
                assert (root/f"labs/lab{n}-{key}/lab{n}_{key}_{fw}.ipynb").exists()
count=0
for path in root.rglob("*.ipynb"):
    n=json.loads(path.read_text())
    assert n["nbformat"]==4
    codes=[c for c in n["cells"] if c["cell_type"]=="code"]
    assert len(codes)>=3, path
    for c in codes:
        assert "".join(c["source"]).strip()=="", f"Possible student solution code: {path}"
        assert not c.get("outputs"), f"Filled output: {path}"
    count+=1
print(f"Validation passed: {count} notebooks, {len(released)} published week(s), all code cells blank.")
