# AUDIT — capture production (ref3)

| | |
| --- | --- |
| Source | `lab/sources/conversation-reference-3.txt` |
| Cible | `brain/registry/entries.jsonl` |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |
| run_id | `production` |
| IDs | CAP-239 → CAP-350 (112 ajoutées ; CAP-001…238 intactes) |

## Couverture source↔registre

| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |
| Demande prompt 0.1.2 + source suite | OK | CAP-239–240, 268 |
| Philosophie Capture (collecte ≠ sélection) | OK | CAP-241–242, 312, 347, 350 |
| Périmètre Skill only | OK | CAP-243 |
| Fenêtres ~5 + mémoire globale | OK | CAP-244, 271 |
| 4 passes | OK | CAP-245 |
| Intention / position / validation | OK | CAP-246–247, 272, 350 |
| Atomicité | OK | CAP-248, 297–299, 306, 315, 335 |
| Autonomie / richesse | OK | CAP-249, 307, 316, 336 |
| Attribution / citations | OK | CAP-250, 300, 308, 317, 339 |
| approval_global_partial / set | OK | CAP-251, 273, 293 |
| Métier vs bruit | OK | CAP-252, 266, 330 |
| Relations | OK | CAP-253, 338 |
| Actionable task/milestone | OK | CAP-254 |
| Registres futurs vs 0.1.2 | OK | CAP-255 |
| Samples 1/2 + COMPARISON | OK | CAP-256–258, 275–276, 309, 311, 318 |
| Scénarios A–H | OK | CAP-259–267 |
| Plan Cursor + 5/6 ajustements + feu vert | OK | CAP-269–278 |
| Audit 180454 (_gen.py, CAP-009/047, vide) | OK | CAP-279–288 |
| Audit 184105 (méthode, CAP-009/049) | OK | CAP-289–294 |
| Audit 194948 (CAP-031/022/028, validate.json) | OK | CAP-295–303, 348 |
| Feedback architecture Review=graphe | OK | CAP-304–305, 313–314, 326–327, 349 |
| Validations user Q1–Q5 | OK | CAP-320–324, 329–333 |
| Brief 0.1.3 — 6 axes individuels | OK | CAP-335–340, 346 |
| Test A / Test B | OK | CAP-319, 341–342 |
| Freeze 0.1.3 | OK | CAP-344–345 |
| Contradiction « pas de 0.1.3 » → faire 0.1.3 | OK | CAP-288/294/325 `contradicts`↔ CAP-328 ; aussi CAP-239/278 vs CAP-193 (pas de 0.1.2) |
| Capture ≠ Review deux niveaux | OK | CAP-312, 334, 343 |
| Bruit méta-test / simulation | Exclu | Pas de CAP métier sur l’exécution locale de cette capture ; audits de testruns capturés comme feedback/journal |

## Atomicité et richesse

- Splits effectués : scénarios A–H ; 5+1 ajustements plan ; 6 axes 0.1.3 ; Q1–Q5 séparées ; P1/P2 audits séparés ; CAP-022/028/031 comme feedback distincts.
- CAP courtes liées / enrichies : CAP-295 enrichie ; autonomie/richesse reliées à audit final.
- Incomplet signalé : détails exhaustifs du prompt 0.1.2 (tous les sous-points livrables) non éclatés phrase à phrase — couverts par CAP parent philosophie/périmètre/qualité.

## Provenance et refs

- Locators : oui (tous non vides ; multi-passages sur décisions plan, audits, brief 0.1.3)
- URLs/refs conservées : chemins/IDs exacts (`20261030-061941`, `180454`, `184105`, `194948`, `_gen.py`, `validate.json`, `conversation-reference-*.txt`, `clickup.md`, `6dddde5`, `956e6f7`, registres proposés, `--require-intention`) — pas de périphrase « lien fourni »
- Multi-passages : oui

## Grounding, mapping, space, approbation

- intention→type OK : mapping 0.1.4 strict sous `--require-intention`
- Anti-faux-explicit : oui — orientations/suggestions assistant en `none` ; `approval_global_partial` sans `explicit` ; explicites limités aux validations user claires (plan, feu vert, architecture, Q1–Q5, 0.1.3, scissions, sources officielles)
- Space (atelier par défaut) : propositions/conventions de prompt en `atelier` ; `pilotage` pour tâches/jalons/décisions de roadmapping ; `journal` pour push/audits factuels

## Contradictions / tensions

- Relations posées :
  - CAP-239 / CAP-278 `contradicts` CAP-193 (pas de 0.1.2) — réciproque non écrite sur CAP-193 (append-only)
  - CAP-328 `contradicts` CAP-288, CAP-294, CAP-325 (« pas de refonte 0.1.3 » / ne pas modifier Skill avant test) + réciproques `contradicted_by` sur nouvelles CAP
- WARN acceptés : réciproques manquantes vers CAP ≤238 (ne pas réécrire les anciennes)

## Corrections avant clôture

- Spaces `referentiel` trop précoces ramenés en `atelier` (CAP-241,242,244,245,247,312,334,343)
- CAP-309 : validation ramenée à `none` (exigence confirmée ≠ approbation formelle d’item)
- CAP-295 : contenu enrichi
- `conflicts_with` redondants vers CAP-328 retirés (déjà couverts par `contradicts`)
- Staging `lab/_staging_ref3.jsonl` + scripts one-shot `lab/_append_ref3_caps.py` / `lab/_fix_ref3_caps.py` à supprimer après run
