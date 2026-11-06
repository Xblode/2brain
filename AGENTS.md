---
metadata_version: 1
title: "Instructions agents 2brain"
type: index
description: "Point d'entrée des agents IA : identité du projet, organisation, règles de travail et documents à lire selon la tâche."
version: "1.7.0"
status: review
created: "2026-10-31"
updated: "2026-11-06"
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

Mécanismes : Capture (collecte fidèle, append only) → Review (consolidation) → Search → Sync (outils externes comme ClickUp). **Capture, Search et Review sont outillés par des scripts** (`brain-main/skills/brain-capture/`, `brain-search/`, `brain-review/` ; Review en rapport seulement, Search en lecture seule) ; **Sync reste conceptuel**. La commande unique `/brain` (Bootstrap 0.4.0 dans le dépôt) : `-i`, `-u`, `-o` (remplit `brain/docs/` d'un projet, écrit seulement après validation), `-c`, `-c <fichier>`, `-c 1`, `-s`, `-r` construits et testés par scripts ; le compte porte le Bootstrap 0.3.0 (`-i` essayé en session réelle le 2026-11-06 ; `-o`, `-c`, `-s`, `-r` présents mais pas encore essayés en session ; le routeur demande la 0.4.0, donc une réinstallation du compte). Le guide des outils, tel que le reçoit un projet installé, est `brain-main/README.md`. Sans la commande, la capture se fait en lisant `brain-main/skills/brain-capture/SKILL.md`.

Espaces logiques d'une capture : `atelier` (exploration), `referentiel` (établi), `journal` (historique), `pilotage` (tâches, jalons). Ranger n'est pas valider.

Sources de vérité : `brain/` en local (registre JSONL) ; ClickUp est une interface synchronisée, pas une seconde source.

## Organisation

| Chemin | Nature | Rôle |
| --- | --- | --- |
| `README.md` | Navigation racine | Index court du dépôt : oriente vers `AGENTS.md`, `brain-main/`, `brain/`, `lab/` |
| `brain-main/skills/README.md` | Index des skills | Relie chaque commande d'outil (`-c`, `-o`, `-s`, `-r`) à son dossier et à son point d'entrée |
| `brain/README.md` | Index de l'instance | Oriente dans `docs/`, `registry/` et `conventions/` de l'instance |
| `brain/` | Instance projet | `docs/` (documentation), `registry/` (données : `entries.jsonl`, contrat `SCHEMA.md`), `conventions/` (conventions d'instance, aucune définie à ce jour) |
| `brain-main/` | Moteur universel | `conventions/` communes à toute instance ; `skills/` (outils) ; `bootstrap/` (spécification de la commande `/brain`) ; `ROUTER.md` (règles de délégation entre agents) ; `adapters/claude-code/` (source de l'adaptateur que `/brain -i` copie dans `.claude/` des projets installés) |
| `brain-main/skills/brain-capture/` | Outil | Skill de capture, ses références et scripts. Claude Code ne le charge pas comme skill : lire `SKILL.md` pour une capture |
| `brain-main/skills/brain-onboarding/` | Outil | `SKILL.md` de `/brain -o`, lu quand l'outil sert |
| `brain-main/registry/SCHEMA.md` | Contrat | Contrat du registre pour un projet installé (même contenu que `brain/registry/SCHEMA.md` du dépôt) |
| `brain-main/skills/brain-search/`, `brain-review/` | Outils | Scripts de recherche (lecture seule) et de Review (rapport seulement), appelés par `/brain -s` et `/brain -r`. Pas de `SKILL.md` |
| `.claude/` | Adaptateur Claude Code | Applique `brain-main/ROUTER.md` avec `agents/` (orchestrateur et workers) et `settings.json`, documenté dans `.claude/README.md` ; copie de travail de ce dépôt, comparée par test à `brain-main/adapters/claude-code/` |
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
| Se servir des outils 2brain | `brain-main/README.md` (guide : commandes, niveaux de lecture, règles) |
| Commandes `/brain`, Bootstrap | `brain-main/bootstrap/README.md` (état par commande ; construits et testés par scripts, compte en 0.3.0 ; Search et Review : §8.3 et §8.4) |
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

Search et Review (`search-registry.py`, `review-registry.py`) ne se lancent que sur demande claire, et jamais sur le vrai registre pour un essai : travailler sur une copie. La commande `/brain` : voir `brain-main/bootstrap/README.md`.
