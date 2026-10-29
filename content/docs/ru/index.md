---
title: Документация
description: Основные руководства и справка по шаблону.
---

Добро пожаловать в документацию шаблона сайта на Quartz 5.

### 🌍 Локализация и языки

Чтобы изменить язык интерфейса Quartz (заполнитель поиска, даты, заголовки таблиц), обновите параметр `locale` в `quartz.config.yaml` (например, `locale: ru-RU`).

> [!tip]- Поддерживаемые языки интерфейса
>
> - `ar-SA`
> - `ca-ES`
> - `cs-CZ`
> - `de-DE`
> - `en-GB`
> - `en-US` (По умолчанию)
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
    - file.inFolder("docs/ru")
    - file.name != "index"
properties:
  title:
    displayName: Руководство
  description:
    displayName: Описание
views:
  - type: table
    name: Руководства
    order:
      - title
      - description
    sort:
      - property: priority
        direction: ASC
```
