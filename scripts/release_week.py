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
    ("orientation", "2026-11-10", "Week 0: Dataset release and preparation", []),
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
   ("Evaluate and improve","Produce classification metrics, a confusion matrix and at least two analysed mistakes. Change exactly one model factor and repeat fairly.")],
  "questions":["Why do shared local filters require fewer parameters than an equally expressive dense mapping?","Why should the test set not be used to select an architecture?"]},
 "resnet": {
  "number":2,"title":"Residual Networks and Controlled Comparison",
  "data":"CIFAR-10, 32 x 32 RGB images and ten classes",
  "goal":"Understand y = F(x) + x and the effect of an identity shortcut.",
  "steps":[
   ("Explore RGB images","Load CIFAR-10, inspect the N/H/W/C dimensions, normalise inputs and set up a fixed train/validation/test split."),
   ("Plan a residual block","Draw the identity and residual paths. Specify when tensor shapes agree for addition and when a projection would be needed."),
   ("Implement paired models","Create a compact plain block and matching residual block with identical convolution branches. Check parameter counts and dummy-batch output shapes."),
   ("Train both fairly","Use the same optimiser, learning rate, epoch budget and data split. Plot loss and validation performance; document variance and limitations."),
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
   ("Compare training behaviour","Use the same split, optimiser and training budget; report parameters and validation loss or accuracy for each model."),
   ("Check failure modes","Select using validation results; evaluate on held-out examples, plot errors and explain what padding/masking means for variable length.")],
  "questions":["Why is an order-blind average insufficient for this task?","How do recurrent gates influence retention of state?"]},
 "transformer": {
  "number":4,"title":"Transformer Encoder and Self-Attention",
  "data":"Fashion-MNIST, 28 x 28 grayscale images",
  "goal":"Trace patch tokens, positional embeddings and scaled dot-product attention.",
  "steps":[
   ("Inspect image patches","Divide each 28 x 28 image into non-overlapping 7 x 7 patches; derive 16 patch tokens containing 49 pixel values each."),
   ("Implement token embeddings","Project each token into 32 features and add learnable position embeddings. Explain why position information is important."),
   ("Build encoder attention","Implement four-head scaled dot-product self-attention, a residual connection and feed-forward layers. Assert attention shape (batch, 4, 16, 16)."),
   ("Train a simple classifier","Pool encoder representations and predict ten class logits. Plot train and validation curves using a small, fixed budget."),
   ("Evaluate and critique","Inspect errors, try one controlled modification, and explain why the encoder is not a complete Seq2Seq translator or generative LLM.")],
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
        if framework == "keras":
            extra = "Use Keras/TensorFlow conventions: channels-last images, keras.layers, compile/fit/evaluate where appropriate."
        else:
            extra = "Use PyTorch conventions: channels-first images, nn.Module, DataLoader, explicit gradient and eval loops."
        cells.append(md(f"## Exercise {idx-1}. {heading}\n\n{description}\n\n**Framework hint:** {extra}\n\n**Check before moving on:** Write down expected tensor shapes and the evidence you will collect.\n",idx))
        cells.append(blank(idx))
    cells.append(md("## Reflection and learning record\n\n"+ "\n".join(f"- {x}" for x in lab["questions"]) +
        "\n\nSubmit no solutions to this public repository. Save a private copy of your experiment with framework versions, "
        "split, parameter counts, train/validation curves, held-out metrics, two errors, one limitation and one justified next experiment.\n",
        90))
    return {"nbformat":4,"nbformat_minor":5,
        "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},
                    "language_info":{"name":"python"}, "colab":{"provenance":[]}},
        "cells":cells}

def orientation_notebook():
    return {"nbformat":4,"nbformat_minor":5,
       "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python"},"colab":{"provenance":[]}},
       "cells":[md("# Week 0: Getting started with Google Colab\n\n**Dataset release and coursework Q&A | 10 November 2026**\n\nThis is a blank instructional worksheet. Open in Colab or download for Jupyter/VS Code. Use your own code to check Python, list packages and inspect the approved coursework dataset following Canvas instructions.\n",0),
       md("## 1. Check your environment\n\nWrite code to report Python version, selected Keras or PyTorch version and the available CPU/GPU. Do not paste access tokens.\n",1),blank(1),
       md("## 2. Explore the data responsibly\n\nFollow the current official Final Coursework data instructions, identify sample shapes and labels, and record your own observations. Keep test data separate from model selection.\n",2),blank(2),
       md("## 3. Questions for the teaching session\n\nWrite one dataset question and one training or evaluation question to discuss in the Q&A.\n",3),blank(3)]}

def lab_readme(key, repo):
    lab=LABS[key]; n=lab["number"]; prefix=f"labs/lab{n}-{key}"
    text=f"# Lab {n}: {lab['title']}\n\n**Imperial I-X MSc AIAI | Deep Learning 2026/27 | Dr Dandan Zhang**\n\n{lab['goal']}\n\n"
    text+="**Two frameworks, two ways to open:**\n\n"
    for fw, label in [("keras","Keras 3 / TensorFlow"),("pytorch","PyTorch")]:
        path=f"{prefix}/lab{n}_{key}_{fw}.ipynb"
        text+=f"- **{label}:** [Jupyter notebook on GitHub](https://github.com/{repo}/blob/main/{path}) | [Open in Google Colab](https://colab.research.google.com/github/{repo}/blob/main/{path})\n"
    text+="\n**Code cells are blank by design:** Follow the instructions and write your own implementation.\n\n## Learning objectives\n\n"
    text+= "\n".join(f"- {x[1]}" for x in lab["steps"])
    text+="\n\n**After the lab:** Compare the training/validation evidence, explain two errors and discuss one limitation. This is unmarked formative learning.\n"
    return text

def render_home(released):
    txt="# Deep Learning | Student Laboratory Hub 2026-2027\n\n**Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**  \n**Module leader:** Dr Dandan Zhang\n\n"
    txt+="Four core practical labs are published weekly. Every released lab offers **Keras 3/TensorFlow and PyTorch**, each with **Jupyter on GitHub** (view/download) and **Google Colab** (run online). **All coding cells start blank:** there are no filled solutions.\n\n"
    txt+="[Start here](docs/STUDENT_START_HERE.md) | [Release calendar](docs/RELEASE_CALENDAR.md) | [Final Coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A)\n\n"
    txt+="| Release | Date | Topic | Availability |\n|---|---|---|---|\n"
    for slug, due, title, labs in WEEKS:
        if slug not in released: entry="Coming soon"
        elif slug=="orientation": entry="[Open orientation](orientation/START_HERE.md)"
        else: entry=" / ".join(f"[Lab {LABS[key]['number']} {key.upper()}](labs/lab{LABS[key]['number']}-{key}/README.md)" for key in labs)
        txt+=f"| {slug.replace('-',' ').title()} | {due} | {title} | {entry} |\n"
    txt+="\n## Study guidance\n\nRead the exercise first, predict tensor shapes, implement your own code, track validation behaviour and assess held-out examples. Use Google Colab or download the Jupyter file for VS Code/JupyterLab. Save your own copy before editing.\n\n"
    txt+="**Quizzes:** Three unmarked formative quizzes are delivered via Canvas, not GitHub. **Final Coursework:** assessment instructions and tactile datasets are separate; Canvas is the authoritative source.\n"
    return txt

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
        changes["orientation/START_HERE.md"]="# Week 0: Dataset release and preparation\n\n[Open setup notebook](environment_check.ipynb). The graded tactile dataset is available through the separate [Final Coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A); Canvas establishes the official course instructions. This is an unmarked Q&A and preparation session.\n"
        changes["orientation/environment_check.ipynb"]=json.dumps(orientation_notebook(),indent=2)+"\n"
    else:
        for key in week[3]:
            n=LABS[key]["number"]
            folder=f"labs/lab{n}-{key}"
            changes[f"{folder}/README.md"]=lab_readme(key,repo)
            for fw in ("keras","pytorch"):
                changes[f"{folder}/lab{n}_{key}_{fw}.ipynb"]=json.dumps(make_notebook(key,fw,repo),indent=2)+"\n"
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
