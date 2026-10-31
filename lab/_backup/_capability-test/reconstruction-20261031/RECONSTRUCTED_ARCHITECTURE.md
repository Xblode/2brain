# Architecture Second Brain (reconstruite)

> Source exclusive : captures des runs ref1 / ref2 / ref3.  
> **Ne pas inventer** de détail technique absent des CAP. Distinguer proposition vs décision.

## 1. Séparation Brain-main / brain / ClickUp

**PROPOSITION (user puis reformulée assistant)** — Deux dossiers centraux : `Brain/` (instance projet) et `Brain-main/` (outil / moteur d’installation).  
`20261031-000600-ref1:CAP-003` · `20261031-000600-ref1:CAP-005` · `20261031-000600-ref1:CAP-006`

**PROPOSITION (assistant, reformulation stable)** —  
- `Brain-main/` = système réutilisable (règles, Skills, mécanismes)  
- `brain/` = mémoire et connaissances propres à chaque projet  
- ClickUp = interface de pilotage, **pas** source de vérité  
`20261031-000600-ref2:CAP-004`

**PROPOSITION (assistant)** — Brain-main = moteur et catalogue ; Brain = instance vivante ; modules étendent sans remplacer.  
`20261031-000600-ref1:CAP-047`

**HYPOTHÈSE** — La casse/orthographe des dossiers (`Brain/` vs `brain/`, `Brain-main/` vs `brain-main/`) varie selon les CAP ; aucune norme orthographique unique n’est figée dans les captures.

## 2. Trois niveaux : Core / Modules / Instance

**PROPOSITION (assistant) → base partiellement retenue (feedback user endorsed)**  
- Niveau 1 Core universel  
- Niveau 2 Modules métier activables  
- Niveau 3 Instance Brain projet (identité, modules, config, connaissances, décisions, historique, état)  
`20261031-000600-ref1:CAP-048` · `20261031-000600-ref1:CAP-067`

**DÉCISION** — Oui aux conventions de modules type « mods » : stockés/maintenus dans brain-main, vivant dans brain.  
`20261031-000600-ref1:CAP-046`

**PROPOSITION** — Module = extension autonome (`module.md`, conventions, agents, skills, templates, rules, workflows) ; définition/versions dans Brain-main.  
`20261031-000600-ref1:CAP-049`

**PROPOSITION** — Séparer Core / Module / Instance / Agent / Skill / Rule / Template / Workflow.  
`20261031-000600-ref1:CAP-050`

**DÉCISION (orientation user)** — Activation modules : IA peut choisir + ajout manuel possible.  
`20261031-000600-ref1:CAP-055`

**DÉCISION (orientation user ; tag ambiguous)** — Updates : auto pour modules natifs brain-main ; pas d’auto-update si module local-only ; brain-main maître si présent des deux côtés.  
`20261031-000600-ref1:CAP-056`  
*Conflit signalé avec reco assistant « updates proposées sans auto-apply » (`ref1:CAP-052`).*

## 3. Interfaces humaines et SoT

**FAIT (preference user)** — ClickUp comme interface principale (après Asana en agence).  
`20261031-000600-ref1:CAP-010`

**PROPOSITION (user)** — Interfaces possibles : ClickUp, Notion, GitHub, Drive.  
`20261031-000600-ref1:CAP-004`

**FAIT** — ClickUp a déjà Organisation (vie / projets rapides / idées) et Projets (un dossier par projet).  
`20261031-000600-ref1:CAP-011`

**DÉCISION** — Arbo ClickUp Projets déjà définie : Docs ; List Inbox ; List Cadrage ; List Roadmap — alignée avec tâches internes brain/.  
`20261031-000600-ref1:CAP-071`

**DÉCISION** — ClickUp cadrage/brainstorm appliqué manuellement ; consigne : ne rien ajouter dans ClickUp pour le moment.  
`20261031-000600-ref1:CAP-087`

**FAIT (requirement)** — SoT locale légère JSONL/SQL.  
`20261031-000600-ref1:CAP-008`

**DÉCISION / requirement confirmé** — Tout contenu destiné à ClickUp a un équivalent local ; local = SoT.  
`20261031-000600-ref2:CAP-068`

**PROPOSITION** — Correspondance locale↔ClickUp à conserver (id local, id ClickUp, type, statut, dernière sync, divergence).  
`20261031-000600-ref2:CAP-120`

## 4. Quatre espaces logiques

**PROPOSITION (assistant) → base retenue partielle** — Atelier/Inbox ; Référentiel ; Journal ; Pilotage.  
`20261031-000600-ref1:CAP-023` · `20261031-000600-ref1:CAP-066`

**PROPOSITION mapping** — Atelier↔idées↔Inbox ; Référentiel↔docs ; Journal↔événements ; Pilotage↔Cadrage+Roadmap. Nuance : Inbox ne reçoit pas toute la capture auto.  
`20261031-000600-ref1:CAP-076`

**CONTRADICTION HISTORIQUE** — User propose Inbox ClickUp = notes externes seulement, **pas d’inbox locale** (`ref1:CAP-086`, `ref1:CAP-100`) — relation `conflicts_with` vers l’espace Atelier/Inbox de `CAP-023`.

## 5. Pipeline et commandes

**PROPOSITION** — Chaîne Sources → Capture → Orchestrateur → Agents → Local + ClickUp.  
`20261031-000600-ref1:CAP-028`

**PROPOSITION** — Trois couches registre : brut / extrait / officiel.  
`20261031-000600-ref1:CAP-029`

**PROPOSITION table ~11 commandes** — `brain init, capture, review, process, validate, status, search, sync, audit, session, help` (non définitive).  
`20261031-000600-ref1:CAP-030`

**PROPOSITION** — Contrat commun d’information (type, origine, projet, statut, date, emplacement, relations).  
`20261031-000600-ref1:CAP-031`

**PROPOSITION → évolution** — Trois niveaux Capture / Organisation / Validation.  
`20261031-000600-ref1:CAP-081`

**PROPOSITION (assistant) puis précisée** — Capture → Review → Validation/exécution.  
`20261031-000600-ref2:CAP-077`

**DÉCISION** — Review prépare en local ; Sync valide avant création ClickUp.  
`20261031-000600-ref2:CAP-098` · clarification `20261031-000600-ref2:CAP-099`

## 6. Agents et orchestration

**DÉCISION (orientation user)** — Agents spécialisés connaissant logique/structure.  
`20261031-000600-ref1:CAP-037`

**FAIT (orientation user)** — Orchestrateur central **et** agents spécialisés : les deux voulus ; traités comme idées/suggestions non validées jusqu’à décision formelle.  
`20261031-000600-ref2:CAP-057`

**PROPOSITION (assistant)** — Un seul agent quand il suffit.  
`20261031-000600-ref2:CAP-011`

**PROPOSITION (assistant, risque)** — Orchestration peut devenir plus complexe que les projets.  
`20261031-000600-ref2:CAP-010`

**DÉCISION** — En conflit : solutions comparées (oui).  
`20261031-000600-ref1:CAP-044`

**DÉCISION** — Conserver historique des décisions remplacées.  
`20261031-000600-ref1:CAP-045`

**PROPOSITION** — Observation / Proposition / Décision / Convention ne doivent pas être confondus.  
`20261031-000600-ref1:CAP-040`

## 7. Registres

**PROPOSITION** — Registres = historique ; docs = état actuel.  
`20261031-000600-ref1:CAP-082`

**FAIT (idée user)** — Plusieurs fichiers registre selon type (`entries`, `tasks`, `roadmap`, éventuellement valid…).  
`20261031-000600-ref2:CAP-071`

**PROPOSITION (assistant)** — `entries.jsonl` = SoT de capture ; Review produit registres organisés (decisions/tasks/roadmap/conventions/knowledge/archive) liés aux CAP ; pas de `validated.jsonl` pour le moment.  
`20261031-000600-ref2:CAP-086`

**DÉCISION (pour 0.1.2)** — Garder `entries.jsonl` ; pas de registres spécialisés dans Capture.  
`20261031-000600-ref3:CAP-024` *(position proposed assistant — périmètre version)*

**DÉCISION** — Une intention principale par entrée.  
`20261031-000600-ref2:CAP-097`

**DÉCISION** — Archivage hybride option D (combinaison Review + taille/état).  
`20261031-000600-ref2:CAP-101` · `20261031-000600-ref2:CAP-102`

**PROPOSITION** — Architecture archive : entries actif + `archive/YYYY/` + `archive-index.jsonl` ; CAP IDs immuables ; jamais supprimer.  
`20261031-000600-ref2:CAP-096`

**PROPOSITION** — Review ne modifie jamais silencieusement le contenu original d’une CAP.  
`20261031-000600-ref2:CAP-103`

## 8. Hiérarchie connaissances (Review)

**DÉCISION** — Captures → relations → sujets consolidés → fonctionnalités → projets.  
`20261031-000600-ref3:CAP-093` (répond à `CAP-085`)

**DÉCISION (preference forte)** — Brain Review = graphe de connaissances, pas seule arborescence docs.  
`20261031-000600-ref3:CAP-094`

**PROPOSITION / décision proposée assistant** — Pas d’objets « sujets consolidés » dans Capture (0.1.3).  
`20261031-000600-ref3:CAP-099`

**PROPOSITION** — Emplacement recommandé `brain/conventions/clickup.md` (instance) vs convention générique dans brain-main.  
`20261031-000600-ref2:CAP-085`  
*Attention audit sample 2 : ne pas fusionner confirmation du nom et question d’emplacement (`ref3:CAP-068`).*

## 9. Onboarding / brain init

**PROPOSITION** — `brain init` = onboarding intelligent progressif (pas simple copie).  
`20261031-000600-ref1:CAP-051`

**PROPOSITION** — `brain init` ≠ onboarding continu ; init unique ; capture/review permanents.  
`20261031-000600-ref1:CAP-061`

**DÉCISION (orientation)** — Démarrer par une phrase ; brief ~500 mots non bloquant.  
`20261031-000600-ref1:CAP-057`

**QUESTION user ouverte (un moment)** — `brain init` une fois ou par session ?  
`20261031-000600-ref1:CAP-054` → réponse proposition `CAP-061`

## 10. Indépendance technologique (proposée)

**PROPOSITION** — Aucun modèle IA indispensable à la lecture ; aucun outil externe indispensable à la conservation ; données exportables ; agents remplaçables ; Skills avec contrats hors Cursor. Markdown + JSONL bonne direction.  
`20261031-000600-ref2:CAP-016` · `20261031-000600-ref2:CAP-017`

## 11. Ce qui n’est PAS spécifié dans les captures

Voir `RECONSTRUCTION_GAPS.md` : formats SQL concrets, schéma fichiers exact hors champs évoqués, implémentation MCP, structure réelle des dossiers sur disque, permissions agents détaillées, sync bidirectionnelle ClickUp (sujet ouvert).
