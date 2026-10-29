"""Tests for the single entry point."""
import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from scripts import main


class MainTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def run_main(self, *args):
        output = io.StringIO()
        with mock.patch.object(main.subprocess, "run") as run, redirect_stdout(output):
            run.return_value = subprocess.CompletedProcess(args=[], returncode=0)
            code = main.main(["--root", str(self.root), *args])
        return code, run.call_args_list

    def test_rejects_unknown_arguments(self):
        with mock.patch.object(main.subprocess, "run") as run, redirect_stdout(
            io.StringIO()
        ), mock.patch.object(sys, "stderr", io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main.main(["--root", str(self.root), "--fix"])
        self.assertEqual(raised.exception.code, 2)
        self.assertEqual(run.call_args_list, [])

    def test_fix_run_uses_expected_commands(self):
        code, calls = self.run_main()

        self.assertEqual(code, 0)
        commands = [call.args[0] for call in calls]
        self.assertEqual(len(commands), 3)
        self.assertTrue(commands[0][1].endswith("ensure_blank_after_embed.py"))
        self.assertTrue(commands[1][1].endswith("convert_links.py"))
        self.assertIn("--apply-all", commands[1])
        self.assertTrue(commands[2][1].endswith("check_math.py"))

    def test_check_run_passes_check_flag(self):
        code, calls = self.run_main("--check")

        self.assertEqual(code, 0)
        for call in calls:
            self.assertEqual(call.args[0][-1], "--check")

    def test_root_is_forwarded_to_every_script(self):
        code, calls = self.run_main("check_math")

        self.assertEqual(code, 0)
        command = calls[0].args[0]
        self.assertEqual(command[command.index("--root") + 1], str(self.root))

    def test_subset_runs_only_named_scripts_in_canonical_order(self):
        code, calls = self.run_main("convert_links", "ensure_blank_after_embed")

        self.assertEqual(code, 0)
        scripts = [Path(call.args[0][1]).name for call in calls]
        self.assertEqual(scripts, ["ensure_blank_after_embed.py", "convert_links.py"])

    def test_subset_with_check_flag(self):
        code, calls = self.run_main("--check", "check_math")

        self.assertEqual(code, 0)
        self.assertEqual(len(calls), 1)
        self.assertTrue(calls[0].args[0][-1] == "--check")

    def test_rejects_missing_root(self):
        with mock.patch.object(main.subprocess, "run") as run, redirect_stdout(
            io.StringIO()
        ), mock.patch.object(sys, "stderr", io.StringIO()):
            code = main.main(["--root", str(self.root / "missing")])

        self.assertEqual(code, 2)
        self.assertEqual(run.call_args_list, [])

    def test_stops_on_first_failure(self):
        with mock.patch.object(main.subprocess, "run") as run, redirect_stdout(
            io.StringIO()
        ), mock.patch.object(sys, "stderr", io.StringIO()):
            run.return_value = subprocess.CompletedProcess(args=[], returncode=1)
            code = main.main(["--root", str(self.root), "--check"])

        self.assertEqual(code, 1)
        self.assertEqual(run.call_count, 1)


class MainIntegrationTest(unittest.TestCase):
    def test_scripts_exist(self):
        for script, _ in main.SCRIPTS.values():
            self.assertTrue((main.SCRIPT_DIR / script).is_file(), script)

    def test_clean_tree_passes_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.png").write_bytes(b"x")
            (root / "page.md").write_text(
                "# Title\n\n$S = a + b$\n\n![x](a.png)\n\ntext\n",
                encoding="utf-8",
                newline="\n",
            )
            result = subprocess.run(
                [sys.executable, str(main.SCRIPT_DIR / "main.py"), "--check", "--root", tmp],
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unformatted_tree_fails_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "page.md").write_text(
                "![x](a.png)\ntext\n", encoding="utf-8", newline="\n"
            )
            result = subprocess.run(
                [sys.executable, str(main.SCRIPT_DIR / "main.py"), "--check", "--root", tmp],
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
