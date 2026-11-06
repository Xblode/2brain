---
metadata_version: 1
title: "Intégrations"
type: reference
description: "Services externes et interconnexions de 2brain : GitHub, registre, ClickUp, skills externes, avec l'état réel de chacun."
summary: "Relation entre GitHub, registre local et ClickUp d'après l'arbitrage du 2026-11-05 et le registre ; règle d'Inbox ancienne et son évolution, tranchée le 2026-11-06 (une Inbox ClickUp et une Inbox locale, sans synchronisation, rien de construit) ; tasks.jsonl décidé mais inexistant ; aucune convention ClickUp. La tension avec CAP-187 est tranchée pour l'Inbox seulement."
version: "0.3.0"
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
  - "brain/conventions/README.md"
---

# Intégrations

## 1. Objet

Ce que 2brain relie à l'extérieur et comment, sans recopier le détail du registre. Aucune convention ClickUp n'existe (`brain/conventions/README.md`) : ce document n'en invente aucune.

Étiquettes : `décision humaine` (validée explicitement), `demande humaine` (dite par l'humain, sans validation formelle), `proposition non validée`, `question ouverte` ; pour l'état du système, `constaté` (avec le chemin) ou `déclaré par l'humain, non contrôlé`.

## 2. GitHub, registre, ClickUp

- `décision humaine` (plan du 2026-11-05, hors registre) : « Git/code = état réel, registre = ce qui a été dit et décidé, docs = connaissance consolidée, ClickUp = vue ».
- `demande humaine`. CAP-443 : GitHub « restera toujours une source de vérité » ; il ne faut pas « enlever quelque chose qui est push ».
- `constaté`. `/brain -i` et `/brain -u` téléchargent `brain-main/` depuis le dépôt GitHub Xblode/2brain, branche `master` (`brain-main/bootstrap/README.md` §5 et §7).
- `constaté`. Il n'y a ni script de synchronisation ni écriture vers ClickUp : Sync reste conceptuel (`AGENTS.md`).

## 3. ClickUp

- `décision humaine`. CAP-071 (validation explicite) : structure « déjà définie » : « List Inbox (idées hors chatbot, 1 tâche/idée) » ; les listes Cadrage et Roadmap y figurent aussi. Cette structure est décrite dans le registre, non dans une convention.
- `décision humaine`. CAP-220 : « Review prépare d'abord les éléments localement et attend une validation avant toute création dans ClickUp », la validation étant faite par Sync.
- `proposition non validée`. CAP-211 : conserver une correspondance entre identifiant local et identifiant ClickUp.
- `constaté`. Aucune convention ClickUp d'instance : `brain/conventions/README.md` indique qu'aucun fichier n'est présent. À ne pas inventer.

## 4. Inbox : règle ancienne et évolution

- Règle ancienne, texte d'origine de cette page (section **Ancienne synthèse**, ancien registre) : « pas d'inbox registre local miroir ».
- Même règle dans le registre actuel. `demande humaine`, CAP-086 : « Inbox ClickUp = notes externes ; pas d'inbox locale ». `proposition non validée`, CAP-100 : « Inbox ClickUp = source externe de capture ».
- Évolution. `demande humaine`, CAP-401 : « Second Brain doit pouvoir utiliser l'Inbox, boîte d'arrivée des tâches avant qu'elles aillent dans une tâche maîtresse ». La capture dit que c'est une règle révisée par rapport à CAP-086, et que « Brain Review s'en occupera probablement ».
- CAP-418 (observation de l'assistant) : « La nouvelle conception d'Inbox évolue ces règles sans effacer CAP-086 ni CAP-100 ». Les deux versions sont donc conservées ici sans être départagées au-delà de CAP-401.
- `décision humaine` (2026-11-06, hors registre) : « Pour l'linbox les deux vive de leur coté ». Une Inbox existe dans ClickUp et une Inbox locale, chacune de son côté, sans synchronisation entre elles. Elle répond à la question du lieu, qu'aucune capture ne tranchait. Rien n'est construit : l'Inbox locale et le format de `tasks.jsonl` restent à construire.

## 5. Tension possible à lire

CAP-187 (`demande humaine`, `validation: none`) : « tout le contenu qui finira dans ClickUp doit avoir son équivalent en local » et « Le local est toujours la source de vérité (SoT) ». Mise en regard : CAP-086 (« pas d'inbox locale »), CAP-401 (Inbox utilisable par Second Brain, lieu non précisé) et l'arbitrage du 2026-11-05 (ClickUp = vue). Pour l'Inbox seulement, la tension entre CAP-187, CAP-086 et CAP-401 est tranchée par la décision de l'humain du 2026-11-06 (§4) : deux Inbox, ClickUp et locale, chacune de son côté, sans synchronisation ; le reste du contenu ClickUp n'est pas concerné par cette décision.

## 6. Registre de tâches : tasks.jsonl

- `décision humaine`. CAP-415 : « le fichier tasks.jsonl sera créé en même temps que Brain Review ».
- `constaté`. Ce fichier n'existe pas : `brain/registry/` contient `entries.jsonl` et `SCHEMA.md` (et des dossiers de travail de la capture). Review actuelle ne produit qu'un rapport (`brain-main/skills/brain-review/scripts/review-registry.py`).
- `question ouverte`. Contenu, format et rôle de `tasks.jsonl`, et son lien avec l'Inbox (CAP-401, décision du 2026-11-06 : Inbox locale distincte de celle de ClickUp, sans synchronisation) et ClickUp : non définis. CAP-254 (convention proposée par l'assistant) fait capturer les tâches sans créer d'objets ClickUp.

## 7. Autres outils

- `demande humaine`. CAP-470 : six skills externes retenus comme « sources », à intégrer au workflow en évitant de « faire la même choses qu'eux ». CAP-476 (`proposition non validée`) : ne pas les intégrer tous tout de suite. `constaté` : aucune intégration dans le dépôt.
- `demande humaine`. CAP-471 : s'inspirer de Graphify, « je pense pas l'intégrer dans mon projet ».
- `constaté`. Claude Code est le seul outil dont l'adaptateur existe (`brain-main/adapters/claude-code/`). L'indépendance vis-à-vis d'un fournisseur est visée par le cadrage (`brain/docs/CADRAGE.md` §5.5).

## 8. Références

`brain/registry/entries.jsonl` (CAP-071, 086, 100, 187, 211, 220, 254, 401, 415, 418), `brain/conventions/README.md`, `brain/docs/CADRAGE.md`.

## Ancienne synthèse

Texte d'origine, conservé tel quel dans le bloc ci-dessous (règle de l'humain, CAP-399 : rien ne se perd). Il date de la première synthèse provisoire. Les numéros `CAP-xxx` qu'il cite viennent de l'ancien registre de 69 captures et ne correspondent pas au registre actuel ; pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

````markdown
# Integrations

> **Provisoire** — synthèse légère issue de la capture. Détail : `brain/registry/entries.jsonl`.
> Sources : CAP-003, CAP-005, CAP-008, CAP-035–CAP-036, CAP-038, CAP-040, CAP-053–CAP-055.
> **Attention : références obsolètes.** Les `CAP-xxx` de ce document viennent de l'ancien registre de 69 captures (commit `45ba05d`). Le registre actuel réutilise ces numéros pour d'autres contenus : ne pas les y chercher. Pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

## Local vs ClickUp (provisoire)

- Local (`brain/`) = source de vérité (JSONL/SQL) — CAP-003, CAP-008.
- ClickUp = interface humaine / visualiseur synchronisé — CAP-008.
- Mapping espaces ↔ listes ClickUp proposé — CAP-040.

## Structure ClickUp projet (déjà définie)

Sous dossier projet : `docs` / `Inbox` / `Cadrage` / `Roadmap` — CAP-038.

- **Inbox** : notes manuelles externes ; pas d’inbox registre local miroir — CAP-054.
- **Roadmap** : hiérarchie jalons / sous-tâches pour idées validées non encore codées — CAP-053.
- **Cadrage (7)** et **Roadmap (6)** : déjà créés manuellement — **référencés seulement**, non recréés ici — CAP-035, CAP-036, CAP-055.

> Aucune écriture ClickUp effectuée pendant cette capture.
````
