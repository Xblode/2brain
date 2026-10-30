# Brain Capture (reconstruit)

> Reconstruction du workflow, des règles et des limites **uniquement** depuis les CAP.  
> Versions évoquées dans les sources : V1.0 → V0.1.1 → V0.1.2 → (visée) V0.1.3.

## 1. Rôle et philosophie

**FAIT / orientation user confirmée** — Rôle : stocker, classer, ne rien perdre ; validation après.  
`20261031-000600-ref2:CAP-065` · `20261031-000600-ref2:CAP-058`

**PROPOSITION (assistant, reprise 0.1.2)** — Capture avant consolidation ; collecte fidèle ; une info non validée reste utile. Priorité absolue : ne perdre aucune information utile.  
`20261031-000600-ref3:CAP-004` · `20261031-000600-ref3:CAP-005`

**PROPOSITION** — Capture = matière première ; Review = mémoire cohérente.  
`20261031-000600-ref3:CAP-084` · `20261031-000600-ref3:CAP-098`

**ÉVOLUTION ref1** — D’abord combinaison capture passive/session (`ref1:CAP-026`) → capture auto sélective + consolidation (`ref1:CAP-035`) → idée user « après chaque message » (`ref1:CAP-084`) → clarification : auto via intégrations ; `/brain-capture` manuel (`ref1:CAP-093`).  
**FAIT (risk)** — Un skill seul ≠ écriture auto multi-IA.  
`20261031-000600-ref1:CAP-101`

## 2. Workflow opérationnel

### 2.1 Fenêtres

**REQUIREMENT / selected user** — Capture progressive par fenêtres ~5 messages user + 5 réponses assistant ; enchaînement sans validation user.  
`20261031-000600-ref2:CAP-060`

**PROPOSITION formalisée** — Mémoire de travail persistante ; chevauchement inter-fenêtres (ex. relire 2 derniers messages).  
`20261031-000600-ref2:CAP-082` · `20261031-000600-ref3:CAP-007` · `20261031-000600-ref3:CAP-008`

**REQUIREMENT (ajustement plan Cursor)** — Verrouiller définition fenêtre : jusqu’à 5+5 ; chrono ; incomplets conservés ; pas de doublons inter-fenêtres ; fenêtres ≠ limite de contexte.  
`20261031-000600-ref3:CAP-037`

### 2.2 Extraction multi-passes

**PROPOSITION** — Quatre grilles sur la même fenêtre (même agent) : infos / actionable / relations / contexte.  
`20261031-000600-ref2:CAP-088` · `20261031-000600-ref2:CAP-119` · `20261031-000600-ref3:CAP-009`

### 2.3 Couverture et anti-agrégat

**REQUIREMENT** — Contrôle de couverture sémantique obligatoire ; ne pas juger au seul JSONL valide.  
`20261031-000600-ref3:CAP-010` · `20261031-000600-ref3:CAP-025` · `20261031-000600-ref2:CAP-040`

**CONVENTION** — Règle anti-agrégat : sujets individuels retrouvables (ex. 7 sujets de cadrage).  
`20261031-000600-ref3:CAP-011`

### 2.4 Audit final (visée 0.1.3)

**PROPOSITION / convention** — Trois situations richesse ; audit final obligatoire **sans** questions à l’utilisateur ; Review posera les questions.  
`20261031-000600-ref3:CAP-088` · axes `CAP-102` · `CAP-103`

## 3. Taxonomie

### 3.1 Intentions (proposées → utilisées dans schéma captures)

**PROPOSITION** — `idea, suggestion, preference, orientation, question, decision, requirement, convention, task, milestone, observation, risk, feedback`.  
`20261031-000600-ref2:CAP-079` · `20261031-000600-ref3:CAP-012`

**DÉCISION** — Une intention principale par entrée.  
`20261031-000600-ref2:CAP-097`

### 3.2 Positions

**PROPOSITION** — `proposed, exploring, favorable, endorsed, opposed, selected, confirmed, uncertain`.  
`20261031-000600-ref2:CAP-080` · `20261031-000600-ref3:CAP-013`

### 3.3 Intention ≠ position ≠ validation

**CONVENTION (proposée, réaffirmée)** — Ne pas convertir automatiquement favorable/endorsed/selected en validation formelle.  
`20261031-000600-ref2:CAP-078` · `20261031-000600-ref3:CAP-014` · `20261031-000600-ref3:CAP-038`

**FAIT (observation audit)** — Séparation intention/position/validation jugée excellente en conception 0.1.2.  
`20261031-000600-ref3:CAP-053`

## 4. Auteurs et attribution

**CONVENTION (proposée)** — Hiérarchie : métadonnées rôle → structure/export → signatures plateforme → style secondaire → incertitude.  
`20261031-000600-ref2:CAP-094` · `20261031-000600-ref3:CAP-017` · `20261031-000600-ref3:CAP-089`

**FAIT** — Sources brutes souvent sans labels d’auteur (collage txt).  
`20261031-000600-ref3:CAP-079` · `20261031-000600-ref3:CAP-071`

**SUGGESTION user** — Documenter signatures chatbots.  
`20261031-000600-ref3:CAP-080` · axe E `CAP-105`

**CONVENTION** — Citation ≠ nouvelle approbation ; distinguer auteur initial et commentaire.  
`20261031-000600-ref2:CAP-087` · `20261031-000600-ref3:CAP-018` · `20261031-000600-ref3:CAP-039`

## 5. Validation et `approval_global_partial`

**FAIT** — `approval_scope` (item/set/null) et tag `approval_global_partial` introduits comme idées pertinentes (0.1.1).  
`20261031-000600-ref2:CAP-033`

**ORIENTATION user favorable** — Adapté aux accords « j’ai lu, d’accord en gros » : ↑ confiance segment, pas validation définitive.  
`20261031-000600-ref2:CAP-061` · `20261031-000600-ref2:CAP-083` · `20261031-000600-ref3:CAP-019`

**DÉCISION** — Capture multi-informations : OUI (séparer certitudes différentes).  
`20261031-000600-ref2:CAP-063`

**PREFERENCE user** — Mieux capturer séparément ; Review tranche ensuite.  
`20261031-000600-ref3:CAP-077`

**CONVENTION atomicité** — Un élément identifiable/exploitable ; pas une phrase = une CAP.  
`20261031-000600-ref3:CAP-087` · `20261031-000600-ref3:CAP-101`

## 6. Grounding et autonomie

**REQUIREMENT confirmé user** — Chaque capture compréhensible sans la source (ex. expliquer modes B et C).  
`20261031-000600-ref2:CAP-055` · `20261031-000600-ref2:CAP-081` · `20261031-000600-ref3:CAP-016`

**PROPOSITION axe F** — Distinguer explicite / interprété / incertain / déduit (prépare Review).  
`20261031-000600-ref3:CAP-106`

**FAIT schéma observé dans les JSONL isolés** — Champ `grounding` avec valeurs du type `source_explicit`, `source_contextual`, `source_interpreted` (présentes dans les entrées des trois runs).

## 7. Relations

**REQUIREMENT** — Améliorer détection relations (réponses, corrections, contradictions, évolutions…) sans fusion auto ni proximité thématique seule.  
`20261031-000600-ref3:CAP-021` · `20261031-000600-ref3:CAP-104`

**FAIT** — Relations présentes dans les registres (ex. `answers`, `related`, `conflicts_with`, `parent_of`, `evolves_to`…).

## 8. Actionnable, Review, bruit

**CONVENTION** — Capturer tâches/jalons sans créer ClickUp ; Review pré-organise.  
`20261031-000600-ref3:CAP-022`

**DÉCISION** — Review local puis Sync avant ClickUp.  
`20261031-000600-ref2:CAP-098`

**REQUIREMENT** — Distinguer métier / instructions Capture / bruit de test.  
`20261031-000600-ref2:CAP-072` · `20261031-000600-ref3:CAP-020`

**PREFERENCE** — Conserver traces test-noise taguées plutôt que supprimer.  
`20261031-000600-ref3:CAP-072`

## 9. Formalisation `/brain-capture` et `/brain-review`

**PROPOSITION user** — Capture enregistre ; Review range sans supprimer.  
`20261031-000600-ref1:CAP-074`

**PROPOSITION assistant** — Capture signale sujets sans modifier référentiel officiel ; Review prépare ; validation humaine avant officiel ; info jamais disparue.  
`20261031-000600-ref1:CAP-077`

**FEEDBACK user** — D’accord globalement avec le workflow (`approval_global_partial`).  
`20261031-000600-ref1:CAP-088`

**CORRECTION user** — Formulation Review : « Enlève les doublons et valide certaines choses ».  
`20261031-000600-ref2:CAP-070`

## 10. Limites et défauts récurrents (issus des audits)

| Défaut | Références |
|--------|------------|
| Fusion multi-certitudes / multi-sujets | `ref2:CAP-035` · `ref3:CAP-068`–`070` |
| Propagation d’accord « bonne base » hors cible | `ref2:CAP-046` |
| Couverture insuffisante (7 sujets, 6 couches) | `ref2:CAP-039` · `ref2:CAP-047` |
| Suggestion « on pourrait » → explicit approval | `ref2:CAP-037` |
| Orchestrateur + agents fusionnés | `ref2:CAP-036` |
| Explicit injustifié sur B/C ou Review ambigu | `ref3:CAP-049` · `ref3:CAP-058` |
| Test `_gen.py` ≠ exécution Skill | `ref3:CAP-047` |
| Confiance trop souvent `high` | `ref3:CAP-051` · `ref3:CAP-060` |
| Validateur structurel ≠ sémantique ; fichier vide non bloquant | `ref2:CAP-040` · `ref3:CAP-052` · `ref3:CAP-062` |
| Comparer CAP-N entre sources différentes | interdit `ref3:CAP-081` · `ref3:CAP-090` |

## 11. Périmètre versions Capture

| Version | Statut dans les CAP |
|---------|---------------------|
| V0.1.1 | Audits 045232 (jeté) / 061941 (baseline) |
| V0.1.2 | Décision lancer conception puis implémentation ; périmètre Skill Capture seul |
| V0.1.3 | Décision user avant cross-conversation : consolider philosophie Capture, **pas** implémenter Review |

`20261031-000600-ref3:CAP-001` · `CAP-006` · `CAP-095` · `CAP-111`
