# Protocole de test — `/brain-capture` 0.1.3

## Sources officielles

| Échantillon | Fichier | Nature | Rôle |
| --- | --- | --- | --- |
| 1 | `brain/sources/conversation-reference-1.txt` | Conception initiale SB (~78 Ko) | Corpus de référence / comparaison historique |
| 2 | `brain/sources/conversation-reference-2.txt` | Stratégie + audits 0.1.1 + conception registres (~80 Ko) | Corpus indépendant |
| 3 | `brain/sources/conversation-reference-3.txt` | Suite post-0.1.2 / brief 0.1.3 / Test A–B (~107 Ko) | Smoke **régression** 0.1.3 |

Ne **pas** comparer les CAP entre sources. `erreur-1.txt` n'est **pas** une source officielle. Ne pas créer de fichier source vide.

## Types de tests (ne pas confondre)

| Test | Objectif | Preuve de |
| --- | --- | --- |
| Smoke technique validateur | Vide KO sous `--require-intention` ; living OK **sans** flag ; fixture 0.1.3 OK | Structure mécanique |
| **Smoke source 3** | Règles 0.1.3 sur exemples **connus** (conversation qui a conçu 0.1.3) | **Régression ciblée** — **pas** généralisation |
| Sources 1 / 2 (ultérieur) | Robustesse sur corpus officiels indépendants | Corpus distincts |
| **Test A** | Conversation Cursor **différente**, skill User figé 0.1.3 | **Généralisation** |
| **Test B** | Accès via lien (ChatGPT/Claude/…) | Accès total + capture |

Ne **jamais** présenter le smoke source 3 comme preuve que le Skill généralise.

## Critères génériques de couverture

Remplacent les scénarios A–H universels (spécifiques à l'échantillon 1) :

- Atomicité
- Couverture source-propre
- Provenance multi-locators
- Grounding honnête (dont `source_interpreted`)
- Relations sans validation implicite
- Contradictions étayées (`contradicts` / `conflicts_with`)
- Bruit distingué du métier

## Smoke technique validateur

1. Fichier vide + `--require-intention` → **ERROR** (exit ≠ 0).
2. `brain/registry/entries.jsonl` **sans** flag → OK (living rétrocompat).
3. Fixture / test-run 0.1.3 + `--require-intention` → OK ; `--json-out validate.json` produit l'artefact.

## Procédure — smoke source 3 (régression)

1. Mode **test-run** forcé ; créer `brain/registry/_test-runs/YYYYMMDD-HHMMSS/` (`run_id` = nom du dossier).
2. Capturer depuis `conversation-reference-3.txt` : fenêtres (~5) + 4 passes + mémoire globale + champs 0.1.3.
3. Skill-direct uniquement — **pas** de `_gen.py` pour générer les captures.
4. Audit final → `AUDIT.md`.
5. Valider :
   `python .cursor/skills/brain-capture/scripts/validate-registry.py <cible>/entries.jsonl --require-intention --json-out <cible>/validate.json`
6. Rédiger `COMPARISON.md` (grille de traçabilité) — qualifier explicitement : **smoke régression, pas Test A**.
7. Bilan template SKILL (3 couches).
8. Archiver ; ne pas écraser les runs précédents ni la production.

## Grille de traçabilité (`COMPARISON.md`)

Colonnes minimales :

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |

## Test A — généralisation (doc ; hors smoke 0.1.3)

- Workspace **indépendant** ; skill User **figé** 0.1.3.
- Conversation Second Brain à progression **différente** des sources 1–3.
- Capture intégrale + audit ; non-destruction ; granularité ; contradictions conservées.
- Succès = validation technique OK + audit + **évaluation humaine**.
- C'est le test qui prouve la **généralisation** — pas le smoke source 3.

## Test B — accès lien (doc)

- Lien ChatGPT / Claude / autre.
- Prérequis : accès à **toute** la conversation.
- Accès partiel = **échec d'accès** (pas un échec de capture sémantique).
- Pas de connecteur dans 0.1.3.

## Artefacts obligatoires (génération neuve / test-run)

| Artefact | Rôle (couche) |
| --- | --- |
| `entries.jsonl` | Registre |
| `validate.json` | Couche 1 — technique |
| `AUDIT.md` | Couche 2 — audit capture |
| `COMPARISON.md` | Traçabilité + type de test |
| Bilan chat | Synthèse (rappelle les 3 couches) |

Évaluation humaine = couche 3, hors artefacts automatiques.

## Avant freeze 0.1.3

Smoke technique + smoke source 3 (artefacts complets) + revue humaine ciblée. Puis Test A.
