# Schéma registre — vue Skill (0.1.3)

Source de vérité : `brain/registry/SCHEMA.md`.

## Champs

| Champ | Obligatoire | Notes |
| --- | --- | --- |
| `id` | oui | `CAP-NNN` (local au registre) |
| `run_id` | oui en génération **0.1.3** ; optionnel historiques | Ex. timestamp test-run ou `production` |
| `capture_ref` | oui en 0.1.3 | `"{run_id}:{id}"` — référence inter-runs |
| `uid` | non | UUID optionnel |
| `type` | oui | Enum 0.1.1 (`idea`, `observation`, `proposition`, `decision`, `convention`, `task`, `open_question`, `event`) |
| `intention` | oui en génération **0.1.3** ; optionnel historiques | Voir capture-rules |
| `position` | oui (peut être `null`) en 0.1.3 | Voir capture-rules |
| `status` | oui | `extracted` en capture |
| `space` | oui | `atelier` \| `referentiel` \| `journal` \| `pilotage` |
| `validation` | oui | `none` \| `implicit` \| `explicit_user_approval` |
| `author` | oui | Auteur principal `user` \| `assistant` |
| `author_confidence` | oui en 0.1.3 | `high` \| `medium` \| `low` \| `uncertain` |
| `approved_by` | oui | `user` \| `null` |
| `approval_scope` | oui | `item` \| `set` \| `null` |
| `title` / `content` / `evidence` | oui | Contenu autonome |
| `confidence` | oui | Extraction : `high` \| `medium` \| `low` |
| `grounding` | oui en 0.1.3 | `source_explicit` \| `source_contextual` \| `source_interpreted` \| `uncertain` |
| `origin` | oui | `{ "source", "url"?, "locators"? }` — `locators[]` obligatoire non vide en 0.1.3 |
| `project` / `created_at` / `storage` | oui | |
| `relations` / `clickup_ref` / `feeds_doc` / `tags` | non | |

### `origin.locators[]`

Chaque item : `kind` ∈ `lines`\|`window`\|`offset` ; `start`/`end` ou `window_id` ; `role?` ; `note?`.

### Mapping indicatif `type` → `intention`

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

`related`, `evolves_from`, `evolves_to`, `answers`, `answered_by`, `conflicts_with`, `resolves`, `supersedes_candidate`, `parent_of`, `child_of`, `clarifies`, `clarified_by`, `contradicts`, `contradicted_by`

## Orientation future (non implémentée en 0.1.3)

D'autres registres (`decisions.jsonl`, `tasks.jsonl`, …) pourront exister plus tard. `entries.jsonl` reste le registre de **capture**. Pas de déplacement automatique. Pas de Brain Review / Sync / ClickUp / graphe en 0.1.3.

## Trois couches de résultat

1. Validation technique (validateur) — 2. Audit de capture (`AUDIT.md`) — 3. Évaluation humaine.

Le validateur est **mécanique uniquement**.

## Validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py path/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py path/entries.jsonl --require-intention
python .cursor/skills/brain-capture/scripts/validate-registry.py path/entries.jsonl --require-intention --json-out validate.json
```

`--require-intention` : obligatoire pour les générations V0.1.3 (test-runs neufs). Vide = ERROR ; exige intention, position, author_confidence, grounding, run_id, capture_ref, locators[] non vide.
