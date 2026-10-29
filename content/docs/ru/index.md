---
title: Документация
---

Добро пожаловать в документацию шаблона сайта на Quartz 5.

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

---
[На главную](index)
