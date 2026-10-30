---
name: brain-capture
description: >-
  Capture les informations utiles d'une conversation dans le registre Brain
  (entries.jsonl) avec métadonnées, preuves et relations, sans valider de
  décisions ni modifier les documents. Utiliser quand l'utilisateur invoque
  /brain-capture, demande une capture de conversation, ou veut extraire des
  entrées registre depuis une source chat.
disable-model-invocation: true
---

# /brain-capture

Capture conversationnelle → registre `brain/registry/entries.jsonl` uniquement.

## Avant de commencer

Lire obligatoirement :

1. [references/capture-rules.md](references/capture-rules.md)
2. [references/registry-schema.md](references/registry-schema.md)
3. `brain/registry/SCHEMA.md`
4. `brain/registry/entries.jsonl` (état actuel)
5. Contexte léger : `brain/docs/vision.md`, `project.md`, `architecture.md`, `workflow.md`, `integrations.md`

## Workflow (obligatoire)

1. Identifier la source exacte de conversation (fichier, transcript, chat courant).
2. Lire le schéma et le registre existant.
3. Comprendre le contexte général du projet.
4. Identifier les passages qui apportent une information utile.
5. Extraire les candidats sans surcapturer.
6. Distinguer faits, observations, idées, propositions, décisions, conventions, tâches, questions et événements.
7. Identifier correctement l'auteur (`user` | `assistant`).
8. Déterminer le niveau de validation uniquement à partir de preuves.
9. Identifier les relations et les évolutions réellement utiles.
10. Préserver les nuances, conditions, exceptions, raisons, limites et éléments refusés.
11. Attribuer les métadonnées (`status: extracted` toujours).
12. Contrôler les doublons potentiels sans fusion automatique.
13. Vérifier les preuves (citation ou paraphrase fidèle ; jamais inventée).
14. Valider mécaniquement les nouvelles entrées :
    `python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl`
15. Corriger les erreurs détectées (métadonnées / relations uniquement sur le brouillon).
16. Ajouter uniquement les nouvelles entrées (append ; ne pas réécrire l'existant).
17. Présenter un bilan clair.

## Interdictions absolues

La capture ne doit jamais :

- valider une décision ;
- mettre à jour les documents de référence ;
- modifier ClickUp ;
- supprimer, fusionner ou renuméroter des entrées ;
- réécrire `content`, `title` ou `evidence` d'entrées existantes ;
- lancer un autre workflow (`/brain-review`, sync, etc.).

## Attribution et validation

- `author` = qui a exprimé l'information.
- `approved_by` = `user` seulement si accord explicite identifiable ; sinon `null`.
- Une proposition assistant reste `author: assistant` même si l'utilisateur l'approuve ensuite.
- Ne jamais déduire une approbation du silence ou de l'absence de contradiction.
- `validation: implicit` est historique ; ne plus l'attribuer automatiquement.
- En cas de doute : `validation: none`, `approved_by: null`, signaler pour vérification humaine.

## Bilan attendu

Après capture, présenter :

- source utilisée ;
- nombre d'entrées ajoutées (IDs) ;
- validations / `approved_by` retenus ;
- relations créées ;
- doublons potentiels détectés (non fusionnés) ;
- cas ambigus nécessitant vérification humaine ;
- résultat du validateur.

## Ressources

- Règles détaillées : [references/capture-rules.md](references/capture-rules.md)
- Schéma / relations : [references/registry-schema.md](references/registry-schema.md)
- Test reproductible : [references/test-protocol.md](references/test-protocol.md)
- Validateur : [scripts/validate-registry.py](scripts/validate-registry.py)
