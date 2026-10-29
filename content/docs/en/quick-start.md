---
title: Quick Start
description: How to create a repository from this template and deploy it to GitHub Pages.
priority: 20
---

### 🚧 Quick start: publish your site

1. Go to the [template repository](https://github.com/sergeypugin/quartz-ready-template), click the green **Use this template** button, and select **Create a new repository**.
2. In the new repository, open **Settings** > **Pages** and select **GitHub Actions** as the deployment source.
3. To start the first deployment, open **Actions**, select **Deploy Quartz site to GitHub Pages**, click **Run workflow**, and choose `main`.
4. Edit `[[index|content/index.md]]` or add your Markdown notes, then commit and push the changes to `main`. Future pushes to `main` start deployments automatically.
5. GitHub Pages shows the site URL in **Settings** > **Pages**; project sites usually use `https://{user}.github.io/{repo}`.

> [!note] File Organization
> - The site's home page is `content/index.md`.
> - Quartz builds the site from files in `content/`; Obsidian is not required. If you use Obsidian to edit your notes, you can open `content/` as a Vault.
> - When you open a folder on the site, Quartz shows its `index.md` if one exists; otherwise, it shows a list of files in that folder.

### Working with your notes

> [!tip] Configuration & Naming
> - To change the Quartz interface language, set the `locale` value in `quartz.config.yaml` (e.g., `locale: en-US`).
> - You can name notes in any language. To keep URLs simple, use English filenames without spaces and set the display name with the `title` property in frontmatter.

---
[Back to Home](index)
