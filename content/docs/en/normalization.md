---
title: Markdown Normalization
description: Python scripts for verifying math formulas, links, and embed spacing.
priority: 40
---

Small Python scripts that verify and format Markdown notes before Quartz builds your site.

Quartz requires specific syntax rules for certain Markdown features (such as display math delimiters). These scripts enforce those rules without npm dependencies.

## Standard Workflows

Run all checks from the root of the repository:

```bash
# Verify notes without modifying files
python scripts/main.py --check

# Format notes in place
python scripts/main.py
```

Pass `--root PATH` if your notes live outside the default `content` directory:

```bash
python scripts/main.py --check --root my-notes
```

## Running a Subset of Scripts

You can run specific scripts through `main.py` by naming them on the command line. They will run in the canonical order (`ensure_blank_after_embed` -> `convert_links` -> `check_math`):

```bash
# Check only math formatting and link relative-ness
python scripts/main.py --check check_math convert_links

# Fix only embeds spacing
python scripts/main.py ensure_blank_after_embed
```

Or invoke individual scripts directly:

```bash
python scripts/ensure_blank_after_embed.py [--check] [--root PATH]
python scripts/convert_links.py [--check] [--apply-all] [--root PATH]
python scripts/check_math.py [--check] [--root PATH]
```

## What Each Script Does

### ensure_blank_after_embed.py

Inserts a blank line after stand-alone image or note embeds (`![alt](path)` or `![[note]]`) so surrounding prose renders cleanly across Markdown parsers. Preserves quote prefixes inside blockquotes.

### convert_links.py

Rewrites Obsidian wikilinks (`[[note]]`, `![[image.png]]`) into relative Markdown links (`[note](note)`, `![image.png](image.png)`). If any target is missing or ambiguous, the script reports the line number and leaves files untouched.

### check_math.py

`remark-math` opens display formulas only when `$$` is alone on its own line. This script moves `$$` delimiters to separate lines, strips leading/trailing spaces in inline math (`$a + b$`), and reports unclosed display blocks or math inside headings.

> [!tip] Adding Your Own Script
> You can easily add a custom script to the pipeline:
> 1. Create a Python file in `scripts/` (e.g., `check_custom.py`).
> 2. Use `import utils` to access shared utilities like `markdown_files(root)` or `display_path(path)`.
> 3. Add your script name and its command to the `SCRIPTS` dictionary in `scripts/main.py`.
>
> Note: please keep code comments in English.

## Enabling in GitHub Actions

The current template workflow (`.github/workflows/deploy.yml`) builds and deploys the site; it does not run normalization. To add normalization, place one of the following steps in the `build` job before the Quartz build.

### Option 1: Verification Only (Strict)

CI will fail if your notes do not follow the canonical format.

```yaml
- name: Check Markdown normalization
  run: python scripts/main.py --check
```

### Option 2: Automatic Fix (Auto-commit)

This option formats notes and commits the changes back to the repository. It requires `permissions: contents: write`; use it only for trusted push events, not for pull requests.

```yaml
- name: Apply Markdown normalization
  run: |
    python scripts/main.py
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
    git add content/
    git diff --cached --quiet || git commit -m "chore: normalize markdown"
    git push origin "HEAD:${GITHUB_REF_NAME}"
```

---
[[docs/en/index|Back to Documentation]]
