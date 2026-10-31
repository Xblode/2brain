# Attribution des sources — `/brain-capture` 0.1.4

## Hiérarchie d’attribution

Du plus fiable au moins :

1. **Métadonnées de rôle** explicites (labels `User` / `Assistant` / système).
2. **Structure conversationnelle** (alternance claire des tours, en-têtes de message).
3. **Indices rédactionnels** (style) — **appoint uniquement**, jamais seuls pour `author_confidence: high`.
4. **Incertitude** — si non établissable → `uncertain` ou `low`.

Ne **pas** inventer de signatures ChatGPT / Claude / Cursor. Marqueur UI non vérifié en live → « à confirmer en live » dans `evidence` / `note`.

## Niveaux `author_confidence`

| Niveau | Quand |
| --- | --- |
| `high` | Structure source permet une attribution **fiable** (labels ou tours clairement séparés) |
| `medium` | Attribution **probable** mais indirecte (export partiellement structuré, collage avec indices) |
| `low` | Indices faibles ; doute sérieux |
| `uncertain` | Auteur non établissable correctement |

**Règle** : le style rédactionnel **seul** ne suffit jamais pour `high`.

## Formats réellement rencontrés

| Format source | Traitement typique |
| --- | --- |
| Export avec labels `User` / `Assistant` | `high` si cohérent |
| Collage brut sans labels (`conversation-reference-*.txt`) | Déduire par alternance / structure → souvent `medium` ; passages ambigus → `low` / `uncertain` |
| User colle un long bloc assistant puis commente | CAP commentaire = `author: user` ; CAP contenu cité si utile = `author: assistant` (ou uncertain) ; liées |
| Citation inline | Auteur du propos cité ≠ auteur du message actuel |

## Auteur principal vs contributions

| Concept | Lieu | Règle |
| --- | --- | --- |
| Auteur principal | `author` | Qui **porte** l’idée capturée |
| Confiance | `author_confidence` | Voir seuils ci-dessus |
| Contribution | `origin.locators[].role` + `note` | Rôle du passage, pas second auteur global |
| Enrichissement | `evidence` | Mentionner reformulation assistant |
| Idées indépendantes | deux CAP | `related` / `clarifies` — ne pas fusionner |

Pas de tableau `contributors`.

## Citations ≠ approbations

- Coller / citer ≠ approuver.
- Ne pas transférer `author` ni monter `validation` sur une citation.

## Lien avec grounding

- Attribution claire + formulation présente → souvent `source_explicit`.
- Contenu reformulé par l’agent de capture → `source_interpreted` (indépendant de `author_confidence`).
- Multi-passages → `source_contextual`.
