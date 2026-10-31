# Tests et audits Capture (reconstruits)

> Uniquement ce que les CAP disent des tests. Les rapports COMPARISON/AUDIT eux-mêmes n’ont **pas** été lus (accès interdit) — seuls les résumés capturés dans les JSONL.

## 1. Objectifs de test (tels que formulés)

**PROPOSITION / requirement** — Artefacts obligatoires : `COMPARISON.md` factuel + `validate.json` archivé ; un CAPTURE_NOTE seul insuffisant.  
`20261031-000600-ref2:CAP-053` · `20261031-000600-ref3:CAP-028` · `20261031-000600-ref3:CAP-073`

**CONVENTION** — Échantillon 1 = référence comparaison ; baseline sémantique `20261030-061941` ; ne plus utiliser `045232`.  
`20261031-000600-ref3:CAP-026` · `20261031-000600-ref2:CAP-075`

**CONVENTION** — Échantillon 2 (`conversation-reference-2.txt`) indépendant ; pas mélangé à la comparaison principale sample 1.  
`20261031-000600-ref3:CAP-003` · `CAP-027`

**REQUIREMENT** — Ne pas déclarer succès sur seul JSONL valide ; validateur structurel ≠ qualité sémantique.  
`20261031-000600-ref2:CAP-040` · `20261031-000600-ref3:CAP-025`

**REQUIREMENT user** — Ne pas comparer CAP-N entre sources différentes.  
`20261031-000600-ref3:CAP-081` · `CAP-090`

**DÉCISION** — Sources 1 et 2 = conversations officielles pour l’instant.  
`20261031-000600-ref3:CAP-082`

## 2. Scénarios prioritaires (échantillon 1, pour 0.1.2)

**TASK proposée** — Scénarios A–H : autonomie B/C ; portée approbation ; roadmap 6 couches ; convention ClickUp ; rôles Review ; sous-tâches roadmap ; 7 sujets cadrage individuels ; bruit test.  
`20261031-000600-ref3:CAP-029`

## 3. Runs mentionnés et verdicts capturés

### 3.1 `20261030-045232` (Skill 0.1.1)

| Aspect | Contenu capturé | Réf. |
|--------|-----------------|------|
| Technique | 69 entrées, IDs uniques, JSONL OK, 0 erreur bloquante, isolation `_test-runs/` | `ref2:CAP-032` |
| Sémantique | Confusions proposition/décision ; attributions ; couverture ; explicit 33→24 | `ref2:CAP-031` · `CAP-032` |
| Verdict | Amélioration vs V1.0, pas assez fiable | `ref2:CAP-031` |
| Suite | **Ne plus prendre en compte** (transformation, pas re-capture) | `ref2:CAP-075` |

### 3.2 `20261030-061941` (Skill 0.1.1, vraie re-capture)

| Aspect | Contenu capturé | Réf. |
|--------|-----------------|------|
| Méthode | Génération indépendante depuis source ; 0/69 couples title+content identiques au précédent | `ref2:CAP-044` |
| Progrès | Segmentation B/C ; sous-tâches non-décision ; ClickUp ; vision.md ; agents sans orchestrateur auto | `ref2:CAP-045` |
| P1 | Propagation « bonne base » ; 7 sujets absents comme entrées distinctes | `ref2:CAP-046` · `CAP-047` |
| P2 | Roadmap 6 couches sans signal partial ; ClickUp obs vs convention ; Review ambigu→décision | `ref2:CAP-048`–`CAP-050` |
| P3 | Bruit simulation/test | `ref2:CAP-051` |
| Baseline | Retenue pour comparer 0.1.2 | `ref3:CAP-026` |

### 3.3 `20261030-180454` (annoncé 0.1.2)

| Aspect | Contenu capturé | Réf. |
|--------|-----------------|------|
| Verdict | Progression structurelle (77 CAP, intentions, jalons/cadrage) — pas production | `ref3:CAP-046` |
| P1 bloquant | `_gen.py` prérempli ≠ exécution Skill ; pas de validate.json | `ref3:CAP-047` |
| P1 sémantique | CAP-009 et CAP-047 explicit injustifiés | `ref3:CAP-049` |
| P2 | Localisateurs manquants ; confiance trop high (73/77) | `ref3:CAP-050` · `CAP-051` |
| Validateur | Fichier vide non bloquant | `ref3:CAP-052` |
| Suite reco | Vrai test Skill depuis source brute | `ref3:CAP-048` |

### 3.4 `20261030-184105` (0.1.2, sans `_gen.py`)

| Aspect | Contenu capturé | Réf. |
|--------|-----------------|------|
| Méthode | 80 CAP ; skill-direct annoncé ; grille comparaison ; exclure 180454 | `ref3:CAP-057` |
| Limite | Pas entièrement reproductible (pas de trace technique indépendante ni validate.json) | `ref3:CAP-057` |
| P1 | CAP-009 et CAP-049 explicit injustifiés (persistant) | `ref3:CAP-058` |
| Positif | Approbations partielles correctement gérées | `ref3:CAP-059` |
| P2 | Confiance 75/80 high encore trop | `ref3:CAP-060` |
| Validateur | Bug vide toujours ouvert | `ref3:CAP-062` |
| Verdict | Prêt pour test sur nouvelle source ; sample 1 = régression utile ≠ généralisation | `ref3:CAP-061` · `CAP-064` |

### 3.5 `20261030-194948` (sample 2)

| Aspect | Contenu capturé | Réf. |
|--------|-----------------|------|
| Méthode | Premier test `conversation-reference-2` sans mélange ni `_gen.py` | `ref3:CAP-066` |
| Chiffres | 62 CAP, 42 relations ; confiance 34 high / 28 medium | `ref3:CAP-066` |
| Forces | Risques séparés ; jalons individualisés ; orientations non-décisions | `ref3:CAP-067` |
| P1 | CAP-031 approbation trop large (convention + emplacement) | `ref3:CAP-068` |
| P2 | CAP-022 et CAP-028 à scinder | `ref3:CAP-069` · `CAP-070` |
| Protocole | Bilan SKILL + validate.json manquants | `ref3:CAP-073` |
| Verdict | Preuve encourageante hors premier échantillon ; pas prod directe | `ref3:CAP-074` |

## 4. Défauts systémiques répétés

1. **Sur-validation** d’ambiguïtés (B/C, « valider certaines choses », multi-sujets dans un message).  
2. **Sous-couverture** d’items listés (7 cadrages, détails ops).  
3. **Preuve d’exécution Skill** parfois absente (`_gen.py`).  
4. **Validateur** ne couvre pas la sémantique ; fichier vide OK.  
5. **Confidence high** trop fréquente.  
6. **Manque** `validate.json` / bilan SKILL standard dans plusieurs runs.

## 5. Protocoles futurs (décidés / proposés, non exécutés dans les CAP)

**DÉCISION protocole cross-conversation** — Réponses Q1–Q5 : conversation Cursor ; toute la conv ; workspace indépendant + skill User ; Capture uniquement ; tout préserver / relier.  
`20261031-000600-ref3:CAP-096`

**MILESTONE proposés** — Test A nouvelle conversation Cursor ; Test B accès par lien.  
`20261031-000600-ref3:CAP-107` · `CAP-108`

**CONVENTION** — Quatre règles pendant tests : non-destruction ; non-validation implicite ; non-consolidation prématurée ; non-perte de provenance.  
`20261031-000600-ref3:CAP-109`

## 6. Confiance de reconstruction des résultats

Les chiffres et verdicts ci-dessus sont **secondaires** (rapports d’audit capturés dans le registre). Sans accès aux fichiers de test originaux, la fidélité des métriques exactes est **moyenne** ; la trajectoire qualitative (amélioration, défauts récurrents, jeter 045232) est **haute**.
