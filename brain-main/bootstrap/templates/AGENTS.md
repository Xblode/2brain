---
metadata_version: 1
title: "Instructions agents"
type: index
description: "Point d'entrée des agents IA : renvoie à brain-main/ (moteur) et à brain/ (contenu du projet)."
version: "0.1.0"
status: draft
created: "{{date}}"
updated: "{{date}}"
---

# AGENTS.md

Point d'entrée des agents IA sur ce projet. Orientation seulement : le détail est dans les documents cités.

- `brain-main/` : moteur 2brain (conventions, skills, bootstrap). Ne pas y mettre de contenu propre au projet.
- `brain/` : contenu du projet (`docs/` pour les documents, `registry/` pour le registre de capture, `conventions/` pour les conventions d'instance).
- Commande : `/brain` donne l'état et l'aide ; `/brain -u` met à jour `brain-main/` après validation.

Ne rien modifier sans validation explicite de l'humain. Une proposition n'est pas une décision.
