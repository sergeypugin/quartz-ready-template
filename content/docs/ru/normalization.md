---
title: Нормализация Markdown
description: Python-скрипты для проверки формул, ссылок и отступов у вставок.
priority: 40
---

Небольшие Python-скрипты, которые проверяют и форматируют Markdown-заметки перед сборкой сайта на Quartz.

Для некоторых возможностей Markdown (например, для формул) Quartz требует соблюдения определённых синтаксических правил. Эти скрипты гарантируют их выполнение без использования дополнительных npm-зависимостей.

## Стандартный запуск

Запускайте проверки из корневой папки репозитория:

```bash
# Проверить заметки без изменения файлов
python scripts/main.py --check

# Исправить заметки на месте
python scripts/main.py
```

Передайте параметр `--root ПУТЬ`, если ваши заметки находятся вне папки `content` по умолчанию:

```bash
python scripts/main.py --check --root my-notes
```

## Запуск отдельных скриптов

Вы можете запустить определенные скрипты через `main.py`, указав их имена в командной строке. Они выполнятся в стандартном порядке (`ensure_blank_after_embed` -> `convert_links` -> `check_math`):

```bash
# Проверить только формулы и относительность ссылок
python scripts/main.py --check check_math convert_links

# Исправить только отступы у вставок
python scripts/main.py ensure_blank_after_embed
```

Или вызовите отдельные скрипты напрямую:

```bash
python scripts/ensure_blank_after_embed.py [--check] [--root ПУТЬ]
python scripts/convert_links.py [--check] [--apply-all] [--root ПУТЬ]
python scripts/check_math.py [--check] [--root ПУТЬ]
```

## Что делает каждый скрипт

### ensure_blank_after_embed.py

Вставляет пустую строку после одиночных вставок изображений или заметок (`![alt](path)` или `![[note]]`), чтобы окружающий текст корректно рендерился во всех парсерах Markdown. Сохраняет префиксы цитат внутри блоков `>`.

### convert_links.py

Преобразует вики-ссылки Obsidian (`[[note]]`, `![[image.png]]`) в относительные Markdown-ссылки (`[note](note)`, `![image.png](image.png)`). Если целевой файл не найден или имеет несколько дубликатов, скрипт выведет номер строки и не станет менять файлы.

### check_math.py

Парсер `remark-math` открывает выключные формулы только тогда, когда разделитель `$$` находится на отдельной строке. Скрипт переносит `$$` на отдельные строки, удаляет лишние пробелы внутри формул (`$a + b$`) и сообщает о незакрытых блоках или математических символах в заголовках.

> [!tip] Добавление собственного скрипта
> Вы можете легко добавить свой скрипт в пайплайн:
> 1. Создайте Python-файл в `scripts/` (например, `check_custom.py`).
> 2. Используйте `import utils` для доступа к общим утилитам, таким как `markdown_files(root)` или `display_path(path)`.
> 3. Добавьте имя скрипта и его команду в словарь `SCRIPTS` в файле `scripts/main.py`.
> 
> Примечание: пожалуйста, пишите комментарии в коде только на английском языке.

## Настройка в GitHub Actions

Основной workflow репозитория (`.github/workflows/deploy.yml`) содержит закомментированный шаг нормализации. Вы можете использовать его либо для **проверки** форматирования (CI упадет, если заметки "грязные"), либо для **автоматического исправления** и создания коммита.

### Вариант 1: Только проверка (строгий)

CI завершится ошибкой, если ваши заметки не соответствуют каноничному формату.

```yaml
- name: Check Markdown normalization
  run: python scripts/main.py --check
```

### Вариант 2: Автоматическое исправление (Auto-commit)

CI сам отформатирует ваши заметки и отправит коммит обратно в репозиторий.

> [!warning]
> Для этого шага в файле workflow должны быть заданы права `permissions: contents: write`.

```yaml
- name: Apply Markdown normalization
  run: |
    python scripts/main.py
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
    git add .
    git diff --quiet && git diff --staged --quiet || git commit -m "chore: normalize markdown"
    git push
```

---
[Назад к документации](index)
