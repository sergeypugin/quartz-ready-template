"""Shared plumbing for the Markdown normalization scripts."""
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_DIR.parent
DEFAULT_CONTENT_DIR = "content"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}


def add_root_argument(parser):
    """Add standard --root argument pointing to default notes directory."""
    parser.add_argument(
        "--root",
        type=Path,
        default=REPOSITORY_ROOT / DEFAULT_CONTENT_DIR,
        metavar="PATH",
        help=f"notes directory (default: {DEFAULT_CONTENT_DIR})",
    )


def resolve_root(path):
    """Return an existing directory or raise ValueError with a readable message."""
    root = Path(path).resolve()
    if not root.is_dir():
        raise ValueError(f"notes directory not found: {root}")
    return root


def markdown_files(root):
    """All Markdown files under root, sorted, minus ignored directories."""
    root = Path(root).resolve()
    ignored = {d.lower() for d in IGNORED_DIRS}
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d.lower() not in ignored]
        for filename in filenames:
            if filename.lower().endswith(".md"):
                files.append(Path(dirpath) / filename)
    return sorted(files)


def display_path(path):
    """Shortest readable form of a path: relative to the working directory when possible."""
    resolved = Path(path).resolve()
    cwd = Path.cwd().resolve()
    try:
        return resolved.relative_to(cwd).as_posix()
    except ValueError:
        try:
            rel = os.path.relpath(resolved, cwd)
            if not rel.startswith(".."):
                return Path(rel).as_posix()
        except ValueError:
            pass
        return resolved.as_posix()
