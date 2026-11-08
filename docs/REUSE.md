# Reusing deep-learning-labs-2026-27-students

Student-facing Deep Learning laboratory hub, 2026–27.

**Current scope:** Scheduled blank worksheets and preparation guidance; unreleased labs and assessed solutions stay unpublished.


## Choose your route

Students should start with [the student guide](STUDENT_START_HERE.md) and [environment setup](ENVIRONMENT_SETUP.md). Google Colab needs no local GPU. GitHub previews notebooks but does not execute them. A downloaded notebook can also be opened in VS Code or JupyterLab.

For another teacher adapting this repository, preserve the blank coding cells and check the release schedule before making any notebook public. Course-specific dates, assessment links and institutional branding need review for a new cohort. This repository's presence on GitHub is not permission to redistribute unrelated teaching materials.

## Structure

| Path | Purpose |
|---|---|
| `README.md` | Student landing page and current release table |
| `docs/STUDENT_START_HERE.md` | Notebook and Git basics |
| `docs/ENVIRONMENT_SETUP.md` | Colab and local setup |
| `docs/COURSEWORK_GUIDANCE.md` | Coursework preparation and authoritative sources |
| `docs/STUDY_GUIDANCE.md` | Experimental habits and responsible AI use |
| `docs/RELEASE_CALENDAR.md` | Scheduled weekly availability |
| `release_manifest.json` | Published-week state |

Released `orientation/` and `labs/` directories appear only when their scheduled materials are published. Their absence before release is expected. Private coursework links require the relevant course permissions.

## Validate a local checkout

These commands check the current public content and simulate releases in temporary directories; they do not publish future notebooks:

```bash
python scripts/check_repository.py
python scripts/check_release.py
python -m unittest discover -s tests -v
```

Python 3.12 matches the existing notebook-check workflow. No deep learning framework is needed for these repository checks. Framework requirements belong to the released notebooks and environment guide.

## Expected outcomes and support

A released worksheet contains instructions and blank code cells in both supported frameworks. Work in your own copy and save it before closing Colab. Use Canvas for assessment decisions, deadlines and private student support; keep public bug reports limited to reproducible setup/documentation problems without assessed solutions.

The checks validate notebook structure and release visibility, not student answers or training results. The teaching schedule and assessment policy are unchanged by this maintenance update.

## Attribution and reuse permissions

No repository-wide licence file is included in this checkout. Confirm reuse and redistribution permissions with the relevant rights holders; this maintenance update does not add a licence or relicense upstream code, data or assets.

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the local workflow and what to include with a proposed change.
