---
metadata_version: 1
title: "Projet"
type: reference
description: "Identité, contexte, périmètre, utilisateurs et contraintes du projet 2brain, avec son état actuel."
summary: "Qui est 2brain, pour qui, dans quelles limites et où il en est. L'état du système est donné avec le chemin qui le prouve, ou signalé comme déclaré par l'humain sans contrôle. Les décisions du plan du 2026-11-05 et la demande de gel du 2026-11-06 y figurent. Ne contient ni vision ni architecture."
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
  - "brain/docs/CADRAGE.md"
  - "brain-main/bootstrap/README.md"
---

# Projet

## 1. Objet

Identité, contexte, périmètre, utilisateurs, contraintes et état actuel de 2brain. La raison d'être est dans `brain/docs/VISION.md`, l'organisation technique dans `brain/docs/ARCHITECTURE.md` (CAP-411 : pas de vision dans le projet).

Étiquettes : `décision humaine`, `demande humaine` (dite par l'humain, sans validation formelle), `proposition non validée`, `question ouverte` ; pour l'état du système, `constaté` (avec le chemin) ou `déclaré par l'humain, non contrôlé`.

## 2. Identité et contexte

- `constaté`. Le dépôt s'appelle 2brain ; `AGENTS.md` le présente comme un Second Brain. Le nom définitif du produit reste ouvert (`brain/docs/CADRAGE.md` §20.4).
- `constaté`. Historique de la compréhension du projet : `brain/docs/CADRAGE.md` §2.
- `constaté`. Le dépôt contient le moteur (`brain-main/`), l'instance du projet (`brain/`) et un dossier hors instance (`lab/`) ; voir `brain/docs/ARCHITECTURE.md`.

## 3. Utilisateurs

- `demande humaine`. CAP-468 : le projet est « pour son utilisation personnelle » et n'a « pas vraiment pour but d'être utilisé par d'autres ». CAP-475 : « chacun doit créer le sien, avec ses conventions et ses règles ».
- `demande humaine`. CAP-407 : Second Brain doit « cadrer n'importe quel type de projet ». Le cadrage garde l'ambition universelle (CAP-468 : « on garde toujours les idées précédentes sur le cadrage ») ; voir `brain/docs/CADRAGE.md` §5.6.
- `demande humaine`. CAP-451 : « 98 % du temps, les modifications sont codées par une IA ».

## 4. Périmètre

- Périmètre et hors périmètre du cadrage : `brain/docs/CADRAGE.md` §15 (cadrage en cours de consolidation, non copié ici).
- `décision humaine` (plan du 2026-11-05, puis 2026-11-06, hors registre) : « CADRAGE.md comme 6e document standard Validé ». `CADRAGE.md` est inscrit au catalogue `brain/docs/README.md` (version 1.1.0, document verrouillé modifié pour ce seul ajout, avec l'autorisation expresse de l'humain) ; le modèle des nouveaux projets le crée (`brain-main/bootstrap/templates/brain/docs/CADRAGE.md`). Règle de CAP-411 : on ajoute, on ne retire pas.
- `demande humaine` (2026-11-06, hors registre) : gel des nouvelles commandes, avec une exception demandée pour le contrôle des README au commit et pour `/brain -m`. Ces deux éléments sont construits et testés par scripts, installés sur le compte le 2026-11-06, non encore confirmés en session ; état et limites : `brain-main/bootstrap/README.md` (§1, §6.4, §9.2). Le gel et son exception restent en vigueur.
- `décision humaine` (plan du 2026-11-05, hors registre) : le projet réel du test final reste à nommer par l'utilisateur.

## 5. Contraintes

- `demande humaine`. CAP-443 : « il faut pas enlever quelque chose qui est push ». GitHub fait foi sur l'état réel.
- `demande humaine`. CAP-411 : « on peut que rajouter des docs pas en enlever ». Les documents standard ne sont ni réduits ni retirés.
- `constaté`. Le registre `brain/registry/entries.jsonl` est en ajout seul ; contrat dans `brain/registry/SCHEMA.md`.
- `proposition non validée`. CAP-413 : les préférences Supabase et Vercel seraient des valeurs par défaut réutilisables, non des contraintes universelles. L'humain dit : « ca sera dans ma convention web, dans mes préférences ».

## 6. État actuel

- `constaté`. Le registre compte 476 captures (`brain/registry/entries.jsonl`).
- `constaté`. Capture, Search et Review sont construits par scripts : `brain-main/skills/brain-capture/scripts/append-captures.py`, `brain-main/skills/brain-search/scripts/search-registry.py`, `brain-main/skills/brain-review/scripts/review-registry.py`. Review fait un rapport seulement. Sync reste conceptuel : aucun script.
- `constaté`. Les commandes `-c`, `-s` et `-r` sont testées par scripts ; leur confirmation en session est à faire selon `brain-main/bootstrap/README.md` (§1). L'état par commande n'est pas recopié : voir ce document.
- `déclaré par l'humain, non contrôlé`. Le 2026-11-06, l'humain dit que `/brain -u` et `/brain -a` marchent très bien dans son projet.
- `constaté`. Le contrôle des README au commit (hook de compte) et `/brain -m` sont construits et testés par scripts (`brain-main/bootstrap/tests/run_readme_tests.py`), installés sur le compte le 2026-11-06, non encore confirmés en session ; détail dans `brain-main/bootstrap/README.md`.
- `constaté`. `brain/docs/` contenait cinq synthèses provisoires et aucun `REQUIREMENTS.md` avant la reprise du 2026-11-06.

## 7. Questions ouvertes

- `question ouverte`. Définition du MVP : aucune n'a été validée.
- `question ouverte`. Nom du projet réel du test final (à nommer par l'utilisateur).

## 8. Références

`brain/docs/CADRAGE.md`, `brain/docs/README.md`, `brain-main/bootstrap/README.md`, `AGENTS.md`.

## Ancienne synthèse

Texte d'origine, conservé tel quel dans le bloc ci-dessous (règle de l'humain, CAP-399 : rien ne se perd). Il date de la première synthèse provisoire. Les numéros `CAP-xxx` qu'il cite viennent de l'ancien registre de 69 captures et ne correspondent pas au registre actuel ; pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

````markdown
# Project

> **Provisoire** — synthèse légère issue de la capture. Détail : `brain/registry/entries.jsonl`.
> Sources : CAP-056 (+ contexte projet 2brain / atelier ChatGPT).
> **Attention : références obsolètes.** Les `CAP-xxx` de ce document viennent de l'ancien registre de 69 captures (commit `45ba05d`). Le registre actuel réutilise ces numéros pour d'autres contenus : ne pas les y chercher. Pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

## Identité (provisoire)

- Projet : **2brain** (Second Brain / Brain-main).
- Phase : atelier de conception / cadrage — pas d’architecture technique figée.
- Objectif immédiat de l’atelier : spécifier le moteur universel avant création lourde de dossiers.

## Socle documentaire candidat (non définitif)

Proposition assistant (CAP-056) : `vision.md`, `project.md`, `architecture.md`, `workflow.md` (candidats standard) ; `design.md` / `integrations.md` selon besoin. Liste **non validée** comme set final — voir aussi CAP-048 / CAP-051.
````
