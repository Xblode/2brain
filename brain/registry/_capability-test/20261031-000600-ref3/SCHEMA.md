# Schéma du registre Brain (`entries.jsonl`)

Chaque ligne de `entries.jsonl` est un objet JSON unique. Contrat **0.1.3** (extension compatible de 0.1.2).

`entries.jsonl` reste le registre de **capture**. D’autres registres spécialisés (décisions, tâches, roadmap…) sont une orientation future — non créés automatiquement ici.

## Champs

| Champ | Obligatoire | Description |
| --- | --- | --- |
| `id` | oui | Identifiant local au registre (`CAP-NNN`) |
| `run_id` | oui en génération **0.1.3** ; absent OK sur historiques | Identifiant du run / registre (ex. `20261030-194948`, `production`) |
| `capture_ref` | oui en 0.1.3 ; absent OK sur historiques | Référence composite : `"{run_id}:{id}"` (ex. `20261030-194948:CAP-031`) |
| `uid` | non | UUID optionnel à la création ; ne remplace pas `capture_ref` |
| `type` | oui | Nature 0.1.1 : `idea` \| `observation` \| `proposition` \| `decision` \| `convention` \| `task` \| `open_question` \| `event` |
| `intention` | oui en génération **0.1.3** ; absent OK sur historiques | `idea` \| `suggestion` \| `preference` \| `orientation` \| `question` \| `decision` \| `requirement` \| `convention` \| `task` \| `milestone` \| `observation` \| `risk` \| `feedback` |
| `position` | oui en 0.1.3 (valeur `null` autorisée) ; absent OK sur historiques | `proposed` \| `exploring` \| `favorable` \| `endorsed` \| `opposed` \| `selected` \| `confirmed` \| `uncertain` \| `null` |
| `status` | oui | En capture : toujours `extracted` |
| `space` | oui | `atelier` \| `referentiel` \| `journal` \| `pilotage` |
| `validation` | oui | `none` \| `implicit` \| `explicit_user_approval` |
| `author` | oui | Auteur **principal** : `user` \| `assistant` |
| `author_confidence` | oui en 0.1.3 ; absent OK sur historiques | `high` \| `medium` \| `low` \| `uncertain` |
| `approved_by` | oui | `user` \| `null` |
| `approval_scope` | oui | `item` \| `set` \| `null` |
| `title` | oui | Titre court |
| `content` | oui | Synthèse **autonome** (compréhensible hors source) |
| `evidence` | oui | Preuve / citation (peut mentionner contributions) |
| `confidence` | oui | Confiance dans l’extraction du contenu : `high` \| `medium` \| `low` |
| `grounding` | oui en 0.1.3 ; absent OK sur historiques | `source_explicit` \| `source_contextual` \| `source_interpreted` \| `uncertain` |
| `origin` | oui | Provenance (voir ci-dessous) |
| `project` | oui | Ex. `2brain` |
| `created_at` | oui | ISO de capture |
| `storage` | oui | Chemin du registre cible |
| `relations` | non | `{ "rel", "to" }` → `CAP-NNN` |
| `clickup_ref` | non | Réf. ClickUp ou `null` |
| `feeds_doc` | non | Doc ou `null` |
| `tags` | non | Tags (ex. `approval_global_partial`, `potential`, `ambiguous`) |

### `origin` (étendu 0.1.3)

```json
{
  "source": "brain/sources/conversation-reference-3.txt",
  "url": null,
  "locators": [
    {
      "kind": "lines",
      "start": 120,
      "end": 125,
      "role": "user",
      "note": "idée initiale"
    },
    {
      "kind": "lines",
      "start": 210,
      "end": 214,
      "role": "user",
      "note": "contrainte ajoutée"
    }
  ]
}
```

- `source` : chemin ou identifiant de source (obligatoire ; string non vide en génération 0.1.3).
- `url` : optionnel (string ou absent/`null`).
- `locators` : **tableau** (1..N) obligatoire non vide en génération 0.1.3 (`--require-intention`). Sous `--require-intention`, `origin` doit être un **objet** (pas `null`), avec `source` + `locators[]` valides.
- Chaque item : `kind` ∈ `lines` \| `window` \| `offset` ; `role` optionnel (`user`\|`assistant`\|`unknown`) ; `note` optionnelle.
- Rétrocompat : anciennes entrées sans `locators` OK hors `--require-intention`. Pas d’ancien champ unique `locator`.

#### Conventions `origin.locators[]`

| `kind` | Bornes | Règles |
| --- | --- | --- |
| `lines` | `start`, `end` | **1-based inclusif** ; entiers positifs (`>= 1`) ; `end >= start` |
| `offset` | `start`, `end` | Positions de **caractères Unicode** ; **0-based** ; `start` inclusif, `end` **exclusif** ; `start >= 0` ; `end >= start` |
| `window` | `window_id` | String **non vide**. Pour retrouver la fenêtre : utiliser `window_id` dans les artefacts / notes de run (découpage fenêtres du skill) ou la source associée à `origin.source` — le schéma ne stocke pas le texte de la fenêtre. |

Rejets mécaniques : négatifs hors convention, booléens utilisés comme int, plages invalides (`end < start`), types incorrects, locators incomplets. Pas de nouveaux kinds.

### Identité inter-runs

- `id` reste local au fichier (`CAP-NNN` réutilisable entre runs).
- `capture_ref` = `"{run_id}:{id}"` est la référence stable pour un Review futur.
- Cohérence mécanique : `capture_ref` doit égaler `run_id + ":" + id`.
- **Limite 0.1.3** : `relations[].to` reste un `CAP-NNN` **local au même run / même fichier**. `capture_ref` prépare l’identité inter-runs mais **n’autorise pas encore** les relations inter-runs. Brain Review traitera ce cas plus tard. Aucun changement de format de `relations` en 0.1.3.

### Attribution

- `author` = auteur principal ; contributions via `evidence` / `origin.locators[].role` — **pas** de tableau `contributors`.
- `author_confidence` distinct de `confidence` (extraction) et `grounding` (ancrage).
- Idées indépendantes user/assistant → deux CAP liées.

### Intention, position, validation, grounding

Quatre dimensions distinctes. `selected` / `confirmed` / `endorsed` / `favorable` **ne déclenchent pas** automatiquement `explicit_user_approval`.

Détail : Skill `references/capture-rules.md` et `references/source-attribution.md`.

### Approbation

- `explicit_user_approval` ⇒ `approved_by: user` **et** `approval_scope` ∈ {`item`, `set`}
- `none` / `implicit` ⇒ `approved_by: null` **et** `approval_scope: null`
- Citation / analyse / correction ≠ approbation
- `set` uniquement si approbation explicite d’un **ensemble identifiable** de captures
- Accords globaux / partiels → tag `approval_global_partial`, `validation: none`

### Relations

`related`, `evolves_from`, `evolves_to`, `answers`, `answered_by`, `conflicts_with` (tension active), `resolves`, `supersedes_candidate`, `parent_of`, `child_of`, `clarifies`, `clarified_by`, `contradicts`, `contradicted_by`

- Cibles : `relations[].to` = `CAP-NNN` **local au même run** (pas de `capture_ref` / ID d’un autre registre).
- `conflicts_with` = tension active ; `contradicts` = incompatibilité affirmée étayée (Capture ne tranche pas).
- Docs → `feeds_doc` ; ClickUp → `clickup_ref`. Pas de double evolves+supersedes sur la même paire.

## Trois couches de résultat

1. **Validation technique** — validateur mécanique uniquement.
2. **Audit de capture** — `AUDIT.md` (couverture, atomicité, richesse).
3. **Évaluation humaine** — hors validateur.

« OK » validateur ≠ qualité sémantique.

## Validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py path/test/entries.jsonl --require-intention
python .cursor/skills/brain-capture/scripts/validate-registry.py path/test/entries.jsonl --require-intention --json-out validate.json
```

Sous `--require-intention` (générations 0.1.3) : fichier vide = **ERROR** ; exige `intention`, `position`, `author_confidence`, `grounding`, `run_id`, `capture_ref` ; `origin` objet avec `source` non vide et `origin.locators` non vide (chaque locator conforme aux conventions).

## Exemple minimal (0.1.3)

```json
{
  "id": "CAP-001",
  "run_id": "20261030-220000",
  "capture_ref": "20261030-220000:CAP-001",
  "type": "idea",
  "intention": "idea",
  "position": "exploring",
  "status": "extracted",
  "space": "atelier",
  "validation": "none",
  "author": "user",
  "author_confidence": "high",
  "approved_by": null,
  "approval_scope": null,
  "title": "...",
  "content": "...",
  "evidence": "...",
  "confidence": "high",
  "grounding": "source_explicit",
  "origin": {
    "source": "brain/sources/conversation-reference-3.txt",
    "url": null,
    "locators": [
      {"kind": "lines", "start": 10, "end": 14, "role": "user"}
    ]
  },
  "project": "2brain",
  "created_at": "2026-10-30T22:00:00Z",
  "storage": "brain/registry/_test-runs/20261030-220000/entries.jsonl",
  "relations": [],
  "clickup_ref": null,
  "feeds_doc": null,
  "tags": []
}
```
