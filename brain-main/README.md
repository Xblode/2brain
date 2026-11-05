# brain-main

Moteur universel Second Brain : conventions, Skills, règles et mécanismes réutilisables d’un projet à l’autre.

Ce dossier n’est **pas** la mémoire d’un projet. La mémoire et l’état d’une instance vivent dans `brain/`.

## Contenu initial

| Chemin | Rôle |
| --- | --- |
| `conventions/` | Conventions transverses (taxonomies, règles partagées) |
| `conventions/README.md` | Catalogue des conventions communes (métadonnées, nommage, taxonomies) |
| `skills/brain-capture/` | Skill de capture (`SKILL.md`, références, scripts) |
| `bootstrap/README.md` | Spécification du Bootstrap et de la commande `/brain` (scripts construits et testés, pas encore installés sur le compte ; `-c`, `-s`, `-r` prévus au lot 3) |

Le skill de capture est sous `brain-main/skills/brain-capture/`. Le Bootstrap est documenté dans `brain-main/bootstrap/README.md`.

## Principes

- Universel et évolutif : pas de détail spécifique à un client ou un outil tiers ici.
- Compatible historiquement : les nouvelles conventions n’imposent pas de réécriture des registres anciens.
- Instance séparée : ClickUp, docs projet, registres living → `brain/`.
