---
title: Documentation
description: Main guides and template reference.
---

Welcome to the documentation for the Quartz 5 Markdown Website Template.

### 🌍 Locales and Languages

To change the Quartz interface language (search placeholder, dates, table headers), update the `locale` value in `quartz.config.yaml` (e.g., `locale: en-US`).

> [!tip]- Supported interface languages
>
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

```base
filters:
  and:
    - file.ext == "md"
    - file.inFolder("docs/en")
    - file.name != "index"
properties:
  title:
    displayName: Guide
  description:
    displayName: Description
views:
  - type: table
    name: Guides
    order:
      - title
      - description
    sort:
      - property: priority
        direction: ASC
```
