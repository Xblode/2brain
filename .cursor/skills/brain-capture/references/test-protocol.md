# Protocole de test — `/brain-capture` 0.1.2

## Échantillons

| Échantillon | Fichier | Rôle |
| --- | --- | --- |
| 1 | `brain/sources/conversation-reference-1.txt` | Référence principale de comparaison |
| 2 | `brain/sources/conversation-reference-2.txt` | Suite de conception (présent dans le dépôt) — **indépendant** ; hors comparaison principale 0.1.2 |

Ne pas créer de fichier source vide. Ne pas mélanger les deux échantillons.

## Référence sémantique

Comparaison principale vs : `brain/registry/_test-runs/20261030-061941/`

Ne **pas** utiliser `20261030-045232` (transformation, pas re-capture).

## Procédure (échantillon 1)

1. Mode **test-run** forcé ; créer `brain/registry/_test-runs/YYYYMMDD-HHMMSS/`.
2. Capturer depuis `conversation-reference-1.txt` avec fenêtres (~5 échanges) + 4 passes + mémoire globale.
3. Ne pas copier / transformer d’anciens JSONL.
4. Valider :
   `python .cursor/skills/brain-capture/scripts/validate-registry.py <cible>/entries.jsonl --require-intention`
5. Rédiger `COMPARISON.md` avec **grille de traçabilité** (messages → infos → CAP → manques).
6. Archiver ; ne pas écraser les runs précédents ni la production.

## Grille de traçabilité (obligatoire dans COMPARISON.md)

Colonnes minimales :

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |

Couvrir au minimum les scénarios A–H (autonomie B/C, portées d’approbation, 6 couches roadmap, ClickUp convention vs observation, Review, sous-tâches, 7 sujets cadrage individuels, bruit de test).

## Critères

Fidélité ; couverture ; autonomie ; attribution ; nuances ; actionable ; relations ; métadonnées ; validité technique. Qualité > nombre d’entrées.
