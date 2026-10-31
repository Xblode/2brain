# Comparaison — génération test `/brain-capture` 0.1.1

## Contexte

| | |
| --- | --- |
| Skill | `version: 0.1.1` |
| Source | `brain/sources/conversation-reference-1.txt` |
| Mode | `test-run` (forcé pour source de référence) |
| Sortie | `brain/registry/_test-runs/20261030-045232/entries.jsonl` |
| Archive 0.1.0 | `brain/registry/_test-runs/20261030-042859/` (**non modifié**) |
| Registre vivant | non modifié par ce test-run |

## Synthèse quantitative

| Métrique | Vivant (après recalibrage 0.1.1) | Test 0.1.0 | Test 0.1.1 |
| --- | --- | --- | --- |
| Entrées | 69 | 69 | 69 |
| `explicit_user_approval` | 24 | 33 | 24 |
| `none` | 45 | 36 | 45 |
| `implicit` | 0 | 0 | 0 |
| `approval_scope: item` | 24 | n/a | 24 |
| `approval_scope: set` | 0 | n/a | 0 |
| `approval_scope: null` | 45 | n/a | 45 |
| Auteur user / assistant | 36 / 33 | 36 / 33 | 36 / 33 |
| Relations (total edges) | 25 | 26 | 24 |

## `approval_global_partial` (test 0.1.1)

- `CAP-013`
- `CAP-016`
- `CAP-018`
- `CAP-026`
- `CAP-027`
- `CAP-048`

## Relations `resolves` (test 0.1.1)

- `CAP-032 → CAP-034`

## Écarts connus vs test 0.1.0

- Champ `approval_scope` introduit partout (`item` ou `null` ; aucun `set` dans cette génération).
- Demotion vers `none` + tag `approval_global_partial` pour accords globaux/partiels assistant : CAP-013, CAP-016, CAP-018, CAP-026, CAP-027, CAP-048.
- Exprimer ≠ approuver : CAP-042, CAP-043, CAP-044 (observation/event) passés en `none` / `null` / `null`.
- Conservé en `explicit` + `item` : CAP-029 (preuve item-level) et décisions/conventions/propositions user claires.
- `CAP-032` → `resolves` `CAP-034` (remplace `conflicts_with` bidirectionnel).
- `CAP-050`↔`CAP-053` : `supersedes_candidate` retiré ; famille `evolves_*` seule conservée.
- Aucun `validation: implicit` attribué.
- Numérotation indépendante du registre vivant (pas d’alignement 1:1 des IDs).

## Validateur

Exécuté sur `brain/registry/_test-runs/20261030-045232/entries.jsonl` (chemin cible test-run).

| | |
| --- | --- |
| OK bloquant | oui (0 erreur) |
| Avertissements | résumé counts uniquement |
| human_review | 6 × tag `approval_global_partial` (CAP-013, 016, 018, 026, 027, 048) |
