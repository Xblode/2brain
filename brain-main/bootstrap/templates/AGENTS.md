---
metadata_version: 1
title: "Instructions agents"
type: index
description: "Point d'entrée des agents IA : contexte 2brain chargé à chaque session et consignes de base."
version: "0.2.0"
status: draft
created: "{{date}}"
updated: "{{date}}"
---

# Instructions agents

Ce projet utilise 2brain. Le moteur est dans `brain-main/` (conventions, outils, guide) ; le contenu du projet est dans `brain/` (documents, registre). Le contenu du projet va dans `brain/`, jamais dans `brain-main/`.

## Contexte chargé

Ces fichiers sont importés dans cet ordre :

@brain-main/conventions/README.md
@brain-main/conventions/TAXONOMY.md
@brain-main/README.md

Pour un outil qui n'applique pas les imports `@` : lire ces mêmes fichiers dans le même ordre (README des conventions, `brain-main/conventions/TAXONOMY.md`, puis le guide `brain-main/README.md`), puis `brain-main/conventions/NAMING.md` et `brain-main/conventions/METADATA.md` au moment voulu. Les instructions détaillées d'un outil se lisent quand l'outil sert, au chemin donné par le guide.

## Consignes

- **Obligatoire avant de créer ou modifier un document** : lire `brain-main/conventions/NAMING.md` pour un nom de fichier ou de dossier, et `brain-main/conventions/METADATA.md` pour un en-tête, une version ou une date (au moins les sections utiles).
- Si `brain/docs/` contient encore « À compléter », proposer `/brain -o` une seule fois par session.
- Ne rien modifier sans validation explicite de l'humain. Une proposition n'est pas une décision.
