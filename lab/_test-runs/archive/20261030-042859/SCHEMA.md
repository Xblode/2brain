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
| `approved_by` | oui | Autorité d’approbation explicite : `user` \| `null` |
| `title` | oui | Titre court |
| `content` | oui | Contenu / synthèse factuelle de l’entrée |
| `evidence` | oui | Citation courte ou repère de message justifiant l’extraction |
| `confidence` | oui | `high` \| `medium` \| `low` |
| `origin` | oui | Provenance (`source`, `url` optionnel, …) |
| `project` | oui | Identifiant projet (ex. `2brain`) |
| `created_at` | oui | Horodatage ISO de **capture** (pas inventé comme date d’événement source) |
| `storage` | oui | Chemin du registre (`brain/registry/entries.jsonl`) |
| `relations` | non | Liste `{ "rel", "to" }` vers des captures `CAP-NNN` uniquement |
| `clickup_ref` | non | Référence ClickUp existante (lecture seule) ; `null` si absent |
| `feeds_doc` | non | Doc alimenté éventuellement (`vision.md`, …) ; `null` si aucun |
| `tags` | non | Tags libres (ex. `potential`) |

### Auteur et approbateur

- `author` identifie qui a exprimé l’information.
- `approved_by` identifie qui a **explicitement** approuvé.
- Une proposition assistant reste `author: assistant` même après approbation utilisateur.
- Ne jamais déduire une approbation du silence ou de l’absence de contradiction.

### Validation

| Valeur | Sens |
| --- | --- |
| `none` | Aucune approbation établie |
| `explicit_user_approval` | Accord explicite identifiable dans la source |
| `implicit` | Valeur **historique** ; ne plus l’attribuer automatiquement en capture |

Cohérence :

- `validation: explicit_user_approval` ⇒ `approved_by: "user"`
- `validation: none` ou `implicit` ⇒ `approved_by: null`

### Espaces

| Espace | Usage |
| --- | --- |
| `atelier` | Idées, propositions, réflexion, questions |
| `referentiel` | Informations établies et suffisamment approuvées pour référence |
| `journal` | Événements, observations datées, historique |
| `pilotage` | Tâches et éléments de suivi actionnables |

Ne pas utiliser `referentiel` seulement parce qu’une information semble importante.

### Dates et provenance

- `created_at` = date de capture.
- Ne pas inventer date source, id de message, URL, approbation ou référence externe.
- `source_at` / `source_message_id` : **non** ajoutés en V1 (`origin` + `evidence` suffisent ; utilité non démontrée pour compatibilité actuelle).

## Relations (`rel`) autorisées

Une relation pointe **uniquement** vers une capture `CAP-NNN` existante.

| `rel` | Sens |
| --- | --- |
| `related` | Lien thématique sans implication supplémentaire |
| `evolves_from` | Évolution depuis une capture antérieure |
| `evolves_to` | Évolution vers une capture postérieure |
| `answers` | Répond à une question |
| `answered_by` | Est répondue par |
| `conflicts_with` | Contradiction ou tension identifiable |
| `supersedes_candidate` | Candidat de remplacement (non résolu) |
| `parent_of` / `child_of` | Hiérarchie |

### Hors `relations`

- Documents → champ `feeds_doc`
- ClickUp → champ `clickup_ref`
- Interdit : `rel: feeds_doc`, `rel: refers_clickup`, cibles `*.md`, `clickup:…`

### Réciprocité

| Relation | Réciproque attendue |
| --- | --- |
| `answered_by` | `answers` |
| `answers` | `answered_by` |
| `evolves_from` | `evolves_to` |
| `evolves_to` | `evolves_from` |
| `parent_of` | `child_of` |
| `child_of` | `parent_of` |
| `conflicts_with` | `conflicts_with` (symétrique) |
| `related` | `related` (optionnel) |
| `supersedes_candidate` | pas d’obligation réciproque |

Une évolution n’implique pas automatiquement une contradiction. Ne pas ajouter de relations pour remplir le registre.

## Règles d’autorité

1. `type: decision` + `status: extracted` **≠** décision officielle.
2. Décision non validée → `space: atelier` ; ne pas la présenter comme vérité dans les docs.
3. Une approbation déjà exprimée par l’utilisateur peut être notée dans `validation` / `approved_by` / `evidence` comme **preuve**, sans re-validation.
4. Ne pas attribuer à `author: user` une proposition assistant jamais acceptée.
5. Ne pas inventer dates, références ou confirmations manquantes.
6. Conserver les évolutions (pas d’écrasement) ; résolution = futur `/brain-review`.
7. Tâches ClickUp déjà présentes : référencer via `clickup_ref` uniquement.
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
  "approved_by": null,
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
