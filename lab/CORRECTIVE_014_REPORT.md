# Rapport — Correctif Brain Capture 0.1.4

| | |
| --- | --- |
| Date | 2026-10-31 |
| Statut | **PRÊT POUR LE TEST MANUEL** |
| Commit / push | **non effectués** (consigne) |
| Test réel ×3 | **non lancé** (consigne) |

---

## 1. Structure actuelle constatée (audit préalable)

```
.cursor/skills/brain-capture/     Skill 0.1.3 (avant correctif)
brain/docs/                       vision, project, architecture, workflow, integrations, README (locked V1)
brain/registry/
  entries.jsonl                   living (localement vide au moment du correctif)
  SCHEMA.md
  _backup/archive/                archives pré-0.1.1 / scripts (déjà déplacés)
  _backup/_capability-test/       résultat capability-test archivé
  _test-runs/20261030-220724/     run actif restant
  _test-runs/archive/             anciens test-runs archivés
brain/sources/                    conversation-reference-1..3 + erreur-1.txt
```

- Pas de `brain-main/` avant ce correctif.
- Pas de `brain/conventions/` ni de `clickup.md` d’instance.
- Archives **non déplacées** par ce correctif.
- Dernier audit capability (`_backup/_capability-test/FINAL_ASSESSMENT.md`) : pertes URL, `type`/`space` poreux, relations inter-runs absentes, Search/Review manquants.

## 2. Structure créée ou modifiée

**Créé**

- `brain-main/README.md`
- `brain-main/conventions/README.md`
- `brain-main/conventions/taxonomy.md`
- `brain/conventions/README.md` (placeholder instance ; pas de clickup.md inventé)
- `.cursor/skills/brain-capture/references/manual-production-sequence.md`
- `.cursor/skills/brain-capture/scripts/run_corrective_014_tests.py`
- `brain/registry/CORRECTIVE_014_REPORT.md` (ce fichier)

**Modifié**

- Skill `SKILL.md` → **0.1.4**
- `references/capture-rules.md`, `source-attribution.md`, `registry-schema.md`, `test-protocol.md`
- `brain/registry/SCHEMA.md` → contrat 0.1.4 + `refs[]` + mapping
- `scripts/validate-registry.py` → mapping, refs, space REVIEW, contrat 0.1.4

**Non touché** : sources, archives, `_capability-test` archivé, `brain/docs/README.md` (locked), pas de Review/Search/Sync.

## 3. Fichiers modifiés (liste)

Voir §2. Skill + schéma + conventions + validateur + tests + instructions manuelles + ce rapport.

## 4. Règles corrigées

| Zone | Correctif |
| --- | --- |
| Atomicité | Exemples bons/mauvais ; anti-fusion / anti-sur-segmentation |
| intention vs type | intention primaire ; mapping déterministe auto |
| position / validation | rappel indépendance ; selected≠explicit |
| space | 4 définitions ; défaut atelier ; classer≠valider |
| URLs | `refs[]` + content littéral ; interdit « lien fourni » |
| Attribution | seuils high/medium/low/uncertain ; style≠high |
| Relations | priorités utilité ; réciproques recommandées non universelles |
| Retrouvabilité | titres spécifiques, tags utiles, noms exacts |
| Modes | plus de forçage test-run sur conversation-reference-* |
| test-run path | `MMDD-HHMM` + suffixes `-2`… si collision |

## 5. Mapping type / intention retenu

| intention | type |
| --- | --- |
| idea | idea |
| suggestion | proposition |
| preference | observation |
| orientation | proposition |
| question | open_question |
| decision | decision |
| requirement | observation |
| convention | convention |
| task | task |
| milestone | task |
| observation | observation |
| risk | observation |
| feedback | observation |

Sous `--require-intention` : écart = **ERROR**. Hors flag : **WARN** (historiques non réécrits).

## 6. Définition des quatre espaces

- **atelier** — réflexion, exploration, propositions, questions (défaut si doute).
- **referentiel** — connaissances / conventions / décisions établies.
- **journal** — événements, historique.
- **pilotage** — tâches, jalons, suivi.

Proposition non validée → pas de `referentiel` automatique.

## 7. Garantie conservation URLs / références

- Champ **`refs: string[]`** (littéraux exacts, multi-URLs OK).
- Obligation Skill : URL dans `refs` **et** `content`/`evidence`.
- `origin.url` ≠ stock multi-liens métier.
- Validateur : REVIEW si « lien fourni » sans URL ; REVIEW si URL texte absente de `refs`.
- Ne reconstruit / n’invente jamais d’URL.

## 8. Relations et attribution

- Priorités : answers, clarifies, evolves, contradicts (≠ différence), validation/rejet.
- Réciproques recommandées pour couples structurés ; `related` non forcé.
- Attribution : high seulement si structure fiable ; collages sans labels → medium/low/uncertain.

## 9. Tests techniques exécutés

```text
python .cursor/skills/brain-capture/scripts/run_corrective_014_tests.py
→ 15/15 PASS
```

Couvre : mapping OK/KO ; position≠explicit ; space atelier / REVIEW referentiel ; multi-URLs + ancres/params ; lien fourni ; refs type ; réciprocité answers WARN ; vide ERROR ; historique sans flag ; IDs uniques ; living sans réécriture.

```text
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
→ OK (fichier vide localement)
```

## 10. Instructions exactes — trois captures manuelles

Voir : `.cursor/skills/brain-capture/references/manual-production-sequence.md`

Résumé :

1. Workspace isolé, `entries.jsonl` **vide**, mode **production**, pas de `_test-runs` / `_capability-test` / `_gen`.
2. `/brain-capture` sur `conversation-reference-1.txt` → vérif N1, IDs, validate, URLs.
3. Idem source 2 en **append** → intégrité bloc 1 inchangée.
4. Idem source 3 → intégrité blocs 1–2.
5. Audit cumulé manuel `AUDIT-CUMUL.md`.

## 11. Limites restantes

- Pas de Search / Review / relations inter-runs (3 captures living partagent un fichier = IDs locaux OK ; pas de graphe sémantique cross-thème auto).
- Validateur ne mesure pas la couverture sémantique.
- Préservation URL dépend encore de la discipline agent + REVIEW mécanique (pas de preuve source↔refs automatique ligne à ligne).
- `brain-main/` n’héberge pas encore les Skills (restent sous `.cursor/skills/`).
- Convention ClickUp d’instance absente — non inventée.
- Atomicité fine et titres restent jugement d’audit (couche 2), pas ERROR validateur.

---

## Conclusion

**PRÊT POUR LE TEST MANUEL**
