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
| `approval_scope` | Portée de l'accord (`item` \| `set` \| `null`) |

- Une proposition de l'assistant reste `author: assistant`, même si l'utilisateur l'approuve ensuite.
- Ne jamais déduire l'approbateur du simple fait que l'utilisateur ne contredit pas une proposition.
- Ne jamais transformer une proposition assistant en décision utilisateur.

## Validation et `approval_scope`

Valeurs validation : `none` | `implicit` | `explicit_user_approval`

| Valeur | Sens |
| --- | --- |
| `none` | Aucune approbation établie |
| `explicit_user_approval` | Accord explicite et identifiable dans la source |
| `implicit` | Valeur historique à réexaminer ; ne plus l'attribuer automatiquement |

| `approval_scope` | Sens |
| --- | --- |
| `item` | Accord visant **cette** capture |
| `set` | Accord visant un **bloc source clairement délimité et cité** dont cette capture est un élément identifiable |
| `null` | Pas d'approbation établie |

Règles dures :

- `approved_by: user` + `validation: explicit_user_approval` **uniquement** si `approval_scope` ∈ {`item`, `set`}
- Accords « bonne base » / « d'accord globalement » **avec réserves** → `validation: none`, `approved_by: null`, `approval_scope: null`, tag `approval_global_partial` + signalement human_review
- Pas de cherry-picking silencieux dans un `set` : un élément non approuvé du même bloc empêche l'héritage automatique ; préférer `none` + tag
- En cas de doute → `none` / `null` / `null`

Cohérence attendue :

- `validation: explicit_user_approval` ⇒ `approved_by: user` **et** `approval_scope` ∈ {`item`, `set`}
- `validation: none` ou `implicit` ⇒ `approved_by: null` **et** `approval_scope: null`

## Exprimer ≠ approuver

| Cas | Règle |
| --- | --- |
| `author: user` + `type: decision` | `explicit` + `approved_by: user` + `scope: item` si l'utilisateur formule/choisit clairement |
| `author: user` + `type: convention` qu'il énonce comme règle | idem |
| `author: user` + `type: observation \| event \| idea` | `validation: none`, `approved_by: null`, `approval_scope: null` (fait rapporté ≠ approbation) |
| `author: user` + `type: proposition` | `explicit` seulement si formulation claire de « je veux que… » comme orientation retenue ; sinon `none` |
| `author: assistant` | `explicit` seulement avec preuve `item`/`set` stricte ; reste `author: assistant` |

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
- `evolves_from` / `evolves_to` : évolution réelle sur le **même fil opérationnel** clairement successif ; sinon `related`.
- `conflicts_with` : tension **encore active** seulement.
- `resolves` : A clôt / tranche la tension portée par B (réciproque non obligatoire). Une décision user qui tranche une reco assistant → `resolves` depuis la décision, pas `conflicts_with` bidirectionnel.
- Interdit : `evolves_*` **et** `supersedes_candidate` sur la **même paire** ; choisir une seule famille.
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
| `resolves` | pas de réciproque obligatoire |
| `supersedes_candidate` | pas de réciproque obligatoire |

## Dates et provenance

- `created_at` = date de capture (ISO), jamais une date d'événement inventée.
- Ne pas inventer : date source, id de message, URL, approbation, référence externe.
- Champs `source_at` / `source_message_id` : non introduits en V1 (utilité non démontrée pour le registre actuel ; `origin` + `evidence` suffisent).

## Preuves

- Chaque capture doit disposer d'une preuve vérifiable.
- Signaler les éléments dont la preuve est insuffisante.
