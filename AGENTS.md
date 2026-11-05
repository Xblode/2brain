---
metadata_version: 1
title: "Instructions agents 2brain"
type: index
description: "Point d'entrée des agents IA : identité du projet, organisation, règles de travail et documents à lire selon la tâche."
version: "1.3.1"
status: review
created: "2026-10-31"
updated: "2026-11-05"
updated_from:
  - "brain-main/ROUTER.md"
  - ".claude/README.md"
  - "brain/docs/VISION.md"
---

# AGENTS.md

Point d'entrée des agents IA sur **2brain**. Orientation seulement : le détail est dans les documents cités, à lire selon la tâche.

## Projet

2brain est un **Second Brain** : système universel de gestion du cycle de vie de l'information (collecter, structurer, relier, versionner, faire évoluer) et de standardisation des projets, pour produire de meilleurs prompts d'agents IA. Trois dimensions : Connaissances, Idées, Projets.

Principes : préserver l'historique et la provenance ; une proposition n'est pas une décision tant qu'elle n'est pas validée explicitement ; le dépôt GitHub fait foi sur l'état réel du projet ; noms courts, simplicité progressive, indépendance des outils.

Mécanismes : Capture (collecte fidèle, append only) → Review (consolidation) → Search → Sync (outils externes comme ClickUp). **Seule Capture est outillée** (Skill `brain-capture`) ; Review, Search et Sync sont conceptuels. La commande unique `/brain` (Bootstrap) : scripts construits et testés (lot 2), **pas encore installés sur le compte** ; `-c`, `-s`, `-r` prévus au lot 3. En attendant, la capture se fait en lisant `brain-main/skills/brain-capture/SKILL.md`.

Espaces logiques d'une capture : `atelier` (exploration), `referentiel` (établi), `journal` (historique), `pilotage` (tâches, jalons). Ranger n'est pas valider.

Sources de vérité : `brain/` en local (registre JSONL) ; ClickUp est une interface synchronisée, pas une seconde source.

## Organisation

| Chemin | Nature | Rôle |
| --- | --- | --- |
| `brain/` | Instance projet | `docs/` (documentation), `registry/` (données : `entries.jsonl`, contrat `SCHEMA.md`), `conventions/` (conventions d'instance, aucune définie à ce jour) |
| `brain-main/` | Moteur universel | `conventions/` communes à toute instance ; `skills/` (outils) ; `bootstrap/` (spécification de la commande `/brain`) ; `ROUTER.md` (règles de délégation entre agents) |
| `brain-main/skills/brain-capture/` | Outil | Skill de capture, ses références et scripts. Claude Code ne le charge pas comme skill : lire `SKILL.md` pour une capture |
| `.claude/` | Adaptateur Claude Code | Applique `brain-main/ROUTER.md` avec `agents/` (orchestrateur et workers) et `settings.json`, documenté dans `.claude/README.md` |
| `lab/` | Hors instance | Sources de test, `_test-runs`, `_backup`, rapports. Pas une source de vérité |

## Conventions

Dossier `brain-main/conventions/` : `README.md` (catalogue et articulation), `METADATA.md` (front matter, versions, dates), `NAMING.md` (nommage), `TAXONOMY.md` (champs de registre). Elles s'appliquent **ensemble**.

- Modifier une convention : lire intégralement les quatre fichiers du dossier.
- **Obligatoire avant de créer ou modifier un document** : lire la convention concernée, au moins ses sections utiles (nom de fichier ou de dossier → `NAMING.md` ; en-tête de document → `METADATA.md` ; champ de registre → `TAXONOMY.md`). Un worker ne reçoit pas ce fichier : son brief nomme la convention à lire.
- Ne pas importer les conventions dans le contexte de départ.

## Quoi lire selon la tâche

| Tâche | Lire |
| --- | --- |
| Comprendre vision, principes, espaces | `brain/docs/CADRAGE.md` (par sections) ; `brain/docs/VISION.md` (provisoire) ; `brain/docs/README.md` (standard documentaire) |
| État du projet, architecture, workflow | `brain/docs/PROJECT.md`, `ARCHITECTURE.md`, `WORKFLOW.md` (provisoires) |
| Capture | `brain-main/skills/brain-capture/SKILL.md`, `brain/registry/SCHEMA.md`, `brain-main/conventions/TAXONOMY.md` |
| Registre | `brain/registry/SCHEMA.md` |
| Délégation entre agents | `brain-main/ROUTER.md`, `.claude/README.md` |
| Commandes `/brain`, Bootstrap | `brain-main/bootstrap/README.md` (état par commande ; scripts construits, pas encore installés sur le compte) |
| ClickUp | `brain/docs/INTEGRATIONS.md`. Aucune convention ClickUp n'existe (`brain/conventions/README.md`) : ne pas en inventer |

Les références `CAP-xxx` des documents provisoires pointent vers un ancien registre : voir `git show 45ba05d:brain/registry/entries.jsonl`.

## Règles

- **Append only** sur `brain/registry/entries.jsonl` : ne pas réécrire ni renuméroter les CAP existantes.
- Ne pas modifier un document avec `locked: true` sans demande explicite.
- Sauf consigne claire : ne pas lancer Brain Review / Sync / Search ; ne pas commit ni push sans demande.

## Commandes

```bash
python brain-main/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python brain-main/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl --require-intention --json-out lab/validate.json
```

`lab/validate.json` est un rapport technique généré à la demande, pas une source de vérité.

La commande `/brain` n'est pas encore installée sur le compte, et `/brain -c` (capture) est prévue au lot 3 : voir `brain-main/bootstrap/README.md`.
