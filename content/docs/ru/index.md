---
title: Документация
description: Основные руководства и справка по шаблону.
---

Добро пожаловать в документацию шаблона сайта на Quartz 5. Выберите тему из списка ниже. Если вы впервые настраиваете сайт, начните с заметки [[docs/ru/quick-start|Быстрый старт]].

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
