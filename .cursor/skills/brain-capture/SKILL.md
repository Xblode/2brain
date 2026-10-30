---
name: brain-capture
version: 0.1.3
description: >-
  Capture fidèle et progressive d'une conversation dans le registre Brain
  (entries.jsonl) : fenêtres d'échanges, multi-passes, intention/position,
  locators, grounding, audit final — sans valider de décisions ni modifier
  les documents. Utiliser pour /brain-capture, capture de conversation,
  ou extraction registre.
disable-model-invocation: true
---

# /brain-capture

Capture conversationnelle → registre Brain (production ou test-run isolé).

**Version** : 0.1.3

**Philosophie** : collecter la matière utile avant consolidation. Une information non validée reste utile. Une proposition assistant non approuvée se conserve. La capture n'est pas une sélection des « meilleures » idées.

## Avant de commencer

1. [references/capture-rules.md](references/capture-rules.md)
2. [references/registry-schema.md](references/registry-schema.md)
3. [references/source-attribution.md](references/source-attribution.md)
4. `brain/registry/SCHEMA.md`
5. Le registre **cible**
6. Contexte léger : `brain/docs/vision.md`, `project.md`, `architecture.md`, `workflow.md`, `integrations.md`

## Mode registre

| Mode | Cible |
| --- | --- |
| `production` | `brain/registry/entries.jsonl` (`run_id`: `production`) |
| `test-run` | `brain/registry/_test-runs/YYYYMMDD-HHMMSS/` (vide + SCHEMA) ; `run_id` = nom du dossier |

**Forcé `test-run`** si la source est un échantillon `brain/sources/conversation-reference-*.txt`. Jamais de génération comparative en production.

## Workflow

Ordre strict (ne pas inverser validation et corrections) :

1. **Brouillon des captures**
   1. Identifier la source exacte.
   2. Choisir le mode ; créer le dossier test-run si besoin ; fixer `run_id`.
   3. Lire schéma + registre cible.
   4. Comprendre le contexte projet.
   5. **Découper en fenêtres** (~5 échanges user/assistant). Chevauchement contextuel. **Même agent / même conversation / mémoire de travail globale**. Éviter les doublons inter-fenêtres.
   6. Pour chaque fenêtre, enchaîner **4 passes** (même agent) :
      - Passe 1 — informations (idées, suggestions, préférences, orientations, décisions, observations, questions, contraintes)
      - Passe 2 — actionable (tâches, jalons, objectifs, cadrage, roadmap, détails opérationnels)
      - Passe 3 — relations (réponses, corrections, précisions, contradictions, évolutions, approbations partielles, rejets)
      - Passe 4 — contexte d'autonomie (explications, alternatives, raisons, exceptions, incertitudes)
   7. **Atomicité** : un élément identifiable par CAP ; lier plutôt que fusionner (voir capture-rules).
   8. Attribuer `author` (principal) + **`author_confidence`**, `type`, **`intention`**, `position` (`null` si non identifiable).
   9. Renseigner **`grounding`** (4 valeurs) et **`origin.locators[]`** pour tous les passages utilisés.
   10. Fixer `capture_ref` = `"{run_id}:{id}"` (et `uid` optionnel).
   11. Déterminer `validation` / `approved_by` / `approval_scope` **uniquement** sur preuves — anti-faux-explicit (orientations ambiguës → `none`).
   12. Contenu autonome : enrichir depuis la source si besoin ; ne pas inventer ; signaler l'inconnu.
   13. Relations utiles (`clarifies`/`contradicts` inclus ; usage strict ; cibles `CAP-NNN` locales au run).
2. **Audit final source↔registre** (complet, sans questions user) — voir section Audit.
3. **Appliquer TOUTES les corrections** avant validation : atomicité, enrichissement, couverture, relations, author, grounding, locators.
4. **Finaliser** `entries.jsonl` (append uniquement les nouvelles entrées ; pas de réécriture d'anciennes captures).
5. **Valider le registre final** :
   `python .cursor/skills/brain-capture/scripts/validate-registry.py <cible>/entries.jsonl --require-intention --json-out <cible>/validate.json`
6. **Garantir** que `validate.json` correspond au registre final.
7. Produire `AUDIT.md`, `COMPARISON.md` (test-run) et le **bilan template**.

**Règle** : aucun changement de registre **après** validation sans re-exécuter le validateur **et** régénérer `validate.json`.

## Audit final (obligatoire)

Avant finalisation / validation, l'agent confronte systématiquement la source au registre :

1. Couverture : thèmes / messages pertinents → CAP ou exclusion motivée (bruit).
2. Atomicité : fusions abusives ? splits manquants ?
3. Provenance : chaque CAP a-t-elle des `locators[]` non vides et exacts ?
4. Grounding / anti-faux-explicit : orientations ambiguës en `none` ?
5. Relations : contradictions étayées signalées ; pas de validation implicite via liens.
6. Toutes les corrections listées sont appliquées **avant** le validateur (étape Workflow 3–4).

### Template `AUDIT.md` (test-run / génération neuve)

```markdown
# AUDIT — capture <run_id>

| | |
| --- | --- |
| Source | <chemin> |
| Run | <chemin dossier> |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |

## Couverture source↔registre
| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |

## Atomicité et richesse
- Splits effectués :
- CAP courtes liées / enrichies :
- Incomplet signalé :

## Provenance
- Locators manquants corrigés : oui/non
- Multi-passages : oui/non/exemples

## Grounding et approbation
- Anti-faux-explicit vérifié :
- Ambiguës en `none` :

## Contradictions / tensions
- `contradicts` / `conflicts_with` posés :

## Corrections avant clôture
- Liste courte des fixes appliqués
```

## Trois couches de résultat

| Couche | Artefact | Rôle |
| --- | --- | --- |
| 1. Validation technique | `validate.json` + sortie validateur | Schéma, enums, ids, relations mécaniques, locators, cohérence structurelle |
| 2. Audit de capture | `AUDIT.md` | Couverture, atomicité, richesse, contradictions signalées |
| 3. Évaluation humaine | Revue utilisateur | Fidélité réelle aux intentions |

Le validateur Python **ne fait que (1)**. « OK » ≠ qualité sémantique.

## Checklist couverture

- Messages pertinents examinés ?
- Propositions assistant conservées ?
- Idées user conservées ?
- Réponses / corrections / contradictions reliées ?
- Infos distinctes séparées (atomicité) ?
- Sujets de cadrage détaillés **individuellement** ?
- Tâches / jalons potentiels identifiés (`intention: task|milestone`) ?
- Contraintes / règles opérationnelles présentes ?
- Nuances et incertitudes préservées ?
- Contenus autonomes / enrichis depuis la source ?
- `locators[]`, `run_id`, `capture_ref`, `grounding`, `author_confidence` renseignés ?
- Bruit de test / instructions de capture exclus du métier ?
- Audit final + `AUDIT.md` produits ?

## Interdictions

- Valider une décision ; écrire docs / ClickUp ; fusionner / renuméroter / réécrire contenu existant.
- Génération comparative en production.
- Transformer citation / analyse / correction en approbation.
- Convertir `favorable` / `endorsed` / `selected` / `confirmed` en `explicit_user_approval` sans preuve d'approbation formelle.
- Inventer des signatures plateforme.
- Lancer `/brain-review` ou autre workflow (Review / Sync / graphe hors scope).
- Script `_gen.py` pour générer les captures (skill-direct uniquement).

## Bilan attendu (obligatoire)

Après chaque `/brain-capture`, produire **exactement** ce bilan (même ordre, mêmes libellés). Remplir chaque ligne ; mettre `0` ou `—` si vide. Ne pas ajouter de sections hors template.

```markdown
### Bilan `/brain-capture`

| | |
| --- | --- |
| Source | <chemin ou « conversation courante »> |
| Mode | `production` \| `test-run` |
| Cible | <chemin entries.jsonl> |
| run_id | <run_id> |
| IDs ajoutés | CAP-XXX → CAP-YYY (N) |
| Validateur | OK \| KO (`--require-intention` + `--json-out`) |
| validate.json | oui/non |
| AUDIT.md | oui/non |
| Production touchée | non \| oui |

**Couches** — technique : OK/KO · audit capture : fait/partiel · éval. humaine : en attente/—

**Comptes** — total N · explicit E · none F · `set` S · partial P · `position` null Z

**Intentions** — <intention: count ; …>

**Grounding** — explicit Ge · contextual Gc · interpreted Gi · uncertain Gu

**Actionnable** — milestones M · tasks T · cadrage individuels C

**Relations** — R liens utiles · clarifies/contradicts : n · doubles évités : oui/non/partiel

**Ambigus** — <CAP-… + motif court ; ou « aucun »>

**Bruit exclu** — <CAP-… méta/test ; ou « aucun »>

**Fenêtres** — W traitées · mémoire globale : oui

**Couverture** — messages pertinents : OK/partiel · propositions conservées : OK/partiel · nuances : OK/partiel · locators : OK/partiel

<!-- test-run seulement : -->
**Test-run** — COMPARISON.md : oui/non · type : smoke-régression \| corpus \| Test-A · vs réf. <run ou —>
```

En **production**, omettre la ligne `Test-run`. En **test-run**, la remplir et détailler la grille dans `COMPARISON.md` (pas dans le bilan).

**Rappel** : un smoke sur source 3 = **régression ciblée**, pas une preuve de généralisation (voir test-protocol — Test A).

## Ressources

- [references/capture-rules.md](references/capture-rules.md)
- [references/registry-schema.md](references/registry-schema.md)
- [references/source-attribution.md](references/source-attribution.md)
- [references/test-protocol.md](references/test-protocol.md)
- [scripts/validate-registry.py](scripts/validate-registry.py)
