---
title: Documentation
---

Welcome to the documentation for the Quartz 5 Markdown Website Template.

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

---
[Back to Home](index)
