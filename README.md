# Deep Learning | Student Laboratory Hub 2026–2027

**ELEC70129 · Imperial College London · I-X MSc AIAI**  
**Module leader: Dr Dandan Zhang**

Learn to build, inspect and explain a deep learning experiment. Start with one framework and work through the four unmarked labs: **CNN → ResNet → RNN → Transformer**.

**Course home:** [Teaching page](https://www.intelligentrobotics-acrossscales.com/teaching). Use it for the course introduction, lecture materials, handbook previews, videos and the Main labs / Additional sessions overview. **Canvas** holds the current assessment handbook, briefing slides, official announcements and submission links.

**Student course access:** contact [Dr Dandan Zhang](mailto:d.zhang17@imperial.ac.uk) at **d.zhang17@imperial.ac.uk**, quoting your module code and the resource title. This public repository contains preparation guides and, when published here, blank student worksheets. Authorised notebooks linked from the teaching page may require separate course access.

## Start in three steps

1. **New here?** Follow [Start here](docs/STUDENT_START_HERE.md). It explains what to do before the first lab.
2. **Set up once:** choose [Colab or local VS Code/Jupyter](docs/ENVIRONMENT_SETUP.md), then run the small readiness check.
3. **When your lab is released:** open its page below, save your own copy and follow the [lab workflow](docs/LAB_WORKFLOW.md).

**Choose Keras/TensorFlow or PyTorch for your first run.** You do not need both. Released notebooks have deliberately blank code cells; writing the code is the exercise. GitHub previews files; Colab or a local Python kernel executes them.

## Weekly worksheets

This table reports **blank worksheet availability in this public repository**, not the availability of lecture slides, authorised worked examples or the assessed dataset. Preparation is separate from the four numbered main labs. [Full teaching and release calendar](docs/RELEASE_CALENDAR.md).

**Part A data has been released:** use the separate [Final Coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A) and its dataset download instructions. A Coming soon worksheet entry below does not mean the coursework data is unreleased.

| Release | Date, 2026 | Topic | Open the worksheet |
|---|---|---|---|
| Preparation (not a main lab) | 2026-11-10 | Environment check and coursework data exploration | Coming soon |
| Lab 1 + Lab 2 | 2026-11-17 | CNN and ResNet | Coming soon |
| Lab 3 | 2026-11-24 | Recurrent Neural Networks | Coming soon |
| Lab 4 | 2026-12-01 | Transformer and Attention | Coming soon |

Each released lab page offers a notebook, a Colab link and a matching blank Python worksheet for each framework. Save completed work in your own files. If a date has passed but a link is not yet available, check Canvas for the teaching team's announcement.

## Four main labs

These lab numbers match **Main labs** on the [teaching page](https://www.intelligentrobotics-acrossscales.com/teaching). Choose Keras 3 / TensorFlow or PyTorch; the eight framework options represent **four labs**, not eight required sessions.

| Lab | Teaching date, 2026 | Practice dataset | Focus |
|---|---|---|---|
| 1 · CNN | 17 November | Fashion-MNIST, 28 × 28 greyscale images | Receptive fields, shared filters, pooling and classification |
| 2 · ResNet | 17 November | CIFAR-10, 32 × 32 colour images | Compact plain versus residual models under a matched training budget |
| 3 · RNN | 24 November | Synthetic forward/reverse sequence pairs | RNN, GRU and LSTM; keep correlated pairs in the same split |
| 4 · Transformer | 1 December | Fashion-MNIST image patches | Sixteen 7 × 7 patch tokens and an encoder classifier |

The ResNet exercise is a compact teaching comparison. The Transformer exercise is an **image-patch encoder classifier**, not a complete Seq2Seq translator, language model or diffusion model.

## Additional sessions are optional

The teaching page also lists setup/tensors/training, image folders (Cats vs Dogs), text sentiment (IMDb), ResNet transfer learning, and earlier CNN, ResNet, RNN and attention tutorials. These are preparation or independent-study extensions, with **no extra required labs or scheduled teaching dates**. They are not part of this repository's four-lab worksheet release sequence. Use the teaching page and approved course access for their availability.

GNNs, full Seq2Seq, diffusion and AGI are lecture or reading topics; this public worksheet repository does not supply runnable labs for them. A blank student worksheet needs your implementation before it can train a model.

## Use the guides when you need them

[All student guides](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/README.md).

| I want to… | Open |
|---|---|
| Set up a notebook for the first time | [Start here](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/STUDENT_START_HERE.md) |
| Install locally or choose a Colab runtime | [Environment setup](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/ENVIRONMENT_SETUP.md) |
| Understand cells, kernels, Python worksheets and saving | [Notebook basics](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/NOTEBOOK_BASICS.md) |
| Work through a lab and know what to check | [Lab workflow](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/LAB_WORKFLOW.md) |
| Record my settings, evidence and reflection | [Learning-log template](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/LEARNING_LOG.md) |
| Find a focused reading or explain a term | [Reading guide](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/READING_GUIDE.md) · [Glossary](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/GLOSSARY.md) |
| Resolve an error or ask a useful question | [Troubleshooting](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/TROUBLESHOOTING.md) · [Get help](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/GETTING_HELP.md) |

## Practice, quizzes and assessed coursework

The four labs are **formative and unmarked**. Three unmarked quizzes are delivered
through Canvas. Keep your own completed worksheets and results; do not post solutions
in this public repository. Use the [study and AI-use guidance](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/STUDY_GUIDANCE.md)
for practice, and the official Canvas policy for assessed work.

| Assessment | Published deadline, GMT |
|---|---|
| Part A: individual, 60 marks | 13 December 2026, 23:59 |
| Part B: group, 40 marks | 20 December 2026, 23:59 |
| Peer assessment | 23 December 2026, 23:59 |

**Canvas is authoritative** for the current handbook, submission links, group rules,
quiz availability and clarified assessment policies. Read the
[coursework guidance](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/blob/main/docs/COURSEWORK_GUIDANCE.md)
and use the [Final Coursework repository](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A)
for the **released Part A tactile dataset**, setup and submission-interface instructions. Follow that repository's dataset download link; downloading this lab repository does not provide the coursework images. Practice datasets and results are not assessed submissions.

On the teaching page, published slides and handbooks have cover previews and open in a view-only reader; videos have visible previews. Public PDF viewing needs no activation code. A PDF download requires an activation code, which is separate from student notebook/course access. The final coursework section displays the **nine-page Simplified Handbook**; use the current Canvas handbook and clarifications for assessment decisions.


## Course and wider resources

[Teaching page](https://www.intelligentrobotics-acrossscales.com/teaching) · [MSEI Lab website](https://zhangrobotics.com/msei_website/) · [MSEI website on GitHub](https://github.com/dianzdd123/msei_website)

For proposed material fixes or reuse, see [Contributing](CONTRIBUTING.md) and [Reuse guidance](docs/REUSE.md). Reuse permissions need clarification because this repository has no repository-wide licence file.
