# Schéma du registre Brain (`entries.jsonl`)

Chaque ligne de `entries.jsonl` est un objet JSON unique. Contrat **0.1.2** (extension compatible de 0.1.1).

`entries.jsonl` reste le registre de **capture**. D’autres registres spécialisés (décisions, tâches, roadmap…) sont une orientation future — non créés automatiquement ici.

## Champs

| Champ | Obligatoire | Description |
| --- | --- | --- |
| `id` | oui | Identifiant unique (`CAP-NNN`) |
| `type` | oui | Nature 0.1.1 : `idea` \| `observation` \| `proposition` \| `decision` \| `convention` \| `task` \| `open_question` \| `event` |
| `intention` | oui en génération **0.1.2** ; absent OK sur historiques | `idea` \| `suggestion` \| `preference` \| `orientation` \| `question` \| `decision` \| `requirement` \| `convention` \| `task` \| `milestone` \| `observation` \| `risk` \| `feedback` |
| `position` | oui en 0.1.2 (valeur `null` autorisée) ; absent OK sur historiques | `proposed` \| `exploring` \| `favorable` \| `endorsed` \| `opposed` \| `selected` \| `confirmed` \| `uncertain` \| `null` |
| `status` | oui | En capture : toujours `extracted` |
| `space` | oui | `atelier` \| `referentiel` \| `journal` \| `pilotage` |
| `validation` | oui | `none` \| `implicit` \| `explicit_user_approval` |
| `author` | oui | `user` \| `assistant` |
| `approved_by` | oui | `user` \| `null` |
| `approval_scope` | oui | `item` \| `set` \| `null` |
| `title` | oui | Titre court |
| `content` | oui | Synthèse **autonome** (compréhensible hors source) |
| `evidence` | oui | Preuve / citation |
| `confidence` | oui | `high` \| `medium` \| `low` |
| `origin` | oui | Provenance (`source`, `url` optionnel) |
| `project` | oui | Ex. `2brain` |
| `created_at` | oui | ISO de capture |
| `storage` | oui | Chemin du registre cible |
| `relations` | non | `{ "rel", "to" }` → `CAP-NNN` |
| `clickup_ref` | non | Réf. ClickUp ou `null` |
| `feeds_doc` | non | Doc ou `null` |
| `tags` | non | Tags (ex. `approval_global_partial`, `potential`) |

### Intention, position, validation

Trois dimensions distinctes. `selected` / `confirmed` / `endorsed` / `favorable` **ne déclenchent pas** automatiquement `explicit_user_approval`.

Détail des valeurs et exemples : Skill `references/capture-rules.md`.

### Approbation

- `explicit_user_approval` ⇒ `approved_by: user` **et** `approval_scope` ∈ {`item`, `set`}
- `none` / `implicit` ⇒ `approved_by: null` **et** `approval_scope: null`
- Citation / analyse / correction ≠ approbation
- `set` uniquement si approbation explicite d’un **ensemble identifiable** de captures
- Accords globaux / partiels → tag `approval_global_partial`, `validation: none`

### Relations

`related`, `evolves_from`, `evolves_to`, `answers`, `answered_by`, `conflicts_with` (tension active), `resolves`, `supersedes_candidate`, `parent_of`, `child_of`

Docs → `feeds_doc` ; ClickUp → `clickup_ref`. Pas de double evolves+supersedes sur la même paire.

## Validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py path/test/entries.jsonl --require-intention
```

## Exemple minimal (0.1.2)

```json
{
  "id": "CAP-001",
  "type": "idea",
  "intention": "idea",
  "position": "exploring",
  "status": "extracted",
  "space": "atelier",
  "validation": "none",
  "author": "user",
  "approved_by": null,
  "approval_scope": null,
  "title": "...",
  "content": "...",
  "evidence": "...",
  "confidence": "high",
  "origin": {
    "source": "brain/sources/conversation-reference-1.txt",
    "url": "https://chatgpt.com/share/6ae3fb90-b6bc-83ed-b432-22f8963f96d8"
  },
  "project": "2brain",
  "created_at": "2026-10-30T00:00:00Z",
  "storage": "brain/registry/entries.jsonl",
  "relations": [],
  "clickup_ref": null,
  "feeds_doc": null,
  "tags": []
}
```
