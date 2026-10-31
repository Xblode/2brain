# AUDIT — capture production

| | |
| --- | --- |
| Source | `lab/sources/conversation-reference-1.txt` |
| Cible | `brain/registry/entries.jsonl` |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |

## Couverture source↔registre

| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |
| Vision SB + problème workflow | OK | CAP-001, CAP-007, CAP-009 |
| Stack IA / UX / démarrage générique | OK | CAP-002, CAP-012, CAP-013 |
| Brain/ vs Brain-main/ | OK | CAP-003…006, CAP-047 |
| Interfaces humaines / ClickUp existant | OK | CAP-004, CAP-010, CAP-011, CAP-071 |
| SoT locale JSONL/SQL | OK | CAP-008, CAP-020, CAP-026 |
| 3 questions atelier + réponses B\|C / local / socle | OK | CAP-014…021 ; ambiguïté B ou C conservée (CAP-019) |
| Exploratoire vs référentiel + 4 espaces | OK | CAP-022…024, CAP-066, CAP-076 |
| Capture modes → combo → auto post-message | OK | CAP-025, CAP-026, CAP-035, CAP-084, CAP-093 |
| Pipeline + 3 couches registre + commandes | OK | CAP-027…031, CAP-066 |
| Validation : tension reco assistant vs user | OK | CAP-033 ↔ CAP-036 (`conflicts_with` / `contradicts`) |
| Agents / orchestration | OK | CAP-034, CAP-037 |
| Conflits Card / CardCarousel / OPDC | OK | CAP-038…040, CAP-044…046 |
| Core / Modules / Instance + mods | OK | CAP-046…050, CAP-067 |
| Onboarding / brain init ≠ continu | OK | CAP-051…054, CAP-061, CAP-062 |
| Updates modules auto vs non-auto | OK | CAP-052 ↔ CAP-056 (`conflicts_with`) |
| GO cadrage + 7 sujets + 6 jalons | OK | CAP-059…065, CAP-079, CAP-080, CAP-103…115 |
| Exemple pratique user + ClickUp arbo | OK | CAP-066…074, CAP-087 |
| Capture/Review formalisés + simulation | OK | CAP-074…083 |
| Docs standard / doutes operating-model | OK | CAP-078, CAP-089…099 ; tension CAP-090↔078/097 |
| Inbox externe / roadmap hiérarchique | OK | CAP-085, CAP-086, CAP-100 |
| Risque skill ≠ écriture auto | OK | CAP-101 |
| Mode atelier | OK | CAP-116, CAP-117 |
| Bruit méta / instructions de test | Exclu | Aucune CAP métier sur instructions de génération |

## Atomicité et richesse

- Splits effectués : 7 sujets de cadrage individuels (CAP-103…109) ; 6 jalons individuels (CAP-110…115) ; Brain/ et Brain-main/ séparés ; questions atelier séparées des réponses ; CardCarousel distinct dans CAP-036/038.
- CAP courtes liées / enrichies : jalons et sujets cadrage liés via `child_of`/`parent_of` à CAP-079/080.
- Incomplet signalé : brief 500 mots non bloquant (CAP-057) ; brain init fréquence d'abord incertaine (CAP-054) puis réponse assistant (CAP-061).

## Provenance et refs

- Locators : oui (tous présents)
- URLs/refs conservées : oui — URL ClickUp exacte dans CAP-087 `content` + `refs[]` ; refs docs (`vision.md`, `operating-model.md`, …), Card/CardCarousel, Brain/, Brain-main/
- Multi-passages : oui — ex. CAP-019, CAP-036, CAP-066…068, CAP-071

## Grounding, mapping, space, approbation

- intention→type OK : oui (mapping 0.1.4, validateur `--require-intention`)
- Anti-faux-explicit : oui — orientations B\|C, « bonne base », « d'accord globalement », `selected` restent `validation: none` + tags `approval_global_partial` / `ambiguous` quand pertinent
- Space (atelier par défaut) : oui — suggestions/orientations/questions non établies en `atelier` ; `referentiel` réservé brief user établi (CAP-002/003/005/006) + décisions explicit (CAP-044…046, CAP-089)

## Contradictions / tensions

- Relations posées : CAP-033↔036 (auto-classer vs attendre accord) ; CAP-052↔056 (updates proposées vs auto Brain-main) ; CAP-023↔086 (Inbox logique vs pas d'inbox locale) ; CAP-078↔090 / CAP-097 (docs proposés vs doutes user)

## Corrections avant clôture

- Remap intention→type (18 écarts hérités corrigés)
- Spaces : propositions/orientations sorties de `referentiel` abusif → `atelier`
- CAP-087 : remplacement « lien fourni » par URL exacte + `refs[]`
- Réciproques relations prioritaires + `parent_of` cadrage/roadmap
- `author_confidence` → `medium` (format `conversation-reference-*.txt` sans labels UI)
- Métadonnées production : `run_id`, `capture_ref`, `storage`, `origin.source`, `created_at`
- Re-validation `--require-intention` après corrections → OK bloquant
