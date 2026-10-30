# Schéma registre — vue Skill

Source de vérité projet : `brain/registry/SCHEMA.md`. Ce fichier résume le contrat pour `/brain-capture` (contrat **0.1.1**).

## Champs

| Champ | Obligatoire | Notes |
| --- | --- | --- |
| `id` | oui | `CAP-NNN` unique |
| `type` | oui | `idea` \| `observation` \| `proposition` \| `decision` \| `convention` \| `task` \| `open_question` \| `event` |
| `status` | oui | Toujours `extracted` en capture |
| `space` | oui | `atelier` \| `referentiel` \| `journal` \| `pilotage` |
| `validation` | oui | `none` \| `implicit` \| `explicit_user_approval` |
| `author` | oui | `user` \| `assistant` |
| `approved_by` | oui | `user` \| `null` |
| `approval_scope` | oui | `item` \| `set` \| `null` |
| `title` | oui | Titre court |
| `content` | oui | Synthèse factuelle |
| `evidence` | oui | Preuve / citation |
| `confidence` | oui | `high` \| `medium` \| `low` |
| `origin` | oui | Objet `{ "source": "...", "url"?: "..." }` |
| `project` | oui | Ex. `2brain` |
| `created_at` | oui | ISO 8601 de capture |
| `storage` | oui | Chemin du registre cible (prod ou test-run) |
| `relations` | non | Liste `{ "rel", "to" }` vers `CAP-NNN` |
| `clickup_ref` | non | Réf. ClickUp ou `null` |
| `feeds_doc` | non | Nom de doc ou `null` |
| `tags` | non | Liste de strings |

## `approval_scope`

| Valeur | Sens |
| --- | --- |
| `item` | Accord visant **cette** capture |
| `set` | Accord visant un **bloc source clairement délimité et cité** |
| `null` | Pas d’approbation établie |

Cohérence obligatoire :

- `explicit_user_approval` ⇒ `approved_by: user` **et** `approval_scope` ∈ {`item`, `set`}
- `none` / `implicit` ⇒ `approved_by: null` **et** `approval_scope: null`

## Relations autorisées (`rel`)

`related`, `evolves_from`, `evolves_to`, `answers`, `answered_by`, `conflicts_with`, `resolves`, `supersedes_candidate`, `parent_of`, `child_of`

Interdit dans `relations` :

- cibles documentaires (`architecture.md`, …) → utiliser `feeds_doc`
- cibles ClickUp (`clickup:…`) → utiliser `clickup_ref`
- `refers_clickup`, `feeds_doc` comme valeurs de `rel`

Contraintes :

- `conflicts_with` = tension encore active seulement
- `resolves` = A clôt / tranche la tension de B (réciproque non obligatoire)
- Interdit : `evolves_*` **et** `supersedes_candidate` sur la même paire

## Exemple minimal

```json
{
  "id": "CAP-001",
  "type": "idea",
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
  "origin": { "source": "chatgpt-share", "url": "https://..." },
  "project": "2brain",
  "created_at": "2026-10-30T00:00:00Z",
  "storage": "brain/registry/entries.jsonl",
  "relations": [],
  "clickup_ref": null,
  "feeds_doc": null,
  "tags": []
}
```

## Numérotation

Prochain ID = max existant + 1, format `CAP-NNN` (padding 3+). Ne jamais réutiliser un ID.
