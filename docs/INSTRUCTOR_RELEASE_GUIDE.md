# Instructor guide: weekly releases

The public student repository intentionally contains only **student instructions and empty code cells**. Future prompt text is part of its public release generator; future notebooks themselves appear only when due. If you require the *questions themselves* to remain confidential, move generation to a private instructor repository rather than relying on the absence of links.

## Operation

- [Student home](../README.md) shows **Coming soon** until a week is published.
- [Release calendar](RELEASE_CALENDAR.md) specifies **10, 17, 24 November and 1 December 2026**.
- [Weekly student lab release](../.github/workflows/weekly-release.yml) runs at **08:35 UTC every Tuesday**, equivalent to 08:35 London time on all four November/December dates.
- [Python release script](../scripts/release_week.py) generates paired Keras/PyTorch `.ipynb` files with *empty code cells*. It does not copy from the private instructor repository.
- [Validation](../scripts/check_release.py) blocks incomplete or prefilled coding cells.

## Initial setup

1. Visit [Settings > Actions > General](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/settings/actions) and allow Actions and **Read and write permissions** for `GITHUB_TOKEN`, if your settings permit this.
2. Open [Actions > Weekly student lab release](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/actions/workflows/weekly-release.yml).
3. Click **Run workflow** with `week=auto` and `dry_run=true` to preview. When a week is due, use `dry_run=false` to publish.
4. Check the new student links and [Actions logs](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/actions).

## Controls

- `week=auto` publishes any due weeks that are not already published.
- `week=cnn-resnet`, `rnn` etc. publish one selected week.
- `allow_early=true` explicitly overrides the date guard.
- `dry_run=true` prints intended paths without changing anything.
- Repeated runs do not overwrite already released notebooks, protecting student-facing edits.

The action commits new materials and creates a GitHub Release snapshot. A scheduled execution can be delayed or missed; manually dispatch it if necessary. Verify new links and notebook content before announcing in Canvas.

**Staff-only**: Never put completed teacher solutions, confidential quiz questions or answers, student personal data, private coursework, or API tokens in this repository.
