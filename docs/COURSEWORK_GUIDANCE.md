# Preparing for the Final Deep Learning Coursework

**Imperial I-X MSc AIAI | 2026–2027**

This page helps you prepare technically and organise your work. It does not replace your current Final Coursework handbook or any Canvas announcements. **Canvas is the authoritative source** for assessments, extension procedures, official marking instructions and submission.

## Assessment overview

| Component | Weight | Main work | Due (GMT) |
|---|---:|---|---|
| **Part A: Individual** | **60 marks** | Tactile shape classification, 3D contact-force regression and technical report | **13 Dec 2026, 23:59** |
| **Part B: Group** | **40 marks** | An advanced tactile-perception project with a working proof of concept and video | **20 Dec 2026, 23:59** |
| **Individual peer assessment** | Contributes to Part B moderation | Complete your own Canvas submission | **23 Dec 2026, 23:59** |

[Official Final Coursework project](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A) · [Assessment overview](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/docs/ASSESSMENT_OVERVIEW.md) · [Data preparation guide](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/docs/GETTING_STARTED.md)

The coursework repository and releases may require access. If you cannot open them, follow the **Canvas** materials and contact the module teaching team; do not assume the student lab repository includes the assessed dataset.

## Part A: What to prepare

The released tactile dataset contains **2,000 shape-classification images and 2,000 force-estimation images**. The two tasks require different prediction targets:

- **Shape:** classify each tactile image into one of ten shape categories; report meaningful class-level results and a confusion matrix.
- **Force:** predict the three contact-force components `fx`, `fy`, `fz` **in newtons**, with the original sign convention. Press and shear samples associated with the same physical contact require careful split handling.

The specified development approach uses **60% training, 20% validation and 20% test** partitions. Shape classification should use suitable class stratification; for force estimation, **split by contact ID** so paired press/shear observations never straddle the partitions. Fit data-dependent preprocessing only on training data, choose architectures on validation data and reserve the held-out test set for evaluation.

The supplied coursework guidance expects at least **three CNN architecture comparisons** for shape classification and at least **two architecture comparisons** for force regression. Report macro precision/recall/F1 and a confusion matrix for shape; report RMSE by force axis and overall for regression, with interpretation of press and shear behaviour.

**Part A submission format:** consult Canvas for the definitive package specification. The existing briefing describes a **3–6-page IEEE two-column report**, code and a CID-labelled model folder containing `predict.py`, all submitted as one ZIP. Check inference, dependency, runtime and model-size rules against the current handbook rather than relying only on a working notebook.

### Part A preparation checklist

- Read and understand the currently issued handbook.
- Access the approved dataset; inspect labels, image shapes and class distribution.
- Verify image-to-label mapping and contact-pair integrity.
- Create and **save** a leakage-free split with a documented seed.
- Establish at least one appropriate baseline before making architectural changes.
- Compare architectures with fair training budgets and relevant metrics.
- Track failures, uncertainty and resource requirements, not merely the highest score.
- Keep assessed code, reports and checkpoints in your **private working space**.

**Dataset rule:** these unmarked student labs use separate teaching datasets such as Fashion-MNIST, CIFAR-10 and synthetic sequences. They must not be treated as extra authorised training data for assessed Part A.

## Part B: Group project preparation

The group project focuses on a **stakeholder-relevant tactile-perception problem**, a **working proof-of-concept model**, credible evaluation and a presentation video of **no more than five minutes**. Every group member must contribute and present in their own voice.

| Milestone | Date |
|---|---|
| Group list confirmed | 23 Nov 2026 |
| Group charter and proposed project direction | 29 Nov 2026, 23:59 GMT |
| TA progress check | 30 Nov–4 Dec 2026 |
| Part B submission | 20 Dec 2026, 23:59 GMT |
| Peer assessment | 23 Dec 2026, 23:59 GMT |

Discuss the problem, intended stakeholder, relevant research literature, available data, evaluation metrics and division of work before implementing a complex architecture. **Do not use the Part A dataset or prohibited TacVerse GelSight subsets for Part B.** Check the current Canvas handbook for approved datasets and project directions.

## Assessment clarification and integrity

Different editions of the earlier and simplified handbook disagree on **Part B group size**, **optional bonus limits** and whether a **training-mean force baseline** is required or recommended. The simplified handbook explicitly defers to the full handbook when inconsistent. **Follow the version or clarification identified on Canvas; ask the teaching team if that remains unclear.** This student hub does not adjudicate those differences.

Part A is individual assessed work. Do not publish solution notebooks, model checkpoints, reports or private data in public GitHub repositories or Issues. Cite relevant datasets, papers and external code. Any permitted AI assistance must be verified and declared according to the current coursework policy; never fabricate results, references or experiments.

**Submission, official help and policy clarifications take place through Canvas**, not through this lab repository.
