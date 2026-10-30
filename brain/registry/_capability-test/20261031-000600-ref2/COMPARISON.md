# COMPARISON — 20261031-000600-ref2

| | |
| --- | --- |
| Type de test | **Corpus indépendant** (source 2) — test de capacité 0.1.3 |
| vs réf. | — (pas de smoke source 3 ; pas Test A) |
| Source | `brain/sources/conversation-reference-2.txt` |
| Run | `brain/registry/_capability-test/20261031-000600-ref2/` |

## Grille de traçabilité

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| L1–3 demande stratégique | Implémentation 1.1 + questions route/bloqueurs/impact | CAP-001, CAP-002 | OK | |
| L5–37 concept & archi | Concept solide ; Brain-main/brain/ClickUp ; problématique intentions | CAP-003–005 | OK | |
| L43–184 six risques | Dette mémoire, déformation IA, orchestration, maintenance, contrainte, outils | CAP-006–017 | OK | |
| L186–266 transformation | Ordre de construction, classique vs SB, tableau activités, coût démarrage | CAP-018–020, CAP-104 | OK | |
| L268–343 étapes & stratégie | 5 étapes, indicateurs, cycle complet, 4 capacités, question design | CAP-021–029 | OK | |
| L349–661 audit 045232 | Verdict, tech/sémantique, anti-patterns, couverture, validateur, axes | CAP-030–042 | OK | Contenu méta-audit conservé (matière projet SB) |
| L665–943 audit 061941 | Re-capture, progrès, P1–P3, manques ops, artefacts test, V0.1.2 | CAP-043–054 | OK | |
| L949–1048 réponses user | Autonomie B/C, multi-info, agents, fenêtres, partial, SoT, clickup.md, bruit, conception | CAP-055–075 | OK | |
| L1053–1467 conception | Capture/Review, intentions/positions, fenêtres, roadmap levels, registres, options A–D, Q1–3 | CAP-076–092, CAP-119 | OK | |
| L1470–1706 décisions | Attribution, archive+index, intention unique, Sync, option D, immutabilité | CAP-093–103 | OK | |
| Roadmap 6 couches (dans audits) | Core…Automatisation individuelles | CAP-106–111 | OK | Ancrage via citations d’audit (source_contextual) |
| 7 sujets cadrage (dans audits) | 7 pistes individuelles | CAP-112–118 | OK | Idem |
| Détails Inbox / brief 500 / fusion doublons | Liste agrégée dans audit | CAP-052 | Partiel | Pas de CAP unitaires pour chaque micro-règle |

## Notes

- Production non touchée.
- Pas de comparaison CAP-à-CAP avec d’autres runs (interdiction explicite du protocole inter-sources ; run isolé `_capability-test`).
- Validateur : OK bloquant sous `--require-intention` (WARN réciproques relations non bloquants).
