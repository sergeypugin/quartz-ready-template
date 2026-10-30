---
title: Home
---

# 🪴 Quartz 5 Markdown Website Template

A ready-to-use template for publishing Markdown notes and knowledge bases as a static website powered by [Quartz 5](https://quartz.jzhao.xyz/). Edit Markdown files with any editor; Obsidian is optional.

---

### 🚧 Quick Start

1.  **Create your repo**: Click the [**Use this template**](https://github.com/sergeypugin/quartz-ready-template/generate) button.
2.  **Enable Pages**: Go to **Settings > Pages** and select **GitHub Actions** as the source.
3.  **First Deploy**: Go to **Actions**, select **Deploy Quartz site**, and click **Run workflow**.

---

### 📚 Documentation

```base
filters:
  and:
    - file.name == "index"
    - file.folder.startsWith("docs/")
properties:
  title:
    displayName: 📚 Language
  description:
    displayName: 📝 Description
views:
  - type: table
    order:
      - title
      - description
```

---

### 🔧 Contributing

Feel free to contribute! Whether it's fixing a typo, improving documentation, or adding new features to the scripts, your help is welcome.

- [How to contribute](https://github.com/sergeypugin/quartz-ready-template/blob/main/CONTRIBUTING.md)
- [Report an issue](https://github.com/sergeypugin/quartz-ready-template/issues)

---

[Quartz 5 docs' site](https://quartz.jzhao.xyz) | [Example site built with this template (in Russian)](https://sergeypugin.github.io/itmo-notebook)
