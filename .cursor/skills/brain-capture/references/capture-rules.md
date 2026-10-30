# Règles de capture `/brain-capture` (0.1.3)

## Fidélité et couverture

- Collecter large la matière **projet** utile ; ne pas sélectionner seulement les « meilleures » idées.
- Exclure du métier : commentaires de test/génération, simulations méta, instructions temporaires de test.
- Conserver les préférences durables sur Second Brain si clairement exprimées.
- Ne pas transformer hypothèse → fait, recommandation assistant → choix user, citation → approbation.
- Préserver conditions, exceptions, refus, alternatives, incertitudes.
- Séparer les infos de natures / positions / certitudes différentes ; ne pas sur-segmenter non plus.

## Atomicité

Une capture = **un élément d'information identifiable**.

| Règle | Détail |
| --- | --- |
| Un élément | Une idée, une contrainte, une décision, une tâche, une observation distincte → une CAP |
| Lier plutôt que fusionner | Si deux infos sont liées mais distinctes → deux CAP + relation (`related`, `clarifies`, …) |
| Idée + explications | Peuvent rester ensemble si c'est **la même** info enrichie (pas deux décisions) |
| Anti-fusion | Ne pas fusionner convention + emplacement, multi-exigences, multi-validations, ou sujets de cadrage distincts |
| Exemple anti-fusion | « clickup.md est la convention » **et** « emplacement proposé sous docs/ » → deux CAP (ou locators distincts + split si idées indépendantes), pas un seul CAP fourre-tout |

### Richesse contrôlée

- Contenu **court OK** s'il est lié (`related` / `clarifies`) à une CAP plus riche, ou si l'info source est elle-même brève.
- Sinon : **enrichir depuis la source** (passages, conditions, alternatives) — ne jamais inventer.
- Si la source ne fournit pas assez → signaler l'incomplet (`grounding: uncertain`, evidence honnête).

## Auteur principal vs contributions

- `author` = auteur **principal** de l'information (celui qui porte l'idée).
- `author_confidence` = `high` \| `medium` \| `low` \| `uncertain` — confiance dans cette attribution.
- Contributions (enrichissements assistant, précisions user) → `evidence` + `origin.locators[].role` / `note` ; **pas** de champ `contributors`.
- Si user et assistant portent des **idées indépendantes** → **deux CAP** liées (`related` / `clarifies`), pas une fusion sous un seul `author`.
- Hiérarchie d'attribution détaillée : [source-attribution.md](source-attribution.md).

Citation : distinguer auteur initial, contenu cité, commentaire actuel. Une citation n'est **pas** une nouvelle approbation.

## Intention (obligatoire en génération 0.1.3)

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

## Grounding (4 valeurs, obligatoire en 0.1.3)

Confiance dans l'**ancrage source** du contenu (distinct de `confidence` et `author_confidence`).

| Valeur | Sens |
| --- | --- |
| `source_explicit` | Formulation explicitement présente dans la source |
| `source_contextual` | Compris grâce à **plusieurs** passages (sans reformuler abusivement le sens) |
| `source_interpreted` | Reformulation / interprétation agent (raisonnable mais ≠ texte original) |
| `uncertain` | Sens ou ancrage insuffisamment établi |

Les reformulations sont autorisées ; les marquer `source_interpreted` quand ce n'est pas la formulation originale.

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

### Anti-faux `explicit`

Ne **jamais** mettre `validation: explicit_user_approval` + `grounding: source_explicit` (ni explicit tout court) quand :

| Cas | Règle |
| --- | --- |
| Orientation ambiguë / non tranchée | `validation: none` ; tag `ambiguous` si utile |
| Multi-validations / accord partiel | tag `approval_global_partial` ; `validation: none` |
| Formulation préférentielle (« B ou C », « pourrait ») | ne pas forcer `decision` + `explicit` |
| Preuve partielle seulement | `validation: none` ; `grounding` honnête (`source_interpreted` / `uncertain`) |

### Exprimer ≠ approuver

| Cas | Règle |
| --- | --- |
| user + observation/event/idea | `validation: none` |
| user + decision claire | peut être `explicit` + `item` |
| user + convention énoncée comme règle | peut être `explicit` + `item` |
| assistant | `explicit` seulement avec preuve item/set stricte ; reste `author: assistant` |

## Contenu autonome

Le `content` doit permettre de comprendre la capture sans la source : définir options (ex. modes A/B/C), raisons, conditions ; signaler l'inconnu ; ne pas inventer.

## Provenance — `origin.locators[]`

- `origin.source` (+ `url` optionnel) inchangé.
- `origin.locators` : **tableau** (1..N) obligatoire non vide en génération 0.1.3.
- Chaque localisateur : `kind` ∈ `lines` \| `window` \| `offset` ; `start`/`end` ou `window_id` selon kind ; `role` optionnel (`user`\|`assistant`\|`unknown`) ; `note` optionnelle.
- Une capture multi-passages → **plusieurs** locators, pas une seule plage approximative.
- Locators portent la provenance ; `evidence` reste lisible humain.

## Identité inter-runs

| Champ | Rôle |
| --- | --- |
| `id` | Identifiant local (`CAP-NNN`) |
| `run_id` | Identifiant du run / registre (ex. timestamp test-run ; `production` pour living) |
| `capture_ref` | `"{run_id}:{id}"` — référence composite canonique |
| `uid` | Optionnel (UUID) ; ne remplace pas `capture_ref` |

Brain Review futur cite `capture_ref` (ou `run_id`+`id`). Pas de fusion de registres en 0.1.3.

## Relations

Vocabulaire : `related`, `evolves_from`/`evolves_to`, `answers`/`answered_by`, `conflicts_with`, `resolves`, `supersedes_candidate`, `parent_of`/`child_of`, **`clarifies`/`clarified_by`**, **`contradicts`/`contradicted_by`**.

| Relation | Usage |
| --- | --- |
| `clarifies` / `clarified_by` | Une CAP précise / enrichit une autre sans la remplacer |
| `conflicts_with` | Tension **active** (désaccord non clos, concurrent) |
| `contradicts` / `contradicted_by` | Incompatibilité **affirmée et étayée** (≠ « différent ») ; Capture **ne tranche pas** |
| `resolves` | Tension close / résolution |

- Deux approches différentes mais compatibles → `related`, **pas** `contradicts`.
- Pas de relation pour simple proximité thématique.
- Pas de double `evolves_*` + `supersedes_candidate` sur la même paire.
- Cibles = `CAP-NNN` uniquement ; docs → `feeds_doc` ; ClickUp → `clickup_ref`.

## Actionable

Capturer tâches / jalons / cadrage / roadmap avec `intention: task|milestone` même sans validation définitive. Ne pas créer d'objets ClickUp. Détailler individuellement les sujets (ex. 7 sujets de cadrage = 7 captures ou contenus individuels retrouvables).

## Espaces et statut

- Capture : toujours `status: extracted`.
- Espaces : `atelier` | `referentiel` | `journal` | `pilotage`.
- `type: decision` + `extracted` ≠ décision officielle.

## Trois couches de résultat

1. **Validation technique** — validateur mécanique (schéma, enums, ids, relations, locators, cohérence structurelle).
2. **Audit de capture** — couverture source↔registre, atomicité, richesse (`AUDIT.md`).
3. **Évaluation humaine** — fidélité réelle aux intentions utilisateur (hors validateur).

Le validateur ne fait que (1). « OK » technique ≠ qualité sémantique.
