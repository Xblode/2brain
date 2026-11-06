---
metadata_version: 1
title: "Navigation du dépôt 2brain"
type: index
description: "Présente 2brain en quelques lignes et oriente un agent IA vers le bon dossier du dépôt."
summary: "2brain est un Second Brain : un système de gestion du cycle de vie de l'information et de standardisation des projets. Ce fichier ne fait qu'orienter vers AGENTS.md (point d'entrée des agents), brain-main/ (moteur), brain/ (instance du projet) et lab/ (essais), selon la tâche."
version: "1.0.0"
status: draft
created: "2026-11-06"
updated: "2026-11-06"
updated_from:
  - "AGENTS.md"
  - "brain-main/README.md"
---

# 2brain

**Second Brain** : système de gestion du cycle de vie de l'information (collecter, structurer, relier, versionner) et de standardisation des projets. Ce fichier est un index ; aucune règle n'y est définie.

**Agent IA : commencer par `AGENTS.md`.** Il donne l'identité du projet, les règles et les documents à lire selon la tâche.

## Où aller

| Chemin | Ce qu'on y trouve | Quand y aller |
| --- | --- | --- |
| `AGENTS.md` | Point d'entrée des agents : projet, organisation, règles, lectures par tâche | Toujours en premier |
| `brain-main/` | Moteur universel : conventions, outils (`skills/`), commande `/brain` (`bootstrap/`), règles de délégation (`brain-main/ROUTER.md`). Guide : `brain-main/README.md` | Créer ou modifier un document, capturer, chercher, installer ou mettre à jour |
| `brain/` | Instance du projet 2brain : documentation, registre de capture. Index : `brain/README.md` | Connaître le projet ou lire son registre |
| `lab/` | Essais, sources de test et rapports. Pas une source de vérité. Voir `lab/README.md` | Seulement pour retrouver un essai ou un rapport |

`CLAUDE.md` ne sert qu'à faire charger `AGENTS.md` par Claude Code.
