---
title: Documentation
description: Main guides and template reference.
---

Welcome to the documentation for the Quartz 5 Markdown Website Template. Browse the guides below. If this is your first setup, start with [[docs/en/quick-start|Quick Start]].

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
