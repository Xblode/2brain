# Capture `/brain-capture` 0.1.2 — skill direct

| | |
| --- | --- |
| Source | `brain/sources/conversation-reference-1.txt` |
| Mode | `test-run` (forcé — échantillon de référence) |
| Cible | `brain/registry/_test-runs/20261030-184105/entries.jsonl` |
| Registre production | **non modifié** |
| Méthode | Lecture source → fenêtres (~5 échanges) → 4 passes → écriture directe du JSONL |
| Script de génération | **aucun** (pas de `_gen.py`) |
| Schéma | 0.1.2 (`intention` + `position`) |
| Validateur | OK bloquant avec `--require-intention` |
| Entrées | 80 |
| Explicit | 22 |
| Partial endorsement | 7 |
| Jalons couches | 6 individuels |
| Sujets cadrage | 7 individuels |
| `approval_scope: set` | 0 |

Voir `COMPARISON.md` et `ISSUES.md`.
