# Règles de capture `/brain-capture`

## Fidélité

- Conserver les formulations qui portent une condition ou une limite importante.
- Ne pas transformer une hypothèse en fait.
- Ne pas transformer une recommandation assistant en choix utilisateur.
- Ne pas supprimer les éléments refusés lorsqu'ils expliquent une évolution.
- Ne pas présenter une réponse assistant comme une réponse validée par l'utilisateur.
- Ne jamais fabriquer une citation ; une paraphrase doit rester fidèle.

## Auteur et approbateur

| Champ | Rôle |
| --- | --- |
| `author` | Personne ou agent qui a exprimé l'information (`user` \| `assistant`) |
| `approved_by` | Autorité ayant explicitement approuvé (`user` \| `null`) |

- Une proposition de l'assistant reste `author: assistant`, même si l'utilisateur l'approuve ensuite.
- Ne jamais déduire l'approbateur du simple fait que l'utilisateur ne contredit pas une proposition.
- Ne jamais transformer une proposition assistant en décision utilisateur.

## Validation

Valeurs : `none` | `implicit` | `explicit_user_approval`

| Valeur | Sens |
| --- | --- |
| `none` | Aucune approbation établie |
| `explicit_user_approval` | Accord explicite et identifiable dans la source |
| `implicit` | Valeur historique à réexaminer ; ne plus l'attribuer automatiquement |

Si la preuve ne permet pas de trancher : conserver l'incertitude et demander une vérification.

Cohérence attendue :

- `validation: explicit_user_approval` ⇒ `approved_by: user`
- `validation: none` ou `implicit` ⇒ `approved_by: null`

## Statut et espaces

- Toute capture `/brain-capture` : `status: extracted`.
- Statut, espace et validation sont trois dimensions indépendantes.
- `type: decision` + `status: extracted` ≠ décision officielle.

Espaces :

| Espace | Usage |
| --- | --- |
| `atelier` | Idées, propositions, réflexion, questions |
| `referentiel` | Informations établies et suffisamment approuvées pour servir de référence |
| `journal` | Événements, observations datées, historique |
| `pilotage` | Tâches et suivi actionnables |

Ne pas utiliser `referentiel` uniquement parce qu'une information semble importante.

## Questions et réponses

- Relier une question à sa réponse lorsque cela est démontrable (`answered_by` / `answers`).
- Distinguer une réponse utilisateur d'une réponse assistant.
- Ne pas clôturer une question simplement parce que l'assistant a proposé une solution.
- Une réponse peut être partielle ou laisser des points ouverts.

## Doublons et évolutions

- Détecter les doublons potentiels ; ne jamais fusionner silencieusement.
- Préserver les versions successives.
- `evolves_from` / `evolves_to` : évolution réelle.
- `conflicts_with` : contradiction ou tension identifiable seulement.
- `related` : lien thématique sans implication supplémentaire.
- Une évolution n'implique pas automatiquement une contradiction.

## Relations

- Une relation pointe uniquement vers une capture existante `CAP-NNN`.
- Documents → champ `feeds_doc` (pas dans `relations`).
- ClickUp → champ `clickup_ref` (pas dans `relations`).
- Ne pas inventer de relations pour « remplir » le registre.
- Relation incertaine → signaler, ne pas inventer.

Réciprocité documentée (à appliquer quand les deux côtés sont connus) :

| Relation | Réciproque |
| --- | --- |
| `answered_by` | `answers` |
| `answers` | `answered_by` |
| `evolves_from` | `evolves_to` |
| `evolves_to` | `evolves_from` |
| `parent_of` | `child_of` |
| `child_of` | `parent_of` |
| `conflicts_with` | `conflicts_with` (symétrique) |
| `related` | `related` (optionnel) |
| `supersedes_candidate` | pas de réciproque obligatoire |

## Dates et provenance

- `created_at` = date de capture (ISO), jamais une date d'événement inventée.
- Ne pas inventer : date source, id de message, URL, approbation, référence externe.
- Champs `source_at` / `source_message_id` : non introduits en V1 (utilité non démontrée pour le registre actuel ; `origin` + `evidence` suffisent).

## Preuves

- Chaque capture doit disposer d'une preuve vérifiable.
- Signaler les éléments dont la preuve est insuffisante.
