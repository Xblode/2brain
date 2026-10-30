# Schéma registre — vue Skill (0.1.2)

Source de vérité : `brain/registry/SCHEMA.md`.

## Champs

| Champ | Obligatoire | Notes |
| --- | --- | --- |
| `id` | oui | `CAP-NNN` |
| `type` | oui | Enum 0.1.1 (`idea`, `observation`, `proposition`, `decision`, `convention`, `task`, `open_question`, `event`) |
| `intention` | oui en génération **0.1.2** ; optionnel pour entrées historiques | Voir capture-rules |
| `position` | oui (peut être `null`) en 0.1.2 | Voir capture-rules |
| `status` | oui | `extracted` en capture |
| `space` | oui | `atelier` \| `referentiel` \| `journal` \| `pilotage` |
| `validation` | oui | `none` \| `implicit` \| `explicit_user_approval` |
| `author` | oui | `user` \| `assistant` |
| `approved_by` | oui | `user` \| `null` |
| `approval_scope` | oui | `item` \| `set` \| `null` |
| `title` / `content` / `evidence` | oui | Contenu autonome |
| `confidence` | oui | `high` \| `medium` \| `low` |
| `origin` | oui | `{ "source", "url"? }` |
| `project` / `created_at` / `storage` | oui | |
| `relations` / `clickup_ref` / `feeds_doc` / `tags` | non | |

## Mapping indicatif `type` → `intention`

| type | intention typique |
| --- | --- |
| `idea` | `idea` |
| `proposition` | `suggestion` |
| `decision` | `decision` |
| `convention` | `convention` |
| `observation` | `observation` |
| `open_question` | `question` |
| `task` | `task` (ou `milestone` si jalon) |
| `event` | `observation` |

Les champs restent distincts ; ne pas supprimer `type`.

## Cohérence approbation

- `explicit_user_approval` ⇒ `approved_by: user` et `approval_scope` ∈ {`item`,`set`}
- `none` / `implicit` ⇒ `approved_by: null` et `approval_scope: null`
- `position: selected|confirmed|endorsed|favorable` ≠ validation automatique

## Relations

`related`, `evolves_from`, `evolves_to`, `answers`, `answered_by`, `conflicts_with`, `resolves`, `supersedes_candidate`, `parent_of`, `child_of`

## Orientation future (non implémentée en 0.1.2)

D'autres registres (`decisions.jsonl`, `tasks.jsonl`, …) pourront exister plus tard. `entries.jsonl` reste le registre de **capture**. Pas de déplacement automatique en 0.1.2.

## Validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py path/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py path/entries.jsonl --require-intention
```

`--require-intention` : obligatoire pour les générations V0.1.2 (test-runs neufs).
