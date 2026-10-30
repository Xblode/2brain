# Schéma du registre Brain (`entries.jsonl`)

Chaque ligne de `entries.jsonl` est un objet JSON unique. Ce schéma aligne la capture `/brain-capture` sur les garde-fous de traitement (pas d’autorité officielle implicite).

## Champs

| Champ | Obligatoire | Description |
| --- | --- | --- |
| `id` | oui | Identifiant unique (`CAP-NNN`) |
| `type` | oui | Nature : `idea` \| `observation` \| `proposition` \| `decision` \| `convention` \| `task` \| `open_question` \| `event` |
| `status` | oui | État de traitement Brain. En capture : toujours `extracted` |
| `space` | oui | Espace logique : `atelier` \| `referentiel` \| `journal` \| `pilotage` |
| `validation` | oui | Niveau d’approbation : `none` \| `implicit` \| `explicit_user_approval` |
| `author` | oui | Qui a exprimé le contenu source : `user` \| `assistant` |
| `title` | oui | Titre court |
| `content` | oui | Contenu / synthèse factuelle de l’entrée |
| `evidence` | oui | Citation courte ou repère de message justifiant l’extraction |
| `confidence` | oui | `high` \| `medium` \| `low` |
| `origin` | oui | Provenance (`source`, `url`, …) |
| `project` | oui | Identifiant projet (ex. `2brain`) |
| `created_at` | oui | Horodatage ISO de capture (pas inventé comme date d’événement source) |
| `storage` | oui | Chemin du registre (`brain/registry/entries.jsonl`) |
| `relations` | non | Liste `{ "rel", "to" }` |
| `clickup_ref` | non | Référence ClickUp existante (lecture seule) ; `null` si absent |
| `feeds_doc` | non | Doc alimenté éventuellement (`vision.md`, …) ; `null` si aucun |
| `tags` | non | Tags libres (ex. `potential`) |

## Relations (`rel`) usuelles

- `evolves_from` — évolution d’une proposition antérieure
- `supersedes_candidate` — candidat de remplacement (non résolu)
- `conflicts_with` — tension / contradiction signalée
- `feeds_doc` — nourrit un document
- `refers_clickup` — pointe une tâche ClickUp déjà existante (ne pas recréer)
- `parent_of` / `child_of` — hiérarchie (ex. sous-tâche potentielle)

## Règles d’autorité

1. `type: decision` + `status: extracted` **≠** décision officielle.
2. Décision non validée → `space: atelier` ; ne pas la présenter comme vérité dans les docs.
3. Une approbation déjà exprimée par l’utilisateur peut être notée dans `validation` / `evidence` comme **preuve**, sans re-validation.
4. Ne pas attribuer à `author: user` une proposition assistant jamais acceptée.
5. Ne pas inventer dates, références ou confirmations manquantes.
6. Conserver les évolutions (pas d’écrasement) ; résolution = futur `/brain-review`.
7. Tâches ClickUp déjà présentes : référencer via `clickup_ref` / `refers_clickup` uniquement.
8. Tâches potentielles conversationnelles : `type: task`, tag `potential`, `validation` réelle.

## Exemple minimal

```json
{
  "id": "CAP-001",
  "type": "idea",
  "status": "extracted",
  "space": "atelier",
  "validation": "none",
  "author": "user",
  "title": "...",
  "content": "...",
  "evidence": "...",
  "confidence": "high",
  "origin": {
    "source": "chatgpt-share",
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
