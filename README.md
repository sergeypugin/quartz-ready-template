# Quartz 5 Markdown Website Template

[English](README.md) | [Русский](README.ru.md)

[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-22C55E?logo=github-actions&logoColor=white)](https://pages.github.com/)
[![Quartz 5](https://img.shields.io/badge/Engine-Quartz%205-7C3AED)](https://quartz.jzhao.xyz)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE.md)

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge&logo=github)](https://github.com/sergeypugin/quartz-ready-template/generate)

A ready-to-use template for publishing Markdown notes and knowledge bases as a static website powered by [Quartz 5](https://quartz.jzhao.xyz/). Edit Markdown files with any editor; Obsidian is optional.

[Features](#features) | [Quick start](#quick-start-publish-your-site) | [Local setup and testing](#local-setup-and-testing) | [Markdown normalization](#markdown-normalization) | [Documentation](#documentation)

[Example site built with this template](https://sergeypugin.github.io/itmo-notebook) | [Quartz 5 documentation site](https://quartz.jzhao.xyz)

---

## Features

GitHub's Markdown renderer does not support every extension Quartz can render. Quartz also processes Obsidian-compatible syntax and file formats, including:

- **Wiki-style links:** `[[Note name]]` and `[[Note name|Custom text]]` with automatic path resolution
- **Callouts:** `> [!quote]`, `> [!success]`, `> [!bug]`, and more, including folding and custom titles such as `> [!note]- Clarification` and `> [!important]+ Important!`
- **Bases** (`.base`) and **Canvas** (`.canvas`) files; see [Customization & Bases](content/docs/en/customization.md) for examples

Obsidian is optional. Quartz processes these features from files in `content/` when it builds the site.

## Quick start: publish your site

1. Click the green **Use this template** button at the top of this page and select **Create a new repository**
2. In the new repository, open **Settings** > **Pages** and select **GitHub Actions** as the deployment source
3. To start the first deployment, open **Actions**, select **Deploy Quartz site to GitHub Pages**, click **Run workflow**, and choose `main`
4. Edit `content/index.md` or add your Markdown notes, then commit and push the changes to `main`. You can edit files on GitHub or clone the repository and use your preferred editor. Future pushes to `main` start deployments automatically
5. GitHub Pages shows the site URL in **Settings** > **Pages**; project sites usually use `https://{user}.github.io/{repo}`

> [!important]
> The site's home page is `content/index.md`

> [!note]
> When you open a folder on the site, Quartz shows its `index.md` if one exists; otherwise, it shows a list of files in that folder

> [!tip]
> To change the text in the top-left corner, edit the `pageTitle` value in `quartz.config.yaml`:
>
> ```yaml
> configuration:
>   pageTitle: Quartz 5
> ```

### Working with your notes

> [!important]
> Quartz builds the site from files in `content/`; Obsidian is not required. If you use Obsidian to edit your notes, you can open `content/` as a Vault. To rename the notes folder, rename `content/` and update the Quartz build command in `.github/workflows/deploy.yml`. For example, if the folder is named `notes`, change `npx quartz build` to `npx quartz build -d notes`

> [!tip]
> You can name notes in any language. Non-Latin characters may be percent-encoded in page URLs. To keep URLs simple, use English filenames without spaces and set the display name with the `title` property. See `content/index.md` for an example

> [!note]
> Change the `locale` value in `quartz.config.yaml` to set the Quartz interface language. This changes interface labels, not the language of your notes. The current Quartz version supports 30 locale codes: `ar-SA`, `ca-ES`, `cs-CZ`, `de-DE`, `en-GB`, `en-US`, `es-ES`, `fa-IR`, `fi-FI`, `fr-FR`, `he-IL`, `hu-HU`, `id-ID`, `it-IT`, `ja-JP`, `kk-KZ`, `ko-KR`, `lt-LT`, `nb-NO`, `nl-NL`, `pl-PL`, `pt-BR`, `ro-RO`, `ru-RU`, `th-TH`, `tr-TR`, `uk-UA`, `vi-VN`, `zh-CN`, and `zh-TW`

## Local setup and testing

To preview the site locally, install [Node.js](https://nodejs.org/) version 22 or newer. From the repository root, run:

```bash
# Install dependencies
npm ci

# Install the Quartz plugins configured for this project
npx quartz plugin install --from-config

# Start the local server with the default content/ folder
npx quartz build --serve

# If you renamed the folder, for example to notes/
npx quartz build --serve -d notes
```

The terminal prints the local site address, usually [http://localhost:8080](http://localhost:8080). Changes to files in `content/` refresh the page automatically

## Markdown normalization

The repository includes Python scripts in `scripts/` to verify display math (`$$`), convert wikilinks to relative links, and check embed spacing before pushing. See [scripts/README.md](scripts/README.md) for usage and how to enable them in GitHub Actions.

### Generated files and Git

Local dependency installation and site builds create these directories:

- `node_modules/` -- project dependencies
- `public/` -- the generated static site, including HTML, JavaScript, CSS, and graphs
- `.quartz-cache/` -- a Markdown parser cache for faster subsequent builds

These directories are listed in `.gitignore` and will not be added to your Git repository

## Documentation

- [Bases & Note Properties](content/docs/en/bases-and-properties.md) — Configuring YAML metadata and dynamic tables.
- [Markdown Normalization](content/docs/en/normalization.md) — Python scripts for formatting and validation.
- [Local Setup](content/docs/en/local-setup.md) — Running Quartz locally and configuring locales.

> [!important] Recommended: delete demo content
> You can safely delete or replace the default files in the `content/` directory. They are provided solely as an example of the site structure and as documentation for the template.

- [Official Quartz documentation](https://quartz.jzhao.xyz/)
- [Quartz source repository on GitHub](https://github.com/jackyzha0/quartz)
