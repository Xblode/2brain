---
metadata_version: 1
title: "Instructions agents 2brain"
type: index
description: "Point d'entrée des agents IA : identité du projet, organisation, règles de travail et documents à lire selon la tâche."
version: "1.11.0"
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

Mécanismes : Capture (collecte fidèle, append only) → Review (consolidation) → Search → Sync (outils externes comme ClickUp). **Capture, Search et Review sont outillés par des scripts** (`brain-main/skills/brain-capture/`, `brain-search/`, `brain-review/` ; Review en rapport seulement, Search en lecture seule) ; **Sync reste conceptuel**. La commande unique `/brain` (Bootstrap 0.7.0 dans le dépôt ; le compte se met à jour par `install-account.py`) : `-i`, `-u`, `-a` (audit en profondeur d'un projet existant : lecture seule, rapport, puis écritures validées une à une ; essayé par l'humain dans son projet, selon lui, non contrôlé), `-o` (remplit `brain/docs/` d'un projet, écrit seulement après validation), `-c`, `-c <fichier>`, `-c 1`, `-s`, `-r`, `-d on|off` construits et testés par scripts ; `-m` et `-m <nombre>` (README des dossiers maîtres, nombre maximum réglé dans `brain/settings.json`, 8 par défaut) construits et testés par scripts, avec un hook de compte qui refuse une fois chaque `git commit` dont les README sont à relire ; `-a`, `-m` et ce hook restent à confirmer en session réelle (test réel du 2026-11-06 : `-i`, `-o`, `-c`, `-s`, `-r`, `-c 1` ont abouti en session sans routeur ; selon l'humain, le routeur fonctionne dans une nouvelle conversation (non contrôlé)). Le guide des outils, tel que le reçoit un projet installé, est `brain-main/README.md`. Sans la commande, la capture se fait en lisant `brain-main/skills/brain-capture/SKILL.md`.

Espaces logiques d'une capture : `atelier` (exploration), `referentiel` (établi), `journal` (historique), `pilotage` (tâches, jalons). Ranger n'est pas valider.

Sources de vérité (arbitrage du 2026-11-05) : Git/code = état réel, registre = ce qui a été dit et décidé, docs = connaissance consolidée, ClickUp = vue.

## Organisation

| Chemin | Nature | Rôle |
| --- | --- | --- |
| `README.md` | Navigation racine | Index court du dépôt : oriente vers `AGENTS.md`, `brain-main/`, `brain/`, `lab/` |
| `brain-main/skills/README.md` | Index des skills | Relie chaque commande d'outil (`-c`, `-o`, `-a`, `-m`, `-s`, `-r`) à son dossier et à son point d'entrée |
| `brain/README.md` | Index de l'instance | Oriente dans `docs/`, `registry/` et `conventions/` de l'instance |
| `brain/` | Instance projet | `docs/` (documentation), `registry/` (données : `entries.jsonl`, contrat `SCHEMA.md`), `conventions/` (conventions d'instance, aucune définie à ce jour) |
| `brain-main/` | Moteur universel | `conventions/` communes à toute instance ; `skills/` (outils) ; `bootstrap/` (spécification de la commande `/brain`) ; `ROUTER.md` (règles de délégation entre agents) ; `adapters/claude-code/` (source de l'adaptateur que `/brain -i` copie dans `.claude/` des projets installés) |
| `brain-main/skills/brain-capture/` | Outil | Skill de capture, ses références et scripts. Claude Code ne le charge pas comme skill : lire `SKILL.md` pour une capture |
| `brain-main/skills/brain-onboarding/` | Outil | `SKILL.md` de `/brain -o`, lu quand l'outil sert |
| `brain-main/skills/brain-audit/` | Outil | `SKILL.md` de `/brain -a` et `scripts/scan-project.py` (lecture seule) |
| `brain-main/skills/brain-readme/` | Outil | `SKILL.md` de `/brain -m` : README des dossiers maîtres et leur nombre maximum |
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
| Comprendre vision, principes, espaces | `brain/docs/CADRAGE.md` (par sections) ; `brain/docs/VISION.md` (`draft`) ; `brain/docs/README.md` (standard documentaire : six documents standards, dont `CADRAGE.md`) |
| État du projet, architecture, workflow | `brain/docs/PROJECT.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `WORKFLOW.md` (`draft`, états étiquetés `constaté` ou `déclaré par l'humain, non contrôlé`) |
| Capture | `brain-main/skills/brain-capture/SKILL.md`, `brain/registry/SCHEMA.md`, `brain-main/conventions/TAXONOMY.md` |
| Registre | `brain/registry/SCHEMA.md` |
| Délégation entre agents | `brain-main/ROUTER.md`, `.claude/README.md` |
| Se servir des outils 2brain | `brain-main/README.md` (guide : commandes, niveaux de lecture, règles) |
| Commandes `/brain`, Bootstrap | `brain-main/bootstrap/README.md` (état par commande ; construits et testés par scripts, Bootstrap 0.7.0 dans le dépôt ; Search et Review : §8.3 et §8.4) |
| ClickUp | `brain/docs/INTEGRATIONS.md`. Aucune convention ClickUp n'existe (`brain/conventions/README.md`) : ne pas en inventer |

Les références `CAP-xxx` des sections « Ancienne synthèse » des documents de `brain/docs/` pointent vers un ancien registre : voir `git show 45ba05d:brain/registry/entries.jsonl`. Ailleurs, elles renvoient au registre actuel.

## Règles

- **Append only** sur `brain/registry/entries.jsonl` : ne pas réécrire ni renuméroter les CAP existantes.
- Ne pas modifier un document avec `locked: true` sans demande explicite.
- Sauf consigne claire : ne pas lancer Brain Review / Sync ; ne pas commit ni push sans demande.
- **Recherche sans demander** (décision de l'humain, 2026-11-06, CAP-452) : avant de proposer une implémentation, ou quand le sujet a pu être déjà traité, chercher dans le registre sans demander, en lançant `worker-haiku` (lecture seule : `search-registry.py` ou Grep sur le vrai registre). Sans cet agent (session non routée), lancer soi-même la recherche. Elle n'écrit rien.
- **Avant de travailler dans un dossier** : lire son README le plus proche (dossier courant, sinon un parent) et le tenir à jour si le travail change son rôle ou ses fonctionnalités (modèle : `brain-main/conventions/METADATA.md` §6.9).
- Règle immuable de l'humain (2026-11-06) : avant chaque commit, relire les README des dossiers modifiés (le plus proche de chaque fichier) et rapporter ce qui a été relu et corrigé ; un hook du compte (`brain-main/bootstrap/README.md` §9.2) arrête une fois le commit et donne la consigne, sans garantir la lecture.

## Commandes

```bash
python brain-main/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python brain-main/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl --require-intention --json-out lab/validate.json
```

`lab/validate.json` est un rapport technique généré à la demande, pas une source de vérité.

Review (`review-registry.py`) ne se lance que sur demande claire ; Search (`search-registry.py`) se lance sans demander (règle « Recherche sans demander »). Un essai de script se fait toujours sur une copie du registre, jamais sur le vrai. La commande `/brain` : voir `brain-main/bootstrap/README.md`.
