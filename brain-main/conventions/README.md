# Conventions brain-main

Conventions **communes** à toute instance Brain. Elles définissent le langage partagé des registres et des Skills, pas le contenu d’un projet.

## Catalogue

| Fichier | Responsabilité |
| --- | --- |
| [taxonomy.md](taxonomy.md) | Taxonomies des champs de capture / registres (`intention`, `type`, `position`, `status`, `space`, relations, `grounding`, confidences) |

## Règles

- Ne pas dupliquer ici le catalogue documentaire (`brain/docs/README.md`).
- Ne pas y placer les conventions d’instance (ClickUp, naming projet, etc.) → `brain/conventions/`.
- Toute évolution de valeur d’enum doit documenter compatibilité historique dans `taxonomy.md`.
- Les Skills (`/brain-capture`, …) **appliquent** ces conventions ; la source de vérité des valeurs autorisées est `taxonomy.md` + `brain/registry/SCHEMA.md`.
