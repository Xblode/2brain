# Traçabilité — conversation-reference-2 (indépendant)

| | |
| --- | --- |
| Run | `brain/registry/_test-runs/20261030-194948/` |
| Source | `brain/sources/conversation-reference-2.txt` (~1705 lignes) |
| Réf. comparaison échantillon 1 | **non applicable** (échantillon indépendant) |
| Méthode | Skill direct, sans `_gen.py` |
| Validateur | OK `--require-intention` |

## Grille de traçabilité

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| Ouverture | Implémentation 1.1 en cours | CAP-001 | Couvert | — |
| Questions stratégiques | Route / bloquants / impact création | CAP-002→003,011 | Couvert | — |
| Valeur centrale | Raisonnement + séparation Brain-main/brain/ClickUp | CAP-004 | Couvert | — |
| Risque mémoire dette | Risque élevé + besoins | CAP-005 | Couvert | — |
| Risque déformation IA | Suggestion→fait, etc. | CAP-006 | Couvert | — |
| Risque orchestration | Complexité > projets | CAP-007 | Couvert | — |
| Risque maintenance moteur | Schémas / migrations | CAP-008 | Couvert | — |
| Risque contrainte UX | Capture invisible | CAP-009 | Couvert | — |
| Risque dépendance outils | Indépendance modèles/outils | CAP-010 | Couvert | — |
| Changement ordre projet | Cycle SB vs classique | CAP-011 | Couvert | — |
| 5 étapes vision | Fiabiliser… multi-projets | CAP-012…017 | Couvert | Individuels |
| Indicateurs succès | Tableau KPI | CAP-018 | Couvert | — |
| Stratégie cycle complet | Avant plus de features | CAP-019 | Couvert | — |
| Q stratégique ouverte | Aide humaine vs IA directeur | CAP-020 | Couvert | Non tranchée |
| Audits 0.1.1 détaillés | Analyses CAP échantillon 1 | CAP-057…058 | Exclu métier | Tag test-noise ; leçons durables extraites ailleurs |
| Rôle Capture vs Review | Mémoire large puis consolidation | CAP-021 | Couvert | explicit |
| Autonomie contenu | Comprendre sans source (ex. B/C) | CAP-022 | Couvert | — |
| Orchestrateur + agents | Deux idées non incompatibles | CAP-023 | Couvert | `validation: none` (anti-faux explicit) |
| Pré-orga Roadmap | Provisoire non bloquant | CAP-024 | Couvert | none |
| Fenêtres ~5 échanges | Convention capture progressive | CAP-025 | Couvert | — |
| Sens approval_global_partial | Pré-approbation segment | CAP-026 | Couvert | partial tag |
| Search puis valider plus tard | Orientation workflow | CAP-027 | Couvert | none |
| Axes multi-info / couverture / bruit | Exigences | CAP-028,034 | Couvert | — |
| Citations collées | Pas accord multi-CAP | CAP-029,043 | Couvert | — |
| ClickUp ↔ local SoT | Équivalent local obligatoire | CAP-030,040 | Couvert | — |
| clickup.md convention | Décision + emplacement proposé | CAP-031,042 | Couvert | emplacement user encore ouvert |
| Review « valide certaines choses » | Orientation corrigée | CAP-032 | Couvert | none + ambiguous tag |
| Multi-registres idée | entries/tasks/roadmap… | CAP-033→041 | Couvert | — |
| Pause 0.1.2 / conception | Process session | CAP-035 | Couvert | none |
| Capture→Review→Validation | Proposition 3 étapes | CAP-036 | Couvert | — |
| Enum intentions/positions | Proposition standard | CAP-037,060 | Couvert | — |
| Fenêtres + multi-passes + couverture | Proposition méthode | CAP-038 | Couvert | — |
| Niveaux roadmap proposed/provisional/confirmed | Suggestion | CAP-039 | Couvert | — |
| 10 principes conception | Base de discussion | CAP-044 | Couvert | partial |
| Registres historique / index | Q + orientation user | CAP-045…046,050 | Couvert | architecture encore exploratoire |
| Intention principale unique | Décision | CAP-047→048 | Couvert | — |
| Review local / Sync ClickUp | Décision | CAP-049,052 | Couvert | — |
| Attribution auteur hiérarchie | Suggestion | CAP-051 | Couvert | — |
| Archivage option D | Décision + garanties | CAP-053…055 | Couvert | — |
| Review ne modifie pas entries ? | Reco ouverte fin source | CAP-056 | Couvert | Non tranché user |
| Feedback tables couverture | Préférence assistance | CAP-059 | Couvert | — |
| Skill = trame gestionnaire projet | Exigence jalons tôt | CAP-061 | Couvert | — |
| Validateur ≠ sémantique | Limite tests | CAP-062 | Couvert | — |
| Tableau « aujourd'hui vs SB » activités | Détail comparatif | — | **Partiel** | Absorbé dans CAP-011 |
| Agent onboarding détaillé (audit) | Liste capacités | — | **Manque** | Présent surtout dans audits méta échantillon 1 |
| Doublons certains vs similaires (audit) | Règle Review | — | **Manque** | Mention audits ; pas isolé ici |

## Discipline validation (retour audit 184105)

| Cas | Attendu | Résultat run |
| --- | --- | --- |
| Orientation non tranchée / ambiguë | `validation: none` | CAP-023,027,032,035,046 = none |
| Partial endorsement | tag + none | CAP-026,044 |
| Décision nette user | peut être explicit | CAP-021,025,030,048,049,054… |

Aucun couple `ambiguous*` + `explicit` détecté.

## Verdict

Capture indépendante sur source neuve : **crédible**. Couverture solide sur stratégie, risques, conception Capture/Review/Sync/registres. Audits techniques de l'échantillon 1 volontairement réduits au bruit méta. Quelques détails opérationnels d'audit non isolés.
