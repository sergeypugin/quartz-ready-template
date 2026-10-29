---
title: Features
description: Supported Markdown extensions, callouts, wiki-links, Canvas, Bases, and image sizes.
priority: 10
---

GitHub's Markdown renderer does not support every extension Quartz can render. Quartz also processes Obsidian-compatible syntax and file formats, including:

- **Wiki-style links:** `[[Note name]]` and `[[Note name|Custom text]]` with automatic path resolution.
- **Callouts:** `> [!quote]`, `> [!success]`, `> [!bug]`, and more, including folding and custom titles such as `> [!note]- Clarification` and `> [!important]+ Important!`.
- **Bases** (`.base`) and **Canvas** (`.canvas`) files.

> [!tip]
> You can even resize images using the pipe syntax: `![alt text|200](image.png)` or `![alt text|200x100](image.png)`.

Obsidian is optional. Quartz processes these features from files in `content/` when it builds the site.

---
[Back to Home](index)
