# AUDIT — capture 20261031-000600-ref1

| | |
| --- | --- |
| Source | `brain/sources/conversation-reference-1.txt` |
| Run | `brain/registry/_capability-test/20261031-000600-ref1/` |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |

## Couverture source↔registre

| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |
| Vision SB + problème workflow | OK | CAP-001, CAP-007, CAP-009 |
| Stack IA / UX / démarrage générique | OK | CAP-002, CAP-012, CAP-013 |
| Brain/ vs Brain-main/ | OK | CAP-003…006, CAP-047 |
| Interfaces humaines / ClickUp existant | OK | CAP-004, CAP-010, CAP-011, CAP-071 |
| SoT locale JSONL/SQL | OK | CAP-008, CAP-020, CAP-026 |
| 3 questions atelier + réponses B\|C / local / socle | OK | CAP-014…021 ; ambiguïté B ou C conservée |
| Exploratoire vs référentiel + 4 espaces | OK | CAP-022…024, CAP-066, CAP-076 |
| Capture modes → combo → auto post-message | OK | CAP-025, CAP-026, CAP-035, CAP-084, CAP-093 |
| Pipeline + 3 couches registre + commandes | OK | CAP-027…031, CAP-066 |
| Validation : tension reco assistant vs user | OK | CAP-033 ↔ CAP-036 (`conflicts_with` / `contradicts`) |
| Agents / orchestration | OK | CAP-034, CAP-037 |
| Conflits Card / conventions évolutives / OPDC | OK | CAP-038…040, CAP-044…046 |
| Core / Modules / Instance + mods | OK | CAP-046…050, CAP-067 |
| Onboarding / brain init ≠ continu | OK | CAP-051…054, CAP-061, CAP-062 |
| Updates modules auto vs non-auto | OK | CAP-052 ↔ CAP-056 (`conflicts_with`) |
| GO cadrage + 6 sujets + 6 couches | OK | CAP-059…065, CAP-079, CAP-080, CAP-103…115 |
| Exemple pratique user + ClickUp arbo | OK | CAP-066…074, CAP-087 |
| Capture/Review formalisés + simulation | OK | CAP-074…083 |
| Docs standard / doutes operating-model | OK | CAP-078, CAP-089…099 ; tension CAP-090↔078 |
| Inbox externe / roadmap hiérarchique | OK | CAP-085, CAP-086, CAP-100 |
| Risque skill ≠ écriture auto | OK | CAP-101 |
| Mode atelier | OK | CAP-116, CAP-117 |
| Bruit méta / instructions de test | Exclu | Aucune CAP métier sur instructions de génération |

## Atomicité et richesse

- Splits effectués : 7 sujets de cadrage individuels (CAP-103…109) ; 6 jalons individuels (CAP-110…115) ; Brain/ et Brain-main/ séparés ; questions atelier séparées des réponses.
- CAP courtes liées / enrichies : jalons et sujets cadrage enrichis à l'audit ; liés via `child_of`/`parent_of` à CAP-079/080/071.
- Incomplet signalé : brief 500 mots non bloquant (CAP-057) ; brain init fréquence d'abord incertaine (CAP-054) puis réponse assistant (CAP-061).

## Provenance

- Locators manquants corrigés : non (tous présents dès génération)
- Multi-passages : oui — ex. CAP-019 (session+cadrage), CAP-036 (validation+Card), CAP-066…068 (citations multi-blocs), CAP-071 (arbo ClickUp)

## Grounding et approbation

- Anti-faux-explicit vérifié : oui — orientations B\|C, « bonne base », « d'accord globalement » restent `validation: none` + tags `approval_global_partial` / `ambiguous` quand pertinent.
- Ambiguës en `none` : CAP-019 (B ou C), CAP-054 (init fréquence), CAP-056 (updates — tension avec reco assistant), CAP-086 (inbox locale vs espace Atelier), CAP-090 (docs spécialisés).
- Explicit retenus (preuve textuelle) : CAP-044, CAP-045, CAP-046, CAP-071, CAP-087 (set ClickUp cadrage/brainstorm), CAP-089 (`vision.md` 100 %).

## Contradictions / tensions

- `contradicts` / `conflicts_with` posés : CAP-033↔036 (auto-classer vs attendre accord) ; CAP-052↔056 (updates proposées vs auto Brain-main) ; CAP-023↔086 (Inbox logique vs pas d'inbox locale) ; CAP-078↔090 (docs proposés vs doutes user).

## Corrections avant clôture

- Remap des `type` hors enum (`requirement`/`preference`/`feedback`/`orientation`/`risk` → enums 0.1.1).
- CAP-087 : retrait tag `approval_global_partial` (approbation set ClickUp explicite).
- CAP-054 : `answered_by` corrigé vers CAP-061 (pas CAP-065).
- Enrichissement contenus courts (jalons/cadrage/CAP-045/117).
- Réciproques ajoutées sur tensions majeures + `parent_of` cadrage/roadmap.
- Re-validation `--require-intention` après corrections → OK bloquant.
