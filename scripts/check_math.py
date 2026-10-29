#!/usr/bin/env python3
"""Put every `$$` on its own line.

remark-math opens a display formula only when `$$` occupies a whole line.
A delimiter glued to the formula (`a =$$` or `$$= b`) is read as inline
math, the block never closes and swallows headings and paragraphs up to
the next `$$`.
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
HEADING = re.compile(r"^#{1,6}\s")
QUOTE = re.compile(r"^(\s*(?:>\s*)*)")
INLINE = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)(?<!\$)\$(?!\$)")
DOLLARS = re.compile(r"(?<!\\)\$+")
CODE_SPAN = re.compile(r"(`+)(.*?)\1")


def mask_code(text):
    return CODE_SPAN.sub(lambda match: " " * len(match.group(0)), text)


def split_display(text):
    """Cut a line into chunks around `$$` and collect notes about broken delimiters.

    A leftover `$` in `$$$` stays text instead of inventing another delimiter.
    """
    visible = mask_code(text)
    chunks = []
    notes = []
    cursor = 0
    singles = 0

    for match in DOLLARS.finditer(visible):
        width = match.end() - match.start()
        if width == 1:
            singles += 1
            continue
        chunks.append((text[cursor:match.start()], False))
        chunks.extend([("$$", True)] * (width // 2))
        cursor = match.end()
        if width % 2:
            notes.append("odd number of `$` in a row")
            cursor -= 1

    chunks.append((text[cursor:], False))
    if singles % 2:
        notes.append("unpaired `$`, looks like an unterminated inline formula")
    return chunks, notes


def normalize_inline(line):
    stripped = line.strip()
    if stripped.startswith("|") and stripped.endswith("|"):
        return line
    if "`" in line:
        masked = mask_code(line)
        pieces = []
        last = 0
        for match in INLINE.finditer(masked):
            pieces.append(line[last:match.start()])
            pieces.append(f"${line[match.start() + 1 : match.end() - 1].strip()}$")
            last = match.end()
        if not pieces:
            return line
        pieces.append(line[last:])
        return "".join(pieces)
    return INLINE.sub(lambda match: f"${match.group(1).strip()}$", line)


class Formatter:
    def __init__(self):
        self.lines = []
        self.warnings = []
        self.fence = None
        self.frontmatter = False
        self.inside = False

    def format(self, text):
        for number, line in enumerate(text.splitlines(), 1):
            self.handle(number, line)
        if self.inside:
            self.warnings.append("display formula is not closed before the end of the file")
        result = "\n".join(self.lines)
        return result + "\n" if text.endswith(("\n", "\r")) else result

    def handle(self, number, line):
        fence = FENCE.match(line)
        if self.fence:
            if fence and fence.group(1) == self.fence:
                self.fence = None
            self.lines.append(line)
            return
        if fence:
            self.fence = fence.group(1)
            self.lines.append(line)
            return

        if number == 1 and line.strip() == "---":
            self.frontmatter = True
            self.lines.append(line)
            return
        if self.frontmatter:
            if line.strip() == "---":
                self.frontmatter = False
            self.lines.append(line)
            return

        quote = QUOTE.match(line)
        prefix = quote.group(1) if quote else ""
        content = line[len(prefix):]

        if HEADING.match(content):
            if "$" in content:
                self.warnings.append(f"line {number}: formula in a heading")
            self.lines.append(line)
            return

        chunks, notes = split_display(content)
        for note in notes:
            self.warnings.append(f"line {number}: {note}")

        if not any(delimiter for _, delimiter in chunks):
            self.lines.append(line if self.inside else normalize_inline(line))
            return

        for chunk, delimiter in chunks:
            strip = chunk.strip()
            if delimiter:
                self.lines.append(prefix + "$$")
                self.inside = not self.inside
            elif strip:
                if self.inside:
                    self.lines.append(prefix + strip)
                else:
                    self.lines.append(normalize_inline(prefix + strip))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Put every `$$` on its own line.")
    utils.add_root_argument(parser)
    parser.add_argument("--check", action="store_true", help="report instead of writing")
    arguments = parser.parse_args(argv)

    try:
        root = utils.resolve_root(arguments.root)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2

    warnings = 0
    changes = []
    for path in utils.markdown_files(root):
        original = path.read_text(encoding="utf-8")
        formatter = Formatter()
        formatted = formatter.format(original)

        for warning in formatter.warnings:
            print(f"{utils.display_path(path)}: {warning}", file=sys.stderr)
            warnings += 1
        if formatted != original:
            changes.append(path)
            if not arguments.check:
                path.write_text(formatted, encoding="utf-8", newline="\n")

    if arguments.check and changes:
        print(f"Math is not formatted: {len(changes)} file(s).", file=sys.stderr)
        for path in changes:
            print(f"  {utils.display_path(path)}", file=sys.stderr)
        return 1
    if arguments.check and warnings:
        print(f"Math check failed: {warnings} problem(s).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
