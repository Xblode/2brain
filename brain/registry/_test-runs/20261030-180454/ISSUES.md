# Issues — test-run 20261030-180454 (0.1.2)

## Bloquants validateur

Aucun (`--require-intention` OK).

## Couverture (manques confirmés)

1. **Taxonomie éléments** (Core, Module, Instance, Agent, Skill, Rule, Template, Workflow) — présente en 061941 CAP-028, absente ici comme entrée autonome.
2. **Mapping espaces logiques ↔ local ↔ ClickUp** — 061941 CAP-042 manquant.
3. **Consultation ClickUp** (Inbox vide, docs vides) — 061941 CAP-066 manquant.
4. **Liste documentaire initiale** isolée — partiellement absorbée dans CAP-065 ; évolution op/onboarding couverte.

## Ambiguïtés conservées (volontaires)

| CAP | Sujet |
| --- | --- |
| CAP-009 | B ou C non tranché (`ambiguous-b-or-c`) |
| CAP-029 | Silence parfois = OK ≠ validation formelle (`ambiguity-silence`) |
| CAP-047 | « valide certaines choses » (`ambiguous-validation-scope`) |
| CAP-007 + plusieurs | `selected`/`confirmed` + explicit → REVIEW soft (dimensions distinctes OK, à relire) |

## Approbations

- Aucun `approval_scope: set` (correct : pas d’approbation explicite d’un ensemble identifiable).
- 6× `approval_global_partial` : CAP-014, 016, 018, 026, 027, 045.
- ClickUp arbo projet = observation (CAP-043), pas convention explicit — correction vs 061941 CAP-039.

## Bruit

- CAP-077 : exercice méta-test (`test-noise`) — hors connaissance métier durable.

## Production

- `brain/registry/entries.jsonl` **non modifié**.
- Compatibilité : validateur sans `--require-intention` OK sur le registre vivant.

## Hors périmètre

- Échantillon 2 non capturé (fichier réel, non mélangé).
- Aucun commit / push.
