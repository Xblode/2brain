# Gaps de reconstruction

> Ce que les trois JSONL **ne permettent pas** de reconstruire fidèlement, ou seulement de façon floue. Aucune invention pour combler.

## 1. Impossible à reconstruire (absent des CAP)

| Zone | Pourquoi |
|------|----------|
| Contenu réel de `vision.md` / docs ClickUp | Seule la validation « 100 % » et des noms de fichiers sont cités ; pas le texte du document |
| Code / SKILL.md / SCHEMA.md du Skill | Jamais inclus dans les captures (seules règles et audits paraphrasés) |
| Structure réelle du dépôt sur disque | Propositions de chemins seulement ; pas d’inventaire filesystem |
| Implémentation MCP / Rules / adaptateurs multi-IA | Exigences/noms ; pas de design technique |
| Identifiants ClickUp réels, API sync | Arbo conceptuelle seulement ; lien folder mentionné sans détail exploitable |
| Résultats bruts COMPARISON.md / validate.json | Audits résumés ; fichiers non fournis dans les JSONL |
| Conversations sources complètes | Interdites ; seuls extraits `evidence` |
| État post-0.1.3 / Tests A–B | Décidés/proposés ; non exécutés dans les CAP |
| Modèle de données champ-par-champ figé | Contrat évoqué + schéma observé dans les JSONL de test, mais pas de spécification officielle complète dans le contenu des CAP |
| SQL vs JSONL | Les deux cités ; aucun choix technique final |

## 2. Zones floues / infos dispersées

### 2.1 Orthographe et frontières Brain / brain / Brain-main

Les CAP mélangent `Brain/`, `brain/`, `Brain-main/`, `brain-main/`. Le rôle conceptuel est clair ; le naming filesystem exact ne l’est pas.

### 2.2 Mode quotidien B vs C

User répond « B ou C » sans trancher (`ref1:CAP-019`). Audits traitent l’ambiguïté comme défaut de capture. **HYPOTHÈSE** : hybride probable, non décidé.

### 2.3 Capture automatique « après chaque message »

Évolution : combinaison → auto sélective → après chaque message → auto via intégrations + manuel. Le comportement cible production multi-plateforme reste **ouvert** (`ref1:CAP-101`).

### 2.4 Inbox locale vs Inbox ClickUp seulement

Contradiction explicite entre 4 espaces (Atelier/Inbox) et « pas d’inbox locale » (`ref1:CAP-023` vs `CAP-086`/`CAP-100`).

### 2.5 Orchestrateur central

Reco assistant + volonté agents spécialisés. User veut les deux comme **idées non validées** (`ref2:CAP-057`). Pas de décision formelle « orchestrateur = oui ».

### 2.6 Updates modules auto

User : auto pour brain-main. Assistant avait recommandé propositions sans auto-apply (`ref1:CAP-052` vs `CAP-056`). Tag `ambiguous`.

### 2.7 Périmètre exact de validation Review

Formulation user corrigée (« valider certaines choses ») ; audits refusent d’élargir en pouvoir de validation formelle. Frontière Review vs Sync vs humain **floue**.

### 2.8 Niveau d’approbation des « bases de travail »

Beaucoup d’`approval_global_partial`. Reconstruction doit éviter de les élever en architecture figée — risque principal de sur-interprétation.

### 2.9 Chiffres de tests

Comptes (69, 77, 80, 62 CAP…) viennent d’audits paraphrasés. Sans fichiers de run : **confiance moyenne** sur les métriques exactes.

### 2.10 Relations entre runs

ref1 / ref2 / ref3 capturent des conversations successives du même projet, mais les registres sont indépendants. Relier une idée « CAP-X ref1 » à « CAP-Y ref2 » est une **reconstruction thématique**, pas une relation native.

## 3. Risques de sur-reconstruction (à éviter)

- Transformer suggestions assistant (tables commandes, AGENTS.md, taxonomies) en décisions user.  
- Confondre `position: selected/confirmed` avec `validation: explicit_user_approval`.  
- Assumer qu’un graphe Review ou des registres spécialisés existent déjà (ils sont validés comme **direction**, pas comme livrable).  
- Assumer le contenu de production `entries.jsonl` hors de ces trois copies isolées.

## 4. Couverture relative par thème

| Thème | Densité dans les CAP | Fiabilité reconstruction |
|-------|----------------------|--------------------------|
| Vision / problème | Haute | Haute |
| Archi conceptuelle Brain-main/brain/ClickUp | Haute | Moyenne–haute (propositions vs décisions) |
| Workflow Capture (fenêtres, taxonomie, validation) | Très haute | Haute |
| Historique versions Skill | Haute | Haute |
| Audits / défauts tests | Haute | Moyenne (métriques) / Haute (tendances) |
| Roadmap 6 couches SB | Moyenne | Moyenne (base partielle) |
| Review / Sync / Search implémentés | Faible (design seulement) | Faible |
| Multi-projets réels hors 2brain | Quasi nulle | Faible |
