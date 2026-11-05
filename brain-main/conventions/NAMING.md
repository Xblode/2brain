---
metadata_version: 1

title: "Convention de nommage"
type: convention
description: "Définit les principes communs de nommage des fichiers et dossiers des projets utilisant le socle de standardisation."
summary: "Convention universelle de nommage des fichiers et dossiers : concept et responsabilité avant description, noms courts, contexte fourni par l'arborescence, casse par type de fichier, centralisation des variantes, portabilité, exceptions et règles applicables aux agents IA. Elle ne couvre pas les identifiants internes au code."

version: "1.0.0"
status: review

created: "2026-11-02"
updated: "2026-11-05"

scope:
  level: universal
  targets:
    - all-projects

depends_on:
  - "brain-main/conventions/METADATA.md"

updated_from:
  - "brain-main/conventions/METADATA.md"
  - "brain-main/conventions/TAXONOMY.md"
  - "brain-main/conventions/README.md"

tags:
  - naming
  - files
  - standardization
---

# NAMING — Convention de nommage

## 1. Objectifs et périmètre

### 1.1. Objectif

Cette convention définit les principes communs de nommage des fichiers et dossiers au sein des projets utilisant le socle de standardisation.

Elle vise à garantir une organisation :

- Simple et compréhensible.
- Cohérente entre les projets.
- Facile à parcourir pour les humains et les agents IA.
- Adaptable aux différentes technologies.
- Évolutive sans multiplication inutile des règles.

Le nommage doit permettre d'identifier rapidement la responsabilité d'un élément, en tenant compte de son emplacement dans l'arborescence.

Conventions associées (catalogue : [README.md](README.md)) : [METADATA.md](METADATA.md) pour le front matter des fichiers Markdown, [TAXONOMY.md](TAXONOMY.md) pour les valeurs des champs de registre. Les fichiers de métadonnées associés à une ressource suivent cette convention de nommage (METADATA §6.8).

### 1.2. Périmètre

Cette convention couvre :

- Les documents et fichiers de documentation.
- Les dossiers et sous-dossiers.
- Les fichiers de code source.
- Les modules, services et composants.
- Les fichiers de configuration.
- Les données et registres.
- Les ressources et fichiers multimédias.
- Les fichiers générés et temporaires.

Elle définit uniquement le nommage des fichiers et dossiers.

Le nommage des variables, fonctions, classes, propriétés, composants au niveau de leur déclaration et autres identifiants internes relève des conventions propres aux langages et technologies.

### 1.3. Vocabulaire normatif

Les termes suivants indiquent le niveau d'exigence des règles :

| Terme       | Signification                                              |
| ----------- | ---------------------------------------------------------- |
| DOIT        | Règle obligatoire, sauf contrainte technique incompatible. |
| NE DOIT PAS | Pratique à proscrire, sauf nécessité technique.            |
| DEVRAIT     | Pratique recommandée par défaut.                           |
| PEUT        | Possibilité autorisée selon le contexte.                   |

Une préférence ne devient pas une obligation simplement parce qu'elle apparaît dans cette convention.

---

## 2. Philosophie générale

### 2.1. Nommer selon le concept et la responsabilité

Un nom doit représenter le concept principal ou la responsabilité de l'élément.

Le nommage doit privilégier la fonction réelle du fichier plutôt que sa description détaillée.

Exemples :

| À privilégier     | À éviter par défaut                    |
| ----------------- | -------------------------------------- |
| `card.tsx`        | `main-card-component.tsx`              |
| `payment.ts`      | `payment-processing-service-module.ts` |
| `VISION.md`       | `PROJECT_GLOBAL_VISION.md`             |
| `ARCHITECTURE.md` | `PROJECT_TECHNICAL_ARCHITECTURE.md`    |
| `DECISIONS.md`    | `ARCHITECTURAL_DECISION_REGISTER.md`   |

Un nom court est préférable lorsque le contexte permet de comprendre sa signification.

### 2.2. Privilégier les noms courts

Les noms composés d'un seul mot sont privilégiés lorsqu'ils sont suffisamment explicites.

Exemples :

- `components/`
- `services/`
- `card.tsx`
- `button.tsx`
- `ARCHITECTURE.md`

Les noms composés restent autorisés lorsqu'ils apportent une distinction utile.

Exemples :

- `user-profile.ts`
- `payment-gateway.ts`
- `PROJECT_BRIEF.md`

La simplicité ne doit jamais rendre le nom ambigu.

### 2.3. Utiliser le contexte fourni par l'arborescence

Le chemin d'un fichier fait partie intégrante de son identification.

Le nom ne doit pas répéter inutilement des informations déjà présentes dans les dossiers parents.

Exemple recommandé :

```
components/
├── card.tsx
├── button.tsx
└── modal.tsx
```

Exemple à éviter :

```
components/
├── component-card.tsx
├── component-button.tsx
└── component-modal.tsx
```

Le dossier `components` fournit déjà le contexte nécessaire.

Le même principe s'applique à la documentation, aux services, aux ressources et aux autres catégories.

### 2.4. Éviter les noms artificiellement descriptifs

Les noms ne doivent pas accumuler des qualificatifs qui n'apportent pas de distinction réelle.

Éviter notamment les termes suivants lorsqu'ils sont redondants :

- `main`
- `primary`
- `global`
- `default`
- `base`
- `manager`
- `handler`
- `component`
- `module`
- `file`

Ces termes ne sont pas interdits. Ils doivent correspondre à une distinction fonctionnelle réelle.

Par exemple, `user-manager.ts` peut être pertinent si le concept de manager existe réellement dans l'architecture.

En revanche, `main-card.tsx` n'est pas justifié simplement parce que le composant est le plus utilisé.

### 2.5. Favoriser la stabilité

Les noms doivent rester valables pendant la durée de vie de leur responsabilité.

Éviter les noms temporaires ou liés à un état de développement :

```
new-card.tsx
card-v2.tsx
final-architecture.md
test-final.md
```

Une évolution doit normalement modifier le contenu ou la version documentaire, pas entraîner une succession de renommages.

---

## 3. Conventions générales de casse

### 3.1. Convention par défaut

Le `kebab-case` constitue la convention technique générale.

Il utilise des lettres minuscules et sépare les mots par des tirets.

Exemples :

```
user-profile.ts
payment-gateway.ts
design-system/
product-images/
```

Cette convention est recommandée pour les fichiers techniques, les ressources et les dossiers lorsqu'aucune contrainte spécifique ne s'applique.

### 3.2. Documents de référence

Les documents structurants et de référence utilisent de préférence le `UPPER_SNAKE_CASE`.

Les mots sont écrits en majuscules et séparés par des underscores.

Exemples :

```
VISION.md
ARCHITECTURE.md
ROADMAP.md
DECISIONS.md
PROJECT_BRIEF.md
TECHNICAL_OVERVIEW.md
```

Les noms d'un seul mot restent privilégiés lorsqu'ils suffisent.

Cette convention permet de distinguer visuellement les documents de référence des fichiers techniques et des notes ordinaires.

Les noms imposés par des outils, tels que `README.md`, `AGENTS.md`, `CLAUDE.md` ou `SKILL.md`, sont conservés.

Les autres fichiers Markdown peuvent utiliser le `kebab-case` :

```
docs/
├── ARCHITECTURE.md
├── DECISIONS.md
├── guides/
│   ├── installation.md
│   └── deployment.md
└── notes/
    ├── 2026-11-02-review.md
    └── component-refactor.md
```

### 3.3. Conventions complémentaires

Les autres styles peuvent être utilisés lorsqu'ils sont imposés ou recommandés par une technologie.

| Convention         | Exemple            | Usage possible                                      |
| ------------------ | ------------------ | --------------------------------------------------- |
| `kebab-case`       | `user-profile.ts`  | Convention technique générale                       |
| `UPPER_SNAKE_CASE` | `PROJECT_BRIEF.md` | Documents de référence                              |
| `snake_case`       | `user_profile.py`  | Modules Python                                      |
| `camelCase`        | `userProfile.js`   | Certains projets JavaScript                         |
| `PascalCase`       | `UserProfile.java` | Classes et fichiers associés dans certains langages |

Il ne faut pas forcer une technologie à adopter une casse incompatible avec ses pratiques établies.

### 3.4. Extensions

Les extensions doivent être conservées et utiliser de préférence les minuscules.

Exemples :

```
card.tsx
config.json
architecture.md
logo.svg
```

Les extensions multiples sont autorisées lorsqu'elles correspondent à une convention technique :

```
card.test.tsx
card.module.css
```

Il ne faut pas créer artificiellement des extensions personnalisées pour remplacer une organisation documentaire cohérente.

---

## 4. Principes de nommage des fichiers

### 4.1. Identifier la responsabilité principale

Un fichier doit avoir une responsabilité identifiable.

Exemples :

```
card.tsx
payment.ts
product.ts
authentication.ts
```

Un fichier peut contenir plusieurs éléments étroitement liés, à condition qu'ils participent au même concept.

Le nom ne doit pas nécessairement énumérer tous les éléments contenus dans le fichier.

### 4.2. Utiliser des noms composés lorsque nécessaire

Un nom composé est pertinent lorsqu'il permet de distinguer plusieurs éléments de même catégorie.

Exemple :

```
services/
├── payment.ts
├── payment-gateway.ts
└── payment-provider.ts
```

Il permet ici de différencier des responsabilités.

Un nom composé peut également préciser :

- Un domaine.
- Une fonctionnalité.
- Une plateforme.
- Un format.
- Un rôle technique.
- Une distinction fonctionnelle.

Le nombre de mots n'est pas limité arbitrairement.

En revanche, chaque mot doit apporter une information utile.

### 4.3. Éviter les préfixes redondants

Les préfixes correspondant au type de fichier sont généralement inutiles lorsque l'extension ou le dossier suffit.

Exemple :

```
components/
├── card.tsx
└── button.tsx
```

Plutôt que :

```
components/
├── component-card.tsx
└── component-button.tsx
```

Cette règle ne concerne pas les préfixes imposés par une technologie ou utiles à la découverte automatique.

### 4.4. Abréviations

Les abréviations reconnues et largement utilisées sont autorisées.

Exemples :

- `api`
- `ui`
- `db`
- `css`
- `svg`
- `auth`

Les abréviations propres à un projet ou difficiles à comprendre sont à éviter.

Le nom doit rester interprétable sans nécessiter une documentation supplémentaire pour chaque fichier.

---

## 5. Principes de nommage des dossiers

### 5.1. Convention générale

Les dossiers utilisent par défaut le `kebab-case` en minuscules.

Exemples :

```
components/
services/
design-system/
user-settings/
product-images/
```

Les noms courts sont privilégiés.

### 5.2. Noms génériques

Les noms suivants sont autorisés lorsque leur périmètre est suffisamment clair :

```
docs/
src/
assets/
components/
hooks/
services/
styles/
types/
tests/
config/
```

Leur utilisation doit être cohérente dans le projet.

Un dossier générique ne doit pas devenir un espace de stockage pour des éléments sans relation.

### 5.3. Organisation par domaine

Lorsque le projet possède plusieurs domaines fonctionnels, l'organisation par domaine peut être préférable à une multiplication des dossiers techniques globaux.

Exemple :

```
features/
├── auth/
│   ├── components/
│   ├── services/
│   └── types/
└── products/
    ├── components/
    ├── services/
    └── types/
```

Cette organisation permet de regrouper les éléments qui appartiennent à une même fonctionnalité.

Elle ne doit toutefois pas être imposée à tous les projets.

### 5.4. Profondeur de l'arborescence

L'arborescence doit rester aussi simple que possible.

Un niveau de dossier supplémentaire est justifié lorsqu'il :

- Regroupe plusieurs éléments cohérents.
- Définit un domaine identifiable.
- Sépare des responsabilités distinctes.
- Correspond à une exigence technique.
- Améliore réellement la navigation.

Éviter de créer des dossiers contenant uniquement un fichier, lorsque cette séparation n'apporte aucun bénéfice.

> **Note d'auteur (non normative, à arbitrer), reprise telle qu'écrite :** si on commence un projets par quelque choses de petit il faut pas non plus qu'il prévoit trop simple alors je pense qu'il faut toujours prévoir un projets moyen qui va facilement s'upgrade vers en gros, imagine que de base tu mes card.tsx dans un dossier général a la création du site car c'est une nouvelle création, bas on va devoir le déplacer plus tard

### 5.5. Singularité et pluralité

La pluralité peut être utilisée pour désigner une collection de ressources.

Exemples :

```
components/
services/
hooks/
templates/
```

La singularité convient naturellement aux dossiers représentant un domaine ou une fonctionnalité.

Exemples :

```
auth/
payment/
profile/
```

Il ne s'agit pas d'une obligation grammaticale absolue. La cohérence de l'arborescence prime.

---

## 6. Conventions selon les formats et technologies

Cette section fixe des recommandations générales. Les conventions spécialisées restent responsables des détails propres à leurs technologies.

### 6.1. Documents Markdown

Les documents structurants utilisent de préférence le `UPPER_SNAKE_CASE`.

Exemples :

```
VISION.md
ARCHITECTURE.md
ROADMAP.md
DECISIONS.md
NAMING.md
```

Les documents secondaires, notes et guides peuvent utiliser le `kebab-case`.

Exemples :

```
installation.md
deployment-guide.md
2026-11-02-review.md
```

Les conventions propres aux projets peuvent préciser la nomenclature documentaire.

### 6.2. Templates

Les templates doivent être nommés selon le document ou l'élément qu'ils permettent de générer.

Exemples :

```
templates/
├── project/
│   ├── README.md
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
└── documents/
    ├── meeting.md
    └── review.md
```

Éviter les noms tels que `template-1.md`, `new-template.md` ou `template-final.md`.

### 6.3. Skills, règles et agents

Les noms doivent identifier leur fonction.

Exemples :

```
skills/
├── project-review/
│   └── SKILL.md
└── documentation/
    └── SKILL.md
```

Les noms de fichiers imposés par une plateforme ou un système d'agents doivent être conservés.

La convention spécialisée détermine les formats exacts attendus par chaque environnement.

### 6.4. Code source

Les fichiers de code utilisent par défaut le `kebab-case`, sauf convention propre au langage ou au framework.

Exemples :

```
card.tsx
payment.ts
user-service.ts
product.ts
use-cart.ts
```

Les fichiers doivent représenter un concept ou une responsabilité.

Leur nommage ne doit pas être confondu avec celui des fonctions, classes ou identifiants contenus dans le fichier.

### 6.5. Composants React

Pour les projets React adoptant cette convention, les fichiers de composants utilisent par défaut le `kebab-case`.

Exemples :

```
card.tsx
button.tsx
modal.tsx
navigation.tsx
```

Le nom du composant déclaré respecte les conventions React, notamment le `PascalCase`.

Exemple :

```
export function Card() {
  return <article>...</article>;
}
```

Le nom du fichier et le nom du composant répondent à deux responsabilités différentes.

Cette organisation permet notamment d'avoir :

```
components/
├── card.tsx
├── button.tsx
└── modal.tsx
```

Sans imposer des noms redondants tels que `card-component.tsx`.

React exige que les noms des composants commencent par une majuscule, mais ne prescrit pas une casse universelle pour les noms de fichiers. La convention du projet tranche donc ce point.

### 6.6. Hooks

Les hooks peuvent utiliser le préfixe `use-` dans le nom du fichier.

Exemples :

```
hooks/
├── use-auth.ts
├── use-cart.ts
└── use-theme.ts
```

Cette convention facilite leur identification.

Les règles de déclaration et de nommage des fonctions restent celles de la convention React/JavaScript spécialisée.

### 6.7. Services et modules

Les services utilisent un nom correspondant au domaine ou à leur responsabilité.

Exemple :

```
services/
├── payment.ts
├── authentication.ts
└── notification.ts
```

Il n'est pas nécessaire d'ajouter systématiquement le suffixe `service`.

Un suffixe reste acceptable lorsque plusieurs types de fichiers portant le même nom coexistent dans un même périmètre ou lorsqu'un outil l'impose.

### 6.8. Fichiers de types

Les fichiers de types utilisent généralement le nom du domaine concerné.

Exemple :

```
types/
├── product.ts
├── user.ts
└── payment.ts
```

Un fichier `types.ts` est autorisé lorsque son emplacement définit clairement son périmètre.

Éviter les fichiers globaux qui regroupent des types sans relation.

### 6.9. Tests

Les fichiers de tests utilisent les conventions du framework de test choisi.

Exemples possibles :

```
card.test.tsx
card.spec.tsx
```

Le projet doit privilégier une convention cohérente.

Le suffixe `test` ou `spec` est pertinent puisqu'il permet la découverte automatique et différencie le code source des tests.

### 6.10. Styles

Les fichiers de styles utilisent le nom de l'élément concerné.

Exemples :

```
card.css
card.module.css
global.css
tokens.css
```

Il n'est pas nécessaire de créer un fichier de styles distinct pour chaque composant lorsque le projet utilise une autre méthode cohérente de gestion du style.

### 6.11. Fichiers de configuration

Les configurations utilisent de préférence les noms attendus par les outils.

Exemples :

```
package.json
tsconfig.json
eslint.config.js
vite.config.ts
.editorconfig
.gitignore
.env.example
```

Les noms imposés sont conservés sans tentative de normalisation.

### 6.12. Python, Java et autres langages

Les conventions générales ne remplacent pas les conventions idiomatiques des langages.

Exemples :

**Python :**

```
user_profile.py
payment.py
```

**Java :**

```
UserProfile.java
PaymentService.java
```

**JavaScript / TypeScript :**

```
user-profile.ts
payment.ts
```

Chaque convention spécialisée précise les adaptations nécessaires.

### 6.13. Données et registres

Les fichiers de données utilisent un nom décrivant leur contenu ou leur responsabilité.

Exemples :

```
settings.json
products.json
events.jsonl
workflow.yaml
metadata.toml
```

Les extensions doivent correspondre réellement au format du contenu.

Les conventions de nommage des fichiers et celles des clés internes peuvent être différentes.

Par exemple, un fichier `user-profile.json` peut contenir des clés en `camelCase` si le schéma du projet le prévoit.

La structure interne relève du format de données ou de la convention spécialisée.

### 6.14. Bases de données

Les noms des bases, tables, colonnes et migrations relèvent des conventions techniques propres au système utilisé.

Les scripts de migration doivent conserver le format attendu par l'outil.

Exemple :

```
migrations/
├── 202611020900_create_users.sql
└── 202611021000_add_user_status.sql
```

Les préfixes temporels ou numériques sont pertinents lorsqu'ils garantissent un ordre d'exécution ou une identification unique.

### 6.15. Ressources multimédias

Les ressources utilisent des noms simples correspondant à leur contenu ou à leur fonction.

Exemples :

```
assets/
├── logo.svg
├── icon-search.svg
├── avatar-placeholder.webp
└── hero.webp
```

Une précision supplémentaire est autorisée lorsqu'elle identifie une véritable variante :

```
logo-light.svg
logo-dark.svg
hero-desktop.webp
hero-mobile.webp
```

Il n'est pas nécessaire d'intégrer systématiquement la taille, la résolution, la couleur ou d'autres caractéristiques dans le nom.

Ces informations peuvent être gérées par les métadonnées, le format ou la structure du dossier.

### 6.16. Fichiers audio et vidéo 

Utiliser un nom identifiant le contenu.

> **Note d'auteur (non normative, à arbitrer), reprise telle qu'écrite :** Ici on pourrais faire un super truc, je vais souvent avoir un fichier pas nomé correctement, pour les fichier img, vidéo, audio avec des nom qui ne définise rien exemple "4df6s51f.png" quand le model voit ca dans un dossier il doit demander le contexte du contenu pour trouver un bon nom en suivant ce qui est dit en dessous

Exemples :

```
intro.mp4
ambient.wav
presentation.mp3
```

Pour les ressources versionnées ou chronologiques, une date ou un numéro de séquence peut être ajouté.

Exemple :

```
2026-11-02-interview.mp4
```

---

## 7. Gestion des noms courts et des collisions

### 7.1. Principe de résolution

Lorsqu'un nom générique devient ambigu, privilégier cet ordre :

1. Utiliser le contexte du dossier.
2. Séparer les domaines si cela correspond à l'organisation réelle.
3. Ajouter un qualificatif utile au nom.
4. Utiliser une nomenclature spécifique si une contrainte technique l'impose.

Exemple :

```
services/
├── payment.ts
└── user.ts
```

Si plusieurs fichiers de même domaine existent :

```
services/
├── payment.ts
├── payment-gateway.ts
└── payment-validation.ts
```

Le qualificatif doit représenter une différence réelle.

### 7.2. Gestion des noms génériques

Certains noms nécessitent une vigilance particulière.

| Nom       | Utilisation appropriée                         | Risque                                     |
| --------- | ---------------------------------------------- | ------------------------------------------ |
| `index`   | Point d'entrée ou fichier attendu par un outil | Multiplication des fichiers peu explicites |
| `config`  | Configuration d'un domaine identifié           | Configuration globale indéterminée         |
| `utils`   | Fonctions utilitaires cohérentes et limitées   | Accumulation de fonctions disparates       |
| `types`   | Types regroupés dans un périmètre clair        | Fichier global difficile à maintenir       |
| `common`  | Éléments réellement partagés                   | Fourre-tout transversal                    |
| `shared`  | Ressources partagées entre plusieurs domaines  | Absence de responsabilité identifiable     |
| `helpers` | Fonctions auxiliaires cohérentes               | Duplication ou accumulation                |

Ces noms ne sont pas interdits.

Ils doivent être utilisés uniquement lorsque leur périmètre reste identifiable.

### 7.3. Cas des fichiers `index`

Les fichiers `index` sont pertinents lorsqu'une technologie ou une architecture les utilise comme point d'entrée.

Ils ne doivent pas être créés systématiquement pour chaque dossier.

Un fichier `index.ts` peut servir de point d'export public d'un module, mais ne doit pas remplacer des noms de fichiers explicites lorsqu'il n'apporte aucune valeur.

### 7.4. Éviter les doublons de casse

Les fichiers ne doivent pas se distinguer uniquement par la casse.

À éviter :

```
Card.tsx
card.tsx
```

Certains systèmes de fichiers ne distinguent pas correctement ces deux noms.

Cette règle est particulièrement importante pour les projets partagés entre Windows, macOS et Linux.

---

## 8. Centralisation des variantes et séparation des responsabilités

### 8.1. Principe de centralisation

Le système doit privilégier l'organisation par concept plutôt que la création d'un fichier distinct pour chaque variante.

Lorsqu'un même élément possède plusieurs variantes cohérentes, celles-ci devraient être gérées dans le même fichier.

Exemple :

```
components/
└── card.tsx
```

Le composant `Card` peut proposer les variantes suivantes :

- Default.
- Product.
- Horizontal.
- Featured.
- Compact.

Elles peuvent être contrôlées par des propriétés, des paramètres ou une autre méthode adaptée à la technologie.

### 8.2. Exemple React

Une seule responsabilité principale :

```
type CardVariant =
  | "default"
  | "product"
  | "horizontal"
  | "featured"
  | "compact";

type CardProps = {
  variant?: CardVariant;
};

export function Card({
  variant = "default",
}: CardProps) {
  return (
    <article data-variant={variant}>
      ...
    </article>
  );
}
```

Il n'est pas nécessaire de créer :

```
main-card.tsx
product-card.tsx
horizontal-card.tsx
featured-card.tsx
compact-card.tsx
```

lorsque ces composants représentent en réalité des variantes du même élément.

### 8.3. Quand séparer un fichier ?

La création d'un fichier distinct est pertinente lorsque :

- La responsabilité devient indépendante.
- Le composant devient suffisamment complexe.
- Il possède une logique métier spécifique.
- Il doit être réutilisé indépendamment.
- Sa séparation améliore réellement la lisibilité.
- Il nécessite un cycle de vie ou des dépendances distinctes.
- Une contrainte technique ou architecturale le justifie.

Exemple :

```
components/
├── card.tsx
└── product/
    └── product-card.tsx
```

Cette séparation est pertinente si `ProductCard` devient un composant métier autonome plutôt qu'une simple variante visuelle de `Card`.

### 8.4. Éviter les deux extrêmes

Deux mauvaises pratiques doivent être évitées.

**Sur-segmentation :**

Créer un fichier pour chaque petite variante, chaque état visuel ou chaque fragment de logique.

**Centralisation excessive :**

Regrouper des composants sans relation dans un fichier unique sous prétexte de limiter le nombre de fichiers.

La règle est la cohésion fonctionnelle.

Un fichier doit regrouper ce qui appartient naturellement au même concept, sans devenir un espace de stockage arbitraire.

### 8.5. La simplicité avant le nombre de fichiers

La convention ne fixe aucun nombre maximal de responsabilités par fichier.

Elle encourage une architecture dans laquelle chaque séparation possède une justification identifiable.

Le nombre de fichiers n'est pas un indicateur direct de qualité architecturale.

---

## 9. Fichiers sources, générés et temporaires

### 9.1. Fichiers sources

Les fichiers sources représentent les éléments maintenus directement par les développeurs ou les contributeurs.

Ils doivent respecter les conventions de nommage applicables au projet.

### 9.2. Fichiers générés

Les fichiers générés doivent être placés dans les emplacements prévus par les outils ou par l'architecture.

Exemples :

```
dist/
build/
.next/
coverage/
```

Il n'est pas nécessaire d'ajouter artificiellement `generated` à tous les noms lorsque leur emplacement permet déjà de les identifier.

Les fichiers générés ne doivent pas être renommés ou modifiés manuellement lorsque l'outil responsable attend un nom précis.

Leur source de vérité reste le fichier ou le mécanisme qui permet de les générer.

### 9.3. Fichiers temporaires

Les fichiers temporaires doivent utiliser les emplacements prévus à cet effet.

Exemples :

```
tmp/
cache/
```

Ils ne doivent pas se multiplier dans les dossiers de code ou de documentation.

Éviter notamment :

```
card-new.tsx
card-old.tsx
card-backup.tsx
card-copy.tsx
```

Les sauvegardes et historiques doivent être gérés par les mécanismes adaptés, notamment Git lorsque celui-ci est utilisé.

---

## 10. Contraintes de portabilité

### 10.1. Caractères recommandés

Pour les noms techniques partagés entre plusieurs systèmes, privilégier :

- Les lettres ASCII minuscules.
- Les chiffres.
- Les tirets.
- Les underscores lorsque la convention les prévoit.
- Les points nécessaires aux extensions.

Éviter les espaces, les caractères accentués, les caractères spéciaux et les symboles non indispensables.

Exemples :

| Recommandé           | À éviter              |
| -------------------- | --------------------- |
| `user-profile.ts`    | `user profile.ts`     |
| `configuration.json` | `configuration!.json` |
| `project-guide.md`   | `guide du projet.md`  |

Cette recommandation favorise la compatibilité entre systèmes de fichiers, outils de développement, URL et scripts.

### 10.2. Caractères et noms réservés

Les noms ne doivent pas utiliser les caractères incompatibles avec les systèmes ciblés.

En particulier, éviter les caractères suivants dans les noms de fichiers et dossiers :

```
< > : " / \ | ? *
```

Éviter également les espaces ou points en fin de nom.

Certains noms sont réservés par Windows, notamment :

```
CON
PRN
AUX
NUL
COM1
LPT1
```

Il faut aussi tenir compte des autres variantes réservées par la plateforme.

### 10.3. Portabilité entre systèmes

Éviter les noms qui diffèrent uniquement par les majuscules et minuscules.

Éviter également les conventions qui dépendent d'un comportement spécifique à un système de fichiers sans nécessité.

La convention doit favoriser le fonctionnement sur les environnements Windows, macOS et Linux lorsqu'un projet est destiné à être partagé entre ces plateformes.

---

## 11. Gestion des exceptions

### 11.1. Principe

Une exception est autorisée lorsqu'une règle générale ou spécialisée entre en conflit avec une contrainte réelle du projet.

Les exceptions doivent rester limitées à leur périmètre.

Elles ne modifient pas implicitement la convention générale.

### 11.2. Motifs acceptables

Une exception peut être justifiée par :

- Un framework.
- Une bibliothèque.
- Un outil de génération.
- Une API externe.
- Une contrainte de compatibilité.
- Une nomenclature métier.
- Une convention déjà établie et cohérente dans le projet.
- Une architecture particulière.

### 11.3. Documentation des exceptions

Une exception durable ou susceptible d'être modifiée par un agent IA doit être documentée dans la convention spécialisée ou dans la documentation propre au projet.

Elle doit préciser :

1. La règle concernée.
2. Le périmètre de l'exception.
3. Sa justification.
4. Le comportement attendu.

Les exceptions évidentes et imposées par un framework n'ont pas besoin d'être documentées individuellement si leur fonctionnement est déjà clairement établi.

### 11.4. Éviter les exceptions inutiles

Il ne faut pas créer une règle spécifique pour chaque fichier ou chaque cas particulier.

Lorsqu'une exception devient fréquente, il faut réexaminer la convention spécialisée concernée.

Une adaptation cohérente peut devenir une règle de domaine plutôt qu'une succession d'exceptions locales.

---

## 12. Articulation avec les conventions spécialisées

### 12.1. Héritage

Les niveaux (universel, domaine, projet) et les règles d'héritage sont définis dans [METADATA.md](METADATA.md) §7. Dans ce document, « convention générale » désigne le niveau universel.

La convention générale constitue le socle commun.

Les conventions spécialisées héritent de ses principes et les précisent selon les besoins du domaine.

Exemple :

```
Convention générale
       │
       ├── Convention Web
       │      ├── React
       │      └── Next.js
       │
       ├── Convention Mobile
       │
       ├── Convention Logiciel
       │      ├── Python
       │      └── Java
       │
       └── Convention Création
              ├── Design
              └── Audiovisuel
```

Cette représentation illustre une organisation logique. Les conventions peuvent être regroupées ou subdivisées selon les besoins réels.

### 12.2. Responsabilité de chaque niveau

**Convention générale :**

Définit les principes universels :

- Simplicité.
- Clarté.
- Cohérence.
- Non-redondance.
- Centralisation.
- Gestion des exceptions.
- Portabilité.

**Convention spécialisée :**

Définit les adaptations du domaine :

- Casse des fichiers.
- Préfixes et suffixes.
- Nommage des modules.
- Conventions de tests.
- Noms imposés par les frameworks.
- Structures techniques.

**Convention du projet :**

Définit uniquement les adaptations locales nécessaires.

### 12.3. Ordre de priorité

En cas de conflit, appliquer l'ordre suivant :

1. Contraintes obligatoires de la plateforme, du langage ou de l'outil.
2. Exceptions explicitement définies pour le projet.
3. Convention spécialisée applicable.
4. Convention générale.

Une exception de projet ne s'applique que dans son périmètre.

Elle ne modifie pas les règles des autres projets ni celles du socle commun.

### 12.4. Limitation de la duplication

Les conventions spécialisées ne doivent pas recopier intégralement la convention générale.

Elles doivent la référencer et préciser uniquement les règles supplémentaires ou les adaptations nécessaires.

La documentation doit ainsi rester modulaire et maintenable.

---

## 13. Exemples d'organisation

### 13.1. Architecture Web avec React et Next.js

Exemple d'organisation cohérente :

```
project/
├── README.md
├── package.json
├── tsconfig.json
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── products/
│   │       ├── page.tsx
│   │       └── [slug]/
│   │           └── page.tsx
│   ├── components/
│   │   ├── card.tsx
│   │   ├── button.tsx
│   │   └── modal.tsx
│   ├── hooks/
│   │   └── use-cart.ts
│   ├── services/
│   │   ├── payment.ts
│   │   └── product.ts
│   ├── styles/
│   │   ├── global.css
│   │   └── tokens.css
│   ├── types/
│   │   ├── product.ts
│   │   └── user.ts
│   └── assets/
│       ├── logo.svg
│       └── hero.webp
└── docs/
    ├── VISION.md
    ├── ARCHITECTURE.md
    ├── ROADMAP.md
    └── DECISIONS.md
```

Cette architecture est illustrative.

Les noms `page.tsx` et `layout.tsx` sont conservés parce qu'ils correspondent aux conventions de Next.js. Les autres fichiers suivent la convention générale proposée.

### 13.2. Organisation d'un composant

Organisation simple :

```
components/
└── card.tsx
```

Organisation plus complexe mais justifiée :

```
components/
└── card/
    ├── card.tsx
    ├── card-media.tsx
    └── card-header.tsx
```

La deuxième organisation devient pertinente lorsque les éléments possèdent suffisamment de logique et de responsabilités pour justifier leur séparation.

Elle ne doit pas être créée simplement pour séparer chaque fragment visuel.

---

## 14. Règles applicables aux agents IA

Les agents IA doivent appliquer les règles suivantes lorsqu'ils créent, modifient ou organisent des fichiers et dossiers.

### 14.1. Avant de créer un fichier

L'agent DOIT :

1. Examiner l'emplacement et son contexte.
2. Identifier la responsabilité du fichier envisagé.
3. Consulter les conventions applicables.
4. Vérifier si un fichier correspondant existe déjà.
5. Vérifier si la responsabilité peut être intégrée à un fichier existant.
6. Respecter les conventions imposées par les outils et frameworks.

L'agent NE DOIT PAS créer un nouveau fichier simplement parce qu'une variante ou une fonctionnalité supplémentaire apparaît.

### 14.2. Lors du choix du nom

L'agent DEVRAIT :

- Privilégier un nom court.
- Utiliser le contexte du chemin.
- Éviter les répétitions.
- Utiliser un seul mot lorsque cela suffit.
- Ajouter un qualificatif uniquement lorsqu'il apporte une distinction utile.
- Respecter la casse applicable au domaine.
- Éviter les abréviations obscures.
- Préserver les noms techniques imposés.

### 14.3. Lors d'une modification de l'arborescence

L'agent NE DOIT PAS :

- Renommer massivement les fichiers sans justification.
- Modifier arbitrairement les noms imposés par un framework.
- Créer des dossiers supplémentaires sans raison.
- Introduire plusieurs conventions concurrentes.
- Remplacer un nom existant cohérent uniquement pour satisfaire une préférence stylistique.

Un renommage doit être justifié par une amélioration réelle de la clarté, de la cohérence ou de la maintenabilité.

### 14.4. Lorsqu'une ambiguïté existe

Si plusieurs noms sont possibles, l'agent doit privilégier celui qui :

1. Correspond le mieux à la responsabilité.
2. Utilise le moins de mots nécessaire.
3. S'intègre à la nomenclature existante.
4. Respecte les conventions applicables.

Si le choix implique une décision architecturale importante, l'agent doit signaler les options plutôt que créer une nouvelle règle implicitement.

### 14.5. Préserver la cohérence existante

Lorsqu'un projet possède déjà une convention cohérente, l'agent doit la prendre en compte.

La convention générale ne justifie pas une normalisation systématique de tous les fichiers existants.

Les modifications doivent rester proportionnées au travail demandé.

---

## 15. Vérification de conformité

### 15.1. Contrôle d'un nom

Un nom doit être vérifié selon les critères suivants :

- Est-il compréhensible ?
- Représente-t-il correctement le concept ou la responsabilité ?
- Est-il suffisamment court ?
- Le contexte du dossier rend-il le nom explicite ?
- Contient-il des informations redondantes ?
- Respecte-t-il la casse applicable ?
- Est-il compatible avec les contraintes techniques ?
- Est-il cohérent avec les fichiers voisins ?

### 15.2. Contrôle de l'arborescence

L'arborescence doit être vérifiée selon les critères suivants :

- Les dossiers représentent-ils des catégories ou domaines identifiables ?
- Les fichiers sont-ils placés dans le bon périmètre ?
- Existe-t-il des dossiers inutiles ?
- Existe-t-il une profondeur excessive ?
- Des responsabilités distinctes sont-elles regroupées sans raison ?
- Des variantes équivalentes ont-elles été multipliées en fichiers ?
- Des fichiers génériques servent-ils de fourre-tout ?
- Les noms sont-ils cohérents entre les différents niveaux ?

### 15.3. Contrôle technique

Vérifier également :

- Les noms réservés par les plateformes.
- Les extensions et formats.
- Les fichiers attendus par les frameworks.
- Les conventions de tests et de génération.
- Les collisions de casse.
- Les chemins et imports après renommage.
- La cohérence entre les noms déclarés et les noms attendus par les outils.

### 15.4. Checklist de validation

Avant de considérer une nouvelle organisation comme conforme :

- Les noms correspondent aux responsabilités réelles.
- Les noms courts sont privilégiés lorsque le contexte suffit.
- Les noms composés apportent une distinction utile.
- Les informations déjà présentes dans le chemin ne sont pas répétées.
- Les variantes cohérentes sont centralisées.
- Les séparations de fichiers sont justifiées.
- Les conventions techniques sont respectées.
- Les fichiers générés et temporaires sont correctement organisés.
- Les exceptions nécessaires sont explicites.
- L'organisation reste compréhensible pour un nouvel agent IA.

### 15.5. Niveau de conformité

La conformité doit être évaluée selon deux dimensions :

**Conformité nominale :** respect des règles de syntaxe, de casse, de portabilité et des conventions applicables.

**Conformité organisationnelle :** pertinence des noms, cohérence de l'arborescence et adéquation entre les fichiers et leurs responsabilités.

Un nom peut être techniquement conforme tout en étant mal choisi sur le plan organisationnel.

La vérification doit donc prendre en compte les deux dimensions.

---

## 16. Références techniques

Les ressources suivantes servent de références pour les adaptations propres aux technologies. Elles ne remplacent pas les conventions générales de ce document.

- [MDN — Dealing with files](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Dealing_with_files) : recommandations de nommage des fichiers et dossiers Web.
- [PEP 8 — Python Style Guide](https://peps.python.org/pep-0008/) : conventions Python pour les modules, packages et classes.
- [Effective Go](https://go.dev/doc/effective_go) : principes de nommage Go.
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) : conventions Java, notamment l'association entre fichiers et classes.
- [React — Your First Component](https://react.dev/learn/your-first-component) : conventions relatives aux noms de composants React.
- [Next.js — Project Structure](https://nextjs.org/docs/app/getting-started/project-structure) : organisation des fichiers et dossiers Next.js.
- [Next.js — Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages) : conventions de fichiers pour les routes et layouts.
- [Microsoft — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file) : contraintes de nommage Windows.
- [Git — core.ignoreCase](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreignoreCase) : gestion des systèmes de fichiers sensibles ou non à la casse.

---

## 17. Principe directeur

La convention de nommage doit faciliter l'organisation et la compréhension des projets, et non leur imposer une architecture artificielle.

Le nom doit être aussi court que possible, mais aussi explicite que nécessaire.

Le contexte doit compléter le nom, les variantes doivent rester regroupées lorsqu'elles appartiennent au même concept et les séparations doivent répondre à de véritables responsabilités.

Les conventions spécialisées et les contraintes techniques peuvent préciser ou adapter ces principes sans remettre en cause le socle commun.

**La meilleure convention est celle qui permet de retrouver, comprendre et maintenir un élément sans avoir besoin de multiplier les mots, les fichiers ou les règles.**