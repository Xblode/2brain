# Protocole de test reproductible — `/brain-capture`

## Source de référence

Conversation ayant produit les 69 captures initiales :

| Propriété | Valeur |
| --- | --- |
| Fichier local | `C:\Users\planc\Documents\_Projets\Perso\2nd brain\2nd-brain\brain\conversation-référence-1.txt` |
| Origin registre | `chatgpt-share` / `https://chatgpt.com/share/6ae3fb90-b6bc-83ed-b432-22f8963f96d8` |
| Taille (~) | 78 341 octets / 1452 lignes |
| Nom stable | `conversation-référence-1.txt` |

Ce fichier n'est **pas** dans le dépôt `2brain` au moment du V1. Pour un test isolé, copier sans écraser :

```text
brain/sources/conversation-reference-1.txt
```

Ne jamais utiliser `entries.jsonl` comme source de re-capture.

## Procédure (chaque version du Skill)

1. Utiliser **exactement** la même source (`conversation-référence-1.txt` ou sa copie locale).
2. Créer un emplacement temporaire isolé, ex. :
   `brain/registry/_test-runs/YYYYMMDD-HHMMSS/`
3. Y placer une copie vide ou minimale de travail (`entries.jsonl` vide + SCHEMA).
4. Lancer `/brain-capture` en indiquant la source et le registre temporaire.
5. **Ne jamais** écraser `brain/registry/entries.jsonl` ni les archives `_test-runs/` précédentes.
6. Valider :
   `python .cursor/skills/brain-capture/scripts/validate-registry.py <chemin-temporaire>/entries.jsonl`
7. Comparer qualitativement avec les générations précédentes (et/ou les 69 captures de référence).

## Critères d'évaluation

- couverture des informations utiles ;
- informations perdues ;
- faux positifs ;
- attribution auteur correcte ;
- validations injustifiées ;
- questions restées ouvertes ;
- doublons potentiels ;
- relations pertinentes ;
- préservation des évolutions ;
- fidélité des preuves ;
- cohérence des métadonnées.

**Ne pas** chercher à reproduire exactement 69 entrées. Qualité et fidélité > nombre.

## Premier test manuel (checklist)

```text
[ ] Source = conversation-référence-1.txt (chemin ci-dessus ou copie brain/sources/)
[ ] Registre de sortie = dossier _test-runs/ isolé (pas le registre vivant)
[ ] Invoker /brain-capture avec ces chemins explicites
[ ] Exécuter validate-registry.py sur le résultat
[ ] Rédiger une note de comparaison (couverture, auteurs, validations, relations)
[ ] Archiver la note à côté de la génération ; ne pas écraser
```

## Commande validateur

```bash
python .cursor/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl
python .cursor/skills/brain-capture/scripts/validate-registry.py path/to/test/entries.jsonl --json
```
