---
metadata_version: 1
title: "Exigences"
type: specification
description: "Ce que le projet doit accomplir : exigences dites par l'humain, avec leur source et leur état réel."
summary: "Tableau des exigences exprimées par l'humain dans le registre, avec la capture source et l'état constaté dans le dépôt (fait, partiel, absent). Aucune exigence n'est ajoutée par l'assistant. Pas de critères d'acceptation ni de priorités : aucun n'a été validé."
version: "0.2.0"
status: draft
created: "2026-11-06"
updated: "2026-11-06"
scope:
  level: project
  targets:
    - 2brain
depends_on:
  - "brain/docs/README.md"
updated_from:
  - "brain/registry/entries.jsonl"
---

# Exigences

## 1. Objet

Ce que 2brain doit accomplir, d'après ce que l'humain a réellement dit. `brain/docs/README.md` exige ce document dans le socle ; il n'existait pas dans `brain/docs/` avant le 2026-11-06. Pourquoi (vision) : `brain/docs/VISION.md`. Comment (architecture) : `brain/docs/ARCHITECTURE.md`.

## 2. Lecture du tableau

- Source : numéro de capture. Toutes sont de l'humain, en `validation: none`, sauf mention contraire : ce sont des `demande humaine` (dites, sans validation formelle). Une décision validée est signalée `décision humaine`.
- État : `fait`, `partiel` ou `absent`, constaté dans le dépôt le 2026-11-06 avec le chemin qui le prouve. Un état n'est pas une validation.
- Ne figurent pas : critères d'acceptation et priorités. Aucun n'a été validé ; les inventer n'est pas permis (`question ouverte`).

## 3. Exigences

| Exigence (telle que dite) | Source | État | Preuve ou manque |
| --- | --- | --- | --- |
| « le cycle de vie des informations sera le cœur (core) du projet » | CAP-436 | partiel | Capture, Search et Review existent (`brain-main/skills/brain-capture/scripts/append-captures.py`, `brain-main/skills/brain-search/scripts/search-registry.py`, `brain-main/skills/brain-review/scripts/review-registry.py`) ; Sync n'a aucun script |
| « stocker les informations d'un même projet issues de sources différentes » | CAP-389 | partiel | Sources de session et de fichier capturables (`brain-main/skills/brain-capture/scripts/read-session.py`) ; le tri en documents consolidés n'est pas outillé |
| Un même message peut mêler une idée structurante, une vision et une petite modification : « C'est aussi ca que ca doit résoudre » | CAP-448 | partiel | Règle d'atomicité de la capture (`brain-main/skills/brain-capture/references/capture-rules.md`) ; la qualité du résultat n'est pas contrôlée ici |
| « rechercher dans notre base ce qui a déja été fait pour un sujets similaire puis de proposer l'implémentation » | CAP-452 | partiel | Recherche dans le registre construite (`brain-main/skills/brain-search/scripts/search-registry.py`) ; règle écrite le 2026-11-06 d'après la demande de l'humain : chercher sans demander avant une implémentation, par `worker-haiku` en lecture seule (`AGENTS.md`, `brain-main/adapters/claude-code/agents/orchestrator.md`) ; c'est une règle, aucun contrôle automatique ne vérifie qu'elle est suivie, non essayée en session |
| « produire des prompts de qualité » pour les correctifs et mises à jour | CAP-439 | absent | Aucun outil de production de prompts parmi les dossiers de `brain-main/skills/` (brain-audit, brain-capture, brain-onboarding, brain-readme, brain-review, brain-search) |
| « épaule le brainstorming en gardant toujours un contexte des idées interconnectées pour un projet » | CAP-440 | absent | Aucun mécanisme dédié ; seuls registre et recherche existent |
| « lancer rapidement un projet et brainstormer régulièrement des idées » | CAP-438 | partiel | Lancement : `/brain -i` puis `/brain -o` (`brain-main/bootstrap/README.md` §2) ; brainstorming absent (ligne précédente) |
| Documents standard : « jamais être réduits ou enlevés », on peut seulement en ajouter | CAP-411 | partiel | Six modèles dans `brain-main/bootstrap/templates/brain/docs/` dont `CADRAGE.md` ; `CADRAGE.md` inscrit au catalogue `brain/docs/README.md` le 2026-11-06 (« CADRAGE.md comme 6e document standard Validé », ajout seul) ; aucun contrôle outillé n'empêche un retrait |
| « une nouvelle compréhension du projet doit pouvoir faire évoluer sa documentation sans détruire les traces des anciennes compréhensions » | CAP-399 | partiel | Registre en ajout seul (`brain/registry/SCHEMA.md`) ; section **Ancienne synthèse** dans les documents de `brain/docs/` ; Review ne consolide pas les documents |
| « GitHub restera toujours une source de vérité » | CAP-443 | partiel | Règle écrite (`AGENTS.md`, `brain/docs/CADRAGE.md` §11) ; aucun contrôle outillé |
| Conventions générales appliquées à tous les projets (naming, taxonomie) | CAP-459 | fait | `brain-main/conventions/NAMING.md`, `brain-main/conventions/TAXONOMY.md`, `brain-main/conventions/METADATA.md`, `brain-main/conventions/README.md` (NAMING, TAXONOMY et README en `status: review`) |
| Conventions de projet par type (web, mobile, autres), « quand le projet sera prêt » | CAP-437 | absent | Aucune convention spécialisée dans `brain-main/conventions/` ; `brain/conventions/README.md` : aucune convention d'instance |
| La convention Web « utilise bien » la convention générale | CAP-460 | absent | Pas de convention Web |
| Noms de documents d'un seul mot, composés tolérés | CAP-444 | partiel | `brain-main/conventions/NAMING.md` §2.2 (convention en `status: review`) |
| « la plus pars des fichier ai des propriétés comme on l'as pour Skill.md en haut du docs » | CAP-463 | partiel | `brain-main/conventions/METADATA.md` (`status: approved`) ; application aux fichiers existants non contrôlée |
| « On créera tasks.jsonl en meme temps que brain-review » | CAP-415 (`décision humaine`) | absent | Aucun `tasks.jsonl` dans `brain/registry/` ; Review écrit seulement un rapport. Voir `brain/docs/INTEGRATIONS.md` |
| « Second brain doit pouvoir utiliser Inbox » | CAP-401 | absent | Aucun mécanisme d'Inbox construit. Décision de l'humain (2026-11-06, hors registre) : « Pour l'linbox les deux vive de leur coté » : une Inbox dans ClickUp et une Inbox locale, sans synchronisation ; voir `brain/docs/INTEGRATIONS.md` §4 |
| Annuler la dernière capture avec « /brain-capture 1 » | CAP-422 | fait | `brain-main/skills/brain-capture/scripts/rollback-captures.py` ; commande `/brain -c 1` testée par scripts (`brain-main/bootstrap/tests/run_commands_tests.py`) |
| « on devrais toujours avoir un Design Systeme qui suit des code standardisé » | CAP-474 | absent | Aucun document ni convention de Design System dans le dépôt |
| Six skills externes comme sources, qui « ne doit jamais faire la même choses qu'eux » | CAP-470 | absent | Aucune intégration ; l'assistant a proposé de les garder comme références à évaluer (CAP-476, `proposition non validée`) |
| « Il doit faire le role d'un gestionnaire » avec plusieurs agents | CAP-407 | absent | `.claude/agents/` ne contient que le routage (`orchestrator.md`, `worker-haiku.md`, `worker-sonnet.md`) |
| « plusieurs pierre autour par la suite qui me permettrons de piloter mes activités depuis n'importe ou » | CAP-469 | absent | Rien de construit |

## 4. Questions ouvertes

- `question ouverte`. Critères d'acceptation et priorités : aucun validé.
- `question ouverte`. MVP : aucune définition validée ; une proposition de cheminement sur le test de reprise est restée sans validation.
- `question ouverte`. Un registre local de tâches (`tasks.jsonl`), son format et son lien avec l'Inbox : voir `brain/docs/INTEGRATIONS.md`.

## 5. Références

`brain/registry/entries.jsonl`, `brain/docs/CADRAGE.md` (§5 besoins, §16 exigences non fonctionnelles), `brain/docs/README.md`, `brain-main/bootstrap/README.md` (§1 état par commande).
