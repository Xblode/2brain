# COMPARISON — 20261031-000600-ref3

| | |
| --- | --- |
| Type de test | **Smoke régression source 3** — **pas** Test A (généralisation) |
| Source | `brain/sources/conversation-reference-3.txt` (2296 lignes) |
| Run | `20261031-000600-ref3` |
| Réf. comparative | — (smoke capacité 0.1.3 sur corpus qui a conçu 0.1.3 ; pas de baseline CAP-à-CAP) |
| Qualificatif | Régression ciblée des règles 0.1.3 (atomicité, grounding, locators, audit, relations, anti-faux-explicit). **Ne prouve pas** la généralisation. |

## Grille de traçabilité

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| L1–4 User | Prêt 0.1.2 + prompt Cursor + sample 2 | CAP-001…003 | Conservée | — |
| L6–683 Assistant prompt | Philosophie, fenêtres, passes, intentions, validations, samples, A–H | CAP-004…032 | Conservée | Sous-détails prompt non atomisés un-par-un |
| L688–821 Plan Cursor collé | Extension 0.1.1 / schema intention | CAP-033, CAP-034 | Conservée | Auteur plan = Cursor via collage user |
| L825–972 Ajustements | 5 ajustements + feu vert | CAP-035…044 | Conservée | — |
| L976–1220 Audit 180454 | _gen.py, false explicit, locators, vide, priorités | CAP-045…055 | Conservée | Chiffres exacts du run = bruit de test (exclus) |
| L1225–1481 Audit 184105 | Méthode OK, CAP-009/049, confiance, pas 0.1.3 encore | CAP-056…064 | Conservée | Tension avec décision ultérieure 0.1.3 |
| L1486–1791 Audit 194948 | Sample2, CAP-031/022/028, validate.json, verdict | CAP-065…074 | Conservée | Dimensions tableau CAP-011 sample2 = hors source3 métier |
| L1795–1822 User feedback | Atomicité, Review, signatures, Cross-test | CAP-075…083,112 | Conservée | — |
| L1827–2067 Assistant | Graphe, atomicité, audit, Cross-test, 5 questions | CAP-084…092 | Conservée | — |
| L2073–2099 User | Valide hiérarchie/graphe, impose 0.1.3, Q1–Q5 | CAP-093…096 | Conservée | — |
| L2105–2296 Brief 0.1.3 | Capture≠Review, 6 axes, Test A/B, freeze | CAP-097…111 | Conservée | — |

## Synthèse quantitative (ce run)

| Indicateur | Valeur |
| --- | --- |
| Captures | 112 |
| Relations (arcs) | 152 |
| explicit_user_approval | 12 |
| validation none | 100 |
| approval_scope set | 1 (CAP-096) |
| position null | 6 |
| Intention convention | 30 |
| Intention requirement | 15 |
| Intention observation | 15 |
| Intention task | 10 |
| Intention feedback | 8 |
| Intention suggestion | 8 |
| Intention decision | 7 |
| Intention orientation | 7 |
| Intention milestone | 5 |
| Intention preference | 3 |
| Intention question | 3 |
| Intention risk | 1 |
| Grounding source_explicit | 108 |
| Grounding source_contextual | 4 |
| Grounding interpreted / uncertain | 0 / 0 |

## Points de régression 0.1.3 exercés

| Règle 0.1.3 | Exercée ? | Preuve |
| --- | --- | --- |
| `intention` + `position` + `grounding` + `author_confidence` | Oui | 112/112 |
| `run_id` / `capture_ref` | Oui | `20261031-000600-ref3:CAP-NNN` |
| `origin.locators[]` non vides | Oui | lines (+ window tags) |
| Atomicité / lier plutôt que fusionner | Oui | CAP-068…077, CAP-101 |
| Anti-faux-explicit | Oui | CAP-049/058/068 en none ; partials tagués |
| `contradicts` étayé | Oui | CAP-095 ↔ CAP-063 |
| Audit final + artefacts | Oui | AUDIT.md + validate.json |
| Bruit vs métier | Oui | stats runs exclus ; CAP-072 bruit tagué conceptuellement |

## Limites assumées

- Source sans labels User/Assistant → attribution structurale (`author_confidence` high sur tours clairs, medium sur collages).
- Smoke source 3 ≠ Test A.
- Pas de comparaison CAP-à-CAP avec d’autres runs (interdit / non pertinent).
