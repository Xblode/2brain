# AUDIT — capture production (ref2)

| | |
| --- | --- |
| Source | `lab/sources/conversation-reference-2.txt` |
| Cible | `brain/registry/entries.jsonl` |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |
| run_id | `production` |
| IDs | CAP-118 → CAP-238 (121 ajoutées ; CAP-001…117 intactes) |

## Couverture source↔registre

| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |
| Lancement 1.1 + questions stratégiques | OK | CAP-118–122 |
| Six risques long terme (individuels) | OK | CAP-123,125,127,129,131,133 (+ exigences liées) |
| Transformation méthode / 5 étapes / indicateurs | OK | CAP-135–146 |
| Question assist vs IA-directeur | OK | CAP-146 |
| Audit V0.1.1 — 045232 | OK | CAP-147–161 |
| Audit V0.1.1 — 061941 (re-capture source) | OK | CAP-162–173 |
| Réponses user problèmes sémantiques | OK | CAP-174–194 |
| Fenêtres ~5 + multi-passes | OK | CAP-178,199,205–206 |
| Intentions / positions | OK | CAP-183–184,196–198,219 |
| Capture / Review / Sync | OK | CAP-195–196,190,220–221 |
| Registres multi-fichiers + SoT | OK | CAP-187–188,204,211–212,215–217 |
| clickup.md emplacement | OK | CAP-188 (Q) + CAP-203 (reco `brain/conventions/clickup.md`) |
| Archivage D + immutabilité entries | OK | CAP-222–225 |
| 6 jalons individuels (couches) | OK | CAP-226–231 (liés CAP-110…115) |
| 7 sujets cadrage individuels | OK | CAP-232–238 (liés CAP-103…109) |
| Décisions user explicites | OK | multi-info OUI ; jeter 045232 ; pas 0.1.2 maintenant ; intention unique ; Review local / Sync ClickUp ; archivage D |
| Bruit méta-test | Exclu | Pas de CAP métier sur la simulation de capture elle-même ; filtre documenté (CAP-171,191) |

## Atomicité et richesse

- Splits effectués : 6 risques séparés ; 5 étapes manquantes ; 6 jalons roadmap ; 7 cadrages ; orchestrateur vs agents (réponses distinctes) ; intention/position/validation ; Review vs Sync ; clickup.md Q vs emplacement ; SoT vs correspondance IDs.
- CAP courtes liées / enrichies : exigences anti-risque liées via `clarifies` ; jalons/cadrages liés aux CAP production source 1.
- Incomplet signalé : détails Inbox/onboarding/brief 500 mots restent surtout agrégés dans CAP-172 (observation couverture) — pas re-éclatés unitairement faute de formulation source primaire hors audit.

## Provenance et refs

- Locators : oui (tous non vides ; multi-passages sur fenêtres, jalons, cadrages, décisions Q2)
- URLs/refs conservées : chemins/IDs exacts (`20261030-045232`, `20261030-061941`, `generate_testrun_011.py`, `brain/registry/_backup/correction-diff-0.1.1.json`, `brain/conventions/clickup.md`, `entries.jsonl`, `archive-index.jsonl`, registres proposés, etc.) — pas de périphrase « lien fourni »
- Multi-passages : oui

## Grounding, mapping, space, approbation

- intention→type OK : mapping 0.1.4 strict (risk/requirement → observation ; orientation/suggestion → proposition ; milestone → task)
- Anti-faux-explicit : oui — suggestions/orients restent `none` ; explicites limités aux 6 choix user clairs ; `approval_global_partial` → `validation: none`
- Space (atelier par défaut) : propositions non établies en `atelier` ; `referentiel` réservé aux règles/observations présentées comme établies ou décisions explicites ; `pilotage` pour jalons/tâches

## Contradictions / tensions

- Relations posées : CAP-193 (`Pas de 0.1.2`) `contradicts` reco assistant V0.1.2 + réciproque `contradicted_by`
- WARN accepté : CAP-189 `clarifies` → CAP-074 sans réciproque (ne pas réécrire CAP-001…117)

## Corrections avant clôture

- CAP-118 : `type` ramené à `observation` (mapping ; `event` interdit sous `--require-intention`)
- Réciproques `clarified_by` ajoutées uniquement entre CAP ≥118
- Staging `lab/_staging_*` à supprimer après run
