---
metadata_version: 1
title: "Vision"
type: reference
description: "Pourquoi le projet existe, ses objectifs et sa vision à long terme."
summary: "Finalité de 2brain telle que l'humain l'a dite (registre), principes directeurs et critères de réussite renvoyés au cadrage. Distingue ce qui est demandé, décidé, proposé ou ouvert. Ne décrit ni le projet, ni l'architecture."
version: "0.2.0"
status: draft
created: "2026-10-30"
updated: "2026-11-06"
scope:
  level: project
  targets:
    - 2brain
depends_on:
  - "brain/docs/README.md"
updated_from:
  - "brain/registry/entries.jsonl"
  - "brain/docs/CADRAGE.md"
---

# Vision

## 1. Objet

Pourquoi 2brain existe et où il veut aller. Ce document ne décrit pas le projet (voir `brain/docs/PROJECT.md`) ni son architecture (voir `brain/docs/ARCHITECTURE.md`). Règle de l'humain, CAP-411 : « la vision ne doit jamais vivre dans projet ni l'architecture dans vision ». Le détail et les preuves restent dans le registre et dans `brain/docs/CADRAGE.md` (§3).

Étiquettes : `décision humaine` (validée explicitement), `demande humaine` (dite par l'humain, sans validation formelle), `proposition non validée`, `question ouverte`.

## 2. Pourquoi le projet existe

- `demande humaine`. CAP-389, finalité énoncée par l'humain : « stocker les informations d'un même projet issues de sources différentes » et les trier pour produire des documents exploitables sur le long terme ; « le reprendre de n'importe où » ; « pour qu'une IA n'oublie plus aucun détail ».
- `demande humaine`. CAP-436 : « le cycle de vie des informations sera le cœur (core) du projet ».
- `demande humaine`. CAP-441 : le travail consiste à « standardiser les documents du démarrage d'un projet », puis à conventionner des documents non génériques pour chaque type de projet.
- `demande humaine`. CAP-439 : le projet permettra surtout de « produire des prompts de qualité » pour les correctifs et les mises à jour.
- `demande humaine`. CAP-438 : « lancer rapidement un projet et brainstormer régulièrement des idées ». CAP-440 : « épaule le brainstorming en gardant toujours un contexte des idées interconnectées pour un projet ».
- `demande humaine`. CAP-468 : le projet est « pour son utilisation personnelle ». CAP-475 : « chacun doit créer le sien, avec ses conventions et ses règles ». L'articulation avec l'ambition universelle du cadrage est une question ouverte (§5).

## 3. Orientation

- `demande humaine` (orientation, `validation: none`). CAP-433 : choix de la « vision C (versionnement universel des connaissances) », à approfondir avant de modifier l'architecture. CAP-434 : « les trois » dimensions (connaissances, idées, projets), « avec une priorité aux projets ».
- `demande humaine` (accord global, non validé point par point). CAP-445 : standardiser les projets revient à « voir un projet comme un produit ».

## 4. Principes directeurs

- `demande humaine`. CAP-399 : « une nouvelle compréhension du projet doit pouvoir faire évoluer sa documentation sans détruire les traces des anciennes compréhensions ». Chaque document de `brain/docs/` applique ce principe par sa section **Ancienne synthèse**.
- `demande humaine`. CAP-443 : « GitHub restera toujours une source de vérité ».
- `demande humaine`. CAP-414 : le cadrage « peut ne jamais se terminer » et une même base standard reste commune à tous les projets (accord exprimé, validation formelle non établie).

## 5. Questions ouvertes

- `question ouverte`. Critère du MVP : aucune définition n'a été validée par l'humain. Une proposition de cheminement faite sur le test de reprise n'a pas non plus été validée.
- `question ouverte`. Usage personnel et ambition universelle : comment les tenir ensemble n'est pas tranché (voir `brain/docs/CADRAGE.md` §5.6).
- `question ouverte`. Nom définitif du produit (`brain/docs/CADRAGE.md` §20.4, question 10).

## 6. Références

- Cadrage : `brain/docs/CADRAGE.md` (§3 vision actuelle, §18 critères de réussite, §20 décisions et questions). Les critères du §18 sont rédigés dans un cadrage dont le statut est « Cadrage en cours de consolidation » (CAP-465) ; ils ne sont pas copiés ici.
- Standard documentaire : `brain/docs/README.md`.

## Ancienne synthèse

Texte d'origine, conservé tel quel dans le bloc ci-dessous (règle de l'humain, CAP-399 : rien ne se perd). Il date de la première synthèse provisoire. Les numéros `CAP-xxx` qu'il cite viennent de l'ancien registre de 69 captures et ne correspondent pas au registre actuel ; pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

````markdown
# Vision

> **Provisoire** — synthèse légère issue de la capture. Détail et preuves dans `brain/registry/entries.jsonl`.
> Sources : CAP-001, CAP-004, CAP-047, CAP-049, CAP-065, CAP-068.
> **Attention : références obsolètes.** Les `CAP-xxx` de ce document viennent de l'ancien registre de 69 captures (commit `45ba05d`). Le registre actuel réutilise ces numéros pour d'autres contenus : ne pas les y chercher. Pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

## Intention (provisoire)

Second cerveau pour accompagner un travail créatif / vibecode multi-IA : capturer idées et avancées, garder la cohérence sur la durée, sans imposer un process rigide.

## Problème adressé (provisoire)

Idées perdues entre chatbots, contextes saturés, cadrage faible au départ — besoin de suivi de ce qui est décidé ou non.

## Statut documentaire

- `vision.md` retenu comme **document standard** généraliste (`validation: explicit_user_approval`) — CAP-047.
- Toute évolution contradictoire doit être **proposée** (pas d’écrasement silencieux) — CAP-049.
- Documenter dès le flux, sans attendre un cadrage « fini » — CAP-065.
````
