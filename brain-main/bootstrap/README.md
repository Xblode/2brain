---
metadata_version: 1
title: Bootstrap et commande /brain
type: specification
description: Spécifie la commande unique /brain, le rôle du Bootstrap qui l'orchestre, la détection d'un projet, l'installation et la mise à jour de 2brain, avec l'état réel de chaque commande.
summary: Une seule porte d'entrée, /brain, avec des options à une lettre. Le Bootstrap est un skill léger installé sur le compte Claude Code ; il détecte, diagnostique, récupère les ressources, prépare des propositions et coordonne les mécanismes existants, sans rien modifier sans validation humaine. Ce document est la référence unique des commandes et du Bootstrap. État réel : `/brain`, `-i` et `-u` sont construits et testés par scripts, pas encore installés sur le compte ; `-c`, `-s`, `-r` sont prévus au lot 3.
version: "0.2.0"
status: draft
created: "2026-11-05"
updated: "2026-11-05"
scope:
  level: universal
  targets: [brain-instances]
depends_on:
  - "brain-main/conventions/METADATA.md"
  - "brain-main/ROUTER.md"
tags:
  - bootstrap
  - commands
  - installation
---

# Bootstrap et commande /brain

Référence unique des commandes `/brain` et du Bootstrap. Il n'y a ni `COMMANDS.md` ni `BOOTSTRAP.md`. Les sections sont numérotées pour que les autres fichiers y renvoient.

**État réel (lot 2) :** le skill `/brain`, le hook de démarrage, les scripts de détection, de prévisualisation, d'installation et de mise à jour sont construits dans `brain-main/bootstrap/` et testés par scripts (`tests/run_bootstrap_tests.py`, dossiers temporaires). Ils ne sont pas encore installés sur le compte. Un test réel du 2026-11-05, avec une sonde, a confirmé dans l'onglet Code de Claude Code : le hook `SessionStart` en forme sans shell fonctionne et le skill reçoit `-i` dans `$ARGUMENTS` et `$0`. Les commandes `-c`, `-s`, `-r` restent à construire (lot 3).

## 1. État par commande

| Commande | Fonction | État | Lot |
| --- | --- | --- | --- |
| `/brain` | État du projet et aide | construit et testé par scripts, à installer sur le compte | 2 |
| `/brain -i` | Installation (analyse, questions, prévisualisation, installation) | construit et testé par scripts, à installer sur le compte | 2 |
| `/brain -u` | Mise à jour de `brain-main/` | construit et testé par scripts, à installer sur le compte | 2 |
| `/brain -c` | Capture de la session | prévu | 3 |
| `/brain -c <fichier>` | Capture d'une source externe | prévu | 3 |
| `/brain -c 1` | Annulation de la dernière capture | prévu | 3 |
| `/brain -s <sujet>` | Recherche | prévu | 3 |
| `/brain -r` | Review en rapport seulement | prévu | 3 |

Pour `-c`, le mécanisme de capture existe déjà : `brain-main/skills/brain-capture/`. En attendant la commande, il s'utilise en lisant `brain-main/skills/brain-capture/SKILL.md`.

## 2. Commandes

Une seule porte d'entrée : `/brain`. Une option = un tiret plus une lettre. Cette syntaxe remplace `/brain u`, `/brain-capture c` et `/brain-main u`.

- `/brain` : état du projet et aide. Lecture seule.
- `/brain -i` : analyse du projet, questions d'accueil, prévisualisation, puis installation après validation. Questions : nature du projet, objectif, modules, outils, identité. Une réponse manquante ne bloque pas. La réponse sur les modules note seulement une intention.
- `/brain -u` : met à jour `brain-main/` uniquement, après validation (voir section 7).
- `/brain -c` : capture la session. `/brain -c <fichier>` : capture une source externe. `/brain -c 1` : annule la dernière capture.
- `/brain -s <sujet>` : recherche par mots et filtres. Lecture seule.
- `/brain -r` : Review en rapport seulement (doublons, contradictions, relations, manques). Elle ne modifie ni le registre ni les documents.

## 3. Rôle du Bootstrap

Le Bootstrap est un skill léger installé sur le compte Claude Code. C'est un orchestrateur, pas un générateur.

Il fait :

- détecter l'état du projet ;
- reconnaître les commandes ;
- diagnostiquer ;
- récupérer les ressources nécessaires ;
- préparer les propositions ;
- coordonner les mécanismes spécialisés.

Il ne fait pas :

- contenir une copie des conventions ;
- générer lui-même `brain/` ;
- modifier quoi que ce soit sans validation humaine ;
- dupliquer les autres mécanismes.

Il signale une version plus récente de lui-même, car `/brain -u` ne met pas à jour ce qui est installé sur le compte.

## 4. Détection

| Situation | Comportement |
| --- | --- |
| Dossier strictement vide, sans 2brain | Proposer l'installation dans la première réponse (Claude ne parle pas avant le premier message de l'utilisateur) |
| Uniquement `.git/` | Traité comme un dossier vide |
| Projet avec des fichiers | Aucune proposition automatique ; `/brain -i` reste possible |
| `brain-main/` et/ou `brain/` présents | Détecter leur état (complet, partiel, ancien) |

Phrase exacte de la proposition : « Avant de commencer, souhaites-tu installer 2brain dans ce projet ? »

La détection repose sur un hook `SessionStart`, au démarrage de la session seulement. Ce n'est pas une fenêtre de confirmation bloquante : le hook ajoute une consigne au contexte, et la première réponse de la session demande l'accord. Le hook ne parle que si la session démarre (`source` = `startup`) dans un dossier sans aucune entrée ou contenant seulement `.git` ; sinon il ne dit rien, même si `brain-main/` est présent. Comportement confirmé par le test réel du 2026-11-05.

En cas de refus : continuer normalement, ne pas reposer la question dans la session. Une nouvelle proposition reste possible dans une session ultérieure.

## 5. Installation

L'installation suit cinq phases.

- **A. Diagnostic.** État du dossier et de 2brain.
- **B. Récupération.** Seules les ressources nécessaires sont récupérées depuis `Xblode/2brain`, branche `master`. Pas de clone aveugle.
- **C. Préparation.** Racine par défaut, arborescence, dossier `EMPLACEMENT/` à la racine du projet. Ce n'est qu'une prévisualisation.
- **D. Validation humaine explicite.** Emplacement, arborescence, fichiers créés, conflits, adaptations.
- **E. Installation.** Création de `brain-main/`, puis de `brain/` généré à partir de `brain-main/`. Contrôle de cohérence. Les fichiers existants sont préservés. Bilan final.

Après un « oui », l'utilisateur tape `/brain -i` (Claude ne peut pas lancer la commande lui-même, le skill étant à invocation manuelle). `EMPLACEMENT/` est supprimé en cas de refus. Si un conflit apparaît après la validation, l'installation est suspendue et l'accord est redemandé.

### 5.1. Scripts

Appelés par le skill avec `python -I`, un fichier par script, bibliothèque standard seulement, sortie JSON. `fetch-source.py` récupère `brain-main/` dans un dossier temporaire ; `prepare-install.py` crée `EMPLACEMENT/` (copie prévue, `plan.json`, marqueur `.2brain-emplacement`) et imprime `plan_sha256` ; `apply-install.py --plan-sha256` installe seulement si le plan et l'arborescence correspondent et si aucun conflit n'est apparu (code 4 sinon), écrit `brain-main/manifest.json` (version, commit source, date, SHA-256 par fichier) et supprime `EMPLACEMENT/` ; `cancel-install.py` supprime `EMPLACEMENT/` seulement avec son marqueur. `AGENTS.md` n'est créé que s'il est absent. Le modèle de `brain/` est dans `templates/brain/`.

## 6. Séparation de `brain-main/` et `brain/`

- `brain-main/` : socle réutilisable (conventions, skills, bootstrap).
- `brain/` : contenu propre au projet (documents, registre).

`brain/` n'est jamais remplacé par une mise à jour de `brain-main/`. Le Bootstrap coordonne ; il ne produit pas les fichiers propres au projet.

## 7. Mise à jour

`/brain -u` s'appuie sur `master` et ne touche que `brain-main/`.

1. Comparer les versions.
2. Identifier les fichiers nouveaux, modifiés et supprimés.
3. Repérer les conflits par empreintes, fichier par fichier.
4. Présenter le résultat.
5. Obtenir une validation explicite.
6. N'écraser aucune modification locale.

Une adaptation éventuelle de `brain/` est signalée et proposée à part. `/brain -u` refuse de s'exécuter dans le dépôt source 2brain.

`update-brain-main.py` compare le manifeste, le local et la source fichier par fichier, imprime un plan (sans écrire) puis, avec `--apply --plan-sha256`, applique sans jamais écraser un conflit.

## 8. Capture

`/brain -c` alimente le mécanisme existant (`brain-main/skills/brain-capture/`) sans le dupliquer. Il distingue l'utilisateur, l'agent et les outils. Il préserve l'auteur, la provenance et les nuances d'intention et de validation. Il évite les blocs entiers et les doublons.

Capturer et réduire le contexte sont deux choses différentes : la capture ne lance jamais `/compact`.

## 9. Structure, compte et limites

```
brain-main/bootstrap/
  VERSION                 version du Bootstrap
  account/                part sur le compte (SKILL.md, session-start.py, status.py, fetch-source.py)
  scripts/                arrivent avec brain-main/ (install-account, prepare-install, apply-install, cancel-install, update-brain-main)
  templates/brain/        modèle du brain/ d'un projet ; templates/AGENTS.md
  tests/run_bootstrap_tests.py
```

- **Emplacement sur le compte :** `~/.claude/skills/brain/` (skill, hook, scripts légers, `VERSION`), un groupe `hooks.SessionStart` (matcher `startup`, sans shell) dans `~/.claude/settings.json`, sauvegardes dans `~/.claude/2brain-bootstrap/backups/`. Installation : `python scripts/install-account.py` (options `--home`, `--dry-run`, `--uninstall`, `--replace-probe`).
- **Retrait :** `install-account.py --uninstall` retire seulement son groupe de hooks et son dossier skill, et garde les sauvegardes.
- **Prérequis :** Python 3 (bibliothèque standard seulement). Le chemin absolu de Python est écrit dans le skill et dans le hook à l'installation.
- **Orchestrateur du dépôt 2brain :** il n'a ni Bash, ni Write, ni Edit. `/brain` s'y exécute, mais les commandes sont déléguées à l'agent `worker-sonnet`. Les installations et mises à jour sont refusées dans le dépôt source.
- **Limite actuelle :** le dépôt GitHub ne contient pas le Bootstrap tant qu'il n'est pas poussé. `/brain -i` et `/brain -u` depuis GitHub échouent jusque-là, avec un message explicite de `fetch-source.py`.

## 10. Provenance

Aucune des captures ci-dessous n'est validée (`validation: none`). Elles sont citées telles qu'écrites dans `brain/registry/entries.jsonl`.

- **CAP-052**, question ouverte « Q activation modules / updates / phrase » : l'assistant recommande notamment des updates Brain-main proposées sans auto-apply.
- **CAP-056**, orientation de l'utilisateur « Updates modules : auto Brain-main ; local-only non ». Ce document la fait évoluer vers une validation explicite : décision de l'humain du 2026-11-05. La capture n'est pas écrasée et reste dans le registre telle quelle.
- **CAP-051**, suggestion « brain init = onboarding intelligent progressif » : source des questions d'accueil.
- **CAP-061**, convention proposée « brain init ≠ onboarding continu ».
- **CAP-030**, suggestion « Proposition table ~11 commandes brain * », non définitive.
- **CAP-181**, orientation « Modules : tout noter ; décisions plus tard via recherche thématique ».

Les décisions de ce document viennent de la validation de l'humain du 2026-11-05. Le registre n'a pas été modifié.
