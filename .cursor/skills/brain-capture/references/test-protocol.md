# Protocole de test — `/brain-capture` 0.1.4

## Sources officielles

| Échantillon | Fichier | Rôle |
| --- | --- | --- |
| 1 | `lab/sources/conversation-reference-1.txt` | Corpus conception initiale |
| 2 | `lab/sources/conversation-reference-2.txt` | Corpus indépendant |
| 3 | `lab/sources/conversation-reference-3.txt` | Smoke régression (≠ généralisation) |

Ne pas comparer les CAP entre sources. `erreur-1.txt` n’est pas une source officielle.

## Modes

| Mode | Usage |
| --- | --- |
| `production` | Living `brain/registry/entries.jsonl` — mode du **test manuel séquentiel** |
| `test-run` | Optionnel : `lab/_test-runs/MMDD-HHMM/` (suffixe `-2`, `-3`… si collision ; jamais écraser) |

**Pas** de forçage test-run sur `conversation-reference-*.txt`.

## Types de tests

| Test | Objectif |
| --- | --- |
| Smoke validateur | Voir `scripts/run_corrective_014_tests.py` |
| Test manuel production ×3 | [manual-production-sequence.md](manual-production-sequence.md) |
| Smoke source 3 (optionnel test-run) | Régression ciblée — pas Test A |
| Test A / B | Doc inchangée (généralisation / lien) — hors ce correctif |

## Smoke technique

```bash
python .cursor/skills/brain-capture/scripts/run_corrective_014_tests.py
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
```

Le validateur reste **mécanique** (mapping, enums, refs structure, locators). Il ne certifie pas la couverture sémantique.

## Artefacts

| Artefact | Couche |
| --- | --- |
| `entries.jsonl` | Registre |
| `validate.json` | 1 — technique |
| `AUDIT.md` | 2 — audit capture |
| `COMPARISON.md` | test-run seulement |
| Bilan chat | Synthèse |

Évaluation humaine = couche 3.
