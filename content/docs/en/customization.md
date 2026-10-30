---
title: Customization and Bases
description: Hiding frontmatter note properties and writing Obsidian Bases queries.
priority: 50
---

Quartz 5 provides rich features for managing note properties and displaying dynamic data tables using Obsidian Bases.

## Managing Note Properties (`note-properties`)

By default, Quartz renders a metadata card at the top of notes containing YAML frontmatter properties.

You can configure which properties are displayed or hidden by editing `@quartz-community/note-properties` in `quartz.config.yaml`:

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

- **Hide specific properties:** add property names (e.g. `description`, `priority`, `author`) to `excludedProperties`.
- **Show only selected properties:** set `includeAll: false` and list allowed names in `includedProperties`.
- **Hide the entire properties block:** set `hidePropertiesView: true` or set `enabled: false`.

## Writing Obsidian Bases (`.base` & ```base)

Quartz 5 supports **Obsidian Bases** — a structured query language for rendering dynamic tables, lists, and card views from note metadata. You can use `.base` files or embed inline ` ```base ` blocks directly inside Markdown notes.

### Basic ```base Syntax

```yaml
filters:
  and:
    - file.ext == "md"
    - file.inFolder("docs/en")
    - file.name != "index"
properties:
  title:
    displayName: Guide Title
  description:
    displayName: Description
views:
  - type: table
    name: Guides Table
    order:
      - title
      - description
    sort:
      - property: priority
        direction: ASC
```

### Key Query Elements

1. **`filters`**: criteria for selecting notes (e.g. `file.inFolder("folder")`, `file.hasTag("tag")`, `file.ext == "md"`).
2. **`properties`**: customizing column header titles (`displayName`).
3. **`views`**: view type (`table`, `cards`, or `list`), column sequence (`order`), and sorting (`sort` with `direction: ASC` or `DESC`).

---
[[docs/en/index|Back to Documentation]]
