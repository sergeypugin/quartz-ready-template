---
title: Bases & Note Properties
description: How to configure frontmatter note properties, hide internal fields, and build dynamic Bases tables.
priority: 35
---

Quartz allows you to manage note metadata using YAML frontmatter properties and visualize note collections using dynamic **Bases** tables.

## Managing Note Properties

When you add frontmatter properties at the top of a Markdown file:

```yaml
---
title: My Custom Page
description: A quick overview of the feature.
priority: 10
draft: false
---
```

Quartz displays these properties in a metadata card at the top of the note using the `@quartz-community/note-properties` plugin.

> [!info] Configuring Properties in `quartz.config.yaml`
> You can control which properties are shown or hidden globally in `quartz.config.yaml`:
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

### Hiding and Unhiding Properties

- **`excludedProperties`**: List property names that should be hidden from the top metadata card. For instance, internal metadata like `priority` or redundant fields like `title` can be hidden from the note header while remaining accessible to search, scripts, and Bases.
- **`hidePropertiesView`**: Set to `true` if you want to collapse or hide the properties card entirely across all notes by default.
- **`includedProperties`**: When `includeAll` is set to `false`, only properties explicitly listed here will be rendered.

## Writing Bases

**Bases** allow you to create dynamic database-like tables directly in your notes using a simple code block syntax (` ```base `).

> [!tip]- Bases Block Syntax Example
> ```base
> views:
>   - name: Documentation Guide
>     type: table
>     filters:
>       and:
>         - file.path.startswith("docs/en")
>     sort:
>       - property: priority
>         order: asc
>     properties:
>       - name: file.name
>         label: Guide
>       - name: description
>         label: Description
> ```

### Key Bases Configuration Options

- **`filters`**: Define conditions to include specific notes (e.g., `file.path.startswith("docs/en")` or `tags.includes("guide")`).
- **`sort`**: Order table entries by properties like `priority`, `title`, or `created` in `asc` or `desc` order.
- **`properties`**: Select which columns to display and assign custom header labels (`label`).

---
[Back to Documentation Index](index)
