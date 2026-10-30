# CAPTURE_NOTE — 20261031-000600-ref1

## Paramètres

| | |
| --- | --- |
| Skill | brain-capture 0.1.3 |
| Mode | test-run (capability-test isolé ; source `conversation-reference-*.txt`) |
| run_id | `20261031-000600-ref1` |
| Source | `brain/sources/conversation-reference-1.txt` |
| Cible | `brain/registry/_capability-test/20261031-000600-ref1/` |
| created_at | `2026-10-31T00:06:00Z` |
| project | `2brain` |
| storage | `brain/registry/_capability-test/20261031-000600-ref1/entries.jsonl` |

## Fenêtres (~5 échanges, mémoire globale)

| Fenêtre | window_id | Lignes approx. | Échanges (user↔assistant) | Focus |
| --- | --- | --- | --- | --- |
| W1 | `w1-brief-3q` | 1–114 | Brief → 3Q → réponses B\|C / ClickUp / socle | Vision, dossiers, premières orientations |
| W2 | `w2-spaces-pipeline` | 122–323 | 4 espaces → combo capture → pipeline + 3Q | Espaces, commandes, validation/orchestration |
| W3 | `w3-conflicts-mods` | 330–431 | Réponses → Card/OPDC → oui×3 mods | Conflits, historique, modules |
| W4 | `w4-archi-onboarding-go` | 434–726 | 3 niveaux → onboarding → bilan GO | Archi conceptuelle, init, sujets ouverts |
| W5 | `w5-practical-review` | 730–1258 | Exemple pratique → simulation review | Bases retenues, ClickUp, capture/review |
| W6 | `w6-auto-docs` | 1264–1451 | Capture auto/msg → synthèse docs/Inbox | Entretien mémoire, socle documentaire |

Chevauchement contextuel : W2 reprend W1 (B\|C, local) ; W3 reprend validation ; W5 cite blocs W2–W4 ; W6 évolue capture (CAP-084 `evolves_from` CAP-026).

Mémoire globale : **oui** (même agent, anti-doublons inter-fenêtres ; IDs continus CAP-001→117).

## Passes par fenêtre

Pour chaque fenêtre : (1) informations (2) actionable (3) relations (4) autonomie/contexte — puis audit global avant validation.

## Artefacts produits

- `entries.jsonl` (117 CAP)
- `validate.json` (OK bloquant, `--require-intention`)
- `AUDIT.md`
- `COMPARISON.md`
- `CAPTURE_NOTE.md`

## Non touché

- Production `brain/registry/entries.jsonl`
- Autres sources / `brain/docs`
- Skill / sources
- Anciens `_test-runs`
