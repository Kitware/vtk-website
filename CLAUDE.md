# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

VTK website built with **VitePress**. The site is deployed to GitHub Pages via GitHub Actions on push to `main`. The project is in early development — not yet published.

## Commands

- `npm run dev` — Start local dev server with hot reload
- `npm run build` — Build static site to `src/.vitepress/dist/`
- `npm run preview` — Preview production build locally
- `npm install` — Install dependencies (use `npm ci` for clean installs)

No linting or testing tools are configured.

## Architecture

- **`src/`** — All site content and VitePress configuration
  - **`src/.vitepress/config.ts`** — Site config: nav, sidebar, social links, base path (`/`)
  - **`src/.vitepress/theme/`** — Custom theme (extends VitePress default theme, adds `custom.css`)
  - **`src/index.md`** — Home page using VitePress `home` layout with hero and features
  - **`src/about/`** — About VTK (overview, history, license, citing, logo, contributors)
  - **`src/features/`** — Feature pages (data model, filters, rendering, interaction, charts, parallel, I/O)
  - **`src/solutions/`** — Domain solutions (medical, engineering, geospatial, scientific, web)
  - **`src/ecosystem/`** — Ecosystem projects (ParaView, Trame, PyVista, vtk.js, 3D Slicer)
  - **`src/getting-started/`** — Getting started guides (Python, C++, JavaScript, frameworks)
  - **`src/guide/`** — User's Guide chapters (12 chapters covering VTK fundamentals to advanced topics)
  - **`src/docs/`** — Documentation hub (API, formats, modules, building, textbook)
  - **`src/community/`** — Community pages (contributing, services, events)
  - **`src/examples/`** — Examples landing (links to examples.vtk.org)
  - **`src/download/`** — Download page
  - **`src/gallery/`** — Showcase gallery
  - **`src/public/`** — Static assets served at site root
- **`.github/workflows/website.yaml`** — CI/CD: builds with Node.js 24, deploys to GitHub Pages

## Key Details

- VitePress is the only dependency
- Content is authored in Markdown (`.md` files in `src/`)
- Vue components can be embedded in Markdown pages
- Base path is `/` (for vtk.org deployment)
- ES modules project (`"type": "module"` in package.json)
- Multi-sidebar config: each section (`/about/`, `/features/`, `/guide/`, etc.) has its own sidebar

## Git Conventions

- Do not mention Claude in any git commits
- Use conventional commit style (e.g., `feat(site): ...`)
- PRs go against `main` branch
