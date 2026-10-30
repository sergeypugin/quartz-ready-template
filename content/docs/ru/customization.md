---
title: Настройка и базы знаний
description: Скрытие YAML-свойств заметок и написание запросов Obsidian Bases.
priority: 50
---

Quartz 5 предоставляет возможности для управления отображением свойств заметок и создания динамических таблиц на основе Obsidian Bases.

## Управление свойствами заметок (`note-properties`)

По умолчанию Quartz отображает карточку метаданных вверху страниц с содержимым YAML frontmatter.

Вы можете изменить список скрытых или отображаемых свойств в файле `quartz.config.yaml` в блоке `@quartz-community/note-properties`:

```yaml
  - source: "@quartz-community/note-properties"
    enabled: true
    options:
      includeAll: true
      includedProperties: []
      excludedProperties:
        - title
        - modified
        - description
        - priority
      hidePropertiesView: false
```

- **Скрыть конкретные свойства:** добавьте имена ключей (например, `description`, `priority`, `author`) в список `excludedProperties`.
- **Показывать только выбранные свойства:** установите `includeAll: false` и перечислите нужные ключи в `includedProperties`.
- **Скрыть весь блок свойств:** установите `hidePropertiesView: true` или `enabled: false`.

## Написание базок Obsidian Bases (`.base` и ```base)

Quartz 5 поддерживает **Obsidian Bases** — язык запросов для построения динамических таблиц, списков и карточек на основе свойств заметок. Вы можете создавать отдельные файлы `.base` или вставлять блоки ` ```base ` прямо внутрь Markdown-страниц.

### Пример синтаксиса ```base

```yaml
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
    name: Таблица руководств
    order:
      - title
      - description
    sort:
      - property: priority
        direction: ASC
```

### Основные элементы запроса

1. **`filters`**: фильтры выбора заметок (например, `file.inFolder("folder")`, `file.hasTag("tag")`, `file.ext == "md"`).
2. **`properties`**: заголовки столбцов (`displayName`).
3. **`views`**: тип отображения (`table`, `cards` или `list`), порядок столбцов (`order`) и сортировка (`sort` с направлением `ASC` или `DESC`).

---
[[docs/ru/index|Назад к документации]]
