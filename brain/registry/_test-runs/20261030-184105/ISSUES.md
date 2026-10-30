# Issues — test-run 20261030-184105 (skill direct)

## Bloquants validateur

Aucun (`--require-intention` OK).

## Méthode

Capture effectuée **sans script de génération** (`_gen.py` absent de ce run). Le run précédent `20261030-180454` contenait un générateur — à ne plus reproduire pour tester le skill.

## Ambiguïtés conservées

| CAP | Sujet |
| --- | --- |
| CAP-009 | B ou C non tranché |
| CAP-030 | Silence parfois = OK ≠ validation formelle |
| CAP-049 | « valide certaines choses » |

## Approbations

- 0× `approval_scope: set` (pas d'ensemble identifiable approuvé explicitement).
- 7× `approval_global_partial`.
- ClickUp arbo = observation (CAP-044).

## Bruit

- CAP-080 : exercice méta-test.

## Production

- `brain/registry/entries.jsonl` non modifié.
