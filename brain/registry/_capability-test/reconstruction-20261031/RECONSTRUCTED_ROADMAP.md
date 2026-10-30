# Roadmap (reconstruite)

> Distinguer **validé / retenu** vs **proposé** vs **ouvert**. Une « bonne base » (`approval_global_partial`) ≠ verrouillage.

## 1. Ordre de construction — couches (proposées, base de travail)

**PROPOSITION (assistant)** — Construire en 6 couches, tester chacune avant la suivante.  
`20261031-000600-ref1:CAP-064`

**FAIT (user favorable)** — « Première base pour jalons/tâches » / trame à suivre — **pas** validation définitive de l’organisation.  
`20261031-000600-ref1:CAP-069` · signal manquant noté en audit `ref2:CAP-048`

| # | Jalon | Statut | Réfs |
|---|-------|--------|------|
| 1 | Core minimal (capture, registres, classification, historique, validation) | **proposé** / retenu comme piste | `ref1:CAP-110` · `ref2:CAP-106` |
| 2 | Orchestration et agents | **proposé** | `ref1:CAP-111` · `ref2:CAP-107` |
| 3 | Onboarding universel | **proposé** | `ref1:CAP-112` · `ref2:CAP-108` |
| 4 | Système de modules | **proposé** | `ref1:CAP-113` · `ref2:CAP-109` |
| 5 | Connecteurs et synchronisation | **proposé** | `ref1:CAP-114` · `ref2:CAP-110` |
| 6 | Automatisation et audits | **proposé** | `ref1:CAP-115` · `ref2:CAP-111` |

**PROPOSITION (ref2)** — Niveaux roadmap `proposed` / `provisional` / `confirmed` ; pré-organisation non bloquante tant que non verrouillée.  
`20261031-000600-ref2:CAP-084` · `CAP-059` · `CAP-105`

**ORIENTATION user** — Remplir roadmap/tâches dès détection de base jalons (pré-validation IA).  
`20261031-000600-ref2:CAP-067`

## 2. Cinq étapes stratégiques (proposées, ref2)

| Étape | Contenu | Réf. |
|-------|---------|------|
| 1 | Fiabiliser la capture | `ref2:CAP-021` |
| 2 | Exploitation réelle de la mémoire | `ref2:CAP-022` |
| 3 | Processus de consolidation | `ref2:CAP-023` |
| 4 | Connecter réflexion et exécution | `ref2:CAP-024` |
| 5 | Tester sur plusieurs projets réels | `ref2:CAP-025` |

**ORIENTATION** — Priorité : cycle complet idée → version fonctionnelle avant d’ajouter des features.  
`20261031-000600-ref2:CAP-027` · `CAP-042` (ne pas avancer SB tant que capture insuffisante)

## 3. Sujets de cadrage ouverts (à conserver individuellement)

Listés ref1 puis re-capturés ref2 — **ouverts** (pas de décision de conception complète dans les CAP) :

1. Modèle de données et registres — `ref1:CAP-103` · `ref2:CAP-112`  
2. Capture multi-IA — `ref1:CAP-104` · `ref2:CAP-113`  
3. Cycle de vie des informations — `ref1:CAP-105` · `ref2:CAP-114`  
4. Gestion des conflits — `ref1:CAP-106` · `ref2:CAP-115`  
5. Versionnement des modules — `ref1:CAP-107` · `ref2:CAP-116`  
6. Synchronisation ClickUp — `ref1:CAP-108` · `ref2:CAP-117`  
7. Permissions des agents — `ref1:CAP-109` · `ref2:CAP-118`

**REQUIREMENT user** — Stocker ces pistes pour reprise ultérieure.  
`20261031-000600-ref1:CAP-070`

## 4. Roadmap Skill Capture (évolution réelle dans les conversations)

| Item | Statut | Réf. |
|------|--------|------|
| Conception / implémentation Capture « 1.1 » | **fait** (lancée) | `ref2:CAP-001` |
| V0.1.1 | **fait** (audité ; insuffisant) | `ref2:CAP-031` |
| V0.1.2 | **fait** (décidée, poussée, audité 180454/184105/194948) | `ref3:CAP-001` · `CAP-045` |
| Périmètre 0.1.2 = Capture seul | **convention proposée** appliquée au plan | `ref3:CAP-006` |
| V0.1.3 | **décidée** (avant cross-test) ; axes A–F proposés | `ref3:CAP-095` · `CAP-100`–`CAP-106` |
| Cross-Conversation Test A/B | **proposé / protocolé** ; non exécuté dans les CAP | `ref3:CAP-091` · `CAP-107`–`CAP-110` |
| Implémenter Brain Review | **explicitement hors scope** 0.1.3 | `ref3:CAP-111` |

### Axes 0.1.3 (proposés)

- A Atomicité contrôlée — `ref3:CAP-101`  
- B Enrichir depuis source ou signaler — `CAP-102`  
- C Audit final = vraie passe — `CAP-103`  
- D Relations sans validation implicite — `CAP-104`  
- E Signatures plateformes — `CAP-105`  
- F Explicite / interprété / incertain / déduit — `CAP-106`

## 5. Validé vs proposé — synthèse décisions structurantes

### Validé (`explicit_user_approval` ou confirmation claire)

- Solutions de conflits comparées ; historique décisions ; modules mods — `ref1:CAP-044`–`046`  
- Arbo ClickUp Projets ; ne rien ajouter ClickUp momentanément — `ref1:CAP-071` · `CAP-087`  
- `vision.md` 100 % — `ref1:CAP-089`  
- Capture multi-informations — `ref2:CAP-063`  
- Pas 0.1.2 pendant conception ref2 ; jeter 045232 — `ref2:CAP-074`–`075`  
- Intention principale unique ; Review local / Sync ClickUp ; archivage D — `ref2:CAP-097`–`101`  
- Lancer 0.1.2 ; sources 1/2 officielles ; hiérarchie captures→…→projets ; graphe Review ; 0.1.3 avant cross-test ; Q1–Q5 protocole — `ref3:CAP-001` · `CAP-082` · `CAP-093`–`096`

### Retenu comme base partielle (`approval_global_partial` / endorsed)

- 4 espaces + pipeline + commandes + contrat ; Core/Modules ; principes — `ref1:CAP-066`–`068`  
- Workflow capture/review globalement — `ref1:CAP-088`  
- Dix principes Capture (assistant) — `ref2:CAP-089`  
- Plan Cursor 0.1.2 (avec ajustements) — `ref3:CAP-035`–`043`

### Proposé non verrouillé

- Table exacte des 11 commandes — `ref1:CAP-030`  
- AGENTS.md racine — `ref1:CAP-098`  
- Socle docs standard candidats — `ref1:CAP-096`  
- Registres spécialisés futurs — `ref2:CAP-086` · `ref3:CAP-023`  
- Versionnement schémas/migrations — `ref2:CAP-013`

## 6. Questions ouvertes majeures

1. SB = assistant humain vs IA constructeur avec humain directeur ? — `ref2:CAP-029`  
2. Permissions agents (liste ouverte) — `ref1:CAP-109` · `ref2:CAP-118`  
3. Sync ClickUp bidirectionnelle / conflits sync — `ref1:CAP-108`  
4. Capture multi-IA concrète (adaptateurs) — `ref1:CAP-104` · `ref1:CAP-101`  
5. Standardiser `operating-model` / `onboarding` ? — `ref1:CAP-090`  
6. Emplacement définitif `clickup.md` (reco `brain/conventions/` non validée comme emplacement) — `ref2:CAP-085` · `ref3:CAP-068`  
7. Sync valide-t-il aussi le contenu métier ? — `ref2:CAP-099`  
8. Livraison effective de 0.1.3 et résultats Tests A/B — **absents** des CAP
