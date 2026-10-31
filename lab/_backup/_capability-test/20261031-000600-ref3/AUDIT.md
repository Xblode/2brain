# AUDIT — capture 20261031-000600-ref3

| | |
| --- | --- |
| Source | `brain/sources/conversation-reference-3.txt` |
| Run | `brain/registry/_capability-test/20261031-000600-ref3/` |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |

## Couverture source↔registre

| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |
| Demande prompt 0.1.2 + sample 2 | OK | CAP-001 → CAP-003 |
| Philosophie / périmètre Capture | OK | CAP-004 → CAP-006 |
| Fenêtres / mémoire / 4 passes | OK | CAP-007 → CAP-009, CAP-037 |
| Couverture + sujets individuels | OK | CAP-010, CAP-011, CAP-025, CAP-041 |
| Intention / position / validation | OK | CAP-012 → CAP-014, CAP-038 |
| Atomicité multi-infos | OK | CAP-015, CAP-069, CAP-070, CAP-077, CAP-087, CAP-101 |
| Autonomie / richesse contenu | OK | CAP-016, CAP-078, CAP-088, CAP-102 |
| Attribution / citations / signatures | OK | CAP-017, CAP-018, CAP-071, CAP-079, CAP-080, CAP-089, CAP-105 |
| Approbations partielles / set | OK | CAP-019, CAP-039, CAP-059 |
| Métier vs bruit de test | OK | CAP-020, CAP-072 |
| Relations | OK | CAP-021, CAP-104 |
| Actionable / ClickUp / Review | OK | CAP-022 |
| Registres futurs vs 0.1.2 | OK | CAP-023, CAP-024, CAP-034 |
| Protocoles samples 1/2 + COMPARISON | OK | CAP-026 → CAP-029, CAP-042, CAP-081, CAP-082, CAP-090 |
| Scénarios A–H / qualité / livrables | OK | CAP-029 → CAP-032 |
| Plan Cursor + 5 ajustements + feu vert | OK | CAP-033 → CAP-044 |
| Audit run 180454 (_gen.py, false explicit, vide) | OK | CAP-045 → CAP-055 |
| Audit run 184105 (méthode, CAP-009/049) | OK | CAP-056 → CAP-064 |
| Audit run 194948 (CAP-031, split, validate.json) | OK | CAP-065 → CAP-074 |
| Feedback user architecture / prochain test | OK | CAP-075 → CAP-083, CAP-112 |
| Réponse architecture Review + graphe | OK | CAP-084 → CAP-092 |
| Validations user + réponses Q1–Q5 | OK | CAP-093 → CAP-096 |
| Brief 0.1.3 (6 axes, Test A/B, freeze) | OK | CAP-097 → CAP-111 |
| Détail interne audits (tables chiffres runs) | Exclu motivé | Stats run-spécifiques = observation de test ; essence méthodologique capturée |
| Collage intégral prompt Cursor (sections 1–20) | Partiel | Règles structurantes capturées ; pas une CAP par sous-paragraphe du prompt |

## Atomicité et richesse

- Splits effectués : convention vs emplacement (thème CAP-031 via CAP-068/075) ; CAP-022/028 → principes séparés (CAP-069/070/077) ; axes 0.1.3 individuels (CAP-101–106) ; Test A vs B (CAP-107/108).
- CAP courtes liées / enrichies : CAP-044 liée à CAP-043 ; CAP-112 liée à CAP-078/088 ; parent CAP-100 ↔ enfants axes.
- Incomplet signalé : attributions sans labels (CAP-071/079) ; grounding majoritairement `source_explicit`, 4 `source_contextual` (plans collés / reformulations).

## Provenance

- Locators manquants corrigés : oui (tous les CAP ont `origin.locators[]` non vides)
- Multi-passages : oui (ex. CAP-033 plan collé ; CAP-096 réponses Q1–Q5 ; fenêtres taguées W1–W4)

## Grounding et approbation

- Anti-faux-explicit vérifié : orientations / suggestions assistant en `none` ; partials tagués `approval_global_partial` sans forcer `set` hors CAP-096 (réponses Q1–Q5 délimitées).
- Ambiguës en `none` : CAP-049, CAP-058, CAP-063, CAP-068 (+ tags `ambiguous` où pertinent).

## Contradictions / tensions

- `contradicts` / `conflicts_with` posés : CAP-095 (`decision` faire 0.1.3) **contradicts** CAP-063 (ne pas lancer refonte 0.1.3) + réciproque `contradicted_by`.

## Corrections avant clôture

- Remap des `type` hors enum 0.1.1 (`requirement`/`risk`/`feedback`/…) → types valides en conservant `intention`.
- CAP-077 → `convention` ; CAP-094 → `decision` ; CAP-105 → space `atelier`.
- Ajout des relations réciproques recommandées (clarifies/answers/evolves/parent/contradicts).
- Re-validation `--require-intention` + régénération `validate.json`.
