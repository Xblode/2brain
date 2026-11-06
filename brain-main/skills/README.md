---
metadata_version: 1
title: "Index des skills de brain-main"
type: index
description: "Relie chaque commande /brain d'outil à son dossier de skill et à son point d'entrée réel."
summary: "Dossiers d'outils : brain-capture, brain-onboarding, brain-search, brain-review. Pour chacun, la commande /brain associée et le fichier à ouvrir : un SKILL.md ou, sans SKILL.md, un script. Ces dossiers ne sont pas chargés automatiquement comme skills de Claude Code."
version: "1.0.0"
status: draft
created: "2026-11-06"
updated: "2026-11-06"
scope:
  level: universal
  targets:
    - brain-instances
depends_on:
  - "brain-main/bootstrap/README.md"
updated_from:
  - "AGENTS.md"
  - "brain-main/README.md"
---

# Skills de brain-main

Outils de `/brain`. Le détail de chaque commande est dans `brain-main/bootstrap/README.md` (§1 : état par commande) ; il n'est pas repris ici.

## Index

| Dossier | Rôle | Commande | Point d'entrée |
| --- | --- | --- | --- |
| `brain-main/skills/brain-capture/` | Capture | `/brain -c`, `-c <fichier>`, `-c 1` | `brain-main/skills/brain-capture/SKILL.md` (références dans `references/`, scripts dans `scripts/`) |
| `brain-main/skills/brain-onboarding/` | Onboarding | `/brain -o` | `brain-main/skills/brain-onboarding/SKILL.md` |
| `brain-main/skills/brain-search/` | Recherche | `/brain -s <sujet>` | Pas de `SKILL.md` : script `brain-main/skills/brain-search/scripts/search-registry.py` |
| `brain-main/skills/brain-review/` | Review | `/brain -r` | Pas de `SKILL.md` : script `brain-main/skills/brain-review/scripts/review-registry.py` |

## Règles d'usage

Ces dossiers ne sont pas chargés comme skills par Claude Code ; lecture et règles : `brain-main/README.md` (sections « Trois niveaux de lecture » et « Règles »).
