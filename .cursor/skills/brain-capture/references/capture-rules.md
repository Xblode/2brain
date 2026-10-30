# Règles de capture `/brain-capture` (0.1.2)

## Fidélité et couverture

- Collecter large la matière **projet** utile ; ne pas sélectionner seulement les « meilleures » idées.
- Exclure du métier : commentaires de test/génération, simulations méta, instructions temporaires de test.
- Conserver les préférences durables sur Second Brain si clairement exprimées.
- Ne pas transformer hypothèse → fait, recommandation assistant → choix user, citation → approbation.
- Préserver conditions, exceptions, refus, alternatives, incertitudes.
- Séparer les infos de natures / positions / certitudes différentes ; ne pas sur-segmenter non plus.

## Auteur et citations

Priorité d'attribution : métadonnées de rôle → structure conversation → indices rédactionnels → incertitude explicite.

Citation : distinguer auteur initial, contenu cité, commentaire actuel. Une citation n'est **pas** une nouvelle approbation.

## Intention (obligatoire en génération 0.1.2)

Une intention principale par capture. Ne pas inventer de nouvelles valeurs.

| Intention | Signification | Exemple |
| --- | --- | --- |
| `idea` | Idée / possibilité explorée | « Et si on avait un journal d'activité… » |
| `suggestion` | Proposition formulée | Assistant propose quatre espaces logiques |
| `preference` | Préférence exprimée | « Je préfère ClickUp comme visualiseur » |
| `orientation` | Direction provisoire | « On part sur un socle universel + modules » |
| `question` | Question ouverte | « brain init une fois ou par session ? » |
| `decision` | Choix explicitement effectué | « Pour 3 : oui socle universel + modules » |
| `requirement` | Besoin / contrainte | « UX ultra importante, ~10–15 commandes max » |
| `convention` | Règle de fonctionnement | Capture → registres ; Review → docs |
| `task` | Action à réaliser (même potentielle) | « Standardiser le contenu des docs plus tard » |
| `milestone` | Étape / jalon structurant | Une couche « Core minimal » de la roadmap |
| `observation` | Constat factuel | « ClickUp a déjà deux espaces » |
| `risk` | Risque identifié | « Un skill seul ne garantit pas l'écriture auto » |
| `feedback` | Retour / critique / correction | « d'accord globalement… par contre les docs… » |

Conserver aussi `type` (schéma 0.1.1). Mapping indicatif : `proposition`↔`suggestion`, `open_question`↔`question`, `idea`↔`idea`, etc. Les deux champs restent distincts.

## Position (nullable)

Posture de l'auteur. `null` si non identifiable. **Ne pas déduire abusivement.**

| Position | Signification | Exemple |
| --- | --- | --- |
| `proposed` | Proposition formulée | Assistant pose une hypo |
| `exploring` | Piste explorée | User explore sans choisir |
| `favorable` | Avis favorable | « c'est pas mal ce que tu proposes » |
| `endorsed` | Bonne base / à conserver comme matière | « ça fait une bonne base de travail » |
| `opposed` | Opposition | « je ne veux pas ça » |
| `selected` | Option explicitement choisie | « je dirais B ou C » |
| `confirmed` | Règle / info confirmée | « vision.md validé à 100% » |
| `uncertain` | Hésitation | « je sais pas si on a déjà fixé ça » |
| `null` | Aucune position claire | Observation neutre |

### Intention / position / validation = trois dimensions

- `selected` ou `confirmed` **ne déclenchent pas** automatiquement `validation: explicit_user_approval`.
- `favorable` / `endorsed` = signal de pertinence, pas validation formelle.
- Validation formelle uniquement avec preuve d'approbation + `approval_scope` ∈ {`item`,`set`}.

## Validation et `approval_scope`

| validation | Sens |
| --- | --- |
| `none` | Pas d'approbation formelle établie |
| `explicit_user_approval` | Accord explicite identifiable |
| `implicit` | Historique ; ne plus attribuer |

| approval_scope | Sens |
| --- | --- |
| `item` | Approbation explicite de **cette** capture |
| `set` | Approbation explicite d'un **ensemble identifiable** de captures |
| `null` | Pas d'approbation formelle |

### Distinguer

| Acte | Effet |
| --- | --- |
| Citation d'un bloc | Preuve / contexte — **pas** approbation |
| Analyse / reformulation | Compréhension — **pas** approbation |
| Correction | Relation de précision/évolution — **pas** approbation |
| Approbation partielle (« d'accord globalement », « bonne base ») | Tag `approval_global_partial` ; `validation: none` ; confiance ↑ ; suggestions restent suggestions |
| Approbation explicite d'un élément | `explicit` + `scope: item` |
| Approbation explicite d'un ensemble nommé/délimité | `explicit` + `scope: set` (uniquement si l'ensemble de captures est identifiable) |

Ne pas étendre une approbation partielle hors du segment concerné. Pas de cherry-picking silencieux dans un `set`.

### Exprimer ≠ approuver

| Cas | Règle |
| --- | --- |
| user + observation/event/idea | `validation: none` |
| user + decision claire | peut être `explicit` + `item` |
| user + convention énoncée comme règle | peut être `explicit` + `item` |
| assistant | `explicit` seulement avec preuve item/set stricte ; reste `author: assistant` |

## Contenu autonome

Le `content` doit permettre de comprendre la capture sans la source : définir options (ex. modes A/B/C), raisons, conditions ; signaler l'inconnu ; ne pas inventer.

## Relations

Vocabulaire : `related`, `evolves_from`/`evolves_to`, `answers`/`answered_by`, `conflicts_with` (tension **active**), `resolves`, `supersedes_candidate`, `parent_of`/`child_of`.

- Réponse / précision / correction / concurrence / évolution : utiliser ces `rel` selon le sens réel.
- Pas de relation pour simple proximité thématique.
- Pas de double `evolves_*` + `supersedes_candidate` sur la même paire.
- Cibles = `CAP-NNN` uniquement ; docs → `feeds_doc` ; ClickUp → `clickup_ref`.

## Actionable

Capturer tâches / jalons / cadrage / roadmap avec `intention: task|milestone` même sans validation définitive. Ne pas créer d'objets ClickUp. Détailler individuellement les sujets (ex. 7 sujets de cadrage = 7 captures ou contenus individuels retrouvables).

## Espaces et statut

- Capture : toujours `status: extracted`.
- Espaces : `atelier` | `referentiel` | `journal` | `pilotage`.
- `type: decision` + `extracted` ≠ décision officielle.
