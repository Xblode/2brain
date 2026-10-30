---
name: brain-capture
version: 0.1.1
description: >-
  Capture les informations utiles d'une conversation dans le registre Brain
  (entries.jsonl) avec métadonnées, preuves et relations, sans valider de
  décisions ni modifier les documents. Utiliser quand l'utilisateur invoque
  /brain-capture, demande une capture de conversation, ou veut extraire des
  entrées registre depuis une source chat.
disable-model-invocation: true
---

# /brain-capture

Capture conversationnelle → registre Brain uniquement (production ou test-run isolé).

## Avant de commencer

Lire obligatoirement :

1. [references/capture-rules.md](references/capture-rules.md)
2. [references/registry-schema.md](references/registry-schema.md)
3. `brain/registry/SCHEMA.md`
4. Le registre **cible** (prod ou test-run)
5. Contexte léger : `brain/docs/vision.md`, `project.md`, `architecture.md`, `workflow.md`, `integrations.md`

## Mode registre (obligatoire au démarrage)

Choisir explicitement la cible avant toute extraction :

| Mode | Cible |
| --- | --- |
| `production` | `brain/registry/entries.jsonl` |
| `test-run` | Nouveau dossier `brain/registry/_test-runs/YYYYMMDD-HHMMSS/` (entries vide + copie SCHEMA) |

**Règle forcée** : si la source est `brain/sources/conversation-reference-1.txt` (ou équivalent référence), **toujours** `test-run`. Ne jamais écrire une génération comparative dans le registre de production.

Indiquer le mode et le chemin cible dans le bilan.

## Workflow (obligatoire)

1. Identifier la source exacte de conversation (fichier, transcript, chat courant).
2. Choisir le mode registre (`production` | `test-run`) selon les règles ci-dessus ; créer le dossier test-run si besoin.
3. Lire le schéma et le registre cible.
4. Comprendre le contexte général du projet.
5. Identifier les passages qui apportent une information utile.
6. Extraire les candidats sans surcapturer.
7. Distinguer faits, observations, idées, propositions, décisions, conventions, tâches, questions et événements.
8. Identifier correctement l'auteur (`user` | `assistant`).
9. Déterminer `validation`, `approved_by` et `approval_scope` uniquement à partir de preuves (voir ci-dessous).
10. Identifier les relations et les évolutions réellement utiles (`resolves` vs `conflicts_with` actif ; pas de double evolves+supersedes).
11. Préserver les nuances, conditions, exceptions, raisons, limites et éléments refusés.
12. Attribuer les métadonnées (`status: extracted` toujours).
13. Contrôler les doublons potentiels sans fusion automatique.
14. Vérifier les preuves (citation ou paraphrase fidèle ; jamais inventée).
15. Valider mécaniquement les nouvelles entrées sur le **chemin cible** :
    `python .cursor/skills/brain-capture/scripts/validate-registry.py <chemin-cible>/entries.jsonl`
16. Corriger les erreurs détectées (métadonnées / relations uniquement sur le brouillon).
17. Ajouter uniquement les nouvelles entrées (append ; ne pas réécrire l'existant en production).
18. Présenter un bilan clair.

## Interdictions absolues

La capture ne doit jamais :

- valider une décision ;
- mettre à jour les documents de référence ;
- modifier ClickUp ;
- supprimer, fusionner ou renuméroter des entrées ;
- réécrire `content`, `title` ou `evidence` d'entrées existantes ;
- écrire une génération comparative dans le registre de production ;
- lancer un autre workflow (`/brain-review`, sync, etc.).

## Attribution, validation et `approval_scope`

- `author` = qui a exprimé l'information.
- `approved_by` = `user` seulement si accord explicite identifiable ; sinon `null`.
- `approval_scope` : `item` (cette capture) | `set` (bloc source clairement délimité et cité) | `null`.
- `explicit_user_approval` **uniquement** si `approval_scope` ∈ {`item`, `set`} et `approved_by: user`.
- Accords « bonne base » / « d'accord globalement » avec réserves → `none` / `null` / `null` + tag `approval_global_partial`.
- Exprimer ≠ approuver : observation / event / idea user → `none` ; décision / convention user claire → `explicit` + `item` ; proposition user seulement si orientation retenue claire.
- Une proposition assistant reste `author: assistant` même si l'utilisateur l'approuve ensuite.
- Ne jamais déduire une approbation du silence ou de l'absence de contradiction.
- `validation: implicit` est historique ; ne plus l'attribuer automatiquement.
- En cas de doute : `validation: none`, `approved_by: null`, `approval_scope: null`, signaler pour vérification humaine.

## Bilan attendu

Après capture, présenter :

- source utilisée ;
- **mode registre** et chemin cible ;
- nombre d'entrées ajoutées (IDs) ;
- validations / `approved_by` / `approval_scope` retenus ;
- tags `approval_global_partial` ;
- relations créées (dont `resolves`) ;
- doublons potentiels détectés (non fusionnés) ;
- cas ambigus nécessitant vérification humaine ;
- résultat du validateur sur le chemin cible.

## Ressources

- Règles détaillées : [references/capture-rules.md](references/capture-rules.md)
- Schéma / relations : [references/registry-schema.md](references/registry-schema.md)
- Test reproductible : [references/test-protocol.md](references/test-protocol.md)
- Validateur : [scripts/validate-registry.py](scripts/validate-registry.py)
