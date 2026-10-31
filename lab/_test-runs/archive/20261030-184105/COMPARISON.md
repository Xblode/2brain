# Comparaison — capture skill-direct 0.1.2 vs référence 0.1.1

| | |
| --- | --- |
| Nouvelle capture | `brain/registry/_test-runs/20261030-184105/` |
| Référence sémantique | `brain/registry/_test-runs/20261030-061941/` |
| Source | `brain/sources/conversation-reference-1.txt` uniquement |
| Échantillon 2 | non utilisé |
| Méthode | **Skill direct** (fenêtres + 4 passes) — aucun script de génération |
| Validateur 184105 | OK bloquant avec `--require-intention` |
| Production | non modifiée |

## Synthèse chiffrée

| Indicateur | 061941 (réf.) | 184105 (skill direct) |
| --- | ---: | ---: |
| Entrées | 69 | 80 |
| `intention` renseignée | 0 | 80 |
| `position` = `null` | n/a | 10 |
| `explicit_user_approval` | 23 | 22 |
| `approval_scope: set` | 0 | 0 |
| Tags `approval_global_partial` | présents | 7 |
| Jalons couches individuels | 1 agrégat | **6** |
| Sujets cadrage individuels | 0 (réf. ClickUp seule) | **7** |

## Améliorations vs 061941

1. Métadonnées `intention` / `position` sur chaque entrée.
2. 6 couches + 7 cadrages **individuels**.
3. ClickUp arbo = **observation** (CAP-044), pas convention explicit sur-approuvée.
4. Endossements partiels taggés sans forcer `item`/`set`.
5. Relations `answers`/`answered_by`, `resolves`, `evolves_*`.
6. Couverture des manques fréquents : taxonomie éléments (CAP-028), mapping espaces (CAP-046), consultation ClickUp (CAP-063).

## Grille de traçabilité

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| Brief | Intention SB multi-chatbots | CAP-001 | Couvert | — |
| Brief | Brain/ vs Brain-main/ | CAP-002 | Couvert | — |
| Brief | SoT locale + ClickUp prioritaire | CAP-003 | Couvert | preference ; validation none |
| Brief | Douleur idées perdues | CAP-004 | Couvert | — |
| Brief | ClickUp Organisation/Projets | CAP-005 | Couvert | — |
| Brief | Périmètre transverse | CAP-006 | Couvert | — |
| Brief | UX ~10–15 commandes | CAP-007 | Couvert | REVIEW position+explicit |
| Q1 rôle A/B/C | Question | CAP-008 | Couvert | — |
| **A. Autonomie B/C** | B ou C ; valider cadrage | CAP-009 | Couvert | tag ambiguous-b-or-c |
| Q2 ClickUp | Miroir vs sync | CAP-010→011 | Couvert | — |
| Q3 standardisation | Socle + modules | CAP-012 | Couvert | — |
| Exploratoire / officiel | Principe | CAP-013 | Couvert | proposed, pas explicit |
| Quatre espaces | Suggestion | CAP-014 | Couvert | endorsed + partial |
| Modes capture | Passive/session | CAP-015 | Couvert | related CAP-048 |
| Pipeline | Sources→… | CAP-016 | Couvert | partial |
| Commandes brain * | Liste non définitive | CAP-017 | Couvert | — |
| Contrat commun | Champs entrée | CAP-018 | Couvert | partial |
| Capture sélective | Décision | CAP-019 | Couvert | — |
| Entrée référentiel | Proposition + conflits | CAP-020 | Couvert | — |
| Agents spécialisés | Décision | CAP-021 | Couvert | orchestrateur non tranché |
| Taxonomie Obs/Prop/Déc/Conv | Convention proposée | CAP-022 | Couvert | — |
| Conflits multi-solutions | Oui | CAP-023 | Couvert | — |
| Historique décisions | Oui | CAP-024 | Couvert | — |
| Conventions 3 niveaux + mods | Oui | CAP-025 | Couvert | — |
| Core/Modules/Instance | Suggestion | CAP-026 | Couvert | partial |
| Modules extensions | Convention | CAP-027 | Couvert | partial |
| Taxonomie éléments Agent/Skill… | Table | CAP-028 | Couvert | manquait souvent |
| Onboarding progressif | « effectivement… » | CAP-029 | Couvert | item explicit |
| Silence ≠ validation auto | Convention | CAP-030 | Couvert | ambiguity-silence |
| Activation / MàJ modules | Décisions | CAP-031…033 | Couvert | resolves CAP-032 |
| Phrase / 500 mots | Décision | CAP-034 | Couvert | — |
| brain init fréquence | Q + proposition | CAP-035→036 | Couvert | pas décision user |
| Verdict GO | Observation | CAP-037 | Couvert | — |
| **C. 6 couches roadmap** | Individuels | CAP-038…043 | Couvert | — |
| **D. ClickUp docs/Inbox/Cadrage/Roadmap** | Observation | CAP-044 | Couvert | pas convention explicit |
| Capture/Review convention | User | CAP-045 | Couvert | — |
| Mapping espaces↔ClickUp | Suggestion | CAP-046 | Couvert | manquait souvent |
| Formalisation workflow | Partial | CAP-047 | Couvert | « d'accord globalement » |
| Capture après chaque message | Décision | CAP-048 | Couvert | — |
| **E. Review ambigu** | Orientation | CAP-049 | Couvert | ambiguous-validation-scope |
| Entretien mémoire | Convention | CAP-050 | Couvert | — |
| Inbox ClickUp | Convention | CAP-051 | Couvert | — |
| **F. Sous-tâches Roadmap** | Suggestion | CAP-052 | Couvert | « on pourrait » |
| **G. 7 sujets cadrage** | Individuels | CAP-053…059 | Couvert | — |
| Réfs ClickUp | Ne pas recréer | CAP-060…061 | Couvert | — |
| Peuplement manuel | Event | CAP-062 | Couvert | — |
| Consultation Inbox/docs | Observation | CAP-063 | Couvert | manquait souvent |
| operating-model évolue | evolves | CAP-064→065 | Couvert | — |
| onboarding.md évolue | evolves | CAP-066→067 | Couvert | — |
| Socle documentaire | Suggestion | CAP-068 | Couvert | — |
| vision.md 100% | Décision | CAP-069 | Couvert | — |
| Docs : accumuler puis standardiser | Q | CAP-070 | Couvert | — |
| Pas d'écrasement docs | Convention | CAP-071 | Couvert | — |
| AGENTS.md | Suggestion | CAP-072 | Couvert | — |
| Deux phases docs | Suggestion | CAP-073 | Couvert | — |
| Tâche standardiser docs | Potential | CAP-074 | Couvert | — |
| Capture/Orga/Validation | Convention proposée | CAP-075 | Couvert | — |
| Registres/docs/ClickUp | Convention proposée | CAP-076 | Couvert | — |
| Documenter dès le flux | Convention proposée | CAP-077 | Couvert | — |
| Adaptateurs multi-IA | Task | CAP-078 | Couvert | — |
| Périmètre modèle docs | Question | CAP-079 | Couvert | — |
| **H. Bruit méta-test** | Exercice | CAP-080 | Couvert | test-noise |
| **B. Portées d'approbation** | Citation ≠ set | tags partial | Couvert | 0× set |

## Scénarios A–H

| Scénario | Verdict |
| --- | --- |
| A Autonomie B/C | OK — CAP-009 |
| B Portées d'approbation | OK — 7 partial ; 0 set |
| C 6 couches | OK — CAP-038…043 |
| D ClickUp obs vs convention | OK — CAP-044 |
| E Review ambigu | OK — CAP-049 |
| F Sous-tâches Roadmap | OK — CAP-052 |
| G 7 cadrage | OK — CAP-053…059 |
| H Bruit de test | OK — CAP-080 |

## Verdict

Capture skill-direct **conforme** au protocole 0.1.2, plus complète que 061941 sur granularité actionable et sémantique d'approbation, sans script de génération.
