---
title: Локальный запуск
description: Локальный просмотр сайта с помощью Node.js.
priority: 30
---

Для локального просмотра сайта установите [Node.js](https://nodejs.org/) версии 22 или новее. Из корневой папки репозитория выполните:

```bash
# Установить зависимости
npm ci

# Установить плагины Quartz, настроенные для этого проекта
npx quartz plugin install --from-config

# Запустить локальный сервер со стандартной папкой content/
npx quartz build --serve
```

Терминал покажет адрес локального сайта, обычно это [http://localhost:8080](http://localhost:8080). При изменении файлов в `content/` страница обновится автоматически.

### Локализация и языки

Чтобы изменить язык интерфейса Quartz (заполнитель поиска, даты, заголовки таблиц), обновите параметр `locale` в `quartz.config.yaml` (например, `locale: ru-RU`).

> [!tip]- Поддерживаемые языки интерфейса
> - `ar-SA`
> - `ca-ES`
> - `cs-CZ`
> - `de-DE`
> - `en-GB`
> - `en-US` (Стандартный)
> - `es-ES`
> - `fa-IR`
> - `fi-FI`
> - `fr-FR`
> - `he-IL`
> - `hu-HU`
> - `id-ID`
> - `it-IT`
> - `ja-JP`
> - `kk-KZ`
> - `ko-KR`
> - `lt-LT`
> - `nb-NO`
> - `nl-NL`
> - `pl-PL`
> - `pt-BR`
> - `ro-RO`
> - `ru-RU`
> - `th-TH`
> - `tr-TR`
> - `uk-UA`
> - `vi-VN`
> - `zh-CN`
> - `zh-TW`

---
[На главную](index)
