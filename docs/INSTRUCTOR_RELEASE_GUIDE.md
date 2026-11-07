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

## Initial Actions diagnostic and manual fallback

**Status on 7 November 2026:** the repository and workflows are installed, but the initial validation workflow runs reported a GitHub Actions **failure before any job steps were returned**. The GitHub connector cannot retrieve execution logs or adjust repository Actions/billing settings, so automated publication is **configured but not confirmed operational**. Review the [Actions run page](https://github.com/dianzdd123/deep-learning-labs-2026-27-students/actions/runs/42410088045), then check repository **Settings > Actions > General**, available hosted-runner minutes and any account billing or policy restrictions. Once a validation run succeeds, test the release workflow using its `dry_run=true` input. Do not assume a future scheduled run will succeed until these checks are completed.

For a manual release if Actions is unavailable, clone the **student** repository to your computer, then run these commands from its root. Do not clone or publish the private instructor repository:

```bash
# Preview all weeks due as of today
python scripts/release_week.py --week auto --dry-run
# Publish only due weeks, generating empty-code student notebooks
python scripts/release_week.py --week auto
python scripts/check_release.py
git add README.md release_manifest.json labs orientation release_notes
git commit -m "Publish due weekly lab instructions"
git push origin main
```

Only use the commands on or after a release date. The release script is date-gated; `--allow-early` exists for an explicitly intended early release. The script is idempotent and will not overwrite an already published week. On Windows, use PowerShell or Git Bash after installing Python and Git.
