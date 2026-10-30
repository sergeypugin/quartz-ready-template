---
title: Quick Start
description: How to create a site from this template, configure a custom domain and locale, and deploy it to GitHub Pages.
priority: 20
---

### 🚧 Quick start: publish your site

1. Go to the [template repository](https://github.com/sergeypugin/quartz-ready-template), click the green **Use this template** button, and select **Create a new repository**.
2. In the new repository, open **Settings** > **Pages** and select **GitHub Actions** as the deployment source.
3. To start the first deployment, open **Actions**, select **Deploy Quartz site to GitHub Pages**, click **Run workflow**, and choose `main`.
4. Edit `[[index|content/index.md]]` or add your Markdown notes, then commit and push the changes to `main`. Future pushes to `main` start deployments automatically.
5. GitHub Pages shows the site URL in **Settings** > **Pages**; project sites usually use `https://{user}.github.io/{repo}`.

### Custom domain

To use a custom domain, configure its DNS records with your DNS provider and add the domain in **Settings** > **Pages**. Follow [GitHub's official instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

Then add a plain-text file named `CNAME` to the repository root containing only the domain name, for example `notes.example.com`. Do not include `https://` or a path. On each deployment, the workflow reads this value to set `baseUrl` and copies `CNAME` into the published site.

You do not need a `CNAME` file for a standard GitHub Pages project URL (`{user}.github.io/{repo}`).

### Localization and site title

Set the interface language and site title in `quartz.config.yaml`. Both settings go under `configuration`:

```yaml
configuration:
  locale: en-US
  pageTitle: My Knowledge Base
```

`locale` controls interface text, including the Explorer label, search, dates, and table headers. `pageTitle` sets the site title displayed above the Explorer file tree.

> [!tip]- Supported `locale` values
>
> - `ar-SA`
> - `ca-ES`
> - `cs-CZ`
> - `de-DE`
> - `en-GB`
> - `en-US` (default)
> - `es-ES`
> - `fa-IR`
> - `fi-FI`
> - `fr-FR`
> - `he-IL`
> - `hu-HU`
> - `id-ID`
> - `it-IT`
> - `ja-JP`
> - `kk-KZ`
> - `ko-KR`
> - `lt-LT`
> - `nb-NO`
> - `nl-NL`
> - `pl-PL`
> - `pt-BR`
> - `ro-RO`
> - `ru-RU`
> - `th-TH`
> - `tr-TR`
> - `uk-UA`
> - `vi-VN`
> - `zh-CN`
> - `zh-TW`

> [!note] File Organization
>
> - The site's home page is `content/index.md`.
> - Quartz builds the site from files in `content/`; Obsidian is not required. If you use Obsidian to edit your notes, you can open `content/` as a Vault.
> - When you open a folder on the site, Quartz shows its `index.md` if one exists; otherwise, it shows a list of files in that folder.

### Naming your notes

> [!tip] File names
>
> You can write notes and headings in Russian. Browsers may percent-encode Cyrillic in copied links. For example, a link to the heading `добро-пожаловать` may look like `https://{user}.github.io/{repo}/path/to/note/#%D0%B4%D0%BE%D0%B1%D1%80%D0%BE-%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%82%D1%8C`. If you want readable note paths, use English filenames without spaces and set the display name with the `title` property in frontmatter.
