# Шаблон Markdown-сайта на Quartz 5

[English](README.md) | [Русский](README.ru.md)

[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-22C55E?logo=github-actions&logoColor=white)](https://pages.github.com/)
[![Quartz 5](https://img.shields.io/badge/Engine-Quartz%205-7C3AED)](https://quartz.jzhao.xyz)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE.md)

[![Использовать шаблон](https://img.shields.io/badge/Использовать_шаблон-2ea44f?style=for-the-badge&logo=github)](https://github.com/sergeypugin/quartz-ready-template/generate)

Готовый шаблон для публикации Markdown-заметок и баз знаний в виде статического сайта на [Quartz 5](https://quartz.jzhao.xyz/). Markdown-файлы можно редактировать в любом редакторе; Obsidian необязателен.

[Возможности](#возможности) | [Быстрый старт](#быстрый-старт-публикация-сайта) | [Локальный запуск и проверка](#локальный-запуск-и-проверка) | [Нормализация Markdown](#нормализация-markdown) | [Документация](#документация)

[Пример сайта на основе шаблона](https://sergeypugin.github.io/itmo-notebook) | [Сайт документации Quartz 5](https://quartz.jzhao.xyz)

---

## Возможности

GitHub не отображает все расширения, которые поддерживает Quartz. Quartz также обрабатывает Obsidian-совместимый синтаксис и форматы файлов, в том числе:

- **Вики-ссылки:** `[[Название заметки]]` и `[[Название заметки|Свой текст]]` с автоматическим поиском пути
- **Коллауты:** `> [!quote]`, `> [!success]`, `> [!bug]` и другие, включая сворачивание и пользовательские заголовки, например `> [!note]- Уточнение` и `> [!important]+ Важно!`
- Файлы **Bases** (`.base`) и **Canvas** (`.canvas`); см. [Настройка и Bases](content/docs/ru/customization.md) с примерами

Obsidian необязателен. Quartz обрабатывает эти возможности из файлов в `content/` при сборке сайта.

## Быстрый старт: публикация сайта

1. Нажмите зелёную кнопку **Use this template** вверху страницы и выберите **Create a new repository**
2. В новом репозитории откройте **Settings** > **Pages** и выберите **GitHub Actions** как источник публикации
3. Чтобы запустить первую публикацию, откройте **Actions**, выберите **Deploy Quartz site to GitHub Pages**, нажмите **Run workflow** и выберите ветку `main`
4. Отредактируйте `content/index.md` или добавьте Markdown-заметки, затем создайте коммит и отправьте изменения в `main`. Файлы можно редактировать на GitHub или после клонирования репозитория в любом редакторе. В дальнейшем каждый push в `main` будет запускать публикацию автоматически
5. Адрес сайта будет указан в **Settings** > **Pages**; проектные сайты обычно доступны по адресу `https://{user}.github.io/{repo}`

> [!important]
> Главная страница сайта находится в файле `content/index.md`

> [!note]
> При открытии папки на сайте Quartz показывает её файл `index.md`, если он есть; иначе показывает список файлов в папке

> [!tip]
> Чтобы изменить текст в левом верхнем углу, поменяйте значение `pageTitle` в `quartz.config.yaml`:
>
> ```yaml
> configuration:
>   pageTitle: Quartz 5
> ```

### Работа с заметками

> [!important]
> Quartz собирает сайт из файлов в `content/`; Obsidian не требуется. Если вы редактируете заметки в Obsidian, эту папку можно открыть как Vault. Чтобы переименовать папку с заметками, переименуйте `content/` и обновите команду сборки Quartz в `.github/workflows/deploy.yml`. Например, для папки `notes` замените `npx quartz build` на `npx quartz build -d notes`

> [!tip]
> Заметки можно называть на любом языке. Нелатинские символы в адресах страниц могут кодироваться. Чтобы адреса были проще, используйте английские имена файлов без пробелов, а отображаемое название задавайте свойством `title`. Пример есть в `content/index.md`

> [!note]
> Чтобы изменить язык интерфейса Quartz, задайте другое значение `locale` в `quartz.config.yaml`. Это изменит подписи интерфейса, но не язык заметок. Текущая версия Quartz поддерживает 30 кодов локали: `ar-SA`, `ca-ES`, `cs-CZ`, `de-DE`, `en-GB`, `en-US`, `es-ES`, `fa-IR`, `fi-FI`, `fr-FR`, `he-IL`, `hu-HU`, `id-ID`, `it-IT`, `ja-JP`, `kk-KZ`, `ko-KR`, `lt-LT`, `nb-NO`, `nl-NL`, `pl-PL`, `pt-BR`, `ro-RO`, `ru-RU`, `th-TH`, `tr-TR`, `uk-UA`, `vi-VN`, `zh-CN` и `zh-TW`

## Локальный запуск и проверка

Для локального просмотра сайта установите [Node.js](https://nodejs.org/) версии 22 или новее. Из корневой папки репозитория выполните:

```bash
# Установить зависимости
npm ci

# Установить плагины Quartz, настроенные для этого проекта
npx quartz plugin install --from-config

# Запустить локальный сервер со стандартной папкой content/
npx quartz build --serve

# Если папка переименована, например в notes/
npx quartz build --serve -d notes
```

Терминал покажет адрес локального сайта, обычно это [http://localhost:8080](http://localhost:8080). При изменении файлов в `content/` страница обновится автоматически

## Нормализация Markdown

Репозиторий содержит Python-скрипты в `scripts/` для проверки отображаемых формул (`$$`), конвертации вики-ссылок в относительные и проверки отступов у вставок перед отправкой. Подробнее о запуске и включении в GitHub Actions см. в [scripts/README.md](scripts/README.md).

### Создаваемые файлы и Git

При установке зависимостей и сборке сайта локально создаются папки:

- `node_modules/` -- зависимости проекта
- `public/` -- собранный статический сайт, включая HTML, JavaScript, CSS и графы
- `.quartz-cache/` -- кэш Markdown-парсера для ускорения следующих сборок

Эти папки перечислены в `.gitignore` и не будут добавлены в Git-репозиторий

## Документация

- [Базки и свойства заметок](content/docs/ru/bases-and-properties.md) — Настройка YAML метаданных и динамических таблиц.
- [Нормализация Markdown](content/docs/ru/normalization.md) — Python-скрипты для форматирования и проверки.
- [Локальный запуск](content/docs/ru/local-setup.md) — Запуск Quartz локально и настройка языков интерфейса.

> [!important] Рекомендация: удалите примеры
> Вы можете смело удалять или заменять стандартные файлы в папке `content/`. Они предоставлены исключительно для ознакомления со структурой сайта и в качестве документации к шаблону.

- [Официальная документация Quartz](https://quartz.jzhao.xyz/)
- [Исходный код Quartz на GitHub](https://github.com/jackyzha0/quartz)
