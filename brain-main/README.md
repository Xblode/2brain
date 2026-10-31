# brain-main

Moteur universel Second Brain : conventions, Skills, règles et mécanismes réutilisables d’un projet à l’autre.

Ce dossier n’est **pas** la mémoire d’un projet. La mémoire et l’état d’une instance vivent dans `brain/`.

## Contenu initial

| Chemin | Rôle |
| --- | --- |
| `conventions/` | Conventions transverses (taxonomies, règles partagées) |
| `conventions/taxonomy.md` | Valeurs et sémantique des champs de registre communs |

Les Skills Cursor restent pour l’instant sous `.cursor/skills/` (installation outil). Leur migration complète vers `brain-main/` est hors de ce correctif.

## Principes

- Universel et évolutif : pas de détail spécifique à un client ou un outil tiers ici.
- Compatible historiquement : les nouvelles conventions n’imposent pas de réécriture des registres anciens.
- Instance séparée : ClickUp, docs projet, registres living → `brain/`.
