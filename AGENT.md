# AGENT.md

Point d’entrée opérationnel pour les agents IA travaillant sur **2brain** (Second Brain).

## Rôles des dossiers racine

| Dossier | Rôle |
| --- | --- |
| `brain/` | Instance projet : docs, registre living, conventions d’instance |
| `brain-main/` | Moteur universel : conventions communes (taxonomies), futur catalogue Skills/règles |
| `lab/` | Hors instance : sources de test, `_test-runs`, `_backup`, rapports de correctif |
| `.cursor/skills/` | Skills Cursor installés (ex. `/brain-capture`) |

## Registre living

- Fichier : `brain/registry/entries.jsonl`
- Schéma : `brain/registry/SCHEMA.md`
- Taxonomies : `brain-main/conventions/taxonomy.md`
- Capture : Skill `.cursor/skills/brain-capture/` (version courante dans `SKILL.md`)

**Append only** en production : ne pas réécrire / renuméroter les CAP existantes.

## Commandes utiles

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl --require-intention --json-out lab/validate.json
python .cursor/skills/brain-capture/scripts/run_corrective_014_tests.py
```

`validate.json` n’est **pas** une source de vérité : c’est un rapport technique généré à la demande (`--json-out`). Un ancien rapport obsolète peut vivre sous `lab/validate-stale-*.json`.

## Documents projet

Socle documentaire : `brain/docs/` (catalogue dans `brain/docs/README.md`).  
Ne pas modifier un doc avec `locked: true` sans demande explicite.

## Hors scope par défaut

Sauf consigne claire : ne pas lancer Brain Review / Sync / Search ; ne pas inventer de conventions ClickUp ; ne pas commit/push sans demande.
