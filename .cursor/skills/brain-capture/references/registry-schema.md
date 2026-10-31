# Schéma registre — vue Skill (0.1.4)

Source de vérité : `brain/registry/SCHEMA.md` + `brain-main/conventions/taxonomy.md`.

## Champs (delta 0.1.4)

| Champ | Notes |
| --- | --- |
| `intention` | **Primaire** — choisir d’abord |
| `type` | **Dérivé** via mapping taxonomy (automatique) |
| `refs` | Tableau optionnel de strings littérales (URLs, chemins, IDs) |
| Autres | Inchangés vs 0.1.3 (`run_id`, `capture_ref`, `locators`, …) |

## Mapping intention → type

Voir taxonomy / SCHEMA. Points non négociables :

- `orientation` → `proposition` (jamais `decision`)
- `suggestion` → `proposition` (jamais `decision`)
- `question` → `open_question` (jamais `decision`)

## Space

`atelier` (défaut exploration) \| `referentiel` (établi) \| `journal` \| `pilotage`  
Classer ≠ valider.

## refs vs origin.url

- `refs[]` : liens / ancres **du contenu métier** (multiples OK).
- `origin.url` : URL éventuelle du **document source** — pas le stock multi-liens métier.

## Relations / identité

Inchangé : cibles `CAP-NNN` locales au fichier ; pas d’inter-runs.

## Validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py path/entries.jsonl --require-intention --json-out validate.json
```

Mécanique uniquement (mapping, enums, refs structure, locators). Pas de jugement sémantique de couverture.
