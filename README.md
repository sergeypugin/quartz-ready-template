# Obsidian & Quartz Template  
  
![Quartz](https://img.shields.io/badge/Powered%20by-Quartz%205-purple?logo=obsidian&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/CI%2FCD-GitHub%20Pages-22C55E?logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Used as template](https://img.shields.io/github/forks/sergeypugin/quartz-ready-template?label=used%20as%20template&color=blue)

Готовый, настроенный и оптимизированный шаблон для мгновенной публикации заметок и баз знаний из [Obsidian](https://obsidian.md/) в виде статического веб-сайта на движке [Quartz 5](https://quartz.jzhao.xyz/).

[GitHub vs Quartz](#github-vs-quartz) | [Быстрый старт](#быстрый-старт-как-создать-свой-сайт-за-1-минуту) | [Локальный запуск и тестирование](#локальный-запуск-и-тестирование) | [Документация](#документация)

[Пример сайта по этому шаблону](https://sergeypugin.github.io/quartz-ready-template) | [Пример сайта по документации Quartz 5](https://quartz.jzhao.xyz)
## GitHub vs Quartz
  
Markdown на GitHub не поддерживает большинство удобных функций маркдауна Obsidian. Этот шаблон корректно рендерит на сайте:
- **Вики-ссылки:** `[[Имя заметки]]` и `[[Имя заметки|Кастомный текст]]` с авто-поиском путей.
- **Коллауты:** теперь доступны `> [!quote]`, `> [!success]`, `> [!bug]` и другие. Поддерживается сворачивание и кастомные заголовки (`> [!note]- Уточнение`, `> [!important]+ Важно!`).
- Поддержка баз данных Bases (`.base`) и Canvas (`.canvas`) от Obsidian и многое другое

## Быстрый старт: как создать свой сайт за 1 минуту

1. Кликните зеленую кнопку **«Use this template»** вверху этой страницы и выберите **«Create a new repository»**.  
2. В созданном репозитории перейдите в **Settings** -> **Pages**.  
3. В блоке **Build and deployment** выберите **Source: GitHub Actions**.  
4. Склонируйте репозиторий на компьютер, откройте его как Vault в Obsidian
5. В файле `.github/workflows/deploy.yml` раскоментируйте три строки в самом начале
6. Создайте заметки в папке `content/` и сделайте `git push` (после `git commit`, разумеется).
7. Сайт будет автоматически опубликован по адресу `https://{user}.github.io/{repo}` примерно через минуту. Более подробную информацию вы можете увидеть во вкладке `Deployments` справа в вашем репозитории на сайте.

>[!important]
>Важно, чтобы в папке `content/` всегда была заметка `index.md`. Именно она открывается при переходе на сайт `https://{user}.github.io/{repo}`. Без неё пубикация не получится

>[!tip]
>Все заметки вы можете называть на русском, однако при копировании ссылки сайта зачастую она превращается в это: https://sergeypugin.github.io/quartz-ready-template/#%D0%B4%D0%BE%D0%B1%D1%80%D0%BE-%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2-%D0%B1%D0%B0%D0%B7%D1%83-%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B9.
>
>Чтобы такое избжать, рекомендуется называть заметки на английском и без пробелов, а для названий использовать свойство `title`, которое автоматически вырезается из заметки на сайте. Пример такого подхода вы можете увидеть в уже созданном файле `content/index.md`.

>[!note]
>Если вы хотите изменить язык интерфейса на русский, то перейдите в `quartz.config.yaml` в корне репозитория и замените строку `locale: en-US` на `locale: ru-RU`. Сам я предпочитаю так не делать, т.к. со шрифтом сайта, не рассчитанным на русский, надписи станут меньше

## Локальный запуск и тестирование

Для предварительного просмотра сайта на локальной машине необходим установленный [Node.js](https://nodejs.org/) (версии 22 или новее). Перейдите в корень склонированного репозитория и выполните:

```bash
npm ci
npx quartz plugin install --from-config
npx quartz build --serve
```

После этих команд терминал выведет ссылку, на которой будет располагаться сайт. Чаще всего это [http://localhost:8080](http://localhost:8080) (при изменении файлов в папке `content/` страница обновляется автоматически).

### Служебные файлы и Git
В процессе установки зависимостей и сборки локально создаются следующие директории:
- `node_modules/` — библиотеки и зависимости проекта;
- `public/` — скомпилированный статический сайт (HTML, JS, CSS, сгенерированные графы);
- `.quartz-cache/` — кэш парсера Markdown для ускорения повторных сборок.

Все эти папки уже прописаны в `.gitignore`, поэтому они не попадут в ваш GitHub-репозиторий.

## Документация

- [Официальная документация Quartz](https://quartz.jzhao.xyz/)
- [Исходный репозиторий Quartz на GitHub](https://github.com/jackyzha0/quartz)