---
metadata_version: 1
title: "Architecture"
type: specification
description: "Comment 2brain est organisé et conçu : composants, répartition des sources de vérité, état constaté."
summary: "Organisation constatée du dépôt (moteur, instance, adaptateur, laboratoire), répartition des rôles entre Git, registre, documents et ClickUp, mécanismes Capture/Search/Review/Sync et leur état réel, conventions. Les pistes d'architecture cible restent des propositions non validées."
version: "0.2.0"
status: draft
created: "2026-10-30"
updated: "2026-11-06"
scope:
  level: project
  targets:
    - 2brain
depends_on:
  - "brain/docs/README.md"
updated_from:
  - "brain/registry/entries.jsonl"
  - "brain-main/bootstrap/README.md"
  - "AGENTS.md"
---

# Architecture

## 1. Objet

Comment 2brain est organisé. Ce document ne dit pas pourquoi le projet existe (voir `brain/docs/VISION.md`, CAP-411 : « la vision ne doit jamais vivre dans projet ni l'architecture dans vision ») et ne recopie pas les tableaux d'état de `brain-main/bootstrap/README.md` ni l'organisation détaillée de `AGENTS.md` : il y renvoie.

Étiquettes : `décision humaine`, `demande humaine` (dite par l'humain, sans validation formelle), `proposition non validée`, `question ouverte` ; pour l'état du système, `constaté` (avec le chemin) ou `déclaré par l'humain, non contrôlé`.

## 2. Organisation constatée

- `constaté`. `brain-main/` est le moteur universel : conventions (`brain-main/conventions/`), outils (`brain-main/skills/`), commande `/brain` (`brain-main/bootstrap/`), règles de délégation (`brain-main/ROUTER.md`), adaptateur Claude Code (`brain-main/adapters/claude-code/`).
- `constaté`. `brain/` est l'instance du projet : documents (`brain/docs/`), registre (`brain/registry/`), conventions d'instance (`brain/conventions/`, sans convention définie).
- `constaté`. `.claude/` est la copie de travail de l'adaptateur Claude Code (`.claude/agents/`, `.claude/settings.json`). `lab/` est hors instance : sources de test et rapports, pas une source de vérité.
- Le détail de chaque dossier : `AGENTS.md` (section Organisation) et `brain/README.md`.

## 3. Où vit quoi

- `décision humaine` (plan du 2026-11-05, hors registre) : « Git/code = état réel, registre = ce qui a été dit et décidé, docs = connaissance consolidée, ClickUp = vue ».
- `demande humaine`. CAP-443 : « GitHub restera toujours une source de vérité ».
- `proposition non validée`. CAP-404 : « les documents représentent la connaissance consolidée du projet ; le registre conserve la mémoire traçable de sa construction ».
- `constaté`. Le registre est un fichier JSONL en ajout seul, `brain/registry/entries.jsonl`, dont le contrat est `brain/registry/SCHEMA.md`.
- `proposition non validée`. CAP-447 : l'assistant recommande de garder JSONL pour le registre et d'employer TOML pour la configuration. Aucun fichier TOML n'est constaté dans `brain-main/skills/`.

## 4. Mécanismes

- `constaté`. Capture, Search et Review ont des scripts : `brain-main/skills/brain-capture/scripts/append-captures.py`, `brain-main/skills/brain-search/scripts/search-registry.py`, `brain-main/skills/brain-review/scripts/review-registry.py`. Review produit un rapport et n'écrit rien ; elle ne consolide pas les documents (`brain-main/bootstrap/README.md` §8.4).
- `constaté`. Sync n'a aucun script : il reste conceptuel (`AGENTS.md`).
- `constaté`. Prérequis des scripts : Python 3, bibliothèque standard seulement (`brain-main/bootstrap/README.md` §9).
- État par commande `/brain` : `brain-main/bootstrap/README.md` §1. Non recopié ici.
- `constaté`. Routeur : `brain-main/ROUTER.md` décrit les rôles ; `.claude/agents/` contient `orchestrator.md`, `worker-haiku.md`, `worker-sonnet.md` ; `.claude/settings.json` contient la clé `agent`. `déclaré par l'humain, non contrôlé` (2026-11-06) : le routeur fonctionne dans une nouvelle conversation.

## 5. Conventions

- `constaté`. Conventions générales : `brain-main/conventions/README.md`, `METADATA.md`, `NAMING.md`, `TAXONOMY.md`. Aucune convention spécialisée (web, mobile) ni d'instance n'existe.
- `demande humaine`. CAP-459 : « les conventions générales s'appliquent à tous les projets qui les utilisent » ; les conventions spécialisées « ne s'appliquent pas aux niveaux au-dessus ».
- `proposition non validée`. CAP-458 : trois niveaux de conventions (générales, spécialisées, projet), propagation descendante.

## 6. Pistes d'architecture cible

- `proposition non validée`. CAP-405 : cinq couches ; « la troisième (modèle de connaissances du projet) est le manque principal ». Elle correspond à ce que Review ne fait pas aujourd'hui.
- `proposition non validée`. CAP-390 : quatre niveaux à distinguer (sources originales, connaissances structurées, documents consolidés, contexte opérationnel IA).
- `question ouverte`. Modèle de données définitif des informations, versions et relations (`brain/docs/CADRAGE.md` §20.4, question 1).
- `question ouverte`. Répartition entre `architecture.md` et `workflow.md` pour le modèle de fonctionnement : voir la section **Ancienne synthèse** (point alors non décidé).

## 7. Références

`brain/docs/CADRAGE.md` (§7 mécanismes, §8 standardisation, §10 registre, §11 GitHub), `brain-main/bootstrap/README.md`, `brain-main/ROUTER.md`, `AGENTS.md`.

## Ancienne synthèse

Texte d'origine, conservé tel quel dans le bloc ci-dessous (règle de l'humain, CAP-399 : rien ne se perd). Il date de la première synthèse provisoire. Les numéros `CAP-xxx` qu'il cite viennent de l'ancien registre de 69 captures et ne correspondent pas au registre actuel ; pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

````markdown
# Architecture

> **Provisoire** — synthèse légère issue de la capture. Détail : `brain/registry/entries.jsonl`.
> Sources : CAP-002, CAP-009, CAP-010, CAP-016, CAP-019, CAP-022–CAP-026, CAP-043–CAP-044, CAP-058.
> **Attention : références obsolètes.** Les `CAP-xxx` de ce document viennent de l'ancien registre de 69 captures (commit `45ba05d`). Le registre actuel réutilise ces numéros pour d'autres contenus : ne pas les y chercher. Pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

## Brain / Brain-main (provisoire)

- **Brain/** : instance projet (connaissances, registres, état).
- **Brain-main/** : moteur (conventions, agents, skills, modules de référence).

## Directions retenues en atelier (≠ officielles figées)

- Socle universel + modules spécialisés — CAP-009.
- Quatre espaces logiques : Atelier, Référentiel, Journal, Pilotage — CAP-010.
- Core / Modules / Instance — CAP-024 ; modules type « mods » — CAP-023, CAP-025.
- Contrat d’information commun (type, origine, statut, relations…) — CAP-016.
- Agents spécialisés (+ orchestrateur en reco) — CAP-019.
- Historique des décisions conservé — CAP-022.

## Point non décidé : operating-model.md

1. Proposition initiale : document `operating-model.md` dédié — CAP-043.
2. Évolution : **ne pas** en faire un standard ; répartir vers `architecture.md` + `workflow.md` — CAP-044.
3. État actuel : **découpage non définitivement décidé** (à trancher en review).
````
