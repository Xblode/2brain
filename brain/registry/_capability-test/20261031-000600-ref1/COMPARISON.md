# COMPARISON — 20261031-000600-ref1

| | |
| --- | --- |
| Type de test | Corpus (source 1 — conception initiale SB) |
| vs réf. | — (premier run capability-test isolé sur ref1) |
| Source | `brain/sources/conversation-reference-1.txt` (~1452 lignes) |
| Registre | `brain/registry/_capability-test/20261031-000600-ref1/entries.jsonl` |

Grille de traçabilité source → captures (couverture > volume).

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| L1–2 Brief vision | Second cerveau multi-chatbots, suivi, validation | CAP-001 | OK | — |
| L3 Outils IA | Skills, MCP, Rules, Agents | CAP-002 | OK | — |
| L4–11 Brain / Brain-main | Deux dossiers + rôles | CAP-003…006 | OK | — |
| L5 Tiers | ClickUp, Notion, GitHub, Drive | CAP-004 | OK | Notion/Drive non détaillés ensuite (normal) |
| L15–17 Douleur workflow | Désordre, vibecode, perte d'idées | CAP-007 | OK | — |
| L19–24 Local JSONL + cohérence | SoT légère + anti-surcharge + conventions projets | CAP-008, CAP-009, CAP-013 | OK | Naming/workflow web évoqué fusionné dans CAP-013/009 |
| L26–39 ClickUp préféré + 2 espaces | Asana→ClickUp ; Organisation/Projets | CAP-010, CAP-011 | OK | — |
| L30–41 Demande 3Q + Go | Méthode avant build | CAP-014, CAP-015 | OK | — |
| L55–82 Questions A/B/C | Rôle / ClickUp / standardisation | CAP-016…018 | OK | — |
| L94–107 Réponses user | B\|C ; local+ClickUp ; socle+modules | CAP-019…021 | OK | Ambiguité B\|C préservée |
| L122–184 Exploratoire + 4 espaces | Principe + Atelier/Réf/Journal/Pilotage | CAP-022…024 | OK | — |
| L188–216 Capture modes | Passive/session/combo + 10–15 cmd | CAP-025, CAP-026 | OK | — |
| L223–295 Pipeline + commandes + contrat | Chaîne, 3 couches, table cmd, métadonnées | CAP-027…031 | OK | Liste cmd non atomisée commande par commande (volontaire) |
| L301–332 3Q + réponses | Capture / validation / agents | CAP-032…037 | OK | Contradiction validation signalée |
| L337–430 Conflits + OPDC + oui×3 | CardCarousel, 5+1 cas, historique, mods | CAP-038…046 | OK | — |
| L434–565 Archi 3 niveaux + Q modules | Core/Modules/Instance, onboarding Q | CAP-047…052 | OK | — |
| L572–594 Onboarding user + answers | Progressif, init ?, updates, 500 mots, franc | CAP-053…058 | OK | — |
| L598–726 Bilan GO | Principes, init≠onboarding, 6 sujets, couches, GO | CAP-059…065 | OK | GO = proposition assistant (pas explicit user) |
| L730–1094 Exemple pratique | Bases retenues, couches=jalons, arbo ClickUp | CAP-066…074 | OK | — |
| L1098–1258 Simulation review | Mapping espaces, capture/review, docs, 7+6, 3 niveaux | CAP-075…083, CAP-103…115 | OK | Docs proposés plus tard contestés |
| L1264–1287 Précisions user | Capture auto/msg, Inbox, ClickUp validé, vision 100 %, doutes docs | CAP-084…092 | OK | — |
| L1290–1451 Synthèse assistant | Entretien mémoire, socle docs, AGENTS.md, règles CU, risque skill | CAP-093…102 | OK | — |
| L84–86 / L114 Atelier | Mode atelier + confirmation | CAP-116, CAP-117 | OK | — |

## Fidélité / anti-faux-explicit

| Cas source | Traitement capture |
| --- | --- |
| « B ou C » | CAP-019 `orientation` + `ambiguous` + `none` |
| « bonne base de travail » | CAP-066…068 `endorsed` + `approval_global_partial` + `none` |
| « d'accord globalement » | CAP-088 partial + `none` |
| « vision.md validé à 100% » | CAP-089 `explicit` + `item` |
| « éléments validée » ClickUp cadrage | CAP-087 `explicit` + `set` |
| Reco assistant « auto-classer » vs user « attendre accord » | CAP-033↔036 `conflicts_with`/`contradicts` |
| Reco « updates sans auto-apply » vs user auto Brain-main | CAP-052↔056 `conflicts_with` |

## Hors scope volontaire

- Détails stylistiques / formules de politesse.
- Reformulations redondantes assistant déjà couvertes par CAP parent.
- Instructions de test / méta-génération (absentes de cette source).
