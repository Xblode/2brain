# Comparaison — capture 0.1.2 vs référence 0.1.1

| | |
| --- | --- |
| Nouvelle capture | `brain/registry/_test-runs/20261030-180454/` |
| Référence | `brain/registry/_test-runs/20261030-061941/` |
| Source | `brain/sources/conversation-reference-1.txt` uniquement |
| Échantillon 2 | **non utilisé** (`conversation-reference-2.txt` existe, 79 571 o. ; hors comparaison) |
| Méthode | Extraction neuve (script `_gen.py` documentaire) — **pas** une transformation du JSONL 061941 |
| Validateur 180454 | OK bloquant avec `--require-intention` |
| Validateur production | OK bloquant **sans** `--require-intention` (compatibilité) |

## Synthèse chiffrée

| Indicateur | 061941 (réf.) | 180454 (0.1.2) |
| --- | ---: | ---: |
| Entrées | 69 | 77 |
| `intention` renseignée | 0 | 77 |
| `position` = `null` | n/a | 9 |
| `explicit_user_approval` | 23 | 22 |
| `approval_scope: set` | 0 | 0 |
| Tags `approval_global_partial` | présents | 6 |
| Jalons couches individuels | 1 agrégat | **6** |
| Sujets cadrage individuels | 0 (réf. ClickUp seule) | **7** |

## Améliorations 0.1.2 (vs 061941)

1. **Métadonnées** : `intention` + `position` sur chaque entrée ; dimensions distinctes de `validation`.
2. **Actionnable** : 6 couches roadmap et 7 sujets de cadrage capturés **individuellement** (`intention: milestone`).
3. **ClickUp structure** : traitée en **observation** (CAP-043), pas en convention explicitement approuvée (061941 CAP-039) — plus fidèle à la source.
4. **Approbations partielles** : endossements « bonne base » / « servir de base » / « d'accord globalement » taggés `approval_global_partial` sans forcer `item`/`set`.
5. **Relations** : `answers`/`answered_by`, `resolves` (MàJ modules), `evolves_from`/`evolves_to` (operating-model, onboarding).
6. **Ambiguïtés** : tags `ambiguous-b-or-c`, `ambiguous-validation-scope`, `ambiguity-silence`.

## Régressions / manques vs 061941

| Thème présent en 061941 | CAP réf. | Statut 180454 |
| --- | --- | --- |
| Taxonomie éléments Core/Module/Instance/Agent/Skill/Rule/Template/Workflow | CAP-028 | **Manquant** (partiellement absorbé dans CAP-026/027) |
| Mapping espaces logiques ↔ local ↔ ClickUp | CAP-042 | **Manquant** comme entrée autonome |
| Liste docs initiale (vision, architecture, operating-model, onboarding…) | CAP-054 | **Partiel** — évolutions op/onboarding + socle, pas la liste initiale isolée |
| Consultation ClickUp (Inbox vide, docs vides) | CAP-066 | **Manquant** (réfs Cadrage/Roadmap seulement) |

## Grille de traçabilité (messages / thèmes → CAP)

Colonnes : zone source → info pertinente → CAP(s) → statut → manque / remarque.

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| Brief user (début) | Intention SB multi-chatbots, suivi, agents | CAP-001 | Couvert | — |
| Brief | Brain/ vs Brain-main/ | CAP-002 | Couvert | — |
| Brief | SoT locale JSONL/SQL ; ClickUp prioritaire | CAP-003 | Couvert | — |
| Brief | Douleur idées perdues / contextes saturés | CAP-004 | Couvert | — |
| Brief | ClickUp Organisation + Projets | CAP-005 | Couvert | — |
| Brief | Périmètre transverse (MC, Rust, AE…) | CAP-006 | Couvert | — |
| Brief | UX ~10–15 commandes max | CAP-007 | Couvert | `position=confirmed` + explicit : REVIEW |
| Q1 rôle A/B/C | Question assistant | CAP-008 | Couvert | — |
| **A. Autonomie B/C** | Réponse B ou C ; valider cadrage pas chaque test | CAP-009 | Couvert | Ambigu B vs C tagué ; non tranché |
| Q2 ClickUp | Question miroir vs sync | CAP-010 | Couvert | — |
| Réponse ClickUp | Local SoT ; ClickUp visualiseur sync | CAP-011 | Couvert | — |
| Q3 standardisation | Socle universel + modules | CAP-012 | Couvert | — |
| Hypothèse fonctionnement | Séparer exploratoire / officiel | CAP-013 | Couvert | Convention proposée, pas explicit |
| Quatre espaces | Atelier / Réf / Journal / Pilotage | CAP-014 | Couvert | `endorsed` + `approval_global_partial` |
| Modes de capture | Passive / session / combo | CAP-015 | Couvert | Lié à CAP-046 |
| Pipeline Sources→… | Chaîne de traitement | CAP-016 | Couvert | Partial endorsement |
| Commandes brain * | Liste non définitive | CAP-017 | Couvert | Non héritier d’approbation |
| Contrat commun | Champs par entrée | CAP-018 | Couvert | Partial |
| Capture sélective | Auto + consolidation | CAP-019 | Couvert | — |
| Entrée référentiel | Proposition + accord ; conflits | CAP-020 | Couvert | — |
| Agents spécialisés | Maîtrise conventions | CAP-021 | Couvert | Orchestrateur vs file non tranché |
| Taxonomie Obs/Prop/Déc/Conv | Quatre notions | CAP-022 | Couvert | — |
| Conflits multi-solutions | Oui | CAP-023 | Couvert | — |
| Historique décisions | Conserver remplacées | CAP-024 | Couvert | — |
| Conventions 3 niveaux + mods | Oui | CAP-025 | Couvert | — |
| Archi Core/Modules/Instance | Suggestion | CAP-026 | Couvert | Partial « servir de base » |
| Modules extensions | Pas systèmes parallèles | CAP-027 | Couvert | Partial |
| Taxonomie éléments (Agent/Skill…) | Liste détaillée | — | **Manque** | Présent en 061941 CAP-028 |
| Onboarding progressif | « effectivement… » | CAP-028 | Couvert | Item explicit |
| Onboarding silence | Q/R ; silence ≠ validation auto | CAP-029 | Couvert | Tag ambiguity-silence |
| Activation modules | IA et/ou manuel | CAP-030 | Couvert | — |
| MàJ modules | Reco puis décision auto brain-main | CAP-031→032 | Couvert | `resolves` |
| Démarrage phrase / 500 mots | Non bloquant | CAP-033 | Couvert | — |
| brain init fréquence | Q user + réponse assistant | CAP-034→035 | Couvert | Pas décision user |
| Verdict GO cadrage | Pas créer dossiers encore | CAP-036 | Couvert | — |
| **C. 6 couches roadmap** | Core…Automatisation | CAP-037…042 | Couvert | Individuels (vs agrégat 061941) |
| **D. ClickUp docs/Inbox/Cadrage/Roadmap** | Structure projet | CAP-043 | Couvert | **Observation** (pas convention explicit) |
| Capture/Review convention | Capture→registres ; Review→docs | CAP-044 | Couvert | — |
| Formalisation workflow | Capturer / Review formalisés | CAP-045 | Couvert | « d'accord globalement » = partial |
| Capture après chaque message | Décision auto | CAP-046 | Couvert | related CAP-015/019 |
| **E. Review / « valide certaines choses »** | Consolider, dédup, portée ambiguë | CAP-047 | Couvert | Tag ambiguous-validation-scope |
| Entretien mémoire | Éviter explosion | CAP-048 | Couvert | — |
| Inbox ClickUp | Notes externes ; pas miroir local | CAP-049 | Couvert | — |
| **F. Sous-tâches Roadmap** | Idées validées sans docs/code | CAP-050 | Couvert | Suggestion (« on pourrait ») |
| **G. 7 sujets cadrage** | 7 thèmes individuels | CAP-051…057 | Couvert | Individuels |
| Réfs ClickUp Cadrage/Roadmap | Ne pas recréer | CAP-058…059 | Couvert | — |
| Peuplement manuel + consigne | Ne rien écrire ClickUp | CAP-060 | Couvert | — |
| Mapping espaces↔ClickUp | Tableau de mapping | — | **Manque** | 061941 CAP-042 |
| operating-model évolue | Créer → répartir | CAP-061→062 | Couvert | evolves_* |
| onboarding.md évolue | Créer → chapitre workflow | CAP-063→064 | Couvert | evolves_* |
| Liste docs initiale complète | Première liste assistant | — | **Partiel** | Absorbe dans CAP-065 |
| Socle documentaire candidat | vision, project, architecture… | CAP-065 | Couvert | Non définitif |
| vision.md 100% | Validé | CAP-066 | Couvert | — |
| Docs : accumuler puis standardiser | Orientation ouverte | CAP-067 | Couvert | — |
| Pas d’écrasement docs | Proposer adaptations | CAP-068 | Couvert | — |
| AGENTS.md | Point d’entrée IA | CAP-069 | Couvert | — |
| Deux phases docs | Accumulation / standardisation | CAP-070 | Couvert | — |
| Tâche standardiser docs | Potential | CAP-071 | Couvert | — |
| Capture/Orga/Validation | Trois niveaux | CAP-072 | Couvert | proposed, pas explicit |
| Registres / docs / ClickUp | Rôles | CAP-073 | Couvert | — |
| Documenter dès le flux | Ne pas attendre cadrage fini | CAP-074 | Couvert | — |
| Adaptateurs multi-IA | Contrat + adaptateurs | CAP-075 | Couvert | — |
| Périmètre modèle docs | Question ouverte | CAP-076 | Couvert | — |
| Consultation ClickUp Inbox/docs | Inbox vide, docs vides | — | **Manque** | 061941 CAP-066 |
| **H. Bruit méta-test** | Exercice simulation SB | CAP-077 | Couvert | tag test-noise ; REVIEW |
| **B. Portées d’approbation** | Citation ≠ set ; partial ≠ item | tags + CAP-014/016/018/026/027/045 | Couvert | Aucun `set` (correct : pas d’ensemble identifiable approuvé) |

## Couverture scénarios A–H

| Scénario | Verdict |
| --- | --- |
| A Autonomie B/C | OK — CAP-009 + tag ambiguïté |
| B Portées d’approbation | OK — partial tags ; 0× `set` ; citations non converties |
| C 6 couches | OK — CAP-037…042 |
| D ClickUp convention vs observation | OK — CAP-043 observation |
| E Review ambigu | OK — CAP-047 |
| F Sous-tâches Roadmap | OK — CAP-050 suggestion |
| G 7 cadrage individuels | OK — CAP-051…057 |
| H Bruit de test | OK — CAP-077 exclu métier via tags |

## Verdict

Capture 0.1.2 **plus fidèle** sur granularité actionable (jalons/cadrage), sémantique d’approbation et métadonnées intention/position. Quelques infos satellites de 061941 manquent (taxonomie éléments, mapping espaces, consultation Inbox). Qualité > quantité : +8 entrées justifiées surtout par la décomposition individuelle.
