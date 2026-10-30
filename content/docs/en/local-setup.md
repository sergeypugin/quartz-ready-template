---
title: Local Setup
description: Previewing the site locally with Node.js and testing dependencies.
priority: 30
---

To preview the site locally, install [Node.js](https://nodejs.org/) version 22 or newer. From the repository root, run:

```bash
# Install dependencies
npm ci

# Install the Quartz plugins configured for this project
npx quartz plugin install --from-config

# Start the local server with the default content/ folder
npx quartz build --serve
```

The terminal prints the local site address, usually [http://localhost:8080](http://localhost:8080). Changes to files in `content/` refresh the page automatically.
