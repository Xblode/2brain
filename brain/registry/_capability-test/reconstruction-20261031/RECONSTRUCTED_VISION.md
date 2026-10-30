# Vision Second Brain (reconstruite)

> Source exclusive : captures `20261031-000600-ref1|ref2|ref3`.  
> Légende des statuts : **FAIT** (observation factuelle dans les CAP) · **DÉCISION** (validation user explicite ou `explicit_user_approval`) · **PROPOSITION** (assistant ou user non verrouillé) · **HYPOTHÈSE** (interprétation fragile / partielle).

## 1. Problème adressé

**FAIT** — Le user constate un travail désordonné : idées dispersées dans des chatbots, vibecode, contextes saturés, idées perdues ; besoin de documenter l’avancement au fil de l’eau, y compris l’imprévu.  
`20261031-000600-ref1:CAP-007`

**PROPOSITION (assistant)** — Problématique reformulée : transformer une réflexion humaine désordonnée en connaissances et actions exploitables par des IA **sans perdre les intentions initiales** ; conserver le raisonnement d’évolution du projet, pas seulement stocker des infos.  
`20261031-000600-ref2:CAP-005`

## 2. Vision produit

**FAIT (idée user, exploring)** — Second Brain doit : trier code / propos / idées issus des chatbots ; stocker idées et avancements multi-projets ; suivre le travail ; connaître workflow et logiciels ; ranger l’info dans des boîtes/outils distincts ; disposer d’agents capables de retrouver une info, la traiter et la faire valider.  
`20261031-000600-ref1:CAP-001`

**FAIT (requirement user, confirmed)** — S’appuyer sur Skills, MCP, Rules, Agents, etc.  
`20261031-000600-ref1:CAP-002`

**PROPOSITION (assistant)** — SB = traitement continu d’information, pas seulement un gestionnaire de documentation.  
`20261031-000600-ref1:CAP-027`

**PROPOSITION (assistant)** — Différence vs méthode classique : ne plus reconstruire régulièrement le contexte pour l’IA ; avec SB abouti, l’IA reprend le travail, comprend le « pourquoi » des décisions et identifie le reste à faire.  
`20261031-000600-ref2:CAP-019`

**PROPOSITION (assistant)** — Gain principal possible : réduire le coût de démarrage d’un nouveau projet (idée → discussion libre → émergence problème / features / contraintes / choix / docs / roadmap / tâches).  
`20261031-000600-ref2:CAP-020`

## 3. Principes d’usage quotidien

**DÉCISION (orientation user, selected ; tag `approval_global_partial`)** — Mode quotidien **B ou C**, pas A pur : ne pas valider chaque test/expérimentation ; valider ce qui entre dans le cadrage (conflits, doublons) ; fin de session multi-modèles ; local = SoT et ClickUp.  
`20261031-000600-ref1:CAP-019`  
*Note : hésitation B/C non tranchée — restée ambiguë dans les audits ultérieurs.*

**DÉCISION (orientation user, selected)** — Local machine = SoT (stockage « illisible » humain) ; ClickUp = visualiseur synchronisé via commande analysant le local.  
`20261031-000600-ref1:CAP-020` · repris/renforcé `20261031-000600-ref2:CAP-068`

**DÉCISION (orientation user, selected)** — Socle universel + modules selon nature ; conventions par module ; onboarding modulaire adaptatif **non bloquant**.  
`20261031-000600-ref1:CAP-021`

**FAIT (requirement user, confirmed)** — UX ultra importante ; peu de commandes.  
`20261031-000600-ref1:CAP-012`

**FAIT (orientation user, favorable)** — Combinaison des modes de capture + plafond ~10–15 commandes.  
`20261031-000600-ref1:CAP-026`

**PROPOSITION (assistant) → base partiellement retenue** — Expérimenter sans perdre le fil : séparer exploratoire et référentiel officiel.  
`20261031-000600-ref1:CAP-022` · feedback user « bonne base » `20261031-000600-ref1:CAP-066`

## 4. Philosophie Capture / vérité projet

**FAIT (orientation user)** — Capture stocke large, classe, ne bloque pas le flux vrac ; validation après.  
`20261031-000600-ref2:CAP-058` · `20261031-000600-ref2:CAP-065`

**PROPOSITION (assistant) alignée** — Capture constitue la mémoire ; ne décide pas quoi garder. Tout conserver ≠ tout considérer vrai ; intention ≠ position ≠ validation.  
`20261031-000600-ref2:CAP-076` · `20261031-000600-ref2:CAP-078` · `20261031-000600-ref3:CAP-004` · `20261031-000600-ref3:CAP-005`

**PROPOSITION (assistant, risque)** — L’IA peut déformer progressivement les intentions (suggestion→décision, accord général→validation complète).  
`20261031-000600-ref2:CAP-008`

**PROPOSITION (assistant)** — Une IA peut proposer une interprétation, jamais la figer silencieusement en vérité projet.  
`20261031-000600-ref2:CAP-009`

## 5. Question ouverte structurante (non tranchée)

**PROPOSITION / QUESTION (assistant)** — SB doit-il surtout aider l’humain à construire, ou permettre aux IA de construire avec l’humain comme directeur ?  
`20261031-000600-ref2:CAP-029`  
**Statut :** aucune décision user explicite dans les trois runs.

## 6. Vision documentaire

**DÉCISION** — `vision.md` validé à 100 % (doc généraliste multi-projets).  
`20261031-000600-ref1:CAP-089`

**FAIT (requirement user)** — Évolution docs : challenger les contradictions, ne pas écraser silencieusement.  
`20261031-000600-ref1:CAP-092`

**QUESTION user** — Doutes sur `operating-model.md` et `onboarding.md` (peut-être chapitres d’un doc plus large).  
`20261031-000600-ref1:CAP-090`

## 7. Indicateurs de succès (proposés, non validés comme KPI officiels)

**PROPOSITION (assistant)** — Mesurer la valeur d’usage (perte de contexte, temps de reprise, décisions mal interprétées…), pas le nombre de Skills/fichiers. Test clé : reprendre un projet après trois semaines sans relire toutes les conversations.  
`20261031-000600-ref2:CAP-026`

**PROPOSITION (assistant)** — Quatre capacités à démontrer : compréhension progressive ; conservation correcte ; rétention/usage ; transformation décisions→travail concret.  
`20261031-000600-ref2:CAP-028`
