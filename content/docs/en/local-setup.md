---
title: Local Setup
description: Previewing the site locally with Node.js and testing dependencies.
priority: 30
---

To preview the site locally, install [Node.js](https://nodejs.org/) version 22 or newer. From the repository root, run:

```bash
# Install dependencies
npm ci

# Install the Quartz plugins configured for this project
npx quartz plugin install --from-config

# Start the local server with the default content/ folder
npx quartz build --serve
```

The terminal prints the local site address, usually [http://localhost:8080](http://localhost:8080). Changes to files in `content/` refresh the page automatically.

### Locales and Languages

To change the Quartz interface language (search placeholder, dates, table headers), update the `locale` value in `quartz.config.yaml` (e.g., `locale: ru-RU`).

> [!tip]- Supported interface languages
> - `ar-SA`
> - `ca-ES`
> - `cs-CZ`
> - `de-DE`
> - `en-GB`
> - `en-US` (Default)
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

---
[Back to Home](index)
