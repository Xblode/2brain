---
metadata_version: 1
title: Agent Router
type: specification
description: Spécifie le routage de la délégation entre un orchestrateur unique et des workers d'exécution.
summary: Un orchestrateur unique dialogue avec l'humain, décide, rédige des briefs, délègue à des workers et contrôle leurs rapports. Ce document fixe les rôles, les profils, les critères de sélection, le format du brief et du rapport, le contrôle, la trace et le contrat qu'un adaptateur doit respecter. Il ne contient aucun nom d'outil ni de modèle.
version: "0.1.0"
status: draft
created: "2026-11-05"
updated: "2026-11-05"
scope:
  level: universal
  targets: [brain-instances]
depends_on:
  - "brain-main/conventions/METADATA.md"
tags:
  - routing
  - agents
  - delegation
---

# Agent Router

Spécification universelle de routage. Un adaptateur propre à un outil l'applique ; il ne la copie pas. Les sections sont numérotées pour que les autres fichiers y renvoient.

## 1. Rôles et profils

**Orchestrateur** : seul interlocuteur de l'humain. Il dialogue, analyse, arbitre, lit de façon ciblée, rédige les briefs, contrôle les rapports et consolide. Il ne modifie aucun fichier et n'exécute aucune commande. Il répond de la cohérence du résultat final.

**Worker** : exécute une mission décrite par un brief. Il ne délègue pas, ne décide pas de l'architecture, n'invente pas d'hypothèse. Il s'arrête quand il manque une information.

| Profil | Pour |
| --- | --- |
| `strategic` | Coordination, arbitrage, contrôle qualité |
| `standard` | Développement, refactoring, audit, analyse approfondie |
| `light` | Recherche ciblée, extraction, vérification, correction mineure |

`strategic` est réservé à l'orchestrateur. Les workers relèvent de `standard` ou `light`.

## 2. Sélection

S'arrêter au premier « oui » :

1. Répondre avec ce qui est connu ou une lecture ciblée, sans rien modifier ? L'orchestrateur répond, sans délégation.
2. Micro-tâche (un fichier, résultat évident) ? Une délégation à `light`, sans contre-vérification.
3. Résultat vérifiable mécaniquement, sans jugement ? `light`.
4. Sinon, `standard`.

- Doute entre `light` et `standard` : `light` seulement si l'échec coûte peu.
- Échec de `light` : une reprise par `standard`, puis retour à l'humain.
- Parallèle : deux workers au plus, sans dépendance de résultat ni fichier commun.

### 2.1 Critères

| Critère | Lecture |
| --- | --- |
| Complexité | Nombre de fichiers et de décisions à prendre |
| Type de travail | Lecture, modification, vérification |
| Compétences | Jugement ou application d'une règle |
| Coût | Prix du modèle × volume attendu, y compris la reprise en cas d'échec |
| Contexte nécessaire | Peut-il tenir dans un brief ? |
| Parallélisation | Indépendance réelle |

## 3. Brief

Selon le besoin :

- objectif ;
- périmètre ;
- fichiers concernés ;
- documents précis à lire, avec la section ;
- contraintes citées avec leur référence ;
- actions autorisées ;
- résultat attendu et critères de réussite, dont les vérifications à exécuter.

Pas d'historique de la conversation : le brief se suffit.

## 4. Rapport

Le worker rend, dans cet ordre :

1. statut : `done`, `partial` ou `blocked` ;
2. travail effectué ;
3. résultats et preuves brutes ;
4. fichiers modifiés ;
5. difficultés, limites et points à décider.

Pas de journal d'exploration.

## 5. Connaissances

L'orchestrateur répond de la distribution des connaissances, sans tout lire lui-même. Il lit les métadonnées puis les sections utiles (METADATA §9.4), ou confie l'extraction d'un long document à `light`. Il transmet au worker la règle citée et sa référence. Un worker peut lire un document précis si le rapport coût/qualité le justifie.

## 6. Question en cours de mission

Le worker s'arrête et rend `blocked` avec ses questions. L'orchestrateur répond en reprenant ce même worker. S'il n'a pas la réponse, ou si une décision humaine est nécessaire, il sollicite l'humain.

## 7. Contrôle

- Sans modification : cohérence du rapport.
- Avec modification : vérifications exécutées dans la mission, sortie brute dans le rapport, puis lecture par l'orchestrateur des passages modifiés.
- Exception (risque élevé ou résultat douteux) : contre-vérification par un second worker.

## 8. Trace

Tâche, agent, statut, résultat, décisions, références. En V1, la trace figure dans la réponse finale et dans Git, sans nouveau registre. Aucun raisonnement interne dans le Second Brain.

## 9. Contrat d'adaptateur

Un adaptateur doit :

- interdire l'écriture et l'exécution à l'orchestrateur ;
- limiter ses cibles de délégation ;
- associer chaque profil à un modèle ;
- isoler le contexte des workers ;
- porter le format de rapport (§4) ;
- écrire ce qui n'est pas garanti.

Un outil sans adaptateur travaille normalement selon `AGENTS.md`, sans routage, avec les mêmes règles de registre.
