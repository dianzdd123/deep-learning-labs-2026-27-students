"""Exercise release boundaries and the learning route in isolated temporary copies."""
import ast
import contextlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_release import validate
from release_week import LABS, REPO, WEEKS, make_notebook, publish_week, python_worksheet, render_home


class StudentJourneyTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.root = Path(self.workspace.name) / "student-copy"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "my_work", "data", "runs", "results"))
        for folder in ["orientation", "labs", "release_notes"]:
            shutil.rmtree(self.root / folder, ignore_errors=True)
        (self.root / "release_manifest.json").write_text('{"released": []}\n')
        (self.root / "README.md").write_text(render_home(set()))

    def tearDown(self):
        self.workspace.cleanup()

    def release(self, slug):
        with contextlib.redirect_stdout(io.StringIO()):
            return publish_week(self.root, slug, REPO)

    def command(self, *args):
        return subprocess.run([sys.executable, str(self.root / "scripts/release_week.py"),
                               "--root", str(self.root), *args], capture_output=True, text=True)

    def test_before_first_release_has_no_worksheets(self):
        result = self.command("--as-of", "2026-11-08")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(validate(self.root), (0, 0))
        self.assertEqual((self.root / "README.md").read_text().count("| Coming soon |"), 4)

    def test_explicit_week_is_date_gated(self):
        result = self.command("--week", "cnn-resnet", "--as-of", "2026-11-10")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "labs").exists())
        self.assertEqual(validate(self.root), (0, 0))

    def test_due_week_releases_only_due_content(self):
        result = self.command("--as-of", "2026-11-10")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(validate(self.root), (1, 1))
        self.assertFalse((self.root / "labs").exists())
        self.assertIn("Open in Colab", (self.root / "orientation/START_HERE.md").read_text())

    def test_dry_run_does_not_change_state(self):
        before = (self.root / "release_manifest.json").read_bytes()
        result = self.command("--as-of", "2026-12-01", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "release_manifest.json").read_bytes(), before)
        self.assertEqual(validate(self.root), (0, 0))

    def test_guidance_and_links_survive_all_releases(self):
        for slug, _, _, _ in WEEKS:
            self.release(slug)
            home = (self.root / "README.md").read_text()
            for target in ["STUDENT_START_HERE.md", "ENVIRONMENT_SETUP.md", "NOTEBOOK_BASICS.md",
                           "LAB_WORKFLOW.md", "LEARNING_LOG.md", "GETTING_HELP.md"]:
                self.assertIn(target, home)
            self.assertIn("https://zhangrobotics.com/msei_website/", home)
        self.assertEqual(validate(self.root), (9, 4))
        for path in [self.root / "README.md", *self.root.glob("labs/*/README.md"),
                     self.root / "orientation/START_HERE.md"]:
            for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text()):
                if ":" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent / target.split("#")[0]).exists(), (path, target))

    def test_python_worksheets_have_instructions_but_no_solution_code(self):
        for topic in LABS:
            for framework in ["keras", "pytorch"]:
                script = python_worksheet(make_notebook(topic, framework, REPO))
                self.assertEqual(ast.parse(script).body, [])
                self.assertIn("# %% [markdown]", script)
                self.assertIn("Add your own implementation here", script)
                self.assertIn("LEARNING_LOG.md", script)
        rnn = make_notebook("rnn", "pytorch", REPO)
        prose = "\n".join("".join(c["source"]) for c in rnn["cells"])
        self.assertIn("batch_first=True", prose)
        self.assertNotIn("channels-first images", prose)

    def test_filled_code_and_outputs_are_rejected(self):
        self.release("orientation")
        notebook_path = self.root / "orientation/environment_check.ipynb"
        notebook = json.loads(notebook_path.read_text())
        cell = next(c for c in notebook["cells"] if c["cell_type"] == "code")
        cell["source"] = ["answer = 1\n"]
        notebook_path.write_text(json.dumps(notebook))
        with self.assertRaises(AssertionError):
            validate(self.root)
        cell["source"] = []
        cell["execution_count"] = 1
        notebook_path.write_text(json.dumps(notebook))
        with self.assertRaises(AssertionError):
            validate(self.root)

    def test_filled_python_is_rejected_and_releases_do_not_overwrite(self):
        self.release("orientation")
        script = self.root / "orientation/environment_check.py"
        script.write_text(script.read_text() + "answer = 1\n")
        changed = script.read_bytes()
        with self.assertRaises(AssertionError):
            validate(self.root)
        self.assertEqual(self.release("orientation"), [])
        self.assertEqual(script.read_bytes(), changed)

    def test_published_home_matches_current_template(self):
        released = set(json.loads((ROOT / "release_manifest.json").read_text())["released"])
        self.assertEqual((ROOT / "README.md").read_text(), render_home(released))


if __name__ == "__main__":
    unittest.main()
