---
metadata_version: 1
title: "Instance Brain du projet"
type: index
description: "Oriente vers les documents et le registre de l'instance Brain du projet 2brain."
summary: "Dossiers : docs/ (standard documentaire verrouillé qui impose six documents standards : VISION, CADRAGE, PROJECT, REQUIREMENTS, ARCHITECTURE, WORKFLOW ; INTEGRATIONS est facultatif ; hors CADRAGE, les documents sont en brouillon), registry/ (registre de capture entries.jsonl en append only et son contrat brain/registry/SCHEMA.md), conventions/ (conventions d'instance). Ce fichier renvoie aux documents sans les recopier."
version: "1.2.0"
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
  - "brain/docs/CADRAGE.md"
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
| `brain/docs/README.md` | Standard documentaire, verrouillé (`locked: true`), six documents standards | Lecture seule : ne pas le modifier sans demande explicite (modifié une fois, le 2026-11-06, avec l'autorisation expresse de l'humain, pour ajouter `cadrage.md`) |
| `brain/docs/CADRAGE.md` | Cadrage du projet, sixième document standard | Contexte, besoins, objectifs, périmètre, principes, espaces : lire par sections |
| `brain/docs/VISION.md` | Vision (`status: draft`) | Pourquoi le projet existe, principes, critères de réussite renvoyés au cadrage |
| `brain/docs/PROJECT.md` | Projet (`status: draft`) | Identité, utilisateurs, périmètre, contraintes, état actuel constaté |
| `brain/docs/REQUIREMENTS.md` | Exigences (`status: draft`) | Exigences dites par l'humain, avec capture source et état (fait, partiel, absent) |
| `brain/docs/ARCHITECTURE.md` | Architecture (`status: draft`) | Organisation du dépôt, où vit quoi, mécanismes et leur état |
| `brain/docs/WORKFLOW.md` | Méthode de travail (`status: draft`) | Flux réel de `/brain`, routeur, chaînons manquants |
| `brain/docs/INTEGRATIONS.md` | Intégrations (`status: draft`) | GitHub, registre, ClickUp (Inbox, `tasks.jsonl`), outils externes |

Chacun de ces documents, sauf `REQUIREMENTS.md` (nouveau), garde son texte d'origine dans une section « Ancienne synthèse » ; les anciens numéros `CAP-xxx` (ancien registre) ne se trouvent que là, voir `AGENTS.md`. Ailleurs, les numéros renvoient au registre actuel.

## Registre (`brain/registry/`)

- `brain/registry/entries.jsonl` est en **append only** : ne jamais réécrire ni renuméroter une entrée. On y ajoute uniquement par `brain-main/skills/brain-capture/scripts/append-captures.py` ; seule l'annulation `/brain -c 1` en retire le dernier bloc.
- `brain/registry/SCHEMA.md` est le contrat des lignes du registre ; les valeurs des champs sont dans `brain-main/conventions/TAXONOMY.md`.
