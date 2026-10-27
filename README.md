# Obsidian & Quartz Template

[English](README.md) | [Русский](README.ru.md)

[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-22C55E?logo=github-actions&logoColor=white)](https://pages.github.com/)
[![Quartz 5](https://img.shields.io/badge/Engine-Quartz%205-7C3AED?logo=obsidian&logoColor=white)](https://quartz.jzhao.xyz)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE.md)

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge&logo=github)](https://github.com/sergeypugin/quartz-ready-template/generate)

A ready-to-use, configured, and optimized template for instantly publishing notes and knowledge bases from [Obsidian](https://obsidian.md/) as a static website powered by [Quartz 5](https://quartz.jzhao.xyz/).

[GitHub vs Quartz](#github-vs-quartz) | [Quick start](#quick-start-create-your-website-in-1-minute) | [Local setup and testing](#local-setup-and-testing) | [Documentation](#documentation)

[Example site built with this template](https://sergeypugin.github.io/itmo-notebook) | [Example site from the Quartz 5 documentation](https://quartz.jzhao.xyz)

---

## GitHub vs Quartz
  
GitHub Markdown does not support most of Obsidian's convenient Markdown features. This template renders the following correctly on the site:
- **Wiki-links:** `[[Note name]]` and `[[Note name|Custom text]]` with automatic path resolution.
- **Callouts:** `> [!quote]`, `> [!success]`, `> [!bug]`, and more. Folding and custom titles are supported (`> [!note]- Clarification`, `> [!important]+ Important!`).
- Support for Obsidian Bases (`.base`) and Canvas (`.canvas`) files, and much more

## Quick start: create your website in 1 minute

1. Click the green **Use this template** button at the top of this page and select **Create a new repository**.
2. In your new repository, go to **Settings** -> **Pages**.
3. Under **Build and deployment**, select **Source: GitHub Actions**.
4. Clone the repository to your computer
5. In `.github/workflows/deploy.yml`, uncomment the three lines at the beginning of the file
6. Run `git commit` and then `git push`.
7. The site will be automatically published at `https://{user}.github.io/{repo}` in about a minute. You can find more information in the **Deployments** tab on the right side of your repository page.

>[!important]
>Make sure that the `content/` folder always contains an `index.md` note. This is the page that opens when visiting `https://{user}.github.io/{repo}`. Without it, the site will not be published

>[!note]
>When you click on a folder on the site, its `index.md` opens if it exists; otherwise, a simple list of all files in the folder is shown

>[!tip]
>To set your own text in the top-left corner instead of `Quartz 5`, go to `quartz.config.yaml` and enter your text in this block instead of `Quartz 5`:
> ```yaml
> configuration:
>   pageTitle: Quartz 5
> ```
> 
### Tips for use

>[!important]
>For convenience when working with notes, it is recommended to open the `content/` folder as your Vault rather than opening the repository itself. The folder name may be inconvenient if you have multiple Vaults. To change the name of the notes folder:
>1. Rename the `content/` folder to whatever you prefer. The best option is your repository name
>2. Go to `.github/workflows/deploy.yml` and make the following change:
> ```yml
> # Before:
>       - name: Build Quartz
>         run: npx quartz build
> 
> # After (for example, if the folder is named notes):
>       - name: Build Quartz
>         run: npx quartz build -d notes
> ```
>Now, after every `push` to the repository, the notes folder used for the site will change to the one you specified.

>[!tip]
>You can name notes in Russian, but when copying a site link it often turns into something like this: https://sergeypugin.github.io/quartz-ready-template/#%D0%B4%D0%BE%D0%B1%D1%80%D0%BE-%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2-%D0%B1%D0%B0%D0%B7%D1%83-%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B9.
>
>To avoid this, it is recommended to name notes in English without spaces and use the `title` property for their display names, which is automatically extracted from the note on the site. You can see an example of this approach in the pre-created `content/index.md` file.

>[!note]
>If you want to change the interface language to Russian, go to `quartz.config.yaml` in the repository root and replace `locale: en-US` with `locale: ru-RU`. I personally prefer not to do this, because with a font that is not designed for Russian, the text will appear smaller

## Local setup and testing

To preview the site locally, you need [Node.js](https://nodejs.org/) (version 22 or newer). Go to the root of the cloned repository and run:

```bash
# 1. Install dependencies
npm ci

# 2. Install Quartz plugins
npx quartz plugin install --from-config

# 3. Start the local server (if the folder is the default 'content')
npx quartz build --serve

# If you renamed the folder (for example, to notes):
npx quartz build --serve -d notes
```

After running these commands, the terminal will print the address where the site is available. It is usually [http://localhost:8080](http://localhost:8080). Changes to files in the `content/` folder automatically refresh the page.

### Service files and Git
The following directories are created while installing dependencies and building locally:
- `node_modules/` -- project libraries and dependencies
- `public/` -- the compiled static site (HTML, JS, CSS, generated graphs)
- `.quartz-cache/` -- the Markdown parser cache for faster subsequent builds

All these folders are listed in `.gitignore`, so they will not be added to your GitHub repository.

## Documentation

- [Official Quartz documentation](https://quartz.jzhao.xyz/)
- [Quartz source repository on GitHub](https://github.com/jackyzha0/quartz)
