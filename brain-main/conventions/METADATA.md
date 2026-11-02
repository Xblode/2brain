---

metadata_version: 1

title: "Convention universelle des métadonnées"  
type: convention  
description: "Définit les règles communes de déclaration, de structuration, de traçabilité et de validation des métadonnées dans les projets."  
summary: "Convention universelle définissant le socle de métadonnées des documents et les adaptations propres aux différents formats. Elle établit les propriétés communes, leur classification, les règles d'héritage, la traçabilité des modifications et les modalités de validation automatisée."

version: "1.0.0"  
status: approved

created: "2026-11-02"  
updated: "2026-11-02"

scope:  
level: universal  
targets:  
- all-projects

tags:

- metadata
- documentation
- standardization

---

# Convention universelle des métadonnées

## 1. Objectifs et périmètre

### 1.1 Objectifs

Cette convention définit un standard commun permettant d'identifier, de décrire, de contextualiser et de tracer les informations contenues dans les fichiers d'un projet.

Elle vise notamment à :

- Faciliter la compréhension des documents par les agents IA.
- Uniformiser les propriétés documentaires entre les projets.
- Identifier le type, le statut et le périmètre d'un document.
- Faciliter l'indexation et la recherche ciblée.
- Conserver la provenance des modifications.
- Permettre la validation automatique des documents.
- Assurer la compatibilité entre différents formats de fichiers.
- Faciliter l'héritage des conventions générales par les conventions spécialisées.

### 1.2 Périmètre

Cette convention s'applique à l'ensemble des projets utilisant le socle commun.

Elle concerne notamment :

- Documents Markdown.
- Conventions et standards.
- Règles et instructions pour agents IA.
- Skills et templates.
- Documents de spécification.
- Décisions et comptes rendus.
- Registres et données structurées.
- Fichiers de configuration.
- Code source, dans la mesure où une documentation structurée est pertinente.
- Ressources graphiques, fichiers de conception et documents binaires.

Elle définit un modèle conceptuel commun, mais ne contraint pas tous les formats à utiliser une représentation identique.

### 1.3 Hors périmètre

Cette convention ne définit pas :

- La taxonomie complète des informations.
- Le nommage des fichiers.
- L'organisation des répertoires.
- L'architecture des registres.
- Les règles métier propres à un projet.
- Le contenu documentaire lui-même.
- Les paramètres techniques des applications.

Ces éléments peuvent être définis par des conventions complémentaires.

---

## 2. Principes généraux

Toute implémentation doit respecter les principes suivants.

| Principe        | Règle                                                                     |
| --------------- | ------------------------------------------------------------------------- |
| Lisibilité      | Les métadonnées doivent être compréhensibles sans outil spécialisé.       |
| Simplicité      | Ne déclarer que les propriétés ayant une utilité identifiable.            |
| Cohérence       | Utiliser les mêmes noms et types pour les mêmes concepts.                 |
| Progressivité   | Permettre l'ajout de propriétés selon les besoins.                        |
| Extensibilité   | Autoriser les conventions spécialisées à compléter le socle.              |
| Compatibilité   | Respecter les possibilités natives de chaque format.                      |
| Traçabilité     | Identifier les dates et les sources des dernières modifications.          |
| Maintenance     | Éviter les mises à jour manuelles inutiles.                               |
| Non-duplication | Ne pas recopier des informations déjà disponibles dans une source fiable. |
| Prévisibilité   | Retrouver les mêmes conventions entre les projets.                        |

### 2.1 Séparation des responsabilités

Les métadonnées ne remplacent jamais le contenu du document.

Elles permettent de comprendre et de localiser l'information, pas de reproduire l'intégralité de son contenu.

Il faut distinguer :

- **Métadonnées :** informations décrivant le document.
- **Contenu :** informations réellement portées par le document.
- **Configuration :** paramètres contrôlant le fonctionnement d'un système.
- **Données métier :** informations manipulées par le projet.
- **Historique :** événements et modifications successives.

Une propriété ne doit pas être placée dans les métadonnées simplement parce qu'elle pourrait être utile à un agent IA.

---

## 3. Structure standard

### 3.1 Modèle commun

Les documents compatibles avec une déclaration de métadonnées utilisent le modèle suivant :

```
metadata_version: 1

title: "Titre du document"
type: convention
description: "Description courte du document."
summary: "Résumé du document."

version: "1.0.0"
status: approved

created: "2026-11-02"
updated: "2026-11-02"

scope:
  level: universal
  targets:
    - all-projects

extends:
  - "conventions/PARENT.md"

depends_on:
  - "conventions/DEPENDENCY.md"

updated_from:
  - "sources/reference.md"

tags:
  - example
```

Les propriétés présentées constituent le vocabulaire commun.

Elles ne sont pas toutes obligatoires. Leur utilisation dépend de la classification définie dans cette convention.

### 3.2 Convention de nommage des propriétés

Les noms de propriétés utilisent exclusivement le format `snake_case`.

Exemples :

- `metadata_version`
- `created`
- `updated_from`
- `depends_on`
- `scope`

Les noms de propriétés sont écrits en minuscules.

Les conventions spécialisées doivent conserver cette règle.

Les valeurs textuelles peuvent naturellement utiliser la langue appropriée au projet.

### 3.3 Types de données

| Type    | Représentation  | Exemple                   |
| ------- | --------------- | ------------------------- |
| String  | Texte           | `"Document de référence"` |
| Integer | Nombre entier   | `1`                       |
| Boolean | Booléen         | `true`                    |
| Date    | ISO 8601        | `"2026-11-02"`            |
| Array   | Liste           | `["web", "mobile"]`       |
| Object  | Objet structuré | `scope: { ... }`          |

Les dates documentaires utilisent le format `YYYY-MM-DD`.

Les horodatages complets peuvent être utilisés lorsqu'une précision horaire est nécessaire, avec un fuseau horaire explicite.

Les valeurs textuelles représentant des dates doivent être entre guillemets.

---

## 4. Définition des propriétés

### 4.1 Classification

Trois niveaux de priorité sont définis.

| Classification | Signification                                       |
| -------------- | --------------------------------------------------- |
| Obligatoire    | Doit être renseigné pour les documents concernés.   |
| Recommandé     | Doit être renseigné lorsque son utilité est avérée. |
| Facultatif     | Peut être utilisé selon les besoins.                |

Une propriété conditionnelle peut devenir obligatoire lorsqu'une convention spécialisée le prévoit.

### 4.2 Propriétés du socle commun

| Propriété          | Classification | Type    | Description                                                  |
| ------------------ | -------------- | ------- | ------------------------------------------------------------ |
| `metadata_version` | Obligatoire    | Integer | Version du schéma de métadonnées utilisé.                    |
| `title`            | Obligatoire    | String  | Titre explicite du document.                                 |
| `type`             | Obligatoire    | String  | Nature du document.                                          |
| `description`      | Obligatoire    | String  | Description courte de sa responsabilité.                     |
| `status`           | Obligatoire    | String  | État actuel du document.                                     |
| `created`          | Obligatoire    | Date    | Date de création initiale.                                   |
| `updated`          | Obligatoire    | Date    | Date de dernière modification significative.                 |
| `version`          | Recommandé     | String  | Version propre au document.                                  |
| `summary`          | Recommandé     | String  | Synthèse permettant d'évaluer rapidement son contenu.        |
| `scope`            | Conditionnel   | Object  | Périmètre d'application du document.                         |
| `extends`          | Conditionnel   | Array   | Conventions dont le document hérite.                         |
| `depends_on`       | Facultatif     | Array   | Documents nécessaires à sa compréhension ou son application. |
| `updated_from`     | Recommandé     | Array   | Sources utilisées lors de la dernière mise à jour.           |
| `tags`             | Facultatif     | Array   | Mots-clés facilitant l'indexation.                           |

### 4.3 `metadata_version`

Indique la version du schéma de métadonnées utilisé.

Cette propriété est indépendante de la version du document.

Exemple :

```
metadata_version: 1
```

Elle permet aux outils de savoir comment interpréter les propriétés.

Une évolution incompatible du schéma doit entraîner une nouvelle version majeure du schéma.

Une propriété ajoutée de manière compatible ne nécessite pas automatiquement une nouvelle version majeure.

### 4.4 `title`

Définit le titre humain du document.

Règles :

- Doit être explicite.
- Doit être compréhensible sans connaître le nom du fichier.
- Ne doit pas contenir inutilement le nom du projet.
- Doit rester cohérent avec le contenu réel.

Exemple :

```
title: "Convention universelle des métadonnées"
```

### 4.5 `type`

Identifie la nature du document.

Le socle commun propose les valeurs suivantes :

| Valeur          | Utilisation                                              |
| --------------- | -------------------------------------------------------- |
| `convention`    | Définit des règles communes.                             |
| `standard`      | Définit une norme ou un modèle à respecter.              |
| `guide`         | Explique une méthode ou une pratique.                    |
| `specification` | Décrit un comportement ou une solution attendue.         |
| `decision`      | Formalise une décision.                                  |
| `plan`          | Décrit une organisation ou une trajectoire prévue.       |
| `report`        | Présente une analyse ou un compte rendu.                 |
| `reference`     | Regroupe des informations de référence.                  |
| `skill`         | Définit une compétence ou procédure destinée à un agent. |
| `agent`         | Décrit un agent spécialisé.                              |
| `template`      | Définit un modèle réutilisable.                          |
| `index`         | Permet de retrouver et organiser des ressources.         |
| `data`          | Contient des données structurées.                        |

Une convention spécialisée peut ajouter de nouveaux types si nécessaire.

Les nouvelles valeurs doivent être documentées et réutilisées de manière cohérente.

### 4.6 `description`

Présente la responsabilité principale du document en une phrase courte.

Elle doit permettre de comprendre immédiatement pourquoi le fichier existe.

Recommandations :

- Une phrase.
- Une formulation directe.
- Éviter les formulations génériques.
- Décrire la fonction du document, pas seulement son sujet.

Exemple :

```
description: "Définit les règles communes de déclaration et de validation des métadonnées."
```

### 4.7 `summary`

Présente une synthèse autonome du contenu.

Elle doit permettre à un agent de déterminer si la lecture complète du document est pertinente.

Recommandations :

- Environ 2 à 5 phrases.
- Idéalement moins de 500 caractères.
- Mentionner les principaux sujets couverts.
- Signaler les responsabilités ou limites importantes.
- Éviter de répéter simplement la description.

Un résumé n'est pas un remplacement du document.

Il doit être mis à jour lorsque le contenu évolue suffisamment pour que l'ancien résumé devienne trompeur.

### 4.8 `version`

Définit la version du document.

Pour les conventions, standards, spécifications et ressources réutilisables, utiliser le format SemVer :

`MAJOR.MINOR.PATCH`

| Niveau | Signification                                                 | Exemple       |
| ------ | ------------------------------------------------------------- | ------------- |
| MAJOR  | Modification incompatible ou changement important du contrat. | 1.0.0 → 2.0.0 |
| MINOR  | Ajout compatible de règles ou de capacités.                   | 1.0.0 → 1.1.0 |
| PATCH  | Correction sans modification substantielle du contrat.        | 1.0.0 → 1.0.1 |

Cette convention de versionnement est appliquée aux documents qui possèdent une véritable gestion de versions.

Les notes, comptes rendus et captures ponctuelles n'ont pas besoin d'une version artificielle.

**Important :** `version` désigne toujours la version du document, jamais celle du logiciel décrit.

Lorsqu'un document doit préciser la version d'un produit ou système qu'il décrit, cette information appartient à son contenu ou à une extension spécialisée explicitement définie.

Exemple :

```
version: "1.2.0"
```

### 4.9 `status`

Indique l'état actuel du document.

Valeurs communes :

| Valeur       | Signification                                               |
| ------------ | ----------------------------------------------------------- |
| `draft`      | Document en cours de rédaction.                             |
| `review`     | Document soumis à vérification.                             |
| `approved`   | Document validé pour son utilisation prévue.                |
| `deprecated` | Document conservé mais dont l'utilisation est déconseillée. |
| `archived`   | Document conservé à titre historique.                       |

Un document `deprecated` ou `archived` ne doit pas être supprimé automatiquement.

Lorsqu'un document est remplacé, il est recommandé d'indiquer son successeur dans son contenu ou dans une extension de relation adaptée.

L'état `approved` signifie que le document a été validé selon les règles applicables à son périmètre. Il ne signifie pas qu'il est universellement applicable.

### 4.10 `created`

Indique la date de création initiale du document.

Cette date ne change jamais lors des modifications ultérieures.

```
created: "2026-11-02"
```

### 4.11 `updated`

Indique la date de dernière modification significative du document.

Elle doit être actualisée lorsque le contenu ou les métadonnées ayant une incidence sur son interprétation changent.

Elle ne doit pas être modifiée pour une simple consultation, une ouverture ou une vérification sans changement.

```
updated: "2026-11-02"
```

Cette propriété correspond à la date de modification du document, pas à celle de sa dernière consultation.

### 4.12 `scope`

Définit le périmètre auquel le document s'applique.

Cette propriété est particulièrement importante pour les conventions, standards, règles et instructions.

Structure :

```
scope:
  level: universal
  targets:
    - all-projects
```

Valeurs autorisées pour `level` :

| Valeur      | Périmètre                                       |
| ----------- | ----------------------------------------------- |
| `universal` | Ensemble des projets utilisant le socle commun. |
| `domain`    | Domaine spécialisé.                             |
| `project`   | Projet particulier.                             |

`targets` précise les éléments concernés.

Exemples :

```
scope:
  level: domain
  targets:
    - web-development
```

```
scope:
  level: project
  targets:
    - project-alpha
```

Règles :

- `level` est obligatoire lorsque `scope` est renseigné.
- `targets` doit contenir au moins une valeur.
- Les valeurs doivent être identifiables et cohérentes avec la taxonomie applicable.
- Un document ne doit pas revendiquer un périmètre plus large que celui réellement couvert.

Pour un document purement informatif sans périmètre d'application particulier, `scope` peut être omis.

### 4.13 `extends`

Identifie les conventions dont le document hérite.

Cette propriété est réservée aux documents qui complètent ou spécialisent une convention existante.

Exemple :

```
extends:
  - "conventions/METADATA.md"
```

Règles :

- Les références doivent pointer vers des documents existants.
- Les chemins sont relatifs à la racine du dépôt.
- Les règles héritées ne doivent pas être recopiées inutilement.
- Une règle locale ne peut pas modifier silencieusement une règle héritée.
- Les incompatibilités doivent être explicites et justifiées.

L'héritage permet de construire une hiérarchie de conventions sans duplication.

### 4.14 `depends_on`

Identifie les documents dont dépend la compréhension ou l'application du document courant.

Exemple :

```
depends_on:
  - "conventions/TAXONOMY.md"
  - "conventions/NAMING.md"
```

Différence avec `extends` :

- `extends` exprime une relation d'héritage normatif.
- `depends_on` exprime une dépendance documentaire ou fonctionnelle.

Une convention peut donc dépendre d'un document sans en hériter.

Ne pas déclarer systématiquement tous les documents mentionnés dans le contenu. Cette propriété est réservée aux dépendances réellement utiles.

### 4.15 `updated_from`

Identifie les sources utilisées lors de la dernière mise à jour significative.

Exemple :

```
updated_from:
  - "brain/decisions/DEC-004.md"
  - "docs/architecture.md"
  - "https://example.com/reference"
```

Les références peuvent être :

- Un chemin de fichier relatif à la racine du dépôt.
- Une URL.
- Un identifiant stable provenant d'un registre.
- Une référence à une source externe identifiable.

Règles :

- Ne renseigner que les sources réellement utilisées.
- Ne pas recopier les conversations ou documents entiers.
- Préférer une référence stable plutôt qu'une description libre.
- Ne pas considérer cette propriété comme un historique complet.
- Remplacer les sources lors d'une nouvelle mise à jour significative, plutôt que d'accumuler indéfiniment les anciennes.

Si aucune source externe ou identifiable n'a été utilisée, la propriété peut être omise.

### 4.16 `tags`

Contient des mots-clés facilitant l'indexation.

Exemple :

```
tags:
  - metadata
  - documentation
  - agents
```

Les tags doivent :

- Être courts.
- Être écrits en minuscules.
- Utiliser le `snake_case` si plusieurs mots sont nécessaires.
- Réutiliser les termes existants de la taxonomie lorsqu'ils existent.
- Éviter de répéter les informations déjà présentes dans `type` ou `scope`.

Les tags restent facultatifs.

---

## 5. Propriétés conditionnelles et extensions

### 5.1 Principe

Le socle commun ne doit pas devenir une collection de propriétés spécialisées.

Lorsqu'une propriété ne concerne qu'une catégorie de documents, elle doit être définie dans la convention spécialisée correspondante.

Exemples :

| Propriété      | Documents concernés                                     |
| -------------- | ------------------------------------------------------- |
| `scope`        | Conventions, standards et règles.                       |
| `extends`      | Conventions et standards héritant d'autres conventions. |
| `depends_on`   | Documents présentant des dépendances significatives.    |
| `updated_from` | Documents nécessitant une traçabilité des sources.      |
| `summary`      | Documents suffisamment longs ou complexes.              |

### 5.2 Extensions spécialisées

Les conventions spécialisées peuvent ajouter des propriétés.

Exemple :

```
metadata_version: 1

title: "Convention Web"
type: convention
description: "Définit les règles spécifiques aux projets Web."

version: "1.0.0"
status: approved

created: "2026-11-02"
updated: "2026-11-02"

scope:
  level: domain
  targets:
    - web-development

extends:
  - "conventions/METADATA.md"

web:
  framework: nextjs
  rendering: server_components
```

Dans cet exemple, `web` représente une extension spécialisée.

Règles :

- Les propriétés du socle commun conservent leur signification.
- Une extension ne peut pas redéfinir le type ou la signification d'une propriété existante.
- Les extensions doivent être documentées.
- Les noms doivent rester explicites.
- Les propriétés spécialisées doivent être regroupées sous un espace de noms propre au domaine.
- Les propriétés inutilisées ne doivent pas être déclarées.

Un projet peut également définir une extension locale si ses besoins le justifient.

### 5.3 Compatibilité ascendante

Une convention spécialisée doit rester compatible avec le socle commun.

Si une évolution nécessite de modifier une propriété universelle, la modification doit être apportée au niveau universel et faire l'objet d'une évolution explicite de la convention concernée.

---

## 6. Conventions par format de fichier

### 6.1 Markdown

Markdown constitue le format de référence pour les documents.

Les métadonnées utilisent un YAML Front Matter placé au tout début du fichier.

Structure :

```
---
metadata_version: 1
title: "Exemple de document"
type: guide
description: "Présente un exemple de déclaration de métadonnées."
version: "1.0.0"
status: approved
created: "2026-11-02"
updated: "2026-11-02"
---

# Exemple de document

Contenu du document.
```

Règles :

1. Le front matter doit être le premier élément du fichier.
2. Il commence et se termine par une ligne contenant `---`.
3. Il respecte la syntaxe YAML.
4. Les propriétés communes utilisent les noms définis dans cette convention.
5. Le contenu Markdown commence après la fermeture du front matter.
6. Les propriétés non pertinentes sont omises.
7. Un seul bloc de métadonnées est utilisé.

Le YAML doit être compatible avec un parseur YAML 1.2.

Il est recommandé d'utiliser des guillemets pour les dates, les versions et les chaînes pouvant être interprétées comme des valeurs particulières.

### 6.2 TOML

TOML est destiné en priorité aux fichiers de configuration.

Il ne doit pas être utilisé comme remplacement automatique du YAML Front Matter.

Lorsqu'un fichier TOML doit également décrire ses propres métadonnées, celles-ci peuvent être regroupées dans une section `[metadata]`.

Exemple :

```
[metadata]
metadata_version = 1
title = "Configuration du système"
type = "configuration"
description = "Définit les paramètres du système."
version = "1.0.0"
status = "approved"
created = 2026-11-02
updated = 2026-11-02

[application]
debug = false
environment = "production"
```

Règles :

- La section `[metadata]` est distincte des paramètres fonctionnels.
- Les propriétés documentaires ne doivent pas être mélangées aux paramètres métier.
- Les propriétés facultatives sont omises lorsqu'elles ne sont pas pertinentes.
- Le format TOML doit respecter sa version de spécification adoptée par le projet.

Un fichier de configuration ne doit pas être enrichi de métadonnées simplement pour respecter une uniformité visuelle.

### 6.3 JSON

JSON utilise un objet `_metadata` lorsque le fichier représente une ressource structurée nécessitant ses propres métadonnées.

Exemple :

```
{
  "_metadata": {
    "metadata_version": 1,
    "title": "Registre des projets",
    "type": "data",
    "description": "Contient les informations structurées des projets.",
    "version": "1.0.0",
    "status": "approved",
    "created": "2026-11-02",
    "updated": "2026-11-02"
  },
  "projects": []
}
```

Règles :

- `_metadata` est un espace réservé aux métadonnées documentaires.
- Les données métier restent au niveau fonctionnel prévu.
- Les propriétés non pertinentes sont omises.
- Les objets doivent respecter la syntaxe JSON standard.
- Les clés et types doivent rester cohérents avec le modèle commun.

Si le format d'un outil impose un schéma strict ne permettant pas d'ajouter `_metadata`, utiliser un index externe plutôt que de casser sa compatibilité.

### 6.4 JSONL

JSONL est destiné aux données structurées organisées en enregistrements indépendants.

La convention ne modifie pas son fonctionnement et ne crée pas de nouveau modèle de registre.

Chaque ligne doit rester un objet JSON autonome et valide.

Les métadonnées doivent être intégrées à chaque enregistrement uniquement lorsque celui-ci représente un objet documentaire possédant réellement ses propres propriétés.

Exemple :

```
{"id":"CAP-001","type":"capture","content":"Première capture","created":"2026-11-02"}
{"id":"CAP-002","type":"capture","content":"Deuxième capture","created":"2026-11-02"}
```

Dans cet exemple, les propriétés sont des données propres au registre. Elles ne nécessitent pas automatiquement un bloc `_metadata`.

Pour un enregistrement représentant un document autonome :

```
{"id":"DOC-001","_metadata":{"metadata_version":1,"title":"Document de référence","type":"reference","description":"Décrit une ressource de référence.","status":"approved","created":"2026-11-02","updated":"2026-11-02"},"content":"Contenu du document."}
```

Règles :

- Ne pas ajouter de ligne d'en-tête non JSON.
- Ne pas introduire de commentaires.
- Ne pas transformer le registre en document Markdown.
- Ne pas imposer de métadonnées documentaires à chaque événement.
- Ne pas dupliquer les métadonnées déjà présentes dans le schéma fonctionnel du registre.

Le format JSONL conserve sa fonction première : faciliter l'ajout, la lecture et le traitement automatisé des enregistrements.

### 6.5 Code source

Les fichiers de code source ne doivent pas recevoir de YAML Front Matter artificiel.

La documentation doit utiliser les mécanismes adaptés au langage.

Exemples :

**TypeScript :**

```
/**
 * Gestion des métadonnées documentaires.
 *
 * Fournit les fonctions de validation et de normalisation
 * des métadonnées.
 */
export function validateMetadata() {
  // ...
}
```

**Python :**

```
"""
Gestion des métadonnées documentaires.

Fournit les fonctions de validation et de normalisation
des métadonnées.
"""

def validate_metadata():
    pass
```

Règles :

- Utiliser les commentaires documentaires natifs.
- Documenter la responsabilité du module ou de la fonction.
- Éviter de répéter le nom du fichier, le chemin ou la version du projet.
- Ne pas imposer de propriétés documentaires à chaque fichier source.
- Préférer les mécanismes de documentation déjà adoptés par le langage ou le framework.

Les métadonnées du projet ou du logiciel doivent être déclarées dans leur fichier de référence approprié, et non répétées dans chaque fichier source.

### 6.6 Images et ressources graphiques

Les images et ressources graphiques peuvent posséder des métadonnées natives.

Selon le format, privilégier :

- EXIF.
- IPTC.
- XMP.
- Métadonnées natives des logiciels de conception.

Les propriétés documentaires peuvent inclure :

- Titre.
- Description.
- Date de création.
- Auteur, lorsque pertinent.
- Droits d'utilisation.
- Version ou état d'une ressource, lorsque nécessaire.

Ne pas modifier inutilement les fichiers originaux pour y intégrer des métadonnées.

Attention aux informations personnelles ou techniques pouvant être présentes dans les métadonnées natives, notamment les coordonnées GPS.

### 6.7 Documents bureautiques

Pour les formats DOCX, XLSX, PPTX et autres formats similaires, privilégier les propriétés natives du document lorsqu'elles sont disponibles.

Les métadonnées externes peuvent compléter ces propriétés lorsque les besoins d'indexation dépassent les capacités natives.

Il faut éviter de maintenir deux versions contradictoires des mêmes informations.

### 6.8 Fichiers binaires et formats incompatibles

Certains fichiers ne permettent pas d'intégrer directement des métadonnées exploitables.

Dans ce cas, utiliser un index externe ou un fichier associé.

Exemple :

```
assets/
├── logo.svg
├── background.png
└── metadata/
    ├── logo.svg.json
    └── background.png.json
```

Exemple de fichier associé :

```
{
  "_metadata": {
    "metadata_version": 1,
    "title": "Logo principal",
    "type": "reference",
    "description": "Logo principal utilisé par le projet.",
    "status": "approved",
    "created": "2026-11-02",
    "updated": "2026-11-02"
  },
  "asset": "assets/logo.svg"
}
```

Règles :

- Le fichier associé doit identifier précisément la ressource.
- Le nommage des fichiers associés doit suivre la convention de nommage générale.
- Les chemins doivent être résolus sans ambiguïté.
- L'index externe ne doit pas devenir une copie complète du contenu original.
- La ressource originale reste la source de vérité pour son contenu.

---

## 7. Hiérarchie et héritage des conventions

### 7.1 Trois niveaux d'application

Le système distingue trois niveaux.

**Niveau 1 — Universel**

Définit les règles communes applicables à tous les projets utilisant le socle.

Exemples :

- Métadonnées.
- Nommage.
- Taxonomie.
- Standardisation documentaire.

**Niveau 2 — Domaine**

Complète les règles universelles pour un domaine spécifique.

Exemples :

- Développement Web.
- Développement Mobile.
- Direction artistique.
- Développement logiciel.

**Niveau 3 — Projet**

Ajoute les adaptations nécessaires à un projet particulier.

### 7.2 Déclaration du périmètre

Chaque convention doit déclarer son périmètre à travers `scope`.

Exemple universel :

```
scope:
  level: universal
  targets:
    - all-projects
```

Exemple spécialisé :

```
scope:
  level: domain
  targets:
    - mobile-development

extends:
  - "conventions/METADATA.md"
```

Exemple projet :

```
scope:
  level: project
  targets:
    - project-alpha

extends:
  - "brain-main/conventions/METADATA.md"
  - "brain-main/conventions/SOFTWARE.md"
```

Les chemins présentés sont illustratifs et doivent correspondre à l'organisation réelle du dépôt.

### 7.3 Règles d'héritage

Une convention spécialisée hérite des règles de ses conventions parentes.

Elle peut :

- Ajouter des propriétés.
- Ajouter des règles spécifiques.
- Préciser les modalités d'application.
- Définir des exceptions locales justifiées.

Elle ne peut pas :

- Supprimer silencieusement une propriété obligatoire.
- Modifier la signification d'une propriété universelle.
- Contredire une convention parente sans déclaration explicite.
- Reproduire intégralement les règles héritées sans justification.

### 7.4 Gestion des conflits

En cas de contradiction :

1. Identifier les documents concernés.
2. Vérifier leur statut et leur périmètre.
3. Identifier la règle héritée.
4. Identifier la règle locale contradictoire.
5. Déterminer si l'exception est explicitement autorisée.
6. Signaler le conflit lorsqu'il ne peut pas être résolu par la hiérarchie.

Une convention locale ne devient pas prioritaire simplement parce qu'elle est plus récente.

Toute modification d'une règle universelle doit être réalisée au niveau universel.

---

## 8. Gestion des versions et des mises à jour

### 8.1 Version documentaire

La propriété `version` représente l'évolution du document.

Elle ne doit pas être confondue avec :

- La version du projet.
- La version d'un logiciel.
- La version d'une API.
- La version du schéma de données.
- La version de la convention des métadonnées elle-même.

Chaque concept doit disposer de son propre emplacement lorsqu'il est nécessaire.

### 8.2 Mise à jour de `updated`

`updated` doit être modifié lorsqu'une modification significative intervient.

Exemples :

- Modification d'une règle.
- Ajout ou suppression d'une section.
- Correction d'une information importante.
- Modification d'une dépendance.
- Modification du périmètre.
- Modification des métadonnées ayant une incidence sur l'interprétation.

Une modification purement cosmétique et sans conséquence documentaire ne nécessite pas nécessairement une nouvelle version.

### 8.3 Gestion de `updated_from`

Lorsqu'une mise à jour repose sur des sources identifiables, les références doivent être actualisées.

Exemple :

Avant :

```
updated_from:
  - "brain/decisions/DEC-001.md"
```

Après une nouvelle mise à jour :

```
updated_from:
  - "brain/decisions/DEC-001.md"
  - "brain/decisions/DEC-005.md"
```

La liste représente les sources de la dernière mise à jour, pas l'ensemble des sources historiques du document.

Les sources précédentes peuvent être retrouvées dans Git ou dans les mécanismes historiques déjà utilisés par le projet.

### 8.4 Historique

L'historique détaillé des modifications ne doit pas être intégré systématiquement au front matter.

Utiliser les mécanismes existants :

- Historique Git.
- Journal d'activité.
- Registre des décisions.
- Registre de provenance.
- Historique propre à l'outil concerné.

La convention des métadonnées ne crée pas un nouveau système d'historisation.

### 8.5 Prévention des métadonnées obsolètes

Une mise à jour documentaire doit vérifier :

- Que `description` représente toujours le contenu.
- Que `summary` reste fidèle au document.
- Que `status` est correct.
- Que `updated` est actualisé.
- Que `version` est cohérente avec l'évolution.
- Que `scope` n'est pas devenu incorrect.
- Que les références `extends` et `depends_on` existent.
- Que `updated_from` reflète les sources de la dernière mise à jour.

Une modification du contenu ne doit pas entraîner automatiquement une modification de toutes les propriétés.

---

## 9. Structure documentaire et recherche ciblée

### 9.1 Organisation des documents

Les métadonnées permettent d'identifier un document, mais ne remplacent pas une structure de contenu cohérente.

Les documents longs doivent utiliser des titres Markdown hiérarchisés.

Exemple :

```
# Titre du document

## 1. Présentation

## 2. Principes

## 3. Fonctionnement

### 3.1 Première partie

### 3.2 Deuxième partie

## 4. Références
```

### 9.2 Sections identifiables

Pour faciliter la recherche ciblée :

- Utiliser des titres explicites.
- Conserver une hiérarchie logique.
- Éviter les titres trop génériques.
- Utiliser une numérotation lorsque la stabilité des références est importante.
- Éviter les sections excessivement longues.

### 9.3 Sommaire

Un sommaire n'est pas obligatoire.

Il est recommandé lorsque le document contient suffisamment de sections pour que la navigation devienne utile.

Il doit rester cohérent avec les titres réellement présents.

Un sommaire généré automatiquement est préférable à un sommaire manuel lorsque l'outillage le permet.

### 9.4 Lecture sélective par les agents

Un agent doit pouvoir procéder progressivement :

1. Lire les métadonnées.
2. Évaluer la pertinence du document.
3. Lire le résumé.
4. Consulter le sommaire si nécessaire.
5. Lire uniquement les sections utiles.
6. Consulter le document complet si la tâche l'exige.

Un agent ne doit pas systématiquement charger tous les documents d'un projet.

---

## 10. Gestion des fichiers sans métadonnées natives

### 10.1 Principe

Tous les fichiers n'ont pas besoin d'intégrer directement leurs métadonnées.

Lorsque le format ne le permet pas ou que la modification serait inappropriée, un mécanisme d'indexation externe peut être utilisé.

### 10.2 Priorité des sources

Pour déterminer les informations relatives à un fichier, respecter l'ordre suivant :

1. Métadonnées natives fiables.
2. Métadonnées intégrées au fichier.
3. Fichier associé explicitement référencé.
4. Index externe du projet.
5. Informations déduites du contexte, identifiées comme telles.

Une information déduite ne doit jamais être présentée comme une métadonnée vérifiée.

### 10.3 Cohérence

Si plusieurs sources déclarent la même propriété :

- Identifier la source de vérité.
- Éviter les mises à jour concurrentes.
- Signaler les divergences.
- Ne pas écraser automatiquement une information fiable par une valeur déduite.

---

## 11. Bonnes pratiques pour les agents IA

### 11.1 Découverte d'un document

Lorsqu'un agent découvre un document :

1. Lire son front matter ou son mécanisme de métadonnées.
2. Vérifier son type.
3. Vérifier son statut.
4. Vérifier son périmètre.
5. Examiner ses dépendances.
6. Évaluer son résumé.
7. Lire les sections pertinentes.

L'agent doit prendre en compte les métadonnées avant d'utiliser le contenu comme référence.

### 11.2 Documents obsolètes ou remplacés

Un agent doit tenir compte de `status`.

- `draft` : ne pas considérer comme une règle officiellement validée.
- `review` : considérer comme une proposition en cours de vérification.
- `approved` : peut être utilisé dans le cadre de son périmètre.
- `deprecated` : rechercher une éventuelle alternative.
- `archived` : utiliser principalement à des fins historiques.

Le statut ne doit jamais être utilisé isolément pour déterminer la fiabilité du contenu.

### 11.3 Gestion des dépendances

Avant d'appliquer une convention spécialisée :

- Identifier ses conventions parentes.
- Lire les règles héritées pertinentes.
- Vérifier les éventuelles exceptions.
- Détecter les contradictions.
- Ne pas supposer qu'une dépendance est facultative simplement parce qu'elle n'a pas été chargée.

### 11.4 Mise à jour des métadonnées

Un agent qui modifie un document doit :

- Préserver les propriétés existantes valides.
- Modifier uniquement les propriétés concernées.
- Ne jamais inventer une source.
- Ne pas modifier artificiellement `created`.
- Actualiser `updated` lorsqu'une modification significative intervient.
- Actualiser `summary` si nécessaire.
- Adapter `version` selon les règles applicables.
- Conserver les extensions reconnues.
- Signaler les informations manquantes plutôt que les inventer.

### 11.5 Métadonnées et confiance

Les métadonnées décrivent un document, mais ne prouvent pas à elles seules la véracité de son contenu.

Un agent doit distinguer :

- Information déclarée.
- Information vérifiée.
- Information déduite.
- Information proposée.
- Information validée.

Ces distinctions appartiennent au contenu, au système de provenance ou aux conventions métier appropriées.

Elles ne doivent pas être artificiellement ajoutées au socle universel des métadonnées.

---

## 12. Automatisation et validation

### 12.1 Objectifs

La validation automatique doit permettre de détecter :

- Les propriétés obligatoires manquantes.
- Les propriétés inconnues non documentées.
- Les types incorrects.
- Les valeurs de statut invalides.
- Les dates mal formatées.
- Les versions invalides.
- Les références inexistantes.
- Les problèmes de hiérarchie.
- Les métadonnées incohérentes avec le contenu.

### 12.2 Niveaux de validation

Trois niveaux sont recommandés.

**Niveau 1 — Syntaxe**

Vérifier que le bloc de métadonnées peut être correctement parsé.

**Niveau 2 — Structure**

Vérifier :

- La présence des propriétés obligatoires.
- Le type de chaque valeur.
- Les valeurs autorisées.
- La conformité des structures imbriquées.

**Niveau 3 — Cohérence**

Vérifier :

- La cohérence entre `title`, `description` et le contenu.
- La validité des chemins.
- La cohérence des dépendances.
- La compatibilité des extensions.
- La cohérence entre le statut et l'usage du document.

### 12.3 Règles de validation

| Contrôle                       | Niveau              | Résultat attendu                   |
| ------------------------------ | ------------------- | ---------------------------------- |
| Présence de `metadata_version` | Syntaxe / structure | Obligatoire                        |
| Présence de `title`            | Structure           | Obligatoire                        |
| Présence de `type`             | Structure           | Obligatoire                        |
| Présence de `description`      | Structure           | Obligatoire                        |
| Présence de `status`           | Structure           | Obligatoire                        |
| Présence de `created`          | Structure           | Obligatoire                        |
| Présence de `updated`          | Structure           | Obligatoire                        |
| Format des dates               | Structure           | ISO 8601                           |
| Valeur de `status`             | Structure           | Valeur autorisée                   |
| Format de `version`            | Structure           | SemVer si versionnement applicable |
| Structure de `scope`           | Structure           | Conforme au modèle                 |
| Existence de `extends`         | Cohérence           | Référence valide                   |
| Existence de `depends_on`      | Cohérence           | Référence valide                   |
| Validité de `updated_from`     | Cohérence           | Référence exploitable              |
| Fidélité de `summary`          | Cohérence           | Vérification sémantique            |

Les contrôles conditionnels doivent tenir compte du type de document.

Un fichier qui ne possède pas de `scope` n'est pas nécessairement non conforme.

### 12.4 Tolérance aux extensions

Un validateur universel doit accepter les propriétés supplémentaires lorsqu'elles appartiennent à une extension reconnue.

Il ne doit pas rejeter systématiquement un document parce qu'il contient une propriété spécialisée.

En revanche, une propriété inconnue et non documentée doit pouvoir être signalée.

### 12.5 Sévérité des erreurs

| Sévérité | Utilisation                                                    |
| -------- | -------------------------------------------------------------- |
| Error    | Métadonnées invalides ou incompatibles avec le contrat.        |
| Warning  | Métadonnées incomplètes ou incohérentes sans blocage immédiat. |
| Info     | Amélioration facultative ou recommandation.                    |

Une erreur de validation ne doit pas entraîner automatiquement la suppression ou la correction destructive d'un document.

### 12.6 Validation automatisée du contenu

Certaines propriétés ne peuvent pas être validées correctement par un simple schéma.

Exemples :

- Un résumé fidèle au contenu.
- Une description suffisamment précise.
- Une dépendance réellement nécessaire.
- Un périmètre correctement défini.

Ces vérifications peuvent être assistées par un agent IA, mais doivent être distinguées des validations structurelles déterministes.

---

## 13. Intégration avec Capture et Review

### 13.1 Capture

La phase Capture est responsable de la collecte initiale.

Elle peut :

- Identifier les documents concernés.
- Lire leurs métadonnées.
- Extraire les informations pertinentes.
- Conserver les références des sources.
- Proposer des métadonnées initiales lorsqu'un nouveau document est créé.

Capture ne doit pas modifier arbitrairement les documents de référence existants.

Les informations incertaines doivent rester identifiées comme telles.

### 13.2 Review

La phase Review est responsable de la consolidation.

Elle peut :

- Détecter les métadonnées manquantes.
- Identifier les documents dont les descriptions sont obsolètes.
- Détecter les incohérences entre résumé et contenu.
- Vérifier les références et dépendances.
- Proposer des modifications.
- Mettre à jour les propriétés lorsque les règles d'autorisation le permettent.

### 13.3 Préservation de l'historique

Capture et Review doivent respecter les règles suivantes :

1. Ne jamais modifier `created` après sa création.
2. Ne jamais inventer une source de mise à jour.
3. Ne pas effacer les références historiques conservées dans les mécanismes de provenance.
4. Ne pas remplacer silencieusement un document validé.
5. Ne pas transformer une proposition en décision validée sans autorisation appropriée.
6. Ne pas confondre mise à jour des métadonnées et modification du contenu.
7. Préserver les propriétés spécialisées.
8. Utiliser les mécanismes historiques existants pour tracer les changements.

Une correction de métadonnées peut être réalisée sans modifier le contenu documentaire si celui-ci reste valide.

---

## 14. Exemples de conformité

### 14.1 Convention universelle

```
---
metadata_version: 1

title: "Convention de nommage"
type: convention
description: "Définit les règles communes de nommage des fichiers."

version: "1.0.0"
status: approved

created: "2026-11-02"
updated: "2026-11-02"

scope:
  level: universal
  targets:
    - all-projects
---
```

**Conformité :** les propriétés communes sont présentes et le périmètre est explicite.

### 14.2 Convention spécialisée

```
---
metadata_version: 1

title: "Convention de développement Web"
type: convention
description: "Définit les règles spécifiques aux projets Web."

version: "1.0.0"
status: approved

created: "2026-11-02"
updated: "2026-11-02"

scope:
  level: domain
  targets:
    - web-development

extends:
  - "conventions/METADATA.md"
  - "conventions/SOFTWARE.md"
---
```

**Conformité :** la convention déclare son périmètre et référence ses conventions parentes sans recopier leurs règles.

### 14.3 Document informatif simple

```
---
metadata_version: 1

title: "Compte rendu de réunion"
type: report
description: "Présente les sujets abordés et les conclusions de la réunion."

status: approved

created: "2026-11-02"
updated: "2026-11-02"
---
```

**Conformité :** les propriétés de versionnement et de dépendance sont omises car elles ne sont pas nécessaires.

### 14.4 Document avec sources

```
---
metadata_version: 1

title: "Étude comparative"
type: report
description: "Compare plusieurs solutions techniques."
summary: "Analyse les différences fonctionnelles et techniques entre les solutions étudiées."

version: "1.0.0"
status: review

created: "2026-11-02"
updated: "2026-11-02"

updated_from:
  - "brain/research/RESEARCH-001.md"
  - "https://example.com/documentation"
---
```

**Conformité :** les sources de la dernière mise à jour sont identifiables.

---

## 15. Exemples de non-conformité

### 15.1 Propriétés obligatoires manquantes

```
---
title: "Convention de nommage"
description: "Définit le nommage."
---
```

**Non conforme :**

- `metadata_version` absent.
- `type` absent.
- `status` absent.
- `created` absent.
- `updated` absent.

### 15.2 Noms incohérents

```
---
documentTitle: "Convention"
document_type: convention
lastUpdate: "2026-11-02"
---
```

**Non conforme :** les propriétés utilisent des noms différents de ceux du socle commun.

### 15.3 Version ambiguë

```
version: "V2"
```

**Non conforme pour un document versionné selon SemVer :** format non standard.

### 15.4 Périmètre mal structuré

```
scope: "Tous les projets"
```

**Non conforme pour une convention nécessitant un périmètre :** la structure attendue n'est pas respectée.

### 15.5 Dépendance non résolue

```
extends:
  - "conventions/UNKNOWN.md"
```

**Non conforme :** la convention parente référencée n'existe pas.

### 15.6 Métadonnées redondantes

```
---
title: "Gestion des utilisateurs"
project_name: "Project Alpha"
software_version: "2.4.0"
repository: "Project Alpha"
description: "Gestion des utilisateurs."
---
```

**Non conforme aux principes de conception si ces informations sont déjà disponibles dans une source fiable et n'ont aucune nécessité documentaire.**

Les métadonnées ne doivent pas devenir une copie du contexte complet du projet.

---

## 16. Recommandations d'implémentation

### 16.1 Priorités

L'implémentation doit être progressive.

**Priorité 1 — Standard documentaire**

- Adopter le YAML Front Matter pour Markdown.
- Définir les propriétés communes.
- Uniformiser les noms et les types.
- Documenter les statuts et les types.

**Priorité 2 — Validation**

- Ajouter un parseur YAML.
- Vérifier les propriétés obligatoires.
- Vérifier les valeurs autorisées.
- Vérifier les références documentaires.

**Priorité 3 — Automatisation**

- Permettre aux agents de lire les métadonnées.
- Faciliter les mises à jour.
- Vérifier les résumés et les dépendances.
- Intégrer les contrôles dans Capture et Review.

**Priorité 4 — Formats complémentaires**

- Définir les règles d'intégration JSON et TOML.
- Préserver la compatibilité JSONL.
- Exploiter les métadonnées natives.
- Mettre en place un index externe uniquement lorsque nécessaire.

### 16.2 Principe de validation

La validation doit être centralisée autour d'un même modèle conceptuel.

Il ne faut pas développer une logique documentaire différente pour chaque type de fichier.

Chaque format doit disposer d'un mécanisme d'extraction adapté, puis transmettre les propriétés extraites au même moteur de validation.

### 16.3 Évolution de la convention

Toute évolution doit respecter les règles suivantes :

- Préserver la compatibilité lorsque cela est possible.
- Documenter les nouvelles propriétés.
- Identifier les propriétés devenues obsolètes.
- Prévoir une migration lorsqu'un changement incompatible intervient.
- Éviter les migrations massives sans bénéfice réel.
- Mettre à jour les exemples et les règles de validation.

---

## 17. Règles finales

Les règles suivantes constituent le contrat minimal de cette convention.

1. Les documents Markdown utilisent un YAML Front Matter lorsqu'ils nécessitent des métadonnées documentaires.
2. Les propriétés communes utilisent les noms définis dans cette convention.
3. Les propriétés obligatoires doivent être présentes.
4. Les propriétés non pertinentes doivent être omises.
5. Les propriétés spécialisées doivent être documentées dans leur convention respective.
6. Les conventions déclarent leur périmètre avec `scope`.
7. L'héritage normatif est déclaré avec `extends`.
8. Les dépendances documentaires sont déclarées avec `depends_on`.
9. La version documentaire est indépendante de la version du logiciel décrit.
10. Les dates respectent ISO 8601.
11. Les sources de la dernière mise à jour sont déclarées avec `updated_from` lorsqu'elles sont identifiables.
12. L'historique détaillé reste dans les mécanismes existants.
13. Les formats incompatibles ne doivent pas recevoir artificiellement des métadonnées.
14. Les extensions ne doivent pas modifier silencieusement le sens du socle commun.
15. Les agents IA doivent préserver les métadonnées existantes et ne jamais inventer les informations manquantes.

---

## 18. Glossaire

| Terme                | Définition                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------- |
| Métadonnées          | Informations décrivant une ressource.                                                       |
| Front Matter         | Bloc de métadonnées placé au début d'un document.                                           |
| Socle commun         | Ensemble des propriétés universelles.                                                       |
| Extension            | Propriété complémentaire propre à un domaine ou projet.                                     |
| Périmètre            | Ensemble des éléments auxquels un document s'applique.                                      |
| Héritage             | Relation par laquelle une convention reprend les règles d'une autre.                        |
| Dépendance           | Relation indiquant qu'un document nécessite un autre document.                              |
| Provenance           | Origine d'une information ou d'une modification.                                            |
| Version documentaire | Version propre au document.                                                                 |
| Validation           | Vérification de la conformité structurelle et sémantique.                                   |
| Index externe        | Structure permettant de décrire des fichiers ne supportant pas directement les métadonnées. |

---

**Fin de la convention universelle des métadonnées.**