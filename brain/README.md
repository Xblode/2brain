---
metadata_version: 1
title: "Instance Brain du projet"
type: index
description: "Oriente vers les documents et le registre de l'instance Brain du projet 2brain."
summary: "Dossiers : docs/ (standard documentaire verrouillé, cadrage, documents provisoires), registry/ (registre de capture entries.jsonl en append only et son contrat brain/registry/SCHEMA.md), conventions/ (conventions d'instance). Ce fichier renvoie aux documents sans les recopier."
version: "1.0.0"
status: draft
created: "2026-11-06"
updated: "2026-11-06"
scope:
  level: project
  targets:
    - 2brain
updated_from:
  - "AGENTS.md"
  - "brain/docs/README.md"
---

# brain/

Instance du projet 2brain : sa documentation et son registre. Le moteur (conventions communes, outils) est dans `brain-main/`, pas ici.

## Structure

| Dossier | Contenu |
| --- | --- |
| `brain/docs/` | Documentation du projet (voir ci-dessous) |
| `brain/registry/` | `entries.jsonl` (registre de capture) et `SCHEMA.md` (son contrat) |
| `brain/conventions/` | Conventions propres à l'instance. Voir `brain/conventions/README.md` |

## Documentation (`brain/docs/`)

| Fichier | Nature | Usage |
| --- | --- | --- |
| `brain/docs/README.md` | Standard documentaire, verrouillé (`locked: true`) | Lecture seule : ne pas le modifier sans demande explicite |
| `brain/docs/CADRAGE.md` | Cadrage du projet | Vision, principes, espaces : lire par sections |
| `brain/docs/VISION.md`, `PROJECT.md`, `ARCHITECTURE.md`, `WORKFLOW.md`, `INTEGRATIONS.md` (ClickUp) | Documents provisoires | Synthèses légères, non définitives. Leurs références `CAP-xxx` pointent vers un ancien registre : voir `AGENTS.md` |

## Registre (`brain/registry/`)

- `brain/registry/entries.jsonl` est en **append only** : ne jamais réécrire ni renuméroter une entrée. On y ajoute uniquement par `brain-main/skills/brain-capture/scripts/append-captures.py` ; seule l'annulation `/brain -c 1` en retire le dernier bloc.
- `brain/registry/SCHEMA.md` est le contrat des lignes du registre ; les valeurs des champs sont dans `brain-main/conventions/TAXONOMY.md`.
