#!/usr/bin/env python3
"""Insert a blank line after every embed line.

An embed is a line made entirely of `![alt](path)` or `![[file]]`.
Inside a blockquote the blank line gets the same `>` prefix so the
quote is not broken.
"""
import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import utils

FENCE = re.compile(r"^\s*(```|~~~)")
BLANK = re.compile(r"^\s*(?:>\s*)*$")
EMBED = re.compile(
    r"^(?P<quote>\s*(?:>\s*)*)(?:!\[[^\]\n]*\]\((?:<[^>\n]*>|[^)\n]*)\)|!\[\[[^\]\n]*\]\])\s*$"
)


def frontmatter_end(lines):
    """Index of the closing `---`, or None when there is no frontmatter."""
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return index
    return None


def rewrite(text):
    """Return the new text and whether it changed; trailing newlines are preserved."""
    end = len(text) - len(text.rstrip("\n"))
    lines = text[: len(text) - end].split("\n")
    closing = frontmatter_end(lines)
    out = lines[: closing + 1] if closing is not None else []
    fence, changed, index = None, False, len(out)

    while index < len(lines):
        line = lines[index]
        index += 1
        out.append(line)
        match = FENCE.match(line)
        if fence:
            fence = None if match and match.group(1) == fence else fence
        elif match:
            fence = match.group(1)
        elif index < len(lines) and (embed := EMBED.match(line)):
            blank = embed.group("quote").rstrip()
            if lines[index].strip() != blank:
                changed = True
                if BLANK.match(lines[index]):
                    lines[index] = blank
                else:
                    out.append(blank)

    return "\n".join(out) + "\n" * end, changed


def process_file(path, write=True):
    """Process one file and return True if it changed."""
    path = Path(path)
    result, changed = rewrite(path.read_text(encoding="utf-8"))
    if changed and write:
        path.write_text(result, encoding="utf-8", newline="\n")
    return changed


def process_tree(root, write=True):
    """Process the note tree and return the paths that need a change, relative to root."""
    root = Path(root)
    return [
        path.relative_to(root)
        for path in utils.markdown_files(root)
        if process_file(path, write)
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Insert a blank line after embeds.")
    utils.add_root_argument(parser)
    parser.add_argument("--check", action="store_true", help="report instead of writing")
    arguments = parser.parse_args(argv)

    try:
        root = utils.resolve_root(arguments.root)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2

    changed = process_tree(root, write=not arguments.check)
    if arguments.check and changed:
        print(f"Embeds without a blank line: {len(changed)} file(s).", file=sys.stderr)
        for path in changed:
            print(f"  {utils.display_path(root / path)}", file=sys.stderr)
        return 1

    report = f"Modified {len(changed)} file(s):" if changed else "No changes needed"
    print(
        "\n".join([report, *(f"  {utils.display_path(root / path)}" for path in changed)]),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
