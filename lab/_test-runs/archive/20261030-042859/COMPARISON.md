# Comparaison — génération test `/brain-capture` V1

## Contexte

| | |
| --- | --- |
| Source | `brain/sources/conversation-reference-1.txt` |
| Sortie | `brain/registry/_test-runs/20261030-042859/entries.jsonl` |
| Registre vivant | **non modifié** (69 entrées historiques conservées) |
| Validateur | OK bloquant (0 erreur) |

## Synthèse quantitative

| Métrique | Vivant (réf.) | Cette génération |
| --- | --- | --- |
| Entrées | 69 | 69 |
| `explicit_user_approval` | 33 | 33 |
| `none` | 30 | 36 |
| `implicit` | 6 | **0** (plus attribué) |
| Auteur user / assistant | 36 / 33 | 36 / 33 |
| Relations | 26 | 26 (après correctifs évolutifs) |

Le nombre 69 n’était pas un objectif ; la couverture utile a abouti au même ordre de grandeur.

## Qualité vs référence

### Améliorations V1

- Aucun `validation: implicit` (conforme aux règles actuelles).
- `approved_by` présent et cohérent partout.
- Relations externes (`refers_clickup`, `feeds_doc` dans `relations`) absentes.
- Tension CAP modules auto-update vs reco assistant capturée via `conflicts_with`.
- Ambiguïté « review valide certaines choses » signalée (`tags: ambiguous-validation-scope`).
- Silence ≠ approbation : nuance user sur validation par silence conservée dans le contenu, sans auto-approval.

### Écarts / risques

- Numérotation **non alignée** 1:1 avec les IDs du registre vivant (générations indépendantes).
- Certains principes assistant (niveaux de traitement, registres/docs, documenter dès le flux) restent en `validation: none` + `confidence: medium` faute d’approbation nommément isolée — plus strict que la référence qui avait converti une partie via « d’accord globalement ».
- Mapping espaces↔ClickUp laissé en `none` (pas d’accord dédié).
- Convention « séparateur exploratoire / référentiel » en `none` (alignement CAP mode B/C seulement).

### Couverture

Présents : brief, Brain/Brain-main, SoT, espaces, pipeline, contrat info, décisions user (mode, ClickUp, modules, conflits, historique, onboarding, capture auto, review, Inbox, roadmap hiérarchique), évolutions docs (operating-model, onboarding), vision.md 100 %, tâches potentielles, limite adaptateurs multi-IA.

## Critères protocole

| Critère | Note courte |
| --- | --- |
| Couverture utile | Bonne |
| Infos perdues | Faibles (détails exemples Card/Carousel condensés dans CAP conflits) |
| Faux positifs | Faibles |
| Attribution auteur | Correcte (propositions assistant restent assistant) |
| Validations injustifiées | Évitées volontairement (plus strict) |
| Questions ouvertes | Conservées (brain init, docs standard, modèle doc) |
| Doublons | Non fusionnés ; évolutions tracées |
| Relations | Pertinentes ; réciprocités principales OK |
| Fidélité preuves | Citations / paraphrases ancrées source |
| Métadonnées | Validateur vert |
