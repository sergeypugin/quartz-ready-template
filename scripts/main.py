#!/usr/bin/env python3
"""Bring notes to the canonical form in one run.

The order matters: blank lines after embeds are inserted before link
conversion, and math is formatted last.

Without arguments files are fixed; with `--check` they are only
verified. Pass script names to run a subset:

    python scripts/main.py
    python scripts/main.py --check
    python scripts/main.py ensure_blank_after_embed convert_links
"""
import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import utils

# The fixed order of a full run. convert_links uses --apply-all instead of --check.
SCRIPTS = {
    "ensure_blank_after_embed": ("ensure_blank_after_embed.py", None),
    "convert_links": ("convert_links.py", "--apply-all"),
    "check_math": ("check_math.py", None),
}
ORDER = list(SCRIPTS)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Bring Markdown notes to the canonical form.",
        epilog="script names (subset): " + ", ".join(ORDER),
    )
    utils.add_root_argument(parser)
    parser.add_argument("--check", action="store_true", help="report instead of writing")
    parser.add_argument(
        "scripts",
        nargs="*",
        choices=ORDER,
        metavar="script",
        help=f"run only these scripts: {', '.join(ORDER)}",
    )
    arguments = parser.parse_args(argv)

    try:
        root = utils.resolve_root(arguments.root)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2

    selected = arguments.scripts or ORDER
    # A subset runs in the canonical order regardless of the argument order.
    for name in [script for script in ORDER if script in selected]:
        script, apply_mode = SCRIPTS[name]
        command = [sys.executable, str(SCRIPT_DIR / script), "--root", str(root)]
        if arguments.check:
            command.append("--check")
        elif apply_mode:
            command.append(apply_mode)
        result = subprocess.run(command)
        if result.returncode != 0:
            if arguments.check:
                print(f"{script}: notes are not in the canonical form.", file=sys.stderr)
                print(
                    "Run `python scripts/main.py` and commit the changes.",
                    file=sys.stderr,
                )
            return result.returncode

    print(
        "All notes are in the canonical form."
        if arguments.check
        else "Notes are in the canonical form."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
