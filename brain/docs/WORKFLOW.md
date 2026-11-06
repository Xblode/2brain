---
metadata_version: 1
title: "Méthode de travail"
type: guide
description: "Comment le projet fonctionne, évolue et est travaillé : flux réel de /brain, routeur, chaînons manquants."
summary: "Flux réel constaté de l'information (sources, Capture, registre, Search, Review, documents), rôle du routeur, règle d'évolution des documents sans perte, et chaînons qui manquent : Review ne consolide pas les documents, rien ne produit de prompts. Aucune roadmap validée."
version: "0.3.1"
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
  - "brain-main/ROUTER.md"
---

# Méthode de travail

## 1. Objet

Comment on travaille sur 2brain et comment l'information circule. Les commandes ne sont pas décrites ici : `brain-main/bootstrap/README.md` (§1 état, §2 commandes) en est la référence, et `brain-main/README.md` le guide court.

Étiquettes : `décision humaine`, `demande humaine` (dite par l'humain, sans validation formelle), `proposition non validée`, `question ouverte` ; pour l'état du système, `constaté` (avec le chemin) ou `déclaré par l'humain, non contrôlé`.

## 2. Flux réel

1. `constaté`. Porte d'entrée unique : `/brain` avec des options (`brain-main/bootstrap/README.md` §2). Le skill du compte aiguille vers `brain-main/skills/`.
2. `constaté`. Collecte : `/brain -c` extrait la session (`brain-main/skills/brain-capture/scripts/read-session.py`) puis l'ajoute au registre avec le skill de capture (`brain-main/skills/brain-capture/SKILL.md`). `/brain -c 1` annule la dernière capture (`brain-main/skills/brain-capture/scripts/rollback-captures.py`).
3. `constaté`. Registre : `brain/registry/entries.jsonl`, en ajout seul. Une capture n'est pas une décision : l'auteur, la validation et l'intention sont notés (`brain/registry/SCHEMA.md`).
4. `constaté`. Retrouver : `/brain -s` (`brain-main/skills/brain-search/scripts/search-registry.py`), lecture seule.
5. `constaté`. Contrôler : `/brain -r` (`brain-main/skills/brain-review/scripts/review-registry.py`) donne un rapport de doublons, contradictions, relations et manques. Il n'écrit rien.
6. `constaté`. Documents : `/brain -o` propose le contenu de `brain/docs/` et n'écrit qu'après validation de l'humain ; `/brain -a` audite un projet existant (`brain-main/skills/brain-audit/SKILL.md`).
7. `constaté`. Sync vers les outils externes : aucun script, il reste conceptuel (`AGENTS.md`).
8. `constaté`. Installation et mise à jour : `/brain -i` et `/brain -u` (`brain-main/bootstrap/README.md` §5 et §7). `déclaré par l'humain, non contrôlé` (2026-11-06) : `/brain -u` et `/brain -a` marchent très bien dans son projet.

## 3. Routeur

- `constaté`. Règles de délégation : `brain-main/ROUTER.md`. Application pour Claude Code : `.claude/README.md` et `.claude/agents/`. `/brain -d on|off` active ou retire la clé `agent` de `.claude/settings.json` (`brain-main/bootstrap/README.md` §2).
- `constaté`. Dans le dépôt, `.claude/settings.json` contient la clé `agent`.
- `déclaré par l'humain, non contrôlé` (2026-11-06) : le routeur fonctionne dans une nouvelle conversation. Le fonctionnement en session reste à confirmer selon `brain-main/bootstrap/README.md` §9.1.

## 4. Évolution des documents

- `demande humaine`. CAP-399 : « une nouvelle compréhension du projet doit pouvoir faire évoluer sa documentation sans détruire les traces des anciennes compréhensions ». Application dans `brain/docs/` : l'ancien texte est conservé tel quel dans une section **Ancienne synthèse**.
- `demande humaine`. CAP-408 : les nouvelles réflexions doivent « s'ajouter et poser les bonne question » plutôt qu'affirmer ou contredire les précédentes.
- `demande humaine`. CAP-417 : « cite les presque voir exactement comme elle sont écrire ». Les citations de ces documents suivent cette règle.
- `proposition non validée`. CAP-400 : distinguer idée initiale, précision, évolution, contradiction éventuelle et compréhension actuelle.
- Standard documentaire : `brain/docs/README.md` (verrouillé ; modifié le 2026-11-06, avec l'autorisation expresse de l'humain, pour ajouter `cadrage.md` comme sixième document standard, version 1.1.0).

## 5. Chaînons manquants

- `constaté`. Review ne consolide pas les documents : rapport seulement (`brain-main/bootstrap/README.md` §8.4). CAP-397 (observation de l'assistant) : « Un registre riche n'est pas une connaissance consolidée ». Aucun outil ne fait passer le registre aux documents ; c'est aujourd'hui un travail manuel, comme celui-ci.
- `constaté`. Rien ne produit de prompts. CAP-439 : « produire des prompts de qualité ». Aucun outil dans `brain-main/skills/`.
- `décision humaine` (2026-11-06, hors registre) : « AGENTS.md doit etre autorisé sans demande claire l'ia peut le faire sans demander, il doit lancer un agents haiku pour chercher dans le registre ». Règle écrite dans `AGENTS.md` (et dans le modèle `brain-main/bootstrap/templates/AGENTS.md`, `brain-main/README.md`, `brain-main/adapters/claude-code/agents/orchestrator.md`) : avant de proposer une implémentation, ou quand le sujet a pu être déjà traité, l'IA cherche dans le registre sans demander, par `worker-haiku` en lecture seule, ou elle-même sans routeur. C'est une règle, pas un contrôle automatique : rien ne vérifie qu'elle est suivie (CAP-452).
- `constaté`. Pas de `tasks.jsonl` ni de suivi de tâches (CAP-415) ; voir `brain/docs/INTEGRATIONS.md`.
- `constaté`. Pas d'aide au brainstorming (CAP-440).

## 6. Rythme de travail

- `demande humaine` (2026-11-06, hors registre) : gel des nouvelles commandes, avec une exception pour le contrôle des README au commit et pour `/brain -m`. Ces deux éléments sont construits et testés par scripts, installés sur le compte le 2026-11-06, non encore confirmés en session ; état : `brain-main/bootstrap/README.md` (§1, §6.4, §9.2). Le gel et son exception restent en vigueur.
- `question ouverte`. Définition du MVP : aucune n'a été validée. Une proposition de cheminement faite sur le test de reprise est restée sans validation.
- Les orientations de réalisation du cadrage (`brain/docs/CADRAGE.md` §19) ne constituent pas une roadmap validée.

## 7. Références

`brain-main/bootstrap/README.md`, `brain-main/README.md`, `brain-main/ROUTER.md`, `brain/docs/CADRAGE.md` (§7, §12, §13, §19), `brain/docs/README.md`.

## Ancienne synthèse

Texte d'origine, conservé tel quel dans le bloc ci-dessous (règle de l'humain, CAP-399 : rien ne se perd). Il date de la première synthèse provisoire. Les numéros `CAP-xxx` qu'il cite viennent de l'ancien registre de 69 captures et ne correspondent pas au registre actuel ; pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

````markdown
# Workflow

> **Provisoire** — synthèse légère issue de la capture. Détail : `brain/registry/entries.jsonl`.
> Sources : CAP-007, CAP-011, CAP-013–CAP-014, CAP-017–CAP-018, CAP-020, CAP-027–CAP-028, CAP-031, CAP-033, CAP-039, CAP-041, CAP-045–CAP-046, CAP-050–CAP-052, CAP-061.
> **Attention : références obsolètes.** Les `CAP-xxx` de ce document viennent de l'ancien registre de 69 captures (commit `45ba05d`). Le registre actuel réutilise ces numéros pour d'autres contenus : ne pas les y chercher. Pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

## Mode de travail (provisoire)

- Mode B/C : commandes + validation de ce qui entre dans le cadrage (pas chaque expérimentation) — CAP-007, CAP-011.
- ~10–15 commandes max — CAP-013.
- Chaîne Sources → Capture → Orchestrateur → Agents → Référentiel + ClickUp — CAP-014.
- Niveaux Capture / Organisation / Validation — CAP-061.
- Taxonomie Obs / Prop / Décision / Convention — CAP-020.

## Capture & review (provisoire)

- Capture auto sélective + consolidation — CAP-017 ; après chaque message pertinent — CAP-050.
- Capture → registres ; Review → docs sans supprimer ni empiler — CAP-039, CAP-041.
- Entrée référentiel = proposition de traitement + accord ; conflits challengés — CAP-018.
- Entretien continu de la mémoire — CAP-052.
- Ambiguïté signalée : review qui « valide certaines choses » vs validation explicite uniquement — CAP-051 ↔ CAP-028.

## Onboarding (provisoire)

- Progressif, sans remplir 10 docs d’un coup — CAP-027, CAP-028.
- `brain init` unique vs onboarding continu (proposition assistant) — CAP-033.
- Évolution docs : `onboarding.md` dédié (CAP-045) → plutôt chapitre de `workflow.md` (CAP-046) — **non décidé**.
````
