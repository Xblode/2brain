# Attribution des sources — `/brain-capture` 0.1.3

Règles pour identifier l'auteur principal et les contributions sans inventer de signatures plateforme.

## Hiérarchie d'attribution

Ordre de priorité (du plus fiable au moins) :

1. **Métadonnées de rôle** explicites dans la source (labels User / Assistant / système).
2. **Structure conversationnelle** (alternance des tours, en-têtes de message).
3. **Indices rédactionnels** (style, formules typiques) — uniquement en appoint, jamais seuls pour forcer `high`.
4. **Incertitude explicite** — si le rôle n'est pas établissable → `author_confidence: uncertain` (ou `low`).

Ne **pas** inventer de signatures ChatGPT / Claude / Cursor / autres plateformes. Si un marqueur semble spécifique à une UI mais n'est pas vérifié en live → noter « à confirmer en live » dans `evidence` / `note`, sans figer une signature inventée.

## Auteur principal vs contributions

| Concept | Champ / lieu | Règle |
| --- | --- | --- |
| Auteur principal | `author` | Qui **porte** l'idée / l'info capturée |
| Confiance d'attribution | `author_confidence` | `high` \| `medium` \| `low` \| `uncertain` |
| Contribution à un passage | `origin.locators[].role` + `note` | Rôle du passage cité, pas second auteur global |
| Enrichissement / reformulation | `evidence` | Mentionner si l'assistant a reformulé ou complété |
| Idées indépendantes | deux CAP | Lier via `related` / `clarifies` — **ne pas** fusionner |

**Ne pas** ajouter de tableau `contributors` tant que evidence + locators + splits suffisent.

## Observé vs non vérifié

| Situation | Traitement |
| --- | --- |
| Rôle clairement labelé dans le fichier source | `author` + `author_confidence: high` (si cohérent) |
| Structure claire sans label ambigu | `high` ou `medium` selon clarté |
| Indices seuls / mélange citation | `medium` ou `low` ; evidence précise |
| Impossible à trancher | `author_confidence: uncertain` ; ne pas inventer |
| Marqueur plateforme non confirmé | Ne pas figer ; « à confirmer en live » |

## Citations

- Distinguer : auteur du propos cité ≠ auteur du message actuel.
- Une citation collée n'est **pas** une approbation ni un transfert d'`author`.
- Si le user colle un bloc assistant pour commenter → CAP sur le **commentaire** (author user) + éventuelle CAP séparée sur le contenu cité si utile, liées.

## Lien avec grounding

- Attribution claire + formulation présente → souvent `grounding: source_explicit`.
- Attribution OK mais contenu reformulé par l'agent de capture → `source_interpreted` (indépendamment de `author_confidence`).
- Passages multiples nécessaires pour comprendre → `source_contextual`.
