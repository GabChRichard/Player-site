# Sf2e campaign: Player Site

Player-facing pages for the Starfinder 2e campaign *Renegade legacy*, built with **MkDocs + Material for MkDocs**.

This project started as a copy of the player pages in the `campaign` project. It is now independent: edits here are not synced back.

## Setup (Windows, one time)

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

## Preview and build

```powershell
.venv\Scripts\mkdocs serve             # live preview -> http://127.0.0.1:8000
.venv\Scripts\mkdocs build --strict    # static site -> site/ (fails on broken links)
```

## Layout

```
mkdocs.yml                  site config and nav
docs/
  index.md                  home page
  license.md                Paizo Community Use notice and credits
  players/                  primer, timeline, pre-campaign meeting, form, session zero, homebrew
  assets/images/            images (Paizo art only from the Community Use Package)
  assets/stylesheets/       theme tweaks
```

## Paizo material

The site is published under Paizo's [Community Use Policy](https://paizo.com/licenses/communityuse). Paizo art and maps may only come from the [Community Use Package](https://paizo.com/licenses/communityuse/package) or Paizo's blog. Credit each one in `docs/license.md`. The notice in the footer comes from `copyright:` in `mkdocs.yml`.

## Adding a page

Create the `.md` file under `docs/` and add it to `nav:` in `mkdocs.yml`.
