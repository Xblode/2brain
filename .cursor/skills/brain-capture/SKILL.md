---
name: brain-capture
version: 0.1.4
description: >-
  Capture fidèle et progressive d'une conversation dans le registre Brain
  (entries.jsonl) : fenêtres d'échanges, multi-passes, intention→type, locators,
  refs/URLs, grounding, audit final — sans valider de décisions ni modifier
  les documents. Utiliser pour /brain-capture, capture de conversation,
  ou extraction registre.
disable-model-invocation: true
---

# /brain-capture

Capture conversationnelle → registre Brain (production ou test-run isolé).

**Version** : 0.1.4

**Philosophie** : collecter la matière utile avant consolidation. Une information non validée reste utile. Une proposition assistant non approuvée se conserve. La capture n'est pas une sélection des « meilleures » idées.

## Avant de commencer

1. [references/capture-rules.md](references/capture-rules.md)
2. [references/registry-schema.md](references/registry-schema.md)
3. [references/source-attribution.md](references/source-attribution.md)
4. `brain-main/conventions/taxonomy.md` (taxonomies + mapping intention→type + spaces)
5. `brain/registry/SCHEMA.md`
6. Le registre **cible**
7. Contexte léger : `brain/docs/vision.md`, `project.md`, `architecture.md`, `workflow.md`, `integrations.md`

## Mode registre

Le mode est **choisi explicitement** selon la cible demandée (par l’utilisateur ou la consigne de session). **Aucune** bascule automatique selon le nom de fichier source.

| Mode | Cible | `run_id` |
| --- | --- | --- |
| `production` | `brain/registry/entries.jsonl` | `production` |
| `test-run` | `lab/_test-runs/MMDD-HHMM/` (dossier **vide** + copie SCHEMA si besoin) | = nom du dossier (ex. `1031-1512`) |

### Création d’un test-run

1. Calculer `MMDD-HHMM` (heure locale).
2. Si le dossier existe déjà → **ne jamais écraser**. Essayer `MMDD-HHMM-2`, puis `-3`, etc., jusqu’à un nom libre.
3. Créer le dossier vide ; y placer `entries.jsonl` (nouveau) ; `run_id` = nom final du dossier.
4. Optionnel : `COMPARISON.md` en fin de run.

Jamais de génération comparative artificielle en production. Skill-direct uniquement (pas de `_gen.py` pour fabriquer les CAP).

### Production séquentielle

- **Append only** : ajouter les nouvelles lignes ; **ne jamais** modifier / renuméroter / supprimer d’anciennes CAP.
- Prochain `id` = `CAP-` + (max N existant + 1), zero-pad ≥ 3.
- `capture_ref` = `production:CAP-NNN`.

## Workflow

Ordre strict (ne pas inverser validation et corrections) :

1. **Brouillon des captures**
   1. Identifier la source exacte.
   2. **Choisir le mode** (explicite) ; créer le dossier test-run si besoin ; fixer `run_id`.
   3. Lire schéma + taxonomie + registre cible (pour IDs existants en production).
   4. Comprendre le contexte projet.
   5. **Découper en fenêtres** (~5 échanges user/assistant). Chevauchement contextuel. **Même agent / même conversation / mémoire de travail globale**. Éviter les doublons inter-fenêtres.
   6. Pour chaque fenêtre, enchaîner **4 passes** (même agent) :
      - Passe 1 — informations
      - Passe 2 — actionable
      - Passe 3 — relations
      - Passe 4 — contexte d’autonomie + **références/URLs**
   7. **Atomicité** (capture-rules) : lier plutôt que fusionner.
   8. Choisir **`intention`** (primaire) → appliquer le **mapping → `type`** (taxonomy) ; `position` (`null` si non identifiable) ; `author` + `author_confidence`.
   9. Choisir **`space`** selon taxonomy (défaut `atelier` si incertitude ; pas de `referentiel` auto pour proposition non établie).
   10. Renseigner **`grounding`**, **`origin.locators[]`**, et **`refs[]`** pour toute URL / référence concrète de la source liée à la CAP.
   11. Fixer `capture_ref` = `"{run_id}:{id}"`.
   12. `validation` / `approved_by` / `approval_scope` **uniquement** sur preuves — anti-faux-explicit.
   13. Contenu autonome + titre spécifique (retrouvabilité) ; ne pas inventer.
   14. Relations utiles (priorités capture-rules) ; cibles `CAP-NNN` locales au **fichier** (en production = tout le living).
2. **Audit final source↔registre** — voir section Audit (inclure checklist **URLs**).
3. **Appliquer TOUTES les corrections** avant validation.
4. **Finaliser** `entries.jsonl` (append uniquement).
5. **Valider** :
   `python .cursor/skills/brain-capture/scripts/validate-registry.py <cible>/entries.jsonl --require-intention --json-out <cible-ou-run>/validate.json`
6. Garantir que `validate.json` correspond au registre final validé.
7. Produire `AUDIT.md` ; `COMPARISON.md` si test-run ; **bilan template**.

**Règle** : aucun changement de registre **après** validation sans re-exécuter le validateur **et** régénérer `validate.json`.

## Audit final (obligatoire)

1. Couverture thèmes / messages → CAP ou exclusion motivée.
2. Atomicité : fusions abusives ? splits manquants ?
3. Provenance : `locators[]` non vides et exacts ?
4. **URLs / refs** : toute URL source pertinente est-elle dans `refs[]` **et** dans `content` (pas « lien fourni ») ?
5. Grounding / anti-faux-explicit ; mapping intention→type respecté ?
6. Space cohérent (pas de `referentiel` abusif) ?
7. Relations prioritaires posées ; pas de validation implicite via liens.
8. Corrections appliquées **avant** le validateur.

### Template `AUDIT.md`

```markdown
# AUDIT — capture <run_id>

| | |
| --- | --- |
| Source | <chemin> |
| Cible | <chemin entries.jsonl> |
| Couche | Audit de capture (≠ validation technique ≠ évaluation humaine) |

## Couverture source↔registre
| Zone / thème | Statut | CAP(s) / remarque |
| --- | --- | --- |

## Atomicité et richesse
- Splits effectués :
- CAP courtes liées / enrichies :
- Incomplet signalé :

## Provenance et refs
- Locators : oui/non
- URLs/refs conservées : oui/non/exemples
- Multi-passages : oui/non

## Grounding, mapping, space, approbation
- intention→type OK :
- Anti-faux-explicit :
- Space (atelier par défaut) :

## Contradictions / tensions
- Relations posées :

## Corrections avant clôture
- Liste courte
```

## Trois couches de résultat

| Couche | Artefact | Rôle |
| --- | --- | --- |
| 1. Validation technique | `validate.json` + validateur | Schéma, enums, mapping, ids, relations, locators, refs structure |
| 2. Audit de capture | `AUDIT.md` | Couverture, atomicité, URLs, contradictions |
| 3. Évaluation humaine | Revue utilisateur | Fidélité réelle |

Le validateur Python **ne fait que (1)**. « OK » ≠ qualité sémantique.

## Checklist couverture

- Messages pertinents examinés ?
- Propositions assistant conservées ?
- Atomicité + titres spécifiques ?
- URLs / chemins / IDs dans `refs[]` + content ?
- Mapping intention→type appliqué ?
- Space non abusif ?
- Tâches / jalons / cadrage individuels ?
- Relations utiles (réponses, précisions, contradictions) ?
- `locators[]`, `run_id`, `capture_ref`, `grounding`, `author_confidence` ?
- Bruit de test exclu ?
- Audit final produit ?

## Interdictions

- Valider une décision ; écrire docs / ClickUp ; fusionner / renuméroter / réécrire contenu existant.
- Forcer test-run uniquement parce que la source s’appelle `conversation-reference-*.txt`.
- Génération comparative artificielle / `_gen.py` pour fabriquer les CAP.
- Transformer citation / analyse / correction en approbation.
- Convertir `favorable` / `endorsed` / `selected` / `confirmed` en `explicit_user_approval` sans preuve.
- Remplacer une URL par une périphrase.
- Inventer des signatures plateforme.
- Lancer Review / Sync / Search (hors scope).

## Bilan attendu (obligatoire)

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

**Refs** — URLs/ancres conservées : U · formulaires « lien fourni » évités : oui/non

**Actionnable** — milestones M · tasks T · cadrage individuels C

**Relations** — R liens utiles · clarifies/contradicts : n · doubles évités : oui/non/partiel

**Ambigus** — <CAP-… + motif court ; ou « aucun »>

**Bruit exclu** — <… ; ou « aucun »>

**Fenêtres** — W traitées · mémoire globale : oui

**Couverture** — messages pertinents : OK/partiel · propositions conservées : OK/partiel · nuances : OK/partiel · locators : OK/partiel · refs : OK/partiel

<!-- test-run seulement : -->
**Test-run** — COMPARISON.md : oui/non · type : smoke-régression \| corpus \| Test-A · vs réf. <run ou —>
```

En **production**, omettre la ligne `Test-run`.

## Ressources

- [references/capture-rules.md](references/capture-rules.md)
- [references/registry-schema.md](references/registry-schema.md)
- [references/source-attribution.md](references/source-attribution.md)
- [references/test-protocol.md](references/test-protocol.md)
- [references/manual-production-sequence.md](references/manual-production-sequence.md)
- [scripts/validate-registry.py](scripts/validate-registry.py)
- `brain-main/conventions/taxonomy.md`
