---
title: Features
description: Supported Markdown extensions, callouts, wiki-links, Canvas, Bases, and image sizes.
priority: 10
---

GitHub's Markdown renderer does not support every extension Quartz can render. Quartz also processes Obsidian-compatible syntax and file formats, including:

- **Wiki-style links:** `[[Note name]]` and `[[Note name|Custom text]]` with automatic path resolution.
- **Callouts:** `> [!quote]`, `> [!success]`, `> [!bug]`, and more, including folding and custom titles such as `> [!note]- Clarification` and `> [!important]+ Important!`.
- **Bases** (`.base`) and **Canvas** (`.canvas`) files.

### 🔧 More Than Just Notes

This template transforms your folder of Markdown files into a full-featured website with professional tools:

1.  **Explorer**: intuitive file tree navigation, just like in an IDE or Obsidian.
2.  **Search**: instant full-text search across your entire knowledge base.
3.  **Localization**: 30 interface locale options, set via `locale`.
4.  **Backlinks**: Quartz automatically shows which pages link to the current note.

> [!info] Ready in 15 Minutes
> It takes about 10 minutes to read the docs and 5 minutes to clone and configure the repository to launch your own "digital garden."

> [!tip]
> You can even resize images using the pipe syntax: `![alt text|200](image.png)` or `![alt text|200x100](image.png)`.

Obsidian is optional. Quartz processes these features from files in `content/` when it builds the site.
