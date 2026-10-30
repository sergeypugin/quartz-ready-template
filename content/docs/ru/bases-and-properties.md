---
title: Базки и свойства заметок
description: Как настраивать YAML-свойства заметок, скрывать внутренние поля и создавать динамические таблицы Bases.
priority: 35
---

Quartz позволяет управлять метаданными заметок через свойства YAML-frontmatter и отображать коллекции заметок в виде динамических таблиц **Bases**.

## Управление свойствами заметок

Когда вы добавляете свойства в начало Markdown-файла:

```yaml
---
title: Моя страница
description: Краткий обзор возможностей.
priority: 10
draft: false
---
```

Quartz отображает их в блоке свойств вверху страницы с помощью плагина `@quartz-community/note-properties`.

> [!info] Настройка свойств в `quartz.config.yaml`
> Вы можете настроить глобальное отображение свойств в файле `quartz.config.yaml`:
>
> ```yaml
> - source: "@quartz-community/note-properties"
>   enabled: true
>   options:
>     includeAll: true
>     excludedProperties:
>       - title
>       - modified
>       - description
>       - priority
>     hidePropertiesView: false
> ```

### Как скрыть или раскрыть свойства

- **`excludedProperties`**: перечислите имена свойств, которые нужно скрыть из верхней карточки метаданных. Служебные свойства (например, `priority` или `title`) останутся доступными для поиска, скриптов и Базок, но не будут загромождать шапку страницы.
- **`hidePropertiesView`**: установите `true`, если хотите свернуть или полностью скрыть плашку свойств на всех страницах по умолчанию.
- **`includedProperties`**: если `includeAll` равен `false`, будут отображаться только явно указанные здесь свойства.

## Написание Базок (Bases)

**Базки (Bases)** позволяют создавать динамические таблицы-базы данных прямо в ваших заметках с помощью синтаксиса ` ```base `.

> [!tip]- Пример синтаксиса блока Base
> ```yaml
> views:
>   - name: Руководство по документации
>     type: table
>     filters:
>       and:
>         - file.ext == "md"
>         - file.inFolder("docs/ru")
>         - file.name != "index"
>     sort:
>       - property: priority
>         order: asc
>     properties:
>       - name: file.name
>         label: Раздел
>       - name: description
>         label: Описание
> ```

### Основные параметры Базок

- **`filters`**: задают условия отбора заметок (например, `file.path.startswith("docs/ru")` или `tags.includes("guide")`).
- **`sort`**: сортируют строки по свойствам (`priority`, `title`, `created`) по возрастанию (`asc`) или убыванию (`desc`).
- **`properties`**: определяют, какие колонки показывать и с какими заголовками (`label`).

---
[[docs/ru/index|Назад к документации]]
