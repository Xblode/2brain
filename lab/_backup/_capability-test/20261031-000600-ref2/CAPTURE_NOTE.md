# CAPTURE_NOTE — 20261031-000600-ref2

| | |
| --- | --- |
| Skill | `/brain-capture` **0.1.3** |
| Mode | test-run isolé (`_capability-test`, pas production) |
| Source unique | `brain/sources/conversation-reference-2.txt` (1705 lignes) |
| run_id | `20261031-000600-ref2` |
| Cible | `brain/registry/_capability-test/20261031-000600-ref2/entries.jsonl` |
| Méthode | Skill-direct (fenêtres + 4 passes + mémoire globale) — **pas** `_gen.py` |
| created_at | `2026-10-31T00:06:00Z` |
| project | `2brain` |

## Fenêtres

| Fenêtre | Lignes approx. | Contenu |
| --- | --- | --- |
| W1 | 1–345 | Question stratégique + analyse 6 risques / transformation / étapes |
| W2 | 349–661 | Audit test 20261030-045232 (V0.1.1) |
| W3 | 665–943 | Audit test 20261030-061941 (re-capture) |
| W4 | 949–1048 | Réponses user aux problèmes sémantiques + bascule conception |
| W5 | 1053–1467 | Conception Capture / Review / registres / questions |
| W6 | 1470–1706 | Réponses registres, Sync, intention unique, archivage D |

Chevauchement contextuel + mémoire de travail globale entre fenêtres. Messages longs ⇒ fenêtres = ~1 échange riche plutôt que 5 tours courts.

## Passes par fenêtre

1. Informations (idées, risques, feedbacks, décisions…)
2. Actionnable (milestones, tasks, cadrage)
3. Relations (answers, clarifies, contradicts, related…)
4. Contexte d’autonomie (enrichissement content / multi-locators)

## Résultat

- **120** CAP (`CAP-001` → `CAP-120`)
- Validateur : **OK** bloquant (`--require-intention` + `validate.json`)
- Artefacts : `entries.jsonl`, `validate.json`, `AUDIT.md`, `COMPARISON.md`, `CAPTURE_NOTE.md`
- Production : **non** touchée
