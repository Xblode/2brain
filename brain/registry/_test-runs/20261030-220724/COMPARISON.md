# Traçabilité — conversation-reference-3 (smoke régression 0.1.3)

| | |
| --- | --- |
| Run | `brain/registry/_test-runs/20261030-220724/` |
| Source | `brain/sources/conversation-reference-3.txt` (~1461 lignes) |
| Type de test | **Smoke régression** sur règles 0.1.3 |
| ≠ Test A | Ce run **n'est pas** une preuve de généralisation |
| Méthode | Skill-direct, sans `_gen.py` |
| Validateur | OK `--require-intention` + `validate.json` |
| AUDIT.md | oui |

## Grille de traçabilité

| Zone source / thème | Info pertinente | CAP(s) | Statut | Manque / remarque |
| --- | --- | --- | --- | --- |
| Ouverture | Prêt 0.1.2 + prompt Cursor | CAP-001,004 | Couvert | — |
| Nouvelle source | conversation-reference-2 à ajouter | CAP-002 | Couvert | — |
| Rôles échantillons | 1 = comparaison ; 2 = indépendant | CAP-003,056 | Couvert | Ne pas croiser CAP entre sources |
| Philosophie capture | Collecte ≠ sélection / ≠ validation | CAP-005,007 | Couvert | — |
| Périmètre | Capture only ; pas Review/Sync | CAP-006,050 | Couvert | — |
| Fenêtres + 4 passes | Process capture progressive | CAP-008,009,022 | Couvert | Ajustement précise CAP-022 |
| Couverture sémantique | Checklist + sujets individuels | CAP-010,026 | Couvert | — |
| Intention / position | Taxonomie + 3 dimensions | CAP-011,012,023 | Couvert | — |
| Atomicité multi-infos | Séparer natures/certitudes | CAP-013,046 | Couvert | Clarifié en 0.1.3 |
| Autonomie contenu | Enrichir / ne pas inventer | CAP-014,043 | Couvert | — |
| Attribution | Hiérarchie + citations | CAP-015,044 | Couvert | Signatures non inventées |
| Partial approval | Tag + none | CAP-016 | Couvert | — |
| Bruit vs métier | Exclusion test-noise | CAP-017 | Couvert | — |
| Multi-registres futurs | Orientation seulement | CAP-018 | Couvert | Hors impl 0.1.3 |
| Scénarios A–H | Priorités sample 1 | CAP-019 | Couvert | Spécifiques sample 1 |
| Plan Cursor + 5 ajustements | Feu vert conditionnel | CAP-020…027 | Couvert | Splits atomiques |
| Audit 180454 | `_gen.py` KO ; faux explicit ; vide ; locators | CAP-028…033 | Couvert | Méta audit tagué |
| Audit 184105 | Méthode skill-direct crédible | CAP-034…036 | Couvert | — |
| Audit 194948 | Source 2 indépendante | CAP-037…038 | Couvert | — |
| Exemples atomicité | CAP-031 / 022 / 028 | CAP-039…041 | Couvert | Cas de test 0.1.3 |
| Retours user | Scinder ; Review ; richesse ; Test A | CAP-042…044,047…049,055…056 | Couvert | — |
| Architecture graphe | Sujets / fonctionnalités / projets | CAP-045,055 | Couvert | Future Review |
| Axes 0.1.3 | 6 axes + grounding + 4 règles | CAP-051…054 | Couvert | Aligné plan implémenté |
| Détail exhaustif prompt long | Chaque sous-§ | — | **Partiel** | Smoke : synthèse volontaire |
| Signatures ChatGPT/Claude/Cursor | Adaptateurs | — | **Exclu** | Documenté à confirmer en live ; non inventé |

## Discipline validation

| Cas | Attendu | Résultat run |
| --- | --- | --- |
| Orientation non tranchée | `validation: none` | CAP-033,036,044,049 |
| Partial endorsement | tag + none | CAP-021,042,055 |
| Décision nette user | peut être explicit | CAP-001,027,047,048,056 |
| Ensemble ajustements | `set` si identifiable | CAP-027 |

## Verdict

Smoke **régression 0.1.3** crédible sur la source qui a conçu les règles : champs `run_id` / `capture_ref` / `locators[]` / `grounding` / `author_confidence`, atomicité des ajustements, audit + validate.json présents.

**Ne pas** présenter ce résultat comme preuve que le Skill généralise (réservé au **Test A**).
