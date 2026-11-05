---
name: brain-onboarding
version: 0.1.0
description: >-
  Remplit brain/docs/ (VISION, PROJECT, REQUIREMENTS, ARCHITECTURE, WORKFLOW)
  avec le projet, par propositions marquées confirmé, hypothèse ou à compléter,
  écrites seulement après validation explicite. Utiliser pour /brain -o.
disable-model-invocation: true
---

# /brain -o

Onboarding : proposer le contenu de `brain/docs/` d'après le projet, sans rien décider. Ce skill est appelé par `/brain -o` (voir `brain-main/bootstrap/README.md`). Il ne reprend aucune convention : `brain-main/conventions/METADATA.md` se lit avant toute écriture (voir l'étape 7).

## Garde-fous

- Une proposition reste une proposition : rien n'est écrit avant la validation explicite de ce qui vient d'être présenté, donnée dans le message qui suit.
- Ne rien décider, ne rien coder. Ne modifier ni le registre, ni `brain-main/`, ni les fichiers du projet hors `brain/docs/`.
- Ne jamais remplacer une information confirmée sans le dire et sans accord explicite.
- Une réponse manquante ne bloque pas : l'élément reste « À compléter. ».
- Sans Bash (orchestrateur du dépôt 2brain) : déléguer l'écriture à l'agent `worker-sonnet` s'il existe, avec le contenu validé tel quel.

## Étapes

1. **État.** Lire `status.py --json` (lancé par le skill du compte). Si `brain` est `absent` : dire de faire `/brain -i` et s'arrêter. Noter les documents listés dans `documents_a_completer_noms`. Si le compteur est 0 et que rien n'est à reprendre : le dire et s'arrêter.
2. **Lire les documents.** Lire les 5 documents de `brain/docs/` : réponses déjà notées en section 3 (« Informations confirmées »), manques restants. Ce qui est déjà confirmé n'est pas refait.
3. **Projet avec des fichiers.** Lecture ciblée, sans parcours exhaustif : README, manifestes (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.), structure de premier niveau, documentation existante (`docs/`, `AGENTS.md`, `CLAUDE.md`). Chaque fait relevé garde sa source (fichier).
4. **Projet vide.** Poser des questions adaptées, par document, en partant des réponses déjà notées. Les poser par petits groupes. Ne pas inventer de réponse.
5. **Proposer, document par document.** Pour chacun des 5 documents, présenter le contenu proposé par section. Chaque élément porte l'un de ces marqueurs :
   - `confirmé` : avec sa source, soit un fichier lu, soit une réponse de l'humain ;
   - `hypothèse` : déduit sans preuve directe, à valider ;
   - `à compléter` : information absente.
   Présenter les 5 documents dans l'ordre VISION, PROJECT, REQUIREMENTS, ARCHITECTURE, WORKFLOW.
6. **Valider.** Demander : lesquels de ces contenus écrire ? Rien n'est écrit sur une approbation générale ou passée.
7. **Écrire** seulement ce qui est validé, dans les sections 3 à 5 du document concerné, en gardant le plan existant. Écrire un `confirmé` comme information confirmée, un `hypothèse` comme hypothèse déclarée, un `à compléter` comme « À compléter. ». Avant d'écrire, lire `brain-main/conventions/METADATA.md` §4.8, §4.11 et §8, puis mettre à jour `updated` et `version` selon ces règles.
8. **Bilan.** Relancer `status.py --json`, indiquer les documents qui contiennent encore « À compléter », et rappeler que `/brain -o` peut être relancé dans une autre session.

## Plusieurs sessions

`/brain -o` se relance autant que nécessaire. À chaque lancement : lire l'état, indiquer les manques restants, ne proposer que ce qui manque ou ce que l'humain demande de revoir. Ce qui est confirmé n'est ni redemandé ni réécrit.

## Hors périmètre

Décider d'une architecture, d'une exigence ou d'un module ; activer un outil ; capturer une session (c'est `/brain -c`) ; modifier une convention.
