# Protocole de test reproductible — `/brain-capture`

## Source de référence

Conversation ayant produit les 69 captures initiales :

| Propriété | Valeur |
| --- | --- |
| Fichier local (origine) | `conversation-référence-1.txt` |
| Copie dépôt | `brain/sources/conversation-reference-1.txt` |
| Origin registre | `chatgpt-share` / `https://chatgpt.com/share/6ae3fb90-b6bc-83ed-b432-22f8963f96d8` |
| Nom stable | `conversation-reference-1.txt` |

Ne jamais utiliser `entries.jsonl` comme source de re-capture.

## Mode registre (forcé pour la référence)

Au démarrage de `/brain-capture`, choisir explicitement la cible :

| Mode | Cible |
| --- | --- |
| `production` | `brain/registry/entries.jsonl` |
| `test-run` | Nouveau dossier `brain/registry/_test-runs/YYYYMMDD-HHMMSS/` |

**Règle forcée** : si la source est `brain/sources/conversation-reference-1.txt` (ou équivalent référence), **toujours** `test-run`. Ne jamais écrire une génération comparative dans le registre de production.

Le validateur s'exécute sur le **chemin de la cible choisie**, jamais un chemin hardcodé.

## Procédure (chaque version du Skill)

1. Utiliser **exactement** la même source (`conversation-reference-1.txt`).
2. Créer un emplacement temporaire isolé :
   `brain/registry/_test-runs/YYYYMMDD-HHMMSS/`
3. Y placer `entries.jsonl` vide + copie de `SCHEMA.md`.
4. Lancer `/brain-capture` en mode `test-run` avec cette source et ce registre.
5. **Ne jamais** écraser `brain/registry/entries.jsonl` ni les archives `_test-runs/` précédentes (ex. `20261030-042859` = archive 0.1.0).
6. Valider :
   `python .cursor/skills/brain-capture/scripts/validate-registry.py <chemin-temporaire>/entries.jsonl`
7. Rédiger `COMPARISON.md` **factuel** (counts, répartition `approval_scope`, tags `approval_global_partial`, relations `resolves`, écarts connus vs génération précédente) — **sans** scores subjectifs non vérifiés ni auto-notes « pertes faibles » non prouvées.

## Critères d'évaluation

- couverture des informations utiles ;
- attribution auteur correcte ;
- validations justifiées (exprimer ≠ approuver) ;
- `approval_scope` cohérent (`item` / `set` / `null`) ;
- pas d'approbation héritée d'un accord global partiel sans tag ;
- questions restées ouvertes ;
- doublons potentiels (non fusionnés) ;
- relations pertinentes (`resolves` vs `conflicts_with` actif ; pas de double evolves+supersedes) ;
- préservation des évolutions ;
- fidélité des preuves ;
- cohérence des métadonnées (validateur vert).

**Ne pas** chercher à reproduire exactement 69 entrées. Qualité et fidélité > nombre.

## Checklist test manuel

```text
[ ] Source = brain/sources/conversation-reference-1.txt
[ ] Mode = test-run (forcé pour cette source)
[ ] Registre de sortie = dossier _test-runs/ isolé (pas le registre vivant)
[ ] Invoker /brain-capture avec ces chemins explicites
[ ] Exécuter validate-registry.py sur le résultat
[ ] Rédiger COMPARISON.md factuel (approval_scope, resolves, écarts)
[ ] Archiver à côté de la génération ; ne pas écraser les runs antérieurs
```

## Commande validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py path/to/test/entries.jsonl --json
```
