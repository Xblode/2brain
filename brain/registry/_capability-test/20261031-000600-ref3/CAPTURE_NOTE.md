# CAPTURE_NOTE — 20261031-000600-ref3

## Identité

| | |
| --- | --- |
| Skill | `/brain-capture` 0.1.3 |
| Mode | test-run (capability) — source `conversation-reference-*.txt` ⇒ forcé hors production |
| run_id | `20261031-000600-ref3` |
| Source | `brain/sources/conversation-reference-3.txt` (2296 lignes) |
| Cible | `brain/registry/_capability-test/20261031-000600-ref3/entries.jsonl` |
| created_at | `2026-10-31T00:06:00Z` |
| project | `2brain` |
| Méthode | skill-direct (pas de `_gen.py` dans le dossier run) |

## Fenêtres (~5 échanges)

Échanges repérés (user↔assistant) : **7**.

| Fenêtre | Échanges | Lignes approx. | Focus |
| --- | --- | --- | --- |
| W1 | E1–E3 | 1–1220 | Prompt 0.1.2, plan Cursor, 5 ajustements, feu vert |
| W2 | E3–E5 (chevauchement) | 976–1481 | Audits 180454 puis 184105 |
| W3 | E5–E6 | 1486–1822 | Audit 194948 + feedback user atomicité/Review/test |
| W4 | E6–E7 | 1827–2296 | Architecture Review/graphe + brief 0.1.3 + Test A/B |

Mémoire de travail globale : **oui** (IDs continus CAP-001→112, relations inter-fenêtres, contradiction CAP-063↔CAP-095).

## Quatre passes (par fenêtre)

1. Informations — idées, conventions design, orientations, décisions, feedbacks d’audit  
2. Actionable — tâches/jalons protocole, axes 0.1.3, Test A/B, validate.json  
3. Relations — answers/clarifies/evolves/parent_of/contradicts  
4. Contexte autonomie — contenus enrichis, incertitudes d’auteur, anti-faux-explicit  

## Validateur

```text
python .cursor/skills/brain-capture/scripts/validate-registry.py \
  brain/registry/_capability-test/20261031-000600-ref3/entries.jsonl \
  --require-intention \
  --json-out brain/registry/_capability-test/20261031-000600-ref3/validate.json
```

Résultat : **OK bloquant** (0 erreur) ; avertissement résumé uniquement. Artefact : `validate.json`.

## Artefacts

| Fichier | Statut |
| --- | --- |
| `entries.jsonl` | 112 CAP |
| `validate.json` | oui |
| `AUDIT.md` | oui |
| `COMPARISON.md` | oui (smoke régression, pas Test A) |
| `CAPTURE_NOTE.md` | oui |
| Production `brain/registry/entries.jsonl` | **non touchée** |

## Notes

- Attribution sans métadonnées de rôle : tours déduits de la structure conversationnelle.
- Bruit exclu du métier : tableaux de scores des runs audités ; méta d’exécution Cursor hors décisions de conception.
- Capability-test isolé sous `_capability-test/` (hors `_test-runs/` production-adjacent).
