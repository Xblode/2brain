# Phase 2 — Vérification des captures (capability test)

| | |
| --- | --- |
| Date | 2026-10-31 |
| Runs | `20261031-000600-ref1`, `…-ref2`, `…-ref3` |
| Validateur | `validate-registry.py --require-intention` (rejoué) |

## Synthèse technique

| Run | CAP | Relations | JSONL | IDs uniques | Locators | Champs 0.1.3 | Validateur bloquant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ref1 | 117 | 165 | OK | OK | tous présents | OK | OK (16 WARN réciprocité) |
| ref2 | 120 | 114 | OK | OK | tous présents | OK | OK (37 WARN réciprocité) |
| ref3 | 112 | 152 | OK | OK | tous présents | OK | OK (1 WARN résumé) |

Aucun ID dupliqué, aucune cible de relation hors run, aucun `capture_ref` incohérent, aucun contenu < 40 caractères.

## Auteurs

| Run | user | assistant |
| --- | --- | --- |
| ref1 | 49 | 68 |
| ref2 | 30 | 90 |
| ref3 | 21 | 91 |

Déséquilibre assistant croissant (ref2/ref3 = sessions plus « conception skill / audits » portées par l’assistant).

## Validation / grounding

| Run | explicit | none | grounding explicit | contextual | interpreted |
| --- | --- | --- | --- | --- | --- |
| ref1 | 6 | 111 | 107 | 6 | 4 |
| ref2 | 6 | 114 | 111 | 9 | 0 |
| ref3 | 12 | 100 | 108 | 4 | 0 |

## Points d’attention sémantiques (hors validateur)

1. **Réciprocité relations** : nombreuses WARN `clarifies`/`answers` sans inverse — structure navigable mais graphe asymétrique.
2. **space=referentiel sans explicit** : beaucoup de REVIEW — conventions proposées placées en référentiel avant approbation formelle.
3. **Atomicité** : 2 CAP ref3 très longues multi-points (`CAP-009`, `CAP-096`) — risque de fusion thématique.
4. **Scripts temporaires** : ref1/ref2 ont utilisé des scripts de sérialisation pendant la génération puis les ont retirés — écart au protocole « skill-direct / pas de _gen » (à noter comme limite d’expérience, pas invalidation automatique du JSONL).
5. **Couverture auto-déclarée** : les `AUDIT.md` affirment OK large ; Phase 4 devra confronter sources pour ne pas confondre audit de capture et vérité.

## Verdict Phase 2

Les trois registres sont **techniquement valides 0.1.3**. La qualité sémantique et la couvrabilité réelle restent à éprouver via reconstruction (Phase 3) puis comparaison (Phase 4).
