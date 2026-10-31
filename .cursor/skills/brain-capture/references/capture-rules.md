# Règles de capture `/brain-capture` (0.1.4)

Taxonomies canoniques : `brain-main/conventions/taxonomy.md`.

## Fidélité et couverture

- Collecter large la matière **projet** utile ; ne pas sélectionner seulement les « meilleures » idées.
- Exclure du métier : commentaires de test/génération, simulations méta, instructions temporaires de test.
- Ne pas transformer hypothèse → fait, recommandation assistant → choix user, citation → approbation.
- Préserver conditions, exceptions, refus, alternatives, incertitudes, **URLs et références exactes**.

## Atomicité

Une capture = **une information identifiable**.

| Règle | Détail |
| --- | --- |
| Un élément | Une idée, contrainte, décision, tâche, observation distincte → une CAP |
| Lier plutôt que fusionner | Infos liées mais distinctes → deux CAP + relation |
| Idée + explications | Ensemble OK si **même** info enrichie (autonomie) |
| Anti-fusion | Ne pas fusionner : convention + emplacement ; multi-exigences ; décision + proposition + question ; idées user et assistant indépendantes |
| Anti-sur-segmentation | Ne pas éclater chaque phrase d’explication d’**une** même info |

### Exemples

**Bonne** — deux CAP :

1. Convention : « le fichier de convention ClickUp s’appelle `clickup.md` »
2. Suggestion d’emplacement : « proposer sous `brain/docs/` ou `brain/conventions/` »  
   Relation : `2 clarifies 1` ou `related`.

**Mauvaise** — une CAP fourre-tout : « clickup.md sous docs/ + validé + à sync ».

**Bonne** — idée + raisons dans la même CAP si une seule orientation : « Local = SoT parce que ClickUp est un visualiseur et que le gratuit est limité ».

**Mauvaise** — fusion user « je veux des agents » + assistant « orchestrateur central recommandé » sous un seul `author`.

**Bonne** — décision user séparée de la question encore ouverte, même dans le même message.

## Intention → type (déterministe)

`intention` = référence sémantique. Appliquer le mapping de `taxonomy.md` **automatiquement** pour fixer `type`.

Cas obligatoires :

| intention | type | Interdit |
| --- | --- | --- |
| `orientation` | `proposition` | `decision` |
| `suggestion` | `proposition` | `decision` |
| `question` | `open_question` | `decision` |
| `idea` | `idea` | `decision` |

Proposition assistant ≠ décision utilisateur.  
`selected` / `confirmed` / `favorable` / `endorsed` ≠ `explicit_user_approval` automatique.

Détail des valeurs : `taxonomy.md`.

## Position, validation, status

Trois dimensions **indépendantes** (+ `space` opérationnel de rangement).

- Position = posture ; validation = preuve d’approbation formelle ; status Capture = toujours `extracted`.
- Accords partiels → tag `approval_global_partial`, `validation: none`.

## Space

| space | Usage Capture |
| --- | --- |
| `atelier` | Défaut pour exploration, propositions, questions, orientations non validées |
| `referentiel` | Uniquement connaissances / conventions / décisions **établies** (pas auto pour une suggestion) |
| `journal` | Événements / historique |
| `pilotage` | Tâches, jalons, suivi |

Classer ≠ valider. Incertitude → `atelier`. Voir `taxonomy.md` §6.

## Préservation absolue des URLs et références

Exigence **critique**.

1. Toute URL explicitement présente dans la source et pertinente pour la CAP doit être conservée **complète** (paramètres, ancres, IDs).
2. Interdit : remplacer par « lien fourni », « URL ClickUp », troncature.
3. Stocker dans **`refs[]`** (tableau de strings exactes) **et** reprendre dans `content` / `evidence`.
4. Plusieurs URLs → toutes dans `refs[]`.
5. Chemins, noms de fichiers, IDs concrets : même discipline dans `content` + `refs` si ancre de recherche.
6. Ne jamais inventer / reconstruire une URL absente.
7. `origin.url` = URL de la **source document** éventuelle — **pas** le seul stock des liens métier du contenu.

### Exemple

Source : `https://app.clickup.com/90151633729/v/f/1201110000005979/90156746497`

```json
"content": "… folder ClickUp : https://app.clickup.com/90151633729/v/f/1201110000005979/90156746497 …",
"refs": ["https://app.clickup.com/90151633729/v/f/1201110000005979/90156746497"]
```

## Contenu autonome et retrouvabilité

- Titre **spécifique** (noms concrets : CardCarousel, Minecraft, `vision.md`, …).
- Contenu compréhensible hors source ; options A/B/C définies.
- Tags utiles : `ambiguous`, `approval_global_partial`, `potential`, sujets courts (`clickup`, `inbox`, …) — sans taxonomie de tags figée.
- Éviter titres génériques (« Point important », « Suite »).

## Relations

Priorités : `answers`/`answered_by` ; `clarifies`/`clarified_by` ; `evolves_*` ; `contradicts` (≠ simple différence) ; proposition ↔ validation/rejet.

- Réciproques **recommandées** quand les deux CAP du run sont connues (`answers`↔`answered_by`, `clarifies`↔`clarified_by`, `contradicts`↔`contradicted_by`) — pas obligatoires pour `related`.
- Pas de lien pour seule proximité thématique.
- Pas de double `evolves_*` + `supersedes_candidate` sur la même paire.
- Cibles locales `CAP-NNN` uniquement (pas d’inter-runs en 0.1.4).

## Provenance — `origin.locators[]`

Inchangé vs 0.1.3 : `lines` / `offset` / `window` ; multi-passages → plusieurs locators.

## Identité

| Champ | Rôle |
| --- | --- |
| `id` | Local au fichier (`CAP-NNN`) — en production séquentielle : continuer la numérotation, ne jamais réutiliser ni réécrire |
| `run_id` | `production` ou id du dossier test-run |
| `capture_ref` | `"{run_id}:{id}"` |
| `refs` | Références littérales (URLs, …) |

## Actionable

`intention: task|milestone` même sans validation. Sujets de cadrage = CAP individuelles. Pas d’objets ClickUp créés par Capture.

## Trois couches

1. Validation technique (mécanique)  
2. Audit de capture (`AUDIT.md`)  
3. Évaluation humaine  

Le validateur ne fait que (1).
