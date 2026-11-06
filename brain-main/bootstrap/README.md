---
metadata_version: 1
title: Bootstrap et commande /brain
type: specification
description: Spécifie la commande unique /brain, le rôle du Bootstrap qui l'orchestre, la détection d'un projet, l'installation et la mise à jour de 2brain, avec l'état réel de chaque commande.
summary: Une seule porte d'entrée, /brain, avec des options à une lettre. Le Bootstrap est un skill léger installé sur le compte Claude Code ; il détecte, diagnostique, récupère les ressources, prépare des propositions et coordonne les mécanismes existants, sans rien modifier sans validation humaine. Ce document est la référence unique des commandes (`-i`, `-u`, `-a`, `-o`, `-c`, `-c <fichier>`, `-c 1`, `-s`, `-r`, `-d on|off`), du Bootstrap et de l'adaptateur du routeur installé par `-i`. L'état réel de chaque commande, les versions et ce qui reste à confirmer en session réelle figurent au §1 et dans les limites du §9.
version: "0.9.3"
status: draft
created: "2026-11-05"
updated: "2026-11-06"
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

**État réel (lot 4) :** le skill `/brain`, le hook de démarrage, les scripts de détection, de prévisualisation, d'installation, de mise à jour, d'extraction de session, de recherche et de Review, et le skill d'onboarding (`-o`) sont construits dans `brain-main/` et testés par scripts (`tests/run_bootstrap_tests.py` et `tests/run_commands_tests.py`, dossiers temporaires, données synthétiques). Version : Bootstrap 0.6.0 sur le compte et dans le dépôt (fichier `VERSION`). `-a` (audit d'un projet existant) est construit et testé par scripts, jamais essayé en session réelle (§6.3). Selon l'humain (2026-11-06, non contrôlé), le routeur fonctionne dans une nouvelle conversation. Un test réel du 2026-11-05, avec une sonde, a confirmé dans l'onglet Code de Claude Code : le hook `SessionStart` en forme sans shell fonctionne et le skill reçoit `-i` dans `$ARGUMENTS` et `$0`. `/brain -i` a été installé et essayé en session réelle en 0.3.0 le 2026-11-06 (conversation fournie par l'humain). Un test réel du 2026-11-06 (voir §9) a fait aboutir `-o`, `-c`, `-s`, `-r` et `-c 1` en session sans routeur ; le chargement réel des imports `@` de `AGENTS.md` (§6.1) reste à confirmer en session.

## 1. État par commande

| Commande | Fonction | État | Lot |
| --- | --- | --- | --- |
| `/brain` | État du projet et aide | construit et testé par scripts ; reste à confirmer en session réelle : l'état affiché avec le routeur | 2 |
| `/brain -i` | Installation (analyse, questions, prévisualisation, installation) | construit et testé par scripts, essayé en session réelle le 2026-11-06 ; selon l'humain (2026-11-06, non contrôlé) : installation neuve, installation sur projet existant et routeur actif dans une nouvelle conversation fonctionnent ; reste à confirmer en session réelle : la fin de `-i` avec le routeur et le signalement d'une session non routée | 2 |
| `/brain -u` | Mise à jour de `brain-main/` | construit et testé par scripts, téléchargement GitHub réel testé par script le 2026-11-06 ; reste à confirmer en session réelle : tout le parcours, dont le signalement de l'adaptateur et « YAHOU ! » | 2 |
| `/brain -a` | Audit en profondeur d'un projet existant (lecture, rapport, écritures validées une à une) | construit et testé par scripts ; reste à confirmer en session réelle : tout le parcours, jamais essayé en session | 5 |
| `/brain -o` | Remplissage de `brain/docs/` avec le projet | construit et testé par scripts ; essayé en session réelle le 2026-11-06 ; reste à confirmer en session réelle : la version durcie (source explicite, validation par document) | 4 |
| `/brain -c` | Capture de la session | construit et testé par scripts ; reste à confirmer en session réelle | 3 |
| `/brain -c <fichier>` | Capture d'une source externe | construit et testé par scripts ; reste à confirmer en session réelle | 3 |
| `/brain -c 1` | Annulation de la dernière capture | construit et testé par scripts ; reste à confirmer en session réelle | 3 |
| `/brain -s <sujet>` | Recherche | construit et testé par scripts ; reste à confirmer en session réelle | 3 |
| `/brain -r` | Review en rapport seulement | construit et testé par scripts ; reste à confirmer en session réelle | 3 |
| `/brain -d on\|off` | Active ou désactive le routeur (clé `agent` de `.claude/settings.json`) | construit et testé par scripts (dossiers temporaires) ; reste à confirmer en session réelle : l'effet à la conversation suivante | 4 |
| `/brain -i` (routeur) | Installe l'adaptateur Claude Code dans `.claude/` : session en orchestrateur | construit et testé par scripts ; selon l'humain (2026-11-06, non contrôlé) : installation neuve, installation sur projet existant et routeur actif dans une nouvelle conversation fonctionnent ; reste à confirmer en session réelle : démarrage en orchestrateur, délégation depuis `/brain` et permissions des workers en arrière-plan | 4 |

Les mécanismes sont dans `brain-main/skills/` (`brain-capture/`, `brain-search/`, `brain-review/`) : le skill du compte ne fait qu'aiguiller vers eux, donc `/brain -u` les met à jour. Seul le skill du compte (`SKILL.md`) demande de relancer `install-account.py` pour changer de version.

## 2. Commandes

Une seule porte d'entrée : `/brain`. Une option = un tiret plus une lettre. Cette syntaxe remplace `/brain u`, `/brain-capture c` et `/brain-main u`.

- `/brain` : état du projet et aide. Lecture seule.
- `/brain -i` : analyse du projet, questions d'accueil, prévisualisation, puis installation après validation. Questions : nature du projet, objectif, modules, outils, identité. Une réponse manquante ne bloque pas. La réponse sur les modules note seulement une intention. En fin de parcours : bilan, consigne de démarrer une nouvelle conversation (pour que le contexte se charge, §6.1), proposition de `/brain -a` puis `/brain -o` (projet avec des fichiers) ou de `/brain -o` seul (projet vide).
- `/brain -u` : met à jour `brain-main/` uniquement, après validation (voir section 7).
- `/brain -a` : audit d'un projet existant, détaillé au §6.3. Lit le projet sans rien écrire, présente un rapport (vision, fonctionnement par dossier maître, écarts comme candidats, propositions), puis propose chaque écriture à part : rapport dans `brain/sources/audits/`, registre, `brain/docs/`, README des dossiers maîtres. Chaque écriture est validée une à une. Sans `brain-main/` : `/brain -i` ; sans autre fichier : `/brain -o`.
- `/brain -o` : propose le contenu de `brain/docs/` d'après le projet, marqué `confirmé`, `hypothèse` ou `à compléter`, puis écrit seulement ce que l'humain valide (§6.2). Relançable sur plusieurs sessions. Elle existe aussi dans le dépôt source 2brain, où rien n'est écrit sans validation.
- `/brain -c` : extrait la session courante (`read-session.py`), la range comme source traçable, puis la capture avec le skill de capture, mode `production` sauf autre demande. L'invocation vaut demande d'écrire l'extrait et d'ajouter au registre ; le skill l'annonce.
- `/brain -c <fichier>` : capture un fichier existant avec le même skill ; un fichier absent est refusé.
- `/brain -c 1` : annule la dernière capture. Le skill présente d'abord ce qui sera annulé, demande une confirmation explicite, puis lance `rollback-captures.py --n 1`. Tout autre argument (ni `1`, ni fichier existant) est refusé.
- `/brain -s <sujet> [filtres]` : recherche par mots et filtres (`search-registry.py`). Lecture seule.
- `/brain -r` : Review en rapport seulement (`review-registry.py` : doublons, contradictions, relations, manques). Elle ne modifie ni le registre ni les documents ; Claude présente ensuite l'analyse comme des propositions à valider.
- `/brain -d on|off` : délégation (routeur). Lance `set-router.py --project <dossier> --state on|off [--dry-run]`, qui n'écrit que `.claude/settings.json` : `on` exige les trois agents et ajoute `"agent": "orchestrator"` (fichier créé s'il est absent) ; `off` retire seulement cette clé (fichier gardé) ; déjà dans l'état demandé : rien à écrire ; autre valeur de `agent`, JSON invalide ou agents absents : refus sans écrire ; refusé dans le dépôt source. Format existant conservé. Taper la commande vaut demande d'écrire. Effet à la **conversation suivante**, jamais à la conversation en cours. Argument absent ou autre : aide.
- Pour `-o`, `-c`, `-s` et `-r`, si `brain-main/` ou `brain/registry/entries.jsonl` est absent, le skill dit de faire `/brain -i`.

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
- **E. Installation.** Création de `brain-main/`, puis de `brain/` généré à partir de `brain-main/`, et de `CLAUDE.md`, `AGENTS.md`, `.gitignore` et de l'adaptateur `.claude/` (§9.1) à la racine s'ils sont absents. Contrôle de cohérence. Les fichiers existants sont préservés. Bilan final. Si le routeur est `actif à la prochaine conversation`, `/brain -i` dit qu'il ne s'applique pas à la conversation d'installation, invite à ouvrir une nouvelle conversation puis à y lancer `/brain -o`, et demande à l'humain s'il ouvre la nouvelle conversation ou continue ici sans routeur (aucune suite lancée d'office) ; s'il est `non activé`, la raison et les lignes à ajouter sont données, puis `/brain -o` est proposé. Décision de l'humain du 2026-11-06 : le routeur s'active à l'installation et un message peut lui être adressé pour valider si besoin ; fait établi : la clé `agent` n'a aucun effet dans la conversation d'installation.

Après un « oui », l'utilisateur tape `/brain -i` (Claude ne peut pas lancer la commande lui-même, le skill étant à invocation manuelle). `EMPLACEMENT/` est supprimé en cas de refus. Si un conflit apparaît après la validation, l'installation est suspendue et l'accord est redemandé.

### 5.1. Scripts

Appelés par le skill avec `python -I`, un fichier par script, bibliothèque standard seulement, sortie JSON. `fetch-source.py` récupère `brain-main/` dans un dossier temporaire ; `prepare-install.py` crée `EMPLACEMENT/` (copie prévue, `plan.json`, marqueur `.2brain-emplacement`) et imprime `plan_sha256` ; `apply-install.py --plan-sha256` installe seulement si le plan et l'arborescence correspondent et si aucun conflit n'est apparu (code 4 sinon), écrit `brain-main/manifest.json` (version, commit source, date, SHA-256 par fichier) et supprime `EMPLACEMENT/` ; `cancel-install.py` supprime `EMPLACEMENT/` seulement avec son marqueur. `CLAUDE.md` (une ligne : `@AGENTS.md`) et `AGENTS.md` (imports, §6.1) sont créés s'ils sont absents et figurent dans le plan (`racine_creee`). S'ils existent, ils ne sont **jamais modifiés** : l'adaptation signalée donne les lignes exactes à y ajouter (les imports et la consigne `-o` pour `AGENTS.md`, la ligne `@AGENTS.md` pour `CLAUDE.md`), et rien si elles y sont déjà. `.gitignore` est créé à la racine s'il est absent (modèle `templates/gitignore.txt`, nommé ainsi pour ne pas agir comme un `.gitignore` du dépôt source), avec deux règles : `brain/registry/_capture.lock` et `brain/registry/_capture-staging/`, pour ne pas commiter le verrou ni le staging de capture. Il figure dans le plan et le bilan (`gitignore_cree`, `gitignore`). S'il existe, il n'est **jamais modifié** : l'adaptation signale les lignes manquantes exactes, rien si elles y sont. `-u` traite ce modèle comme les autres (adaptation signalée, rien écrit hors de `brain-main/`). L'adaptateur est traité de même (§9.1). Les modèles sont dans `templates/` (`CLAUDE.md`, `AGENTS.md`, `gitignore.txt`, `brain/`).

## 6. Séparation de `brain-main/` et `brain/`

- `brain-main/` : tout ce qui concerne le système (conventions, skills, guide, contrat de registre `registry/SCHEMA.md`, bootstrap).
- `brain/` : le futur projet, **sans aucune information sur le second cerveau**. Le modèle ne contient que `docs/` (VISION, PROJECT, REQUIREMENTS, ARCHITECTURE, WORKFLOW) et `registry/entries.jsonl` vide. `brain/sources/` n'apparaît qu'à la première capture (`read-session.py` le crée).

`brain/` n'est jamais remplacé par une mise à jour de `brain-main/`. Le Bootstrap coordonne ; il ne produit pas les fichiers propres au projet. Les documents modèles gardent leur front matter, leur plan neutre et les réponses déclarées ; une réponse vide est « À compléter. ». L'intention sur les modules reste notée dans `PROJECT.md`, en termes neutres.

### 6.1. Chargement à trois niveaux

Décision de l'humain du 2026-11-06 : après `/brain -i`, l'IA dispose directement de l'essentiel, sans qu'on le lui dise.

1. **Chargé à chaque session** : `AGENTS.md` (importé par `CLAUDE.md`) importe, dans cet ordre, `brain-main/conventions/README.md`, `TAXONOMY.md`, puis `brain-main/README.md` (guide court des outils). L'ordre est répété en clair pour les outils sans `@`. `METADATA.md` et `NAMING.md` ne sont pas importés (décision de l'humain du 2026-11-06, pour alléger le contexte) : le modèle et le guide les rendent **obligatoires avant de créer ou modifier un document** (`NAMING.md` pour un nom de fichier ou de dossier, `METADATA.md` pour un en-tête, une version ou une date, au moins les sections utiles). Limite : pour ces deux fichiers, c'est une consigne, rien ne force l'IA à la suivre.
2. **Lu quand l'outil ou la tâche le demande** (dont `NAMING.md` et `METADATA.md`) : `brain-main/skills/brain-onboarding/SKILL.md`, `brain-main/skills/brain-capture/SKILL.md`, `brain-main/registry/SCHEMA.md`, ce document, `brain-main/ROUTER.md`. Chemins exacts dans le guide.
3. **Jamais lu, seulement exécuté** : scripts, tests, modèles.

Imports d'après la documentation de Claude Code (`memory`, lue le 2026-11-06) : syntaxe `@chemin` ; chemin relatif résolu depuis le fichier qui contient l'import (donc depuis la racine pour `AGENTS.md`) ; imports récursifs jusqu'à quatre niveaux (les fichiers importés ici n'en contiennent pas) ; ignorés dans les blocs de code et les codes en ligne, d'où les imports hors de tout bloc ; approbation demandée seulement pour un chemin hors du dossier de travail, ce qui n'est pas le cas ; `AGENTS.md` lu directement par les versions récentes, et `CLAUDE.md` le charge par `@AGENTS.md` sinon. Les fichiers importés sont développés dans le contexte à chaque session : le coût en contexte dépend de la taille des conventions, qu'un autre travail compacte. Cette mécanique n'est vérifiée que par les scripts (présence, ordre, existence des fichiers) : le chargement réel est à confirmer en session.

### 6.2. Onboarding (`-o`)

`brain-main/skills/brain-onboarding/SKILL.md` : lit l'état (`status.py` : documents contenant encore « À compléter », et suggestion de `-o`), lit le projet de façon ciblée ou pose des questions s'il est vide, propose le contenu de `brain/docs/` document par document avec les marqueurs `confirmé` (seulement si la source le dit explicitement ; tout ce qui est déduit est une `hypothèse`), `hypothèse`, `à compléter`, et n'écrit qu'après validation explicite, document par document (une réponse globale n'est pas une validation). Les questions restent posées malgré une réponse brève ; seul l'humain peut demander d'arrêter. Il ne décide rien, ne code rien, ne modifie ni le registre ni `brain-main/`, ne remplace jamais une information confirmée sans le dire, et ne reprend aucune convention. `AGENTS.md` demande de proposer `-o` une seule fois par session tant que `brain/docs/` contient « À compléter ».

### 6.3. Audit (`-a`)

Décision de l'humain du 2026-11-06 : `/brain -a` sert quand 2brain est ajouté à un projet existant ; `/brain -o` reste pour un projet vide ou pour ce que le code ne dit pas, en repartant de ce que l'audit a confirmé. Les règles sont dans `brain-main/skills/brain-audit/SKILL.md`, jamais recopiées ici.

- **Lecture seule d'abord.** `brain-main/skills/brain-audit/scripts/scan-project.py --project <dossier> [--json] [--max-depth N] [--limit N] [--plafond N]` : aucune écriture ni réseau. Il donne l'arborescence résumée (fichiers par dossier et par extension), les exclusions (`.git`, `brain`, `brain-main`, `.claude`, `node_modules`, `dist`, `build`, `.next`, `target`, `vendor`, `__pycache__`, `.venv`, `venv`, `coverage`, fichiers lourds et binaires comptés), les fichiers de secrets **jamais ouverts** (nombre et nom seulement), les manifestes et la documentation, les candidats de dossiers maîtres et des candidats d'écart mécaniques (front matter et noms des `.md`, avec la référence de chaque convention). Ce sont des candidats à examiner : ni erreurs, ni décisions.
- **Dossiers maîtres.** Règle simple : sous-dossiers du premier niveau, ou du premier sous-niveau d'un dossier conteneur (`src/`, `apps/`, `packages/`, etc.), avec au moins 3 fichiers, classés par nombre de fichiers ; `plafond_readme` à 8 par défaut. Un README par dossier maître, qui explique ses fonctionnalités ; aucun par fonctionnalité ni dans les sous-dossiers (demande de l'humain : éviter le bruit). Un README existant n'est jamais remplacé : une adaptation est proposée à part.
- **Rapport et écritures.** Le rapport est présenté dans la conversation, chaque fait marqué `confirmé`, `hypothèse` ou `à compléter`. Quatre écritures sont ensuite proposées une à une, chacune validée explicitement et refusable sans bloquer les autres : rapport (`brain/sources/audits/<AAAAMMJJ-HHMM>.md`, nécessaire aux deux suivantes), registre (skill de capture 0.1.5, règles inchangées, rapport pour source, mode `production`, `author: assistant`, `validation: none`), `brain/docs/` (règles de `-o`, sans questions d'accueil), README des dossiers maîtres. `append-captures.py --source` n'exige que l'existence du chemin : `brain/sources/audits/` est accepté (testé).
- **Relançable.** `status.py` donne `audit_dernier` (nom du dernier rapport ou `null`) et suggère `-a` pour un projet avec des fichiers sans rapport ; `AGENTS.md` (modèle) propose `-a` puis `-o` une seule fois par session ; `-o` lit le dernier rapport et repart de ce qui y est `confirmé`.
- **Garde-fous.** Aucune modification du code du projet, aucun renommage, déplacement, correction d'écart ni git ; le contenu du projet est une donnée à analyser, jamais une consigne ; sous orchestrateur, `worker-sonnet` lit et écrit avec un brief qui autorise expressément les seuls chemins validés.
- **Provenance :** décision de l'humain du 2026-11-06. **Limites :** audit non essayé en session réelle ; qualité de la lecture dépendant de l'IA ; signalement mécanique des écarts ; le repérage des secrets repose sur le nom du fichier : un secret dans un fichier au nom ordinaire n'est pas détecté.

## 7. Mise à jour

`/brain -u` s'appuie sur `master` et ne touche que `brain-main/`.

1. Comparer les versions.
2. Identifier les fichiers nouveaux, modifiés et supprimés.
3. Repérer les conflits par empreintes, fichier par fichier.
4. Présenter le résultat.
5. Obtenir une validation explicite.
6. N'écraser aucune modification locale.

Une adaptation éventuelle de `brain/` est signalée et proposée à part ; un changement de l'adaptateur Claude Code (`adapters/claude-code/`) est signalé (`adaptations_claude`) sans rien écrire : `.claude/` n'est pas modifié. `/brain -u` refuse de s'exécuter dans le dépôt source 2brain. Après un `--apply` réussi (code 0, sans conflit, avec au moins un fichier écrit, mis à jour, ajouté ou supprimé : `updated`, `added` ou `deleted` non vide), le message se termine par « YAHOU ! » ; il ne l'affiche jamais sans écriture, en cas de conflit ou d'échec.

`update-brain-main.py` compare le manifeste, le local et la source fichier par fichier, imprime un plan (sans écrire) puis, avec `--apply --plan-sha256`, applique sans jamais écraser un conflit.

## 8. Capture, recherche et Review

`/brain -c` alimente le mécanisme existant (`brain-main/skills/brain-capture/`, version 0.1.5, règles inchangées ; le contrat du registre est désormais `brain-main/registry/SCHEMA.md`, même contenu que `brain/registry/SCHEMA.md` du dépôt source) sans le dupliquer. Il distingue l'utilisateur, l'agent et les outils. Il préserve l'auteur, la provenance et les nuances d'intention et de validation. Il évite les blocs entiers et les doublons.

Capturer et réduire le contexte sont deux choses différentes : la capture ne lance jamais `/compact`.

### 8.1. Extrait de session (`read-session.py`)

`brain-main/skills/brain-capture/scripts/read-session.py` transforme la transcription JSONL de la session en un extrait texte lisible et traçable. Il ne capture rien lui-même.

- **Entrée :** `--session-id <id> --project <dossier>` (fichier `<config>/projects/<dossier encodé>/<id>.jsonl`, `<config>` = `--config-dir`, sinon `CLAUDE_CONFIG_DIR`, sinon `~/.claude` ; dossier encodé = chemin absolu avec tout caractère non alphanumérique remplacé par `-`, d'après la documentation de Claude Code et vérifié sur le disque) ou `--transcript <chemin>`.
- **Sortie :** sans `--out` ni `--out-dir`, seulement un résumé JSON, rien n'est écrit. `--out <fichier>` refuse d'écraser. `--out-dir brain/sources/sessions` écrit `AAAAMMJJ-HHMM-<8 premiers caractères de l'id>.txt` (heure locale de l'extraction) et crée le dossier si besoin.
- **Marqueurs :** `[USER]`, `[ASSISTANT]`, `[TOOL:<nom>]`, `[TOOL-RESULT:<nom>]`, `[SYSTEM]`, `[AGENT-MESSAGE]`, chacun avec son horodatage. En-tête : identifiant de session, fichier d'origine, premier et dernier horodatage, rôle de l'extrait. Les lignes de contenu sont indentées de deux espaces : seules les lignes de marqueur commencent à la colonne 0.
- **Attribution :** seul un vrai message humain est `[USER]` : message d'origine `human` (ou, pour les anciennes versions sans origine, message de forme ordinaire non marqué comme injecté, compté à part), commande tapée par l'utilisateur, message envoyé pendant que l'assistant travaille. Rappels système, notifications de tâche, interruptions, résumé de compactage, sorties de commandes locales sont `[SYSTEM]` ; messages d'un autre agent ou retours de sous-agents sont `[AGENT-MESSAGE]` ; ils ne sont jamais `[USER]`, même avec le rôle `user` dans la transcription. Un contenu collé par l'utilisateur reste dans `[USER]` : coller n'est pas approuver.
- **Exclus :** le raisonnement interne (`thinking`, ROUTER §8) et les entrées de sous-agents (`isSidechain`), comptés dans le résumé. Les sorties d'outils sont limitées à 20 lignes et 2000 caractères avec la mention du retrait ; un appel d'outil garde son nom et un résumé de ses paramètres.
- **Locators :** le résumé donne les plages de lignes par rôle. `origin.locators` utilise `kind: lines` et `role` `user` ou `assistant` ; pour les outils, le système et les agents, le rôle autorisé est `unknown` avec une `note` (aucune nouvelle valeur de taxonomie n'est nécessaire).
- **Secrets :** formes évidentes (clés d'API, jetons, clés privées, `Authorization`, mots de passe en clair) remplacées par `[MASQUÉ]` et comptées. Ce n'est pas une garantie.
- **Format instable :** la transcription est un format interne que la documentation dit pouvant changer à chaque version. Un type d'entrée inconnu est compté et listé (nom seulement). Sans tour reconnu, ou si plus de 20 % des entrées ne sont pas reconnues, le script s'arrête avec le code 3 sans rien écrire. Codes : 0 ok, 2 usage, fichier introuvable ou sortie déjà existante, 3 format non reconnu.
- **Retard possible :** la transcription est écrite en continu ; le résumé donne le dernier horodatage lu, et le fichier peut être en retard sur la conversation.

### 8.2. Stockage de la source

L'extrait n'est écrit qu'au moment d'une capture, dans `brain/sources/sessions/`. Ce chemin est `origin.source` des captures (`append-captures.py --source` et le validateur l'acceptent, testé). Le guide `brain-main/README.md` en dit le rôle (aucun fichier du système n'est installé dans `brain/`). L'extrait peut contenir des extraits de conversation : le relire avant tout commit.

### 8.3. Recherche (`search-registry.py`)

`brain-main/skills/brain-search/scripts/search-registry.py <mots> [filtres]` ; lecture seule stricte (le registre n'est ouvert qu'en `rb`). Mots dans `title`, `content`, `evidence`, `tags`, `refs`, sans tenir compte de la casse ni des accents ; tous présents par défaut, `--any` pour un seul. Filtres : `--intention --type --position --space --status --validation --author --tag --project-name --since --until --id --relation`. Classement : titre, puis tags, puis contenu. Chaque résultat montre toujours l'id et la validation, pour qu'une proposition ne passe pas pour une décision. Une ligne invalide est signalée sans arrêter la lecture ; un fichier qui n'est pas un JSONL est refusé (code 3). `--json` pour la sortie structurée.

### 8.4. Review (`review-registry.py`)

`brain-main/skills/brain-review/scripts/review-registry.py` : rapport sur la sortie standard, **aucun fichier écrit**, aucun changement de statut, aucune validation, aucune proposition de suppression ni de réécriture. Chaque élément est un candidat à examiner (ids et raison).

- **doublons :** titres identiques après normalisation ; contenus proches (mots communs au moins 0,70 puis `difflib` au moins 0,80, au moins 8 mots) ;
- **contradictions :** relations `conflicts_with`, `contradicts`, `contradicted_by` (avec ou sans `resolves`), entrée validée contestée, positions `opposed` et favorables sur un même titre ;
- **relations :** cibles absentes, auto-références, relations inconnues, réciproque attendue manquante (TAXONOMY §7), statistiques du graphe (entrées reliées, isolées, composantes) ;
- **manques :** questions sans réponse reliée, approbation incohérente, `referentiel` avec `validation: none`, locators vides, champs obligatoires absents, URL du contenu absente de `refs`, mapping intention-type incohérent.

Limites : détection mécanique, sans interprétation ; elle peut manquer des doublons reformulés et des contradictions de fond, et signaler des cas sans importance dans un registre historique. Elle se complète par une lecture humaine : Claude présente le jugement de fond comme une proposition à valider. Le contexte cité en §10 (CAP-077, CAP-263, CAP-313, CAP-327) est sans pouvoir de décision.

## 9. Structure, compte et limites

```
brain-main/bootstrap/
  VERSION                 version du Bootstrap
  account/                part sur le compte (SKILL.md, session-start.py, status.py, fetch-source.py)
  scripts/                arrivent avec brain-main/ (install-account, prepare-install, apply-install, cancel-install, update-brain-main)
  templates/              CLAUDE.md, AGENTS.md, gitignore.txt (racine) ; brain/ (docs/ et registry/entries.jsonl vide)
  tests/                  run_bootstrap_tests.py (installation, compte, racine, brain généré), run_commands_tests.py (-c, -s, -r), run_audit_tests.py (-a)
brain-main/registry/      SCHEMA.md (contrat du registre)
brain-main/adapters/claude-code/  agents/ (orchestrator, worker-sonnet, worker-haiku), settings.json, README.md (copiés dans .claude/ par -i)
brain-main/skills/
  brain-capture/scripts/  append-captures, rollback-captures, validate-registry, read-session
  brain-search/scripts/   search-registry
  brain-review/scripts/   review-registry
  brain-onboarding/       SKILL.md (-o)
  brain-audit/            SKILL.md (-a), scripts/scan-project.py
```

- **Emplacement sur le compte :** `~/.claude/skills/brain/` (skill, hook, scripts légers, `VERSION`), un groupe `hooks.SessionStart` (matcher `startup`, sans shell) dans `~/.claude/settings.json`, sauvegardes dans `~/.claude/2brain-bootstrap/backups/`. Installation : `python scripts/install-account.py` (options `--home`, `--dry-run`, `--uninstall`, `--replace-probe`).
- **Retrait :** `install-account.py --uninstall` retire seulement son groupe de hooks et son dossier skill, et garde les sauvegardes.
- **Prérequis :** Python 3 (bibliothèque standard seulement). Le chemin absolu de Python est écrit dans le skill et dans le hook à l'installation.
- **Session orchestrateur :** dans une session routée (§9.1), la session n'a ni Bash, ni Write, ni Edit. `/brain` s'y exécute, mais les commandes sont déléguées à l'agent `worker-sonnet`, avec un brief qui contient tout (le worker ne voit pas la conversation). Les installations et mises à jour sont refusées dans le dépôt source.
- **Limites des commandes de lot 3 :** format de session instable (voir 8.1) ; fichier de transcription pouvant être en retard ; masquage des secrets non garanti ; extraits à relire avant commit ; `read-session.py` ne lit pas les transcriptions de sous-agents ; Search et Review n'ont été essayés que sur des copies du registre et des registres synthétiques.
- **Limites du lot 4 :** sauf mention contraire au §1, testé par scripts seulement (dossiers temporaires, comptes simulés avec `--home`) ; le chargement réel des imports `@` et l'effet de `-o` en session restent à confirmer ; la taille de contexte chargée à chaque session n'est pas mesurée en session.
- **Test réel du 2026-11-06 (compte en 0.4.0 à cette date, projet installé) :** le routeur n'a pas été observé dans ce test, car la session d'installation n'est pas routée (le routeur s'applique aux conversations ouvertes après l'installation) ; il a ensuite été essayé par l'humain dans une nouvelle conversation (§1). `-o`, `-c`, `-s`, `-r` et `-c 1` ont abouti en session sans routeur. Sous Windows, `python -I` ignore `PYTHONIOENCODING` : chaque script configure donc lui-même sa sortie en UTF-8, et un Python ponctuel de lecture utilise `-X utf8`.
- **Téléchargement GitHub :** `/brain -i` et `/brain -u` dépendent de ce qui est poussé sur `master` ; le téléchargement réel a été testé par script le 2026-11-06 avec le commit `e8f44b2`. Sans réseau ou sans source publiée, `fetch-source.py` échoue avec un message explicite.

### 9.1. Adaptateur Claude Code (routeur)

Décision de l'humain du 2026-11-06 : « Je veux que le router soit automatiquement appliqué dès l'installation ». Source : `brain-main/adapters/claude-code/` (`agents/orchestrator.md`, `worker-sonnet.md`, `worker-haiku.md`, `settings.json` = `{"agent": "orchestrator"}`, `README.md`). Règles : `brain-main/ROUTER.md` (§9), jamais recopiées ; correspondance et limites : le `README.md` de l'adaptateur, installé en `.claude/README.md`.

- **Installation (`prepare-install.py`, `apply-install.py`) :** les cinq fichiers sont copiés à la racine du projet, visibles dans la prévisualisation et le bilan. Fichier absent : créé. Agent ou `README.md` existant et identique : rien à faire ; différent : conflit (comme les autres, code 4 à l'application, rien écrasé). `.claude/settings.json` existant : **jamais modifié**. Le plan donne la clé exacte à y ajouter (`"agent": "orchestrator"`, à la main ou par `/brain -d on` après l'installation) et dit que le routeur ne sera pas actif tant qu'elle n'y est pas ; une autre valeur de `agent` est signalée comme conflit, non bloquant puisque le fichier n'est pas écrit. Le bilan donne `routeur` : `actif à la prochaine conversation` ou `non activé`, avec la raison, et rappelle d'ouvrir une nouvelle conversation.
- **Mise à jour :** `-u` n'écrit que dans `brain-main/`. Si l'adaptateur a changé, la liste `adaptations_claude` le signale (« `.claude/` n'est pas modifié »).
- **État :** `status.py` lit la configuration, pas la session en cours, et donne `routeur` : `configuré` (clé `agent` = `orchestrator` et trois agents ; s'applique aux conversations ouvertes après l'installation, sans dire si la session courante est routée), `désactivé` (trois agents présents, clé `agent` absente), `absent` (ni l'un ni l'autre) ou `partiel` (autre valeur de `agent` comprise, signalée dans la raison).
- **Retrait et remise :** `/brain -d off` (retrait de la clé `agent`) et `/brain -d on` (remise, si les trois agents sont présents), puis une nouvelle conversation. Retirer la clé à la main reste valable. Provenance : demande expresse de l'humain, 2026-11-06. `status.py` donne `désactivé` quand les trois agents sont présents sans clé `agent`, et suggère `/brain -d on`.
- **Garde-fou de session non routée :** le skill `/brain` déduit qu'une session n'est pas routée quand elle a Bash, Write ou Edit alors que `status.py --json` donne `routeur: configuré`. `/brain` le dit dans l'état ; `-o`, `-c`, `-c <fichier>`, `-c 1`, `-u` demandent une confirmation explicite avant d'écrire, sinon s'arrêtent ; `-s` et `-r` le signalent en une ligne. Le modèle `AGENTS.md` donne la même consigne (une fois par session). Déduction d'après les outils, sans garantie. Provenance : décision de l'humain du 2026-11-06. Reste à confirmer en session réelle : le routeur n'y a toujours pas été observé.
- **`brain/` :** l'adaptateur va dans `.claude/` et `brain-main/`, jamais dans `brain/`.
- **Limites :** aucune économie de coût n'a été mesurée. Un `.claude/settings.json` existant empêche l'activation automatique. Le fonctionnement réel est à confirmer en session : démarrage en orchestrateur, délégation depuis `/brain`, permissions des workers en arrière-plan. Les autres limites (Bash des workers, modèles non verrouillés, aller-retour pour chaque modification, outils Desktop possiblement absents) sont dans le `README.md` de l'adaptateur.

## 10. Provenance

Sauf CAP-327, aucune des captures ci-dessous n'est validée (`validation: none`). Elles sont citées telles qu'écrites dans `brain/registry/entries.jsonl`.

- **CAP-052**, question ouverte « Q activation modules / updates / phrase » : l'assistant recommande notamment des updates Brain-main proposées sans auto-apply.
- **CAP-056**, orientation de l'utilisateur « Updates modules : auto Brain-main ; local-only non ». Ce document la fait évoluer vers une validation explicite : décision de l'humain du 2026-11-05. La capture n'est pas écrasée et reste dans le registre telle quelle.
- **CAP-051**, suggestion (`validation: none`) « brain init = onboarding intelligent progressif » : source des questions d'accueil.
- **CAP-061**, convention proposée (`validation: none`) « brain init ≠ onboarding continu » : l'initialisation est unique, l'onboarding se poursuit sur plusieurs sessions ; source de `-o` relançable.
- **CAP-062**, suggestion (`validation: none`) « Mission agent d'onboarding » : transformer une intention floue en projet documenté, distinguer hypothèses et décisions, ne jamais coder ni valider sans instruction explicite ; source du skill d'onboarding.
- **CAP-030**, suggestion « Proposition table ~11 commandes brain * », non définitive.
- **CAP-181**, orientation « Modules : tout noter ; décisions plus tard via recherche thématique ».
- **CAP-077**, convention proposée (`validation: none`) « Formaliser /brain-capture et /brain-review » : Review analyse (relations, doublons, contradictions, manques), prépare, et la validation humaine précède tout caractère officiel. Source du principe de §8.4.
- **CAP-263**, exigence proposée (`validation: none`) : ne pas élargir le pouvoir de validation de Review au-delà de l'exprimé. Source de la règle « rapport seulement ».
- **CAP-313**, suggestion (`validation: none`) : Review construit progressivement un graphe de connaissances plutôt qu'une simple arborescence. Source des statistiques de graphe de §8.4.
- **CAP-327**, décision validée par l'utilisateur (`explicit_user_approval`, portée `item`), qui clarifie CAP-313 : seule de ces quatre captures à être validée.

Les décisions de ce document viennent de la validation de l'humain du 2026-11-05, complétée par la décision de l'humain du 2026-11-06 : `/brain -o`, `CLAUDE.md` et `AGENTS.md` créés à l'installation, `brain/` sans trace du système, chargement de l'essentiel à chaque session (conventions puis guide), détail lu quand l'outil sert. Décision de l'humain du 2026-11-06 : le routeur est appliqué dès l'installation (§9.1). CAP-051, CAP-061 et CAP-062 n'ont aucun pouvoir de décision. Le registre n'a pas été modifié.
