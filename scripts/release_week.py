#!/usr/bin/env python3
"""Publish only student instructions and blank .ipynb exercise cells; no solutions."""
import argparse
import json
import os
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = "dianzdd123/deep-learning-labs-2026-27-students"
WEEKS = [
    ("orientation", "2026-11-10", "Preparation: Environment check and coursework data exploration", []),
    ("cnn-resnet", "2026-11-17", "Week 1: CNN and ResNet", ["cnn", "resnet"]),
    ("rnn", "2026-11-24", "Week 2: Recurrent Neural Networks", ["rnn"]),
    ("transformer", "2026-12-01", "Week 3: Transformer and Attention", ["transformer"]),
]
LABS = {
 "cnn": {
  "number":1, "title":"Convolutional Neural Networks",
  "data":"Fashion-MNIST, 28 x 28 grayscale images and ten classes",
  "goal":"Understand local convolution, pooling, weight sharing and image classification.",
  "steps":[
   ("Inspect the data","Load public Fashion-MNIST, display five labelled images, scale pixel values appropriately and construct reproducible, disjoint training/validation/test splits."),
   ("Plan the tensor shapes","Write down input dimensions, expected convolution output dimensions, the effect of pooling and the final output shape (batch, 10)."),
   ("Implement a small CNN","Create two convolution layers, nonlinearities, a pooling stage and a classification head. Print the parameter count; verify the shape of logits."),
   ("Fit a baseline","Choose appropriate loss and optimiser for integer class labels; train for a small number of epochs, record training and validation curves."),
   ("Evaluate and explain","Use validation evidence for one controlled model change. Freeze your choices, then report held-out metrics, a confusion matrix and representative mistakes, if any.")],
  "questions":["Why do shared local filters require fewer parameters than an equally expressive dense mapping?","Why should the test set not be used to select an architecture?"]},
 "resnet": {
  "number":2,"title":"Residual Networks and Controlled Comparison",
  "data":"CIFAR-10, 32 x 32 RGB images and ten classes",
  "goal":"Understand y = F(x) + x and the effect of an identity shortcut.",
  "steps":[
   ("Explore RGB images","Load CIFAR-10, inspect the image dimensions in your framework's axis order, normalise inputs and set up a fixed train/validation/test split."),
   ("Plan a residual block","Draw the identity and residual paths. Specify when tensor shapes agree for addition and when a projection would be needed."),
   ("Implement paired models","Create a compact plain block and matching residual block with identical convolution branches. Check parameter counts and dummy-batch output shapes."),
   ("Train both fairly","Use the same split, optimiser, learning rate and epoch budget. Match compatible initial branch weights and batch order where possible. Plot validation performance; document remaining differences."),
   ("Assess the evidence","Choose a model based on validation evidence; evaluate on the held-out set, inspect failures and discuss what extra seeds/depth would establish.")],
  "questions":["Why is a shortcut impossible if channel counts differ without an additional projection?","Can a short single-seed run establish the superiority of a residual architecture?"]},
 "rnn": {
  "number":3,"title":"Recurrent Neural Networks, GRU and LSTM",
  "data":"Synthetic increasing sequences and their reversed counterparts",
  "goal":"Explain recurrent state, gating and why sequence order matters.",
  "steps":[
   ("Create an order-sensitive task","Generate paired ordered and reversed sequences using the same values; plot an example and verify both have the same mean."),
   ("Prevent paired leakage","Assign entire source-sequence pairs to train/validation/test splits; document why splitting individual sequence copies would be misleading."),
   ("Implement three recurrent models","Implement RNN, GRU and LSTM classifiers with matching hidden sizes and two-class logits. Trace shapes at every timestep."),
   ("Compare training behaviour","Use the same split, optimiser and training budget; report parameters and validation evidence. Consider a simple order-sensitive baseline before claiming a need for long-term memory."),
   ("Check failure modes","Select using validation results belonging to the saved weights you will evaluate; inspect held-out errors and explain padding/masking for variable length.")],
  "questions":["Why is an order-blind average insufficient for this task?","How do recurrent gates influence retention of state?"]},
 "transformer": {
  "number":4,"title":"Transformer Encoder and Self-Attention",
  "data":"Fashion-MNIST, 28 x 28 grayscale images",
  "goal":"Trace patch tokens, positional embeddings and scaled dot-product attention.",
  "steps":[
   ("Inspect image patches","Divide each 28 x 28 image into non-overlapping 7 x 7 patches; derive 16 patch tokens containing 49 pixel values each."),
   ("Implement token embeddings","Project each token into 32 features and add learnable position embeddings. Check that the position weights belong to the model and receive updates. Explain why position information is important."),
   ("Build encoder attention","Implement four-head scaled dot-product self-attention, a residual connection and feed-forward layers. Assert attention shape (batch, 4, 16, 16)."),
   ("Train a simple classifier","Pool encoder representations and predict ten class logits. Plot train and validation curves using a small, fixed budget."),
   ("Evaluate and critique","Use validation for one controlled modification, freeze your choices, then inspect held-out errors. Explain why the encoder is not a complete Seq2Seq translator or generative LLM.")],
  "questions":["Why can't a token's original position be inferred from its contents alone?","Why is an attention heatmap not automatically an explanation of a prediction?"]},
}

def md(text, i):
    return {"cell_type":"markdown","id":f"m{i:03d}","metadata":{},"source":text.splitlines(keepends=True)}

def blank(i):
    return {"cell_type":"code","id":f"c{i:03d}","metadata":{},"execution_count":None,"outputs":[],"source":[]}

def make_notebook(key, framework, repo):
    lab = LABS[key]
    number = lab["number"]
    path = f"labs/lab{number}-{key}/lab{number}_{key}_{framework}.ipynb"
    cells = []
    cells.append(md(
       f"# Lab {number}: {lab['title']} | {framework.title()}\n\n"
       "**Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**\n\n"
       "**Lecturer:** Dr Dandan Zhang | **Formative, unmarked**\n\n"
       f"**Dataset:** {lab['data']}\n\n"
       f"**Learning aim:** {lab['goal']}\n\n"
       "**Student worksheet:** Code cells are intentionally empty. Implement every task yourself. "
       "Save your own Colab or Jupyter copy before editing. Do not confuse these teaching datasets with the graded tactile coursework.\n\n"
       f"[Jupyter on GitHub](https://github.com/{repo}/blob/main/{path}) | "
       f"[Open in Google Colab](https://colab.research.google.com/github/{repo}/blob/main/{path})\n", 0))
    cells.append(md(
       "## Framework and reproducibility\n\n"
       f"**Chosen framework:** {'Keras 3 with TensorFlow backend' if framework=='keras' else 'PyTorch and torchvision (where relevant)'}.\n\n"
       "Before training: inspect your Python/framework version, choose CPU or available GPU, "
       "set a random seed, and write down the dataset split and intended metrics. "
       "No solution code is supplied; add your own imports and configuration below.\n", 1))
    cells.append(blank(1))
    for idx, (heading, description) in enumerate(lab["steps"], start=2):
        extra = ""
        if key == "rnn":
            extra = ("Use (batch, time, features); distinguish recurrent outputs, hidden states and LSTM cell state. "
                     + ("Read the Keras recurrent-layer return options." if framework == "keras" else
                        "Use batch_first=True where appropriate; hidden-state layout is a separate contract."))
        elif framework == "keras":
            extra = "Use channels-last images and Keras layers. Cross-check integer labels with the chosen loss and logits setting."
        else:
            extra = "Use channels-first images, nn.Module and DataLoader. Distinguish training updates from evaluation."
        cells.append(md(f"## Exercise {idx-1}. {heading}\n\n{description}\n\n**Framework hint:** {extra}\n\n**Check before moving on:** Write down expected tensor shapes and the evidence you will collect.\n",idx))
        cells.append(blank(idx))
    cells.append(md(
        "## Help while you work\n\n"
        f"[Lab workflow](https://github.com/{repo}/blob/main/docs/LAB_WORKFLOW.md) · "
        f"[Troubleshooting](https://github.com/{repo}/blob/main/docs/TROUBLESHOOTING.md) · "
        f"[Learning-log template](https://github.com/{repo}/blob/main/docs/LEARNING_LOG.md)\n", 89))
    cells.append(md("## Reflection and learning record\n\n"+ "\n".join(f"- {x}" for x in lab["questions"]) +
        "\n\nSubmit no solutions to this public repository. Save a private copy of your experiment with framework versions, "
        "split, parameter counts, train/validation curves, held-out metrics, representative errors (or state that none were observed), one limitation and one justified next experiment.\n",
        90))
    return {"nbformat":4,"nbformat_minor":5,
        "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},
                    "language_info":{"name":"python"}, "colab":{"provenance":[]}},
        "cells":cells}

def orientation_notebook():
    return {"nbformat":4,"nbformat_minor":5,
       "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python"},"colab":{"provenance":[]}},
       "cells":[md("# Preparation: Getting started with Google Colab\n\n**Environment check and coursework data exploration | 10 November 2026**\n\nThis is an optional blank preparation worksheet, separate from the four main labs. Open in Colab or download for Jupyter/VS Code. Check Python and your chosen framework, then follow the separate [Part A coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A) for the released tactile dataset. This worksheet does not contain that dataset. Use the current handbook and announcements on Canvas for assessed work.\n",0),
       md("## 1. Check your environment\n\nWrite code to report Python version, selected Keras or PyTorch version and the available CPU/GPU. Do not paste access tokens.\n",1),blank(1),
       md("## 2. Explore the data responsibly\n\nFollow the current official Final Coursework data instructions, identify sample shapes and labels, and record your own observations. Keep test data separate from model selection.\n",2),blank(2),
       md("## 3. Questions for the teaching session\n\nWrite one dataset question and one training or evaluation question to discuss in the Q&A.\n",3),blank(3)]}

def python_worksheet(notebook):
    """Mirror the instructions as comments; keep every executable cell empty."""
    parts = ["# Student worksheet: add your own code beneath each # %% marker.\n"
             "# This blank template does not execute a model or training loop.\n"]
    for cell in notebook["cells"]:
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            parts.append("# %% [markdown]\n" + "\n".join("# " + line for line in source.splitlines()) + "\n")
        else:
            if source.strip():
                raise ValueError("Student exports must not contain filled solution code")
            parts.append("# %%\n# Add your own implementation here.\n")
    return "\n".join(parts)


def lab_readme(key, repo):
    lab = LABS[key]
    number = lab["number"]
    prefix = f"labs/lab{number}-{key}"
    text = f"# Lab {number}: {lab['title']}\n\n"
    text += "[Student home](../../README.md) · [Lab workflow](../../docs/LAB_WORKFLOW.md) · [Get help](../../docs/GETTING_HELP.md)\n\n"
    text += f"**Unmarked practice · Dr Dandan Zhang · Imperial I-X MSc AIAI**\n\n{lab['goal']}\n\n"
    text += f"**Data:** {lab['data']}. Choose one framework for your first attempt.\n\n"
    text += "| Framework | Notebook | Run online | Python worksheet |\n|---|---|---|---|\n"
    for framework, label in [("keras", "Keras 3 / TensorFlow"), ("pytorch", "PyTorch")]:
        stem = f"lab{number}_{key}_{framework}"
        path = f"{prefix}/{stem}.ipynb"
        text += (f"| {label} | [View / download]({stem}.ipynb) | "
                 f"[Open in Colab](https://colab.research.google.com/github/{repo}/blob/main/{path}) | "
                 f"[.py with VS Code cells]({stem}.py) |\n")
    text += "\n## Follow this order\n\n"
    text += "1. Save a personal copy and check its kernel/framework.\n"
    text += "2. Read all the tasks, then implement one blank cell at a time.\n"
    text += "3. Check shapes on a tiny batch before training.\n"
    text += "4. Use validation evidence to choose settings; freeze choices before the final held-out evaluation.\n"
    text += "5. Restart and run from the top, then save your work and learning record.\n\n"
    text += "Code cells are **blank by design**. The `.py` file contains the same instructions as comments and will do nothing until you implement the tasks.\n\n"
    text += "## Learning checkpoints\n\n" + "\n".join(f"- {description}" for _, description in lab["steps"])
    text += "\n\n## After the lab\n\n"
    text += "Use the [learning log](../../docs/LEARNING_LOG.md) to explain measured results, representative errors and one limitation. Keep your implementation in your own files. This lab is not a coursework submission.\n"
    return text


def render_home(released):
    text = "# Deep Learning | Student Laboratory Hub 2026–2027\n\n"
    text += "**ELEC70129 · Imperial College London · I-X MSc AIAI**  \n**Module leader: Dr Dandan Zhang**\n\n"
    text += "Learn to build, inspect and explain a deep learning experiment. Start with one framework and work through the four unmarked labs: **CNN → ResNet → RNN → Transformer**.\n\n"
    text += "**Course home:** [Teaching page](https://www.intelligentrobotics-acrossscales.com/teaching). Use it for the course introduction, lecture materials, handbook previews, videos and the Main labs / Additional sessions overview. **Canvas** holds the current assessment handbook, briefing slides, official announcements and submission links.\n\n"
    text += "**Student course access:** contact [Dr Dandan Zhang](mailto:d.zhang17@imperial.ac.uk) at **d.zhang17@imperial.ac.uk**, quoting your module code and the resource title. This public repository contains preparation guides and, when published here, blank student worksheets. Authorised notebooks linked from the teaching page may require separate course access.\n\n"
    text += "## Start in three steps\n\n"
    text += "1. **New here?** Follow [Start here](docs/STUDENT_START_HERE.md). It explains what to do before the first lab.\n"
    text += "2. **Set up once:** choose [Colab or local VS Code/Jupyter](docs/ENVIRONMENT_SETUP.md), then run the small readiness check.\n"
    text += "3. **When your lab is released:** open its page below, save your own copy and follow the [lab workflow](docs/LAB_WORKFLOW.md).\n\n"
    text += "**Choose Keras/TensorFlow or PyTorch for your first run.** You do not need both. Released notebooks have deliberately blank code cells; writing the code is the exercise. GitHub previews files; Colab or a local Python kernel executes them.\n\n"
    text += "## Weekly worksheets\n\n"
    text += "This table reports **blank worksheet availability in this public repository**, not the availability of lecture slides, authorised worked examples or the assessed dataset. Preparation is separate from the four numbered main labs. [Full teaching and release calendar](docs/RELEASE_CALENDAR.md).\n\n"
    text += "**Part A data has been released:** use the separate [Final Coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A) and its dataset download instructions. A Coming soon worksheet entry below does not mean the coursework data is unreleased.\n\n"
    text += "| Release | Date, 2026 | Topic | Open the worksheet |\n|---|---|---|---|\n"
    for index, (slug, due, title, labs) in enumerate(WEEKS):
        if slug not in released:
            entry = "Coming soon"
        elif slug == "orientation":
            entry = "[Preparation worksheet](orientation/START_HERE.md)"
        else:
            entry = " · ".join(f"[Lab {LABS[key]['number']}: {key.upper()}](labs/lab{LABS[key]['number']}-{key}/README.md)" for key in labs)
        topic = title.split(": ", 1)[1]
        label = "Preparation (not a main lab)" if slug == "orientation" else " + ".join(f"Lab {LABS[key]['number']}" for key in labs)
        text += f"| {label} | {due} | {topic} | {entry} |\n"
    text += "\nEach released lab page offers a notebook, a Colab link and a matching blank Python worksheet for each framework. Save completed work in your own files. If a date has passed but a link is not yet available, check Canvas for the teaching team's announcement.\n"
    # Keep this reusable guidance after the changing release table.
    overview = Path(__file__).resolve().parents[1] / "docs" / "HUB_OVERVIEW.md"
    if overview.exists():
        text += "\n" + overview.read_text(encoding="utf-8")
    text += "\n## Course and wider resources\n\n"
    text += "[Teaching page](https://www.intelligentrobotics-acrossscales.com/teaching) · [MSEI Lab website](https://zhangrobotics.com/msei_website/) · [MSEI website on GitHub](https://github.com/dianzdd123/msei_website)\n\n"
    text += "For proposed material fixes or reuse, see [Contributing](CONTRIBUTING.md) and [Reuse guidance](docs/REUSE.md). Reuse permissions need clarification because this repository has no repository-wide licence file.\n"
    return text

def publish_week(root, slug, repo, dry_run=False):
    manifest_path=root/"release_manifest.json"
    state=json.loads(manifest_path.read_text())
    released=set(state.get("released",[]))
    if slug in released:
        print(f"Already published: {slug}")
        return []
    week=next(w for w in WEEKS if w[0]==slug)
    changes={}
    if slug=="orientation":
        changes["orientation/START_HERE.md"] = (
            "# Preparation: Environment check and coursework data exploration\n\n"
            "[Student home](../README.md) · [Environment setup](../docs/ENVIRONMENT_SETUP.md)\n\n"
            "This optional preparation activity is separate from Labs 1–4. Save your own copy of the blank worksheet. The assessed tactile dataset is released through the separate [Part A coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A), not through this worksheet. Follow the current handbook on Canvas.\n\n"
            "[View / download notebook](environment_check.ipynb) · "
            f"[Open in Colab](https://colab.research.google.com/github/{repo}/blob/main/orientation/environment_check.ipynb) · "
            "[Blank Python worksheet](environment_check.py)\n\n"
            "Complete your environment checks, inspect data only through the official coursework route, and record one question for the Q&A. "
            "This is unmarked preparation, not an assessment submission.\n")
        notebook = orientation_notebook()
        changes["orientation/environment_check.ipynb"] = json.dumps(notebook, indent=2) + "\n"
        changes["orientation/environment_check.py"] = python_worksheet(notebook)
    else:
        for key in week[3]:
            n=LABS[key]["number"]
            folder=f"labs/lab{n}-{key}"
            changes[f"{folder}/README.md"]=lab_readme(key,repo)
            for fw in ("keras","pytorch"):
                notebook = make_notebook(key, fw, repo)
                changes[f"{folder}/lab{n}_{key}_{fw}.ipynb"] = json.dumps(notebook, indent=2) + "\n"
                changes[f"{folder}/lab{n}_{key}_{fw}.py"] = python_worksheet(notebook)
    changes[f"release_notes/{slug}.md"]=f"# {week[2]}\n\nPublished: {week[1]}\n\nThe repository now includes student instructions and deliberately empty coding cells for this week's activities. Previous labs remain accessible. No completed implementations or staff-only answer keys are included.\n"
    released.add(slug)
    changes["README.md"]=render_home(released)
    changes["release_manifest.json"]=json.dumps({"released":[w[0] for w in WEEKS if w[0] in released]},indent=2)+"\n"
    if dry_run:
        for name in changes:print("Would publish:",name)
        return list(changes)
    for name,content in changes.items():
        path=root/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding="utf-8")
        print("Published:",name)
    return list(changes)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--week",default="auto",choices=["auto"]+[w[0] for w in WEEKS])
    ap.add_argument("--allow-early",action="store_true")
    ap.add_argument("--dry-run",action="store_true")
    ap.add_argument("--print-tags",action="store_true")
    ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument("--repo",default=os.getenv("GITHUB_REPOSITORY",REPO))
    ap.add_argument("--as-of",help="ISO date for local testing")
    args=ap.parse_args()
    if args.print_tags:
        released=set(json.loads((args.root/"release_manifest.json").read_text())["released"])
        for slug,dt,title,_ in WEEKS:
            if slug in released:
                print(f"week-{dt}-{slug}|{title}|release_notes/{slug}.md")
        return
    today=date.fromisoformat(args.as_of) if args.as_of else datetime.now(ZoneInfo("Europe/London")).date()
    due=[w for w in WEEKS if (w[1]<=today.isoformat() if args.week=="auto" else w[0]==args.week)]
    for slug,dt,title,labs in due:
        if today<date.fromisoformat(dt) and not args.allow_early:
            raise SystemExit(f"{slug} cannot be published before {dt} without --allow-early")
        publish_week(args.root,slug,args.repo,args.dry_run)
    if not due:print(f"No release due yet on {today}")
if __name__=="__main__":
    main()

