"""Run the actual image workflow commit block against local Git remotes."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHELL = os.environ.get("WORKFLOW_TEST_SHELL") or shutil.which("bash") or shutil.which("sh")


class ImageWorkflowCommitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="kandaka-image-workflow-")
        self.root = Path(self.temp.name).resolve()
        assert self.root.parent == Path(tempfile.gettempdir()).resolve()
        self.addCleanup(self.temp.cleanup)
        self.remote = self.root / "remote.git"
        self.writer = self.root / "writer"
        self.runner = self.root / "runner"
        self.git(self.root, "init", "--bare", "--initial-branch=main", str(self.remote))
        self.git(self.root, "clone", str(self.remote), str(self.writer))
        self.git(self.writer, "config", "user.name", "Fixture")
        self.git(self.writer, "config", "user.email", "fixture@example.invalid")
        (self.writer / "content/images").mkdir(parents=True)
        (self.writer / "content/images/existing.md").write_text("existing\n")
        self.git(self.writer, "add", ".")
        self.git(self.writer, "commit", "-m", "Initial fixture")
        self.git(self.writer, "push", "origin", "main")
        self.git(self.root, "clone", str(self.remote), str(self.runner))
        workflow = (ROOT / ".github/workflows/daily-rebuild.yml").read_text()
        match = re.search(r"      - name: Commit and push new content\n        run: \|\n((?:          [^\n]*\n?)+)", workflow)
        self.assertIsNotNone(match)
        self.block = textwrap.dedent(match.group(1))

    def git(self, cwd, *args):
        return subprocess.check_output(["git", *args], cwd=cwd, stderr=subprocess.STDOUT, text=True).strip()

    def advance_remote(self):
        (self.writer / "unrelated.md").write_text("Concurrent work\n")
        self.git(self.writer, "add", "unrelated.md")
        self.git(self.writer, "commit", "-m", "Concurrent work")
        self.git(self.writer, "push", "origin", "main")
        return self.git(self.remote, "rev-parse", "main")

    def run_block(self):
        self.assertIsNotNone(SHELL, "Set WORKFLOW_TEST_SHELL to a POSIX shell")
        return subprocess.run([SHELL, "-e", "-c", self.block], cwd=self.runner, capture_output=True, text=True)

    def test_unchanged_stale_checkout_skips_push(self):
        before = self.git(self.runner, "rev-parse", "HEAD")
        advanced = self.advance_remote()
        result = self.run_block()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("skipping commit and push", result.stdout)
        self.assertEqual(self.git(self.runner, "rev-parse", "HEAD"), before)
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), advanced)

    def test_new_image_is_committed_and_pushed_with_scoped_files(self):
        (self.runner / "content/images/new.md").write_text("New draft candidate\n")
        (self.runner / "unrelated-untracked.md").write_text("Do not commit\n")
        result = self.run_block()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git(self.runner, "rev-parse", "HEAD"), self.git(self.remote, "rev-parse", "main"))
        self.assertEqual(self.git(self.remote, "diff-tree", "--no-commit-id", "--name-only", "-r", "main"), "content/images/new.md")

    def test_real_changed_content_push_conflict_remains_visible(self):
        advanced = self.advance_remote()
        (self.runner / "content/images/new.md").write_text("New draft candidate\n")
        result = self.run_block()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), advanced)
        self.assertNotIn("skipping commit and push", result.stdout)


if __name__ == "__main__":
    unittest.main()
