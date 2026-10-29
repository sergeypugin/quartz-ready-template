"""Tests for shared plumbing in common.py."""
import argparse
import os
import tempfile
import unittest
from pathlib import Path

from scripts import utils


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_resolve_root_valid(self):
        resolved = utils.resolve_root(self.root)
        self.assertEqual(resolved, self.root.resolve())

    def test_resolve_root_invalid(self):
        missing = self.root / "nonexistent"
        with self.assertRaises(ValueError):
            utils.resolve_root(missing)

    def test_add_root_argument(self):
        parser = argparse.ArgumentParser()
        utils.add_root_argument(parser)
        args = parser.parse_args([])
        self.assertTrue(hasattr(args, "root"))

    def test_markdown_files_finds_md_and_ignores_ignored_dirs(self):
        (self.root / "a.md").write_text("a", encoding="utf-8")
        (self.root / "sub").mkdir()
        (self.root / "sub" / "b.md").write_text("b", encoding="utf-8")
        (self.root / "node_modules").mkdir()
        (self.root / "node_modules" / "ignored.md").write_text("c", encoding="utf-8")
        (self.root / ".obsidian").mkdir()
        (self.root / ".obsidian" / "config.md").write_text("d", encoding="utf-8")

        files = utils.markdown_files(self.root)
        relative = [f.relative_to(self.root).as_posix() for f in files]
        self.assertEqual(relative, ["a.md", "sub/b.md"])

    def test_display_path_relative(self):
        file_path = Path.cwd() / "some_file.md"
        disp = utils.display_path(file_path)
        self.assertEqual(disp, "some_file.md")


if __name__ == "__main__":
    unittest.main()
