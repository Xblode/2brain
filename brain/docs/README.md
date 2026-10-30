---
id: DOC-STD-001
name: Standardisation documentaire Brain
description: Catalogue et règles du socle documentaire universel Brain (docs obligatoires, facultatifs, métadonnées, responsabilités).
type: documentation-standard
status: proposed
version: 1.0.0
created_at: 2026-10-30
updated_at: 2026-10-30
update_sources: []
# locked: false = modifiable | true = lecture seule (ne pas modifier ce fichier)
locked: false
---
# Standardisation documentaire Brain



L'objectif est de définir un catalogue documentaire universel, utilisable pour un site web, une application mobile, un logiciel Rust, un serveur Minecraft ou même un projet conceptuel.

La standardisation porte sur les responsabilités et les règles documentaires, pas sur une technologie ou une méthode de développement particulière.

## 1. Architecture documentaire

Trois niveaux :

Niveau 1 · Obligatoire

Socle documentaire universel

Présent dans chaque instance Brain, avec cinq documents.

Niveau 2 · Facultatif

Catalogue documentaire standard

Documents activés selon les besoins du projet, sur recommandation de l'IA et validation humaine.

 Niveau 3 · Extensible

Documents spécialisés

Documents propres à un domaine, module ou projet. Ils ne modifient pas le socle universel.

## 2. Socle obligatoire

Ces cinq documents sont créés lors de l'initialisation, même si certaines sections restent vides.

| Document          | Responsabilité exclusive                                    |
| ----------------- | ----------------------------------------------------------- |
| `vision.md`       | Pourquoi le projet existe, objectifs et vision à long terme |
| `project.md`      | Identité, contexte, périmètre, utilisateurs et contraintes  |
| `requirements.md` | Ce que le projet doit accomplir : besoins et exigences      |
| `architecture.md` | Comment le projet est organisé et conçu                     |
| `workflow.md`     | Comment le projet fonctionne, évolue et est travaillé       |

### Contenu attendu

`vision.md`

- Vision et ambition.
- Problème à résoudre.
- Objectifs et résultats recherchés.
- Principes directeurs.
- Critères de réussite à long terme.

`project.md`

- Présentation générale.
- Contexte et origine.
- Public cible et utilisateurs.
- Périmètre et hors périmètre.
- Contraintes et hypothèses.
- État actuel du projet.

`requirements.md`

- Besoins fonctionnels.
- Exigences non fonctionnelles.
- Fonctionnalités prévues.
- Règles métier.
- Critères d'acceptation.
- Priorités et dépendances.

`architecture.md`

- Architecture générale.
- Technologies et justifications.
- Composants et responsabilités.
- Organisation des éléments.
- Relations et dépendances.
- Contraintes techniques.

`workflow.md`

- Méthodes de travail.
- Processus de développement ou de réalisation.
- Cycle de vie du projet.
- Gestion des changements.
- Outils et pratiques.
- Processus de contribution et de validation.

## 3. Catalogue documentaire facultatif

Chaque document a une responsabilité distincte. Il n'est pas nécessaire de tous les activer.

| Document            | Responsabilité                                        |
| ------------------- | ----------------------------------------------------- |
| `data.md`           | Modèles, structures, stockage et relations de données |
| `flows.md`          | Parcours utilisateurs, navigation et enchaînements    |
| `design.md`         | UI, UX, identité visuelle et règles de conception     |
| `services.md`       | Backend, API, services et logique métier              |
| `implementation.md` | Stratégie, phases et plan d'implémentation            |
| `operations.md`     | Exploitation, installation, maintenance               |
| `security.md`       | Sécurité, permissions et menaces                      |
| `testing.md`        | Stratégie, scénarios et couverture des tests          |
| `deployment.md`     | Construction, distribution et déploiement             |
| `integrations.md`   | Services externes et interconnexions                  |

Règle : Brain recommande un document lorsqu'un besoin réel apparaît, explique son utilité et attend ta confirmation avant activation.

Le catalogue pourra accueillir de nouveaux documents standards, mais leur ajout au catalogue universel nécessitera une validation humaine.

## 4. Standardisation interne des documents

Tous les documents utilisent une structure commune, avec un socle de métadonnées et des sections adaptées à leur responsabilité.

Exemple de structure :

```
---
id: DOC-STD-001
name: Standardisation documentaire Brain
description: Catalogue et règles du socle documentaire universel Brain (docs obligatoires, facultatifs, métadonnées, responsabilités).
type: documentation-standard
status: proposed
version: 1.0.0
created_at: 2026-10-30
updated_at: 2026-10-30
update_sources: []
locked: false
---

# Requirements

## 1. Purpose
## 2. Current State
## 3. Confirmed Information
## 4. Content
## 5. Open Questions
## 6. References
```

Les sections peuvent être adaptées selon le document.

Champ `locked` (métadonnée) :

- `locked: false` — document modifiable (défaut).
- `locked: true` — document verrouillé : les agents ne doivent pas le modifier tant que le champ n’est pas repassé à `false`.

Règles :

- Pas de remplissage artificiel.
- Pas d'informations inventées.
- Pas de duplication entre documents.
- Références vers les éléments sources.
- Sections extensibles selon les besoins.
- Découpage en fichiers distincts lorsque les responsabilités deviennent trop importantes.
- Respecter `locked: true` : aucune modification du corps ni des métadonnées hors déverrouillage explicite demandé par l’humain.

## 5. Gestion des fonctionnalités

Je recommande de distinguer le registre central des fiches détaillées.

`requirements.md`

Registre central des exigences et fonctionnalités.

Fiches individuelles

Créées progressivement lorsque la complexité le justifie.

Exemple :

```
brain/
└── docs/
    ├── requirements.md
    └── requirements/
        ├── REQ-001-authentication.md
        └── REQ-002-notifications.md
```

Chaque fiche peut contenir :

- Identifiant stable.
- Objectif et description.
- Comportement attendu.
- Règles métier.
- Critères d'acceptation.
- Cas limites.
- Dépendances.
- Références techniques et fonctionnelles.

Le registre central reste léger et référence les fiches.

## 6. Règles de gouvernance

| Règle                   | Fonctionnement                                            |
| ----------------------- | --------------------------------------------------------- |
| Propriété               | Une information possède un seul document propriétaire     |
| Références              | Les autres documents peuvent la référencer                |
| Validation              | Les changements substantiels attendent ton accord         |
| Corrections             | Les corrections mécaniques peuvent être automatiques      |
| Historique              | Git + historique sémantique Brain                         |
| Identifiants            | IDs stables pour les éléments importants                  |
| Relations               | Liens Markdown + relations structurées dans les registres |
| Informations manquantes | Questions et hypothèses clairement séparées               |
| Audit                   | Vérification après modifications importantes              |
| Découpage               | Selon la complexité et les responsabilités                |

## 7. Correspondance avec les standards PRD / TRD

C'est important pour garantir que notre standardisation reste compatible avec les pratiques éprouvées.

| Standard connu        | Emplacement Brain          |
| --------------------- | -------------------------- |
| Project Brief         | `vision.md` + `project.md` |
| PRD                   | `requirements.md`          |
| TRD                   | `architecture.md`          |
| App Flow              | `flows.md`                 |
| UI/UX Brief           | `design.md`                |
| Backend Specification | `services.md` + `data.md`  |
| Implementation Plan   | `implementation.md`        |
| Test Plan             | `testing.md`               |
| Deployment Plan       | `deployment.md`            |
| Operations Plan       | `operations.md`            |

Il ne s'agit pas de reproduire ces documents à l'identique, mais d'en conserver les responsabilités et les bonnes pratiques.

## 8. Arborescence de référence

```

brain/
├── AGENTS.md
├── docs/
│   ├── vision.md
│   ├── project.md
│   ├── requirements.md
│   ├── architecture.md
│   ├── workflow.md
│   │
│   ├── requirements/
│   │   └── (fiches individuelles)
│   │
│   ├── data.md
│   ├── flows.md
│   ├── design.md
│   ├── services.md
│   ├── implementation.md
│   ├── operations.md
│   ├── security.md
│   ├── testing.md
│   ├── deployment.md
│   └── integrations.md
│
└── registry/
    └── (registres Brain)

```

Les documents facultatifs ne sont créés que lorsqu'ils sont activés. `AGENTS.md` reste un point d'entrée opérationnel pour les IA, pas un document de spécification du projet.

## 9. Ce que je propose de considérer comme contrat V1

Les décisions suivantes sont suffisamment mûres pour être figées :

1. Les cinq documents obligatoires.
2. Le catalogue facultatif initial.
3. La séparation stricte des responsabilités.
4. Le registre central et les fiches détaillées progressives.
5. La structure interne hybride.
6. La validation humaine des nouveaux documents standards.
7. La gouvernance et la traçabilité décrites ci-dessus.

Deux précisions que je ne figerais pas encore :

- Le schéma exact des métadonnées YAML.
- Les seuils et conditions précis de création automatique des fiches individuelles.

Ils pourront être définis après un premier test réel de capture et de génération documentaire.

## Validation

Est-ce que tu souhaites adopter cette standardisation comme référence V1 de Brain ?

Je valide la standardisation V1.

Je veux modifier certains points.

Je veux encore discuter de quelques responsabilités.



Confirmer

Aucune modification de dépôt ou de ClickUp n'est effectuée ici.