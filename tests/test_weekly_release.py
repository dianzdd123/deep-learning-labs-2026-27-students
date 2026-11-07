"""Simulate every date-gated release without publishing actual student content."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from release_week import REPO, WEEKS, LABS, make_notebook, orientation_notebook, publish_week, render_home

class WeeklyReleaseTests(unittest.TestCase):
    def setUp(self):
        self.work=tempfile.TemporaryDirectory()
        self.root=Path(self.work.name)
        (self.root/"README.md").write_text(render_home(set()))
        (self.root/"release_manifest.json").write_text('{"released":[]}\n')
    def tearDown(self):
        self.work.cleanup()

    def test_no_code_answers(self):
        for key in LABS:
            for fw in ("keras","pytorch"):
                book=make_notebook(key,fw,REPO)
                self.assertEqual(book["nbformat"],4)
                self.assertGreaterEqual(sum(c["cell_type"]=="code" for c in book["cells"]),5)
                self.assertTrue(all(not "".join(c["source"]).strip() for c in book["cells"] if c["cell_type"]=="code"))
        self.assertTrue(all(c["cell_type"]!="code" or not c["source"] for c in orientation_notebook()["cells"]))

    def test_release_schedule_and_idempotency(self):
        for slug,dt,title,labs in WEEKS:
            wrote=publish_week(self.root,slug,REPO)
            self.assertTrue(wrote)
            self.assertEqual(publish_week(self.root,slug,REPO),[])
            for key in labs:
                n=LABS[key]["number"]
                for fw in ("keras","pytorch"):
                    fn=self.root/f"labs/lab{n}-{key}/lab{n}_{key}_{fw}.ipynb"
                    self.assertTrue(fn.exists())
                    book=json.loads(fn.read_text())
                    self.assertTrue(all(not c["source"] for c in book["cells"] if c["cell_type"]=="code"))
        m=json.loads((self.root/"release_manifest.json").read_text())
        self.assertEqual(len(m["released"]),4)

    def test_preview_and_future_not_visible(self):
        preview=publish_week(self.root,"orientation",REPO,True)
        self.assertTrue(preview)
        self.assertFalse((self.root/"orientation").exists())
        self.assertFalse((self.root/"labs").exists())
        self.assertIn("Coming soon",(self.root/"README.md").read_text())

if __name__=="__main__":
    unittest.main()
