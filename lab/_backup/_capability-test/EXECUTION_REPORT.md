# Rapport d’exécution — Test de capacité 2026-10-31

## Artefacts

### Captures

- `brain/registry/_capability-test/20261031-000600-ref1/` — entries, validate, AUDIT, COMPARISON, CAPTURE_NOTE
- `brain/registry/_capability-test/20261031-000600-ref2/` — idem
- `brain/registry/_capability-test/20261031-000600-ref3/` — idem (+ SCHEMA.md extra)

### Vérification / reconstruction / audit

- `brain/registry/_capability-test/PHASE2_VERIFICATION.md`
- `brain/registry/_capability-test/_phase2_stats.py` (outil local de stats)
- `brain/registry/_capability-test/reconstruction-20261031/` — 3 JSONL copies + 7 docs reconstruits
- `brain/registry/_capability-test/PHASE4_COMPARATIVE_AUDIT.md`
- `brain/registry/_capability-test/FINAL_ASSESSMENT.md`
- `brain/registry/_capability-test/EXECUTION_REPORT.md` (ce fichier)

## Commandes de validation

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/_capability-test/20261031-000600-ref1/entries.jsonl --require-intention
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/_capability-test/20261031-000600-ref2/entries.jsonl --require-intention
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/_capability-test/20261031-000600-ref3/entries.jsonl --require-intention
```

(rejouées en Phase 2 ; toutes OK bloquant)

Aussi pendant Phase 1 (par run) :

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py <run>/entries.jsonl --require-intention --json-out <run>/validate.json
```

## Erreurs rencontrées

1. Première vague d’agents Claude Sonnet : échec « out of usage » — relance modèle parent.
2. Scripts temporaires `_entries_build.py` / `_build_entries.py` sur ref1/ref2 (retirés avant clôture) — écart protocole.
3. PowerShell : `python -c` multiligne échoué — contournement via `_phase2_stats.py`.

## Non modifié

- Skill brain-capture
- Sources `conversation-reference-*.txt`
- Registre production `brain/registry/entries.jsonl`
- Pas de Brain Review / Sync
- Pas de commit / push

## Verdict

Voir `FINAL_ASSESSMENT.md` — **mémoire de conception partielle ; insuffisante seule pour poursuivre le développement du dépôt**.
