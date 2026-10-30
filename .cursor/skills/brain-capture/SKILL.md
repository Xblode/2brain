---
name: brain-capture
version: 0.1.2
description: >-
  Capture fidèle et progressive d'une conversation dans le registre Brain
  (entries.jsonl) : fenêtres d'échanges, multi-passes, intention/position,
  preuves et relations — sans valider de décisions ni modifier les documents.
  Utiliser pour /brain-capture, capture de conversation, ou extraction registre.
disable-model-invocation: true
---

# /brain-capture

Capture conversationnelle → registre Brain (production ou test-run isolé).

**Philosophie** : collecter la matière utile avant consolidation. Une information non validée reste utile. Une proposition assistant non approuvée se conserve. La capture n'est pas une sélection des « meilleures » idées.

## Avant de commencer

1. [references/capture-rules.md](references/capture-rules.md)
2. [references/registry-schema.md](references/registry-schema.md)
3. `brain/registry/SCHEMA.md`
4. Le registre **cible**
5. Contexte léger : `brain/docs/vision.md`, `project.md`, `architecture.md`, `workflow.md`, `integrations.md`

## Mode registre

| Mode | Cible |
| --- | --- |
| `production` | `brain/registry/entries.jsonl` |
| `test-run` | `brain/registry/_test-runs/YYYYMMDD-HHMMSS/` (vide + SCHEMA) |

**Forcé `test-run`** si la source est `brain/sources/conversation-reference-1.txt` (ou autre échantillon de référence). Jamais de génération comparative en production.

## Workflow

1. Identifier la source exacte.
2. Choisir le mode ; créer le dossier test-run si besoin.
3. Lire schéma + registre cible.
4. Comprendre le contexte projet.
5. **Découper en fenêtres** (~5 échanges user/assistant = jusqu'à 5 messages user + leurs réponses). Chevauchement contextuel entre fenêtres. **Même agent / même conversation / mémoire de travail globale** — les fenêtres ne sont pas indépendantes. Éviter les doublons inter-fenêtres.
6. Pour chaque fenêtre, enchaîner **4 passes** (même agent) :
   - Passe 1 — informations (idées, suggestions, préférences, orientations, décisions, observations, questions, contraintes)
   - Passe 2 — actionable (tâches, jalons, objectifs, cadrage, roadmap, détails opérationnels)
   - Passe 3 — relations (réponses, corrections, précisions, contradictions, évolutions, approbations partielles, rejets)
   - Passe 4 — contexte d'autonomie (explications, alternatives, raisons, exceptions, incertitudes)
7. Attribuer `author`, `type`, **`intention` (obligatoire en 0.1.2)**, `position` (`null` si non identifiable).
8. Déterminer `validation` / `approved_by` / `approval_scope` **uniquement** sur preuves (voir capture-rules) — distinct de `position`.
9. Contenu autonome : compréhensible sans la source ; ne pas inventer ; signaler l'inconnu.
10. Relations utiles seulement (vocabulaire existant).
11. Contrôle de couverture (checklist ci-dessous) avant clôture.
12. Valider sur le **chemin cible** :
    `python .cursor/skills/brain-capture/scripts/validate-registry.py <cible>/entries.jsonl --require-intention`
13. Corriger le brouillon ; append uniquement les nouvelles entrées.
14. Produire le **bilan template** (section ci-dessous). En test-run : + `COMPARISON.md` (grille), pas dans le bilan.

## Checklist couverture

- Messages pertinents examinés ?
- Propositions assistant conservées ?
- Idées user conservées ?
- Réponses / corrections reliées ?
- Infos distinctes séparées (pas fusion abusives) ?
- Sujets de cadrage détaillés **individuellement** (pas seulement « il existe N sujets ») ?
- Tâches / jalons potentiels identifiés (`intention: task|milestone`) ?
- Contraintes / règles opérationnelles présentes ?
- Nuances et incertitudes préservées ?
- Contenus autonomes ?
- Bruit de test / instructions de capture exclus du métier ?

## Interdictions

- Valider une décision ; écrire docs / ClickUp ; fusionner / renuméroter / réécrire contenu existant.
- Génération comparative en production.
- Transformer citation / analyse / correction en approbation.
- Convertir `favorable` / `endorsed` / `selected` / `confirmed` en `explicit_user_approval` sans preuve d'approbation formelle.
- Lancer `/brain-review` ou autre workflow.

## Bilan attendu (obligatoire)

Après chaque `/brain-capture`, produire **exactement** ce bilan (même ordre, mêmes libellés). Remplir chaque ligne ; mettre `0` ou `—` si vide. Ne pas ajouter de sections hors template.

```markdown
### Bilan `/brain-capture`

| | |
| --- | --- |
| Source | <chemin ou « conversation courante »> |
| Mode | `production` \| `test-run` |
| Cible | <chemin entries.jsonl> |
| IDs ajoutés | CAP-XXX → CAP-YYY (N) |
| Validateur | OK \| KO (`--require-intention` si 0.1.2) |
| Production touchée | non \| oui |

**Comptes** — total N · explicit E · none F · `set` S · partial P · `position` null Z

**Intentions** — <intention: count ; …> (toutes les intentions présentes ; 0 omises OK si absentes)

**Actionnable** — milestones M · tasks T · cadrage individuels C

**Relations** — R liens utiles · doubles évités : oui/non/partiel

**Ambigus** — <CAP-… + motif court ; ou « aucun »>

**Bruit exclu** — <CAP-… méta/test ; ou « aucun »>

**Couverture** — messages pertinents : OK/partiel · propositions conservées : OK/partiel · nuances : OK/partiel

<!-- test-run seulement : -->
**Test-run** — COMPARISON.md : oui/non · scénarios A–H : OK/partiel/manque · vs réf. <run ou —>
```

En **production**, omettre la ligne `Test-run`. En **test-run**, la remplir et détailler la grille dans `COMPARISON.md` (pas dans le bilan).

## Ressources

- [references/capture-rules.md](references/capture-rules.md)
- [references/registry-schema.md](references/registry-schema.md)
- [references/test-protocol.md](references/test-protocol.md)
- [scripts/validate-registry.py](scripts/validate-registry.py)
