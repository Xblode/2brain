---
metadata_version: 1
title: Bootstrap et commande /brain
type: specification
description: Spécifie la commande unique /brain, le rôle du Bootstrap qui l'orchestre, la détection d'un projet, l'installation et la mise à jour de 2brain, avec l'état réel de chaque commande.
summary: Une seule porte d'entrée, /brain, avec des options à une lettre. Le Bootstrap est un skill léger installé sur le compte Claude Code ; il détecte, diagnostique, récupère les ressources, prépare des propositions et coordonne les mécanismes existants, sans rien modifier sans validation humaine. Ce document est la référence unique des commandes et du Bootstrap. État réel : `/brain`, `-i`, `-u`, `-o`, `-c`, `-c <fichier>`, `-c 1`, `-s` et `-r` sont construits et testés par scripts (Bootstrap 0.3.0 dans le dépôt) ; le compte porte le Bootstrap 0.1.0 et n'a pas été réinstallé, et le chargement réel des imports reste à confirmer en session.
version: "0.4.0"
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

**État réel (lot 4) :** le skill `/brain`, le hook de démarrage, les scripts de détection, de prévisualisation, d'installation, de mise à jour, d'extraction de session, de recherche et de Review, et le skill d'onboarding (`-o`) sont construits dans `brain-main/` et testés par scripts (`tests/run_bootstrap_tests.py` et `tests/run_commands_tests.py`, dossiers temporaires, données synthétiques). Constat du 2026-11-06 : le compte porte le Bootstrap 0.1.0 (fichier `VERSION` du skill installé) et n'a pas été réinstallé ; la version du dépôt est 0.3.0. Un test réel du 2026-11-05, avec une sonde, a confirmé dans l'onglet Code de Claude Code : le hook `SessionStart` en forme sans shell fonctionne et le skill reçoit `-i` dans `$ARGUMENTS` et `$0`. Aucune des commandes `-c`, `-s`, `-r`, `-o` n'a encore été essayée en session réelle, et le chargement réel des imports `@` de `AGENTS.md` (§6.1) reste à confirmer en session.

## 1. État par commande

| Commande | Fonction | État | Lot |
| --- | --- | --- | --- |
| `/brain` | État du projet et aide | construit et testé par scripts ; présent sur le compte en 0.1.0 | 2 |
| `/brain -i` | Installation (analyse, questions, prévisualisation, installation) | construit et testé par scripts ; présent sur le compte en 0.1.0 | 2 |
| `/brain -u` | Mise à jour de `brain-main/` | construit et testé par scripts ; présent sur le compte en 0.1.0 | 2 |
| `/brain -o` | Remplissage de `brain/docs/` avec le projet | construit et testé par scripts, à réinstaller sur le compte (0.3.0), confirmation en session réelle à faire | 4 |
| `/brain -c` | Capture de la session | construit et testé par scripts, à réinstaller sur le compte (0.3.0), confirmation en session réelle à faire | 3 |
| `/brain -c <fichier>` | Capture d'une source externe | construit et testé par scripts, à réinstaller sur le compte (0.3.0), confirmation en session réelle à faire | 3 |
| `/brain -c 1` | Annulation de la dernière capture | construit et testé par scripts, à réinstaller sur le compte (0.3.0), confirmation en session réelle à faire | 3 |
| `/brain -s <sujet>` | Recherche | construit et testé par scripts, à réinstaller sur le compte (0.3.0), confirmation en session réelle à faire | 3 |
| `/brain -r` | Review en rapport seulement | construit et testé par scripts, à réinstaller sur le compte (0.3.0), confirmation en session réelle à faire | 3 |

Les mécanismes sont dans `brain-main/skills/` (`brain-capture/`, `brain-search/`, `brain-review/`) : le skill du compte ne fait qu'aiguiller vers eux, donc `/brain -u` les met à jour. Seul le skill du compte (`SKILL.md`) demande de relancer `install-account.py` pour passer en 0.3.0.

## 2. Commandes

Une seule porte d'entrée : `/brain`. Une option = un tiret plus une lettre. Cette syntaxe remplace `/brain u`, `/brain-capture c` et `/brain-main u`.

- `/brain` : état du projet et aide. Lecture seule.
- `/brain -i` : analyse du projet, questions d'accueil, prévisualisation, puis installation après validation. Questions : nature du projet, objectif, modules, outils, identité. Une réponse manquante ne bloque pas. La réponse sur les modules note seulement une intention. En fin de parcours : bilan, consigne de démarrer une nouvelle conversation (pour que le contexte se charge, §6.1), proposition de `/brain -o`.
- `/brain -u` : met à jour `brain-main/` uniquement, après validation (voir section 7).
- `/brain -o` : propose le contenu de `brain/docs/` d'après le projet, marqué `confirmé`, `hypothèse` ou `à compléter`, puis écrit seulement ce que l'humain valide (§6.2). Relançable sur plusieurs sessions. Elle existe aussi dans le dépôt source 2brain, où rien n'est écrit sans validation.
- `/brain -c` : extrait la session courante (`read-session.py`), la range comme source traçable, puis la capture avec le skill de capture, mode `production` sauf autre demande. L'invocation vaut demande d'écrire l'extrait et d'ajouter au registre ; le skill l'annonce.
- `/brain -c <fichier>` : capture un fichier existant avec le même skill ; un fichier absent est refusé.
- `/brain -c 1` : annule la dernière capture. Le skill présente d'abord ce qui sera annulé, demande une confirmation explicite, puis lance `rollback-captures.py --n 1`. Tout autre argument (ni `1`, ni fichier existant) est refusé.
- `/brain -s <sujet> [filtres]` : recherche par mots et filtres (`search-registry.py`). Lecture seule.
- `/brain -r` : Review en rapport seulement (`review-registry.py` : doublons, contradictions, relations, manques). Elle ne modifie ni le registre ni les documents ; Claude présente ensuite l'analyse comme des propositions à valider.
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
- **E. Installation.** Création de `brain-main/`, puis de `brain/` généré à partir de `brain-main/`, et de `CLAUDE.md` et `AGENTS.md` à la racine s'ils sont absents. Contrôle de cohérence. Les fichiers existants sont préservés. Bilan final, puis proposition de `/brain -o`.

Après un « oui », l'utilisateur tape `/brain -i` (Claude ne peut pas lancer la commande lui-même, le skill étant à invocation manuelle). `EMPLACEMENT/` est supprimé en cas de refus. Si un conflit apparaît après la validation, l'installation est suspendue et l'accord est redemandé.

### 5.1. Scripts

Appelés par le skill avec `python -I`, un fichier par script, bibliothèque standard seulement, sortie JSON. `fetch-source.py` récupère `brain-main/` dans un dossier temporaire ; `prepare-install.py` crée `EMPLACEMENT/` (copie prévue, `plan.json`, marqueur `.2brain-emplacement`) et imprime `plan_sha256` ; `apply-install.py --plan-sha256` installe seulement si le plan et l'arborescence correspondent et si aucun conflit n'est apparu (code 4 sinon), écrit `brain-main/manifest.json` (version, commit source, date, SHA-256 par fichier) et supprime `EMPLACEMENT/` ; `cancel-install.py` supprime `EMPLACEMENT/` seulement avec son marqueur. `CLAUDE.md` (une ligne : `@AGENTS.md`) et `AGENTS.md` (imports, §6.1) sont créés s'ils sont absents et figurent dans le plan (`racine_creee`). S'ils existent, ils ne sont **jamais modifiés** : l'adaptation signalée donne les lignes exactes à y ajouter (les imports et la consigne `-o` pour `AGENTS.md`, la ligne `@AGENTS.md` pour `CLAUDE.md`), et rien si elles y sont déjà. Les modèles sont dans `templates/` (`CLAUDE.md`, `AGENTS.md`, `brain/`).

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

`brain-main/skills/brain-onboarding/SKILL.md` : lit l'état (`status.py` : documents contenant encore « À compléter », et suggestion de `-o`), lit le projet de façon ciblée ou pose des questions s'il est vide, propose le contenu de `brain/docs/` document par document avec les marqueurs `confirmé` (source citée), `hypothèse`, `à compléter`, et n'écrit qu'après validation explicite. Il ne décide rien, ne code rien, ne modifie ni le registre ni `brain-main/`, ne remplace jamais une information confirmée sans le dire, et ne reprend aucune convention. `AGENTS.md` demande de proposer `-o` une seule fois par session tant que `brain/docs/` contient « À compléter ».

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
  templates/              CLAUDE.md, AGENTS.md (racine) ; brain/ (docs/ et registry/entries.jsonl vide)
  tests/                  run_bootstrap_tests.py (installation, compte, racine, brain généré), run_commands_tests.py (-c, -s, -r)
brain-main/registry/      SCHEMA.md (contrat du registre)
brain-main/skills/
  brain-capture/scripts/  append-captures, rollback-captures, validate-registry, read-session
  brain-search/scripts/   search-registry
  brain-review/scripts/   review-registry
  brain-onboarding/       SKILL.md (-o)
```

- **Emplacement sur le compte :** `~/.claude/skills/brain/` (skill, hook, scripts légers, `VERSION`), un groupe `hooks.SessionStart` (matcher `startup`, sans shell) dans `~/.claude/settings.json`, sauvegardes dans `~/.claude/2brain-bootstrap/backups/`. Installation : `python scripts/install-account.py` (options `--home`, `--dry-run`, `--uninstall`, `--replace-probe`).
- **Retrait :** `install-account.py --uninstall` retire seulement son groupe de hooks et son dossier skill, et garde les sauvegardes.
- **Prérequis :** Python 3 (bibliothèque standard seulement). Le chemin absolu de Python est écrit dans le skill et dans le hook à l'installation.
- **Orchestrateur du dépôt 2brain :** il n'a ni Bash, ni Write, ni Edit. `/brain` s'y exécute, mais les commandes sont déléguées à l'agent `worker-sonnet`. Les installations et mises à jour sont refusées dans le dépôt source.
- **Limites des commandes de lot 3 :** format de session instable (voir 8.1) ; fichier de transcription pouvant être en retard ; masquage des secrets non garanti ; extraits à relire avant commit ; `read-session.py` ne lit pas les transcriptions de sous-agents ; Search et Review n'ont été essayés que sur des copies du registre et des registres synthétiques.
- **Limites du lot 4 :** tout est testé par scripts seulement (dossiers temporaires, comptes simulés avec `--home`) ; le compte n'est pas réinstallé (0.1.0) ; le chargement réel des imports `@` et l'effet de `-o` en session restent à confirmer ; la taille de contexte chargée à chaque session n'est pas mesurée en session.
- **Limite actuelle :** le dépôt GitHub ne contient pas le Bootstrap tant qu'il n'est pas poussé. `/brain -i` et `/brain -u` depuis GitHub échouent jusque-là, avec un message explicite de `fetch-source.py`.

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

Les décisions de ce document viennent de la validation de l'humain du 2026-11-05, complétée par la décision de l'humain du 2026-11-06 : `/brain -o`, `CLAUDE.md` et `AGENTS.md` créés à l'installation, `brain/` sans trace du système, chargement de l'essentiel à chaque session (conventions puis guide), détail lu quand l'outil sert. CAP-051, CAP-061 et CAP-062 n'ont aucun pouvoir de décision. Le registre n'a pas été modifié.
