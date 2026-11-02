# Cadrage du projet

> Document de référence définissant le contexte, les objectifs, le périmètre, les besoins et les orientations structurantes du projet.

**Version :** 0.1  
**Date de rédaction :** 2 novembre 2026  
**Statut :** Cadrage en cours de consolidation

---

## 1. Objet du document

Ce document définit le cadrage du projet : pourquoi il existe, quels problèmes il doit résoudre, quelles sont ses ambitions et quels principes doivent guider sa conception.

Il constitue un point de référence commun pour les évolutions du projet, son organisation, sa documentation et les futurs développements.

Il ne remplace pas les documents spécialisés :

- La vision présente la finalité et la direction à long terme.
- Le cadrage définit le contexte, les besoins, les objectifs et le périmètre.
- L'architecture définit l'organisation et les principes techniques du système.
- Les conventions définissent les règles communes et spécialisées.
- Les spécifications décrivent les fonctionnalités et leurs comportements.

Le cadrage doit évoluer avec la compréhension du projet, tout en conservant la trace des orientations précédentes et des décisions qui ont conduit à son état actuel.

Les éléments présentés dans ce document ne possèdent pas tous le même niveau de validation. Les décisions explicitement retenues sont distinguées des orientations, des propositions et des questions encore ouvertes.

---

# 2. Évolution du cadrage

Le projet a progressivement changé de nature au fil des réflexions. Cette évolution est importante : la conception actuelle ne doit pas être comprise comme une simple amélioration d'un gestionnaire de notes, mais comme l'élargissement progressif d'une ambition initiale.

## 2.1. Point de départ : un Second Brain

Le projet a initialement été envisagé comme un système de Second Brain.

L'objectif était de construire une mémoire durable capable de conserver les informations issues de différentes conversations, outils et projets.

Les premiers besoins étaient notamment :

- Ne plus perdre les informations importantes entre plusieurs conversations.
- Conserver les idées, décisions, réflexions et préférences.
- Retrouver le contexte d'un travail précédent.
- Éviter de devoir réexpliquer systématiquement les mêmes choses aux assistants IA.
- Organiser les connaissances dans des documents structurés.
- Permettre à plusieurs assistants et agents de partager une même base de connaissances.

Cette première approche mettait principalement l'accent sur la mémoire et la conservation de l'information.

Elle a permis de faire émerger un premier ensemble de mécanismes : capture, consolidation, recherche, relations et standardisation documentaire.

## 2.2. Première évolution : l'idée d'un « GitHub des idées »

Une réflexion a ensuite remis en question la pertinence du concept de Second Brain.

L'expression « GitHub des idées » semblait mieux représenter une partie de l'ambition : ne pas seulement stocker des informations, mais conserver l'historique de leur évolution.

L'analogie avec Git a notamment fait émerger les notions suivantes :

- Historique des idées.
- Évolution d'une réflexion.
- Alternatives et pistes concurrentes.
- Fusion de plusieurs idées.
- Contradictions.
- Conservation des anciennes versions.
- Compréhension du cheminement qui a conduit à une décision.

Cette réflexion a fait apparaître une différence fondamentale entre un système de notes et un système capable de suivre l'évolution des connaissances.

Une idée ne doit pas être simplement conservée. Elle doit pouvoir évoluer, être reliée à d'autres idées, être reprise, abandonnée ou réutilisée ultérieurement.

Cependant, limiter le système aux idées aurait été trop restrictif. Toutes les informations ne sont pas des idées : il existe également des faits, observations, décisions, exigences, préférences, résultats de tests et connaissances techniques.

Le concept « GitHub des idées » reste donc une métaphore intéressante pour présenter certaines capacités du produit, mais ne décrit pas à lui seul son périmètre complet.

## 2.3. Clarification : un système universel de gestion du cycle de vie de l'information

La réflexion a ensuite abouti à une distinction entre trois dimensions :

1. La gestion des connaissances.
2. La gestion des idées.
3. La gestion des projets.

Le choix retenu pour orienter la vision est celui d'un système universel de gestion et de versionnement des connaissances, avec une priorité opérationnelle donnée aux projets.

Le cycle de vie de l'information devient le cœur du système.

Les projets constituent son principal domaine d'application, tandis que les idées et les connaissances alimentent continuellement leur évolution.

Cette clarification évite de construire un système uniquement centré sur la mémoire personnelle ou sur un catalogue d'idées.

## 2.4. Nouvelle précision : standardiser les projets comme des produits

Une autre évolution importante a consisté à préciser le véritable travail que le système doit faciliter.

Il ne s'agit pas uniquement de gérer les informations d'un projet une fois qu'il existe.

Le système doit avant tout permettre de **standardiser le démarrage, le cadrage et l'organisation des projets**.

Chaque projet doit être considéré comme un produit possédant un contexte, des objectifs, une vision, des contraintes, une organisation documentaire et des règles de fonctionnement.

Un socle commun doit permettre de démarrer rapidement, puis être complété par des conventions spécialisées selon le domaine.

Le projet Web, l'application mobile ou le projet créatif doivent bénéficier d'une même logique générale sans être obligés d'utiliser les mêmes conventions techniques. //note : formulation a revoir, c'est trop restrint comme application car ca touchera tout les type de projet pas seulement cela//

## 2.5. Dernière évolution : un système qui accompagne réellement le travail quotidien

Les échanges ont ensuite permis de faire émerger un objectif opérationnel supplémentaire.

Le système ne doit pas être uniquement un référentiel consulté ponctuellement.

Il doit accompagner en continu :

- Le brainstorming.
- L'évolution de la vision.
- La préparation des améliorations.
- Le suivi des idées.
- La compréhension de l'existant.
- La préparation des modifications.
- La collaboration avec différents assistants et agents IA.

Il doit notamment permettre de transformer des réflexions dispersées en prompts de haute qualité, adaptés au contexte réel du projet et suffisamment précis pour faire réaliser des corrections ou évolutions par des agents de développement.

Cette capacité devient l'une des principales finalités pratiques du système.

---

# 3. Vision actuelle du projet

## 3.1. Formulation de la vision

Construire un système universel de gestion du cycle de vie des informations, capable de collecter, structurer, relier, versionner et faire évoluer les connaissances issues de différentes sources.

Ce système doit permettre de standardiser le démarrage et l'organisation des projets grâce à un socle documentaire et méthodologique commun, complété par des conventions, règles, compétences et agents spécialisés selon les domaines.

Il doit accompagner continuellement l'évolution des projets en conservant un contexte interconnecté des idées, décisions, connaissances et réalisations.

Il doit faciliter le passage de la réflexion à l'action, notamment en produisant des prompts de haute qualité permettant aux agents IA de réaliser des corrections, améliorations et évolutions cohérentes avec le projet.

## 3.2. Positionnement conceptuel

Le système repose sur trois dimensions complémentaires :

| Dimension     | Responsabilité                                                 | Priorité                |
| ------------- | -------------------------------------------------------------- | ----------------------- |
| Connaissances | Collecter, conserver et faire évoluer les informations         | Socle                   |
| Idées         | Explorer, relier et faire évoluer les pistes de réflexion      | Fondamentale            |
| Projets       | Structurer, cadrer, piloter et réaliser des objectifs concrets | Priorité opérationnelle |

Ces dimensions doivent partager un même socle de gestion de l'information.

Le système ne doit pas devenir trois outils indépendants.

---

# 4. Problèmes à résoudre

## 4.1. Perte de contexte entre les conversations

Les échanges avec les assistants IA produisent de nombreuses informations utiles.

Cependant, ces informations sont souvent dispersées entre plusieurs conversations et outils.

Lorsqu'un nouveau travail commence, l'assistant ne possède pas nécessairement les éléments qui permettent de comprendre :

- Pourquoi une fonctionnalité a été conçue ainsi.
- Quelles alternatives ont été envisagées.
- Quelles décisions ont réellement été retenues.
- Quels problèmes ont déjà été rencontrés.
- Quelles conventions s'appliquent.
- Quelles idées sont encore en attente.

Le système doit conserver ce contexte et le rendre accessible indépendamment de l'assistant utilisé.

## 4.2. Difficulté à organiser les idées qui évoluent

Une réflexion peut commencer par une petite amélioration et aboutir à une remise en question plus importante.

Les informations structurantes peuvent apparaître au milieu d'une conversation consacrée à un sujet complètement différent.

Un système de notes classique risque de mélanger ces informations ou de ne retenir que le sujet principal de la conversation.

Le système doit être capable de reconnaître plusieurs unités d'information indépendantes dans une même source.

## 4.3. Absence de continuité entre réflexion et réalisation

Le brainstorming, la documentation, la préparation des prompts et le développement sont souvent séparés.

L'agent chargé du développement doit alors redécouvrir des choix et des contraintes déjà discutés.

Le système doit réduire cette rupture en donnant accès au contexte historique et technique pertinent.

## 4.4. Organisation différente d'un projet à l'autre

Recommencer l'organisation à chaque nouveau projet représente une charge cognitive et méthodologique inutile.

Les documents, dossiers, conventions et méthodes peuvent devenir différents sans raison suffisante.

Le système doit proposer un cadre réutilisable permettant de retrouver les mêmes repères d'un projet à l'autre.

## 4.5. Coût de compréhension du code existant

Un agent IA peut être amené à lire de nombreux fichiers pour comprendre une fonctionnalité ou retrouver l'origine d'une décision.

Cette découverte répétée consomme des tokens et augmente le risque de mauvaise interprétation.

Le système doit fournir une carte structurée du projet, permettant de retrouver les informations historiques et les fichiers concernés avant d'engager une lecture ciblée du code.

## 4.6. Régressions provoquées par une connaissance incomplète

Un assistant IA ne connaît pas nécessairement les modifications réalisées entre deux conversations.

Il peut donc proposer de revenir à une ancienne organisation, supprimer une fonctionnalité récente ou écraser des modifications dont il ignore l'existence.

Le système doit explicitement protéger l'état réel du projet et considérer l'historique conversationnel comme une connaissance partielle, jamais comme une représentation complète de l'existant.

---

# 5. Besoins fondamentaux

## 5.1. Une organisation stable et prévisible

Un besoin personnel important a été exprimé pendant le cadrage : disposer de repères constants pour organiser le travail.

L'utilisateur indique avoir un TDAH et explique avoir besoin de ranger les informations dans des catégories stables, de retrouver les mêmes emplacements et de conserver une vision globale pour avancer sereinement dans un projet.

Cette exigence doit être considérée comme une contrainte de conception à part entière.

Le système doit réduire la charge organisationnelle et éviter de demander continuellement de nouvelles décisions sur la manière de ranger ou de structurer les informations.

Les principes recherchés sont :

- Des catégories stables.
- Une organisation reconnaissable.
- Des documents aux responsabilités prévisibles.
- Une vision globale du projet.
- Une progression visible.
- Une capacité à reprendre facilement un travail interrompu.
- Une organisation suffisamment souple pour ne pas devenir bloquante.

Le système ne doit pas transformer ce besoin en une complexité administrative supplémentaire.

## 5.2. Démarrer rapidement un projet

Il doit être possible de lancer un projet sans devoir concevoir intégralement son organisation.

Le socle commun doit fournir les documents et conventions nécessaires pour commencer à cadrer et travailler.

Les éléments spécifiques au domaine peuvent ensuite être activés selon le type de projet.

## 5.3. Brainstormer continuellement

Le système doit permettre d'explorer librement des idées, même lorsque le projet possède déjà une organisation et une roadmap.

Il doit conserver les réflexions, leur contexte et leurs relations afin de pouvoir les reprendre plus tard.

Le brainstorming ne doit pas être limité aux phases initiales d'un projet.

## 5.4. Préparer des interventions de qualité

Le système doit aider à préparer des modifications et évolutions de projet avec un niveau de contexte suffisant pour les confier à des agents IA.

Il doit pouvoir identifier les informations, conventions, décisions et réalisations qui influencent une modification.

Le résultat attendu est un ensemble d'instructions suffisamment précis pour limiter les ambiguïtés, les régressions et les interventions inutiles.

## 5.5. Utiliser plusieurs assistants et agents

Le système doit rester indépendant d'un fournisseur ou d'un assistant unique.

Différents outils doivent pouvoir consulter les mêmes connaissances, respecter les mêmes règles et contribuer au même cycle de vie de l'information.

---

# 6. Le cycle de vie de l'information : cœur du système

## 6.1. Principe central

Le système doit considérer l'information comme un élément pouvant être capturé, qualifié, relié, enrichi, consolidé et exploité au fil du temps.

Une information n'est pas obligée de devenir une décision, une tâche ou une fonctionnalité.

Elle doit pouvoir rester une piste d'exploration tant que son évolution n'est pas déterminée.

L'historique des informations doit être conservé afin de comprendre les changements de réflexion et les décisions successives.

## 6.2. Sources d'information

Le système doit pouvoir collecter des informations provenant de différentes sources :

- Conversations avec des assistants IA.
- Messages de l'utilisateur.
- Réponses des assistants.
- Documents.
- Fichiers du projet.
- Code source.
- Recherches.
- Réunions.
- Retours d'expérience.
- Résultats de tests.
- Modifications et événements du projet.

La nature de la source, son auteur, sa date et son contexte doivent être préservés lorsque ces informations sont disponibles.

## 6.3. Distinguer source et informations extraites

Une source peut contenir plusieurs informations indépendantes.

Le système doit donc distinguer :

**La source originale :**

- Message ou document d'origine.
- Auteur.
- Conversation ou emplacement.
- Date.
- Contexte.
- Référence permettant de retrouver la source.

**Les informations extraites :**

- Une ou plusieurs unités de connaissance.
- Leur nature.
- Leur intention.
- Leur contexte.
- Leur niveau de confiance.
- Leurs relations.
- Leur éventuel rattachement à des projets ou conventions.

Une même source peut ainsi produire plusieurs captures sans perdre leur origine commune.

## 6.4. Granularité des captures

La granularité doit être adaptée au sens de l'information.

Un message peut contenir simultanément :

- Une proposition qui modifie la vision générale du système.
- Une réflexion sur une convention.
- Une nouvelle idée de fonctionnalité.
- Une demande de correction visuelle très ponctuelle.

Ces éléments ne doivent pas être fusionnés dans une capture unique.

Le système doit séparer les informations qui possèdent une responsabilité, une évolution ou une destination indépendante, tout en conservant les liens avec leur source commune.

Il ne faut toutefois pas appliquer une règle artificielle consistant à créer une capture pour chaque phrase.

La règle recherchée est :

**Une capture représente une unité d'information cohérente, avec suffisamment de contexte pour être comprise indépendamment, tout en restant reliée aux autres informations pertinentes.**

## 6.5. Nature et statut des informations

Le système doit pouvoir distinguer plusieurs natures d'informations, notamment :

- Fait.
- Observation.
- Idée.
- Proposition.
- Préférence.
- Orientation.
- Question ouverte.
- Décision.
- Exigence.
- Convention.
- Tâche.
- Risque.
- Retour d'expérience.

Il doit également distinguer la nature d'une information de son niveau de validation.

Une proposition de l'assistant n'est pas une décision de l'utilisateur.

Une idée favorablement accueillie n'est pas automatiquement une règle officielle.

Une convention peut être suffisamment établie pour être documentée sans pour autant être issue d'une validation formelle à chaque étape.

La classification doit préserver les nuances et éviter les approbations implicites.

## 6.6. Relations entre les informations

La valeur du registre dépendra fortement de sa capacité à relier les informations.

Les relations pourront notamment représenter :

- Une précision.
- Une réponse.
- Une dépendance.
- Une évolution.
- Une contradiction.
- Une alternative.
- Une fusion.
- Une dérivation.
- Une parenté.
- Une appartenance à un même sujet.

Les relations doivent permettre de reconstituer le contexte d'un sujet sans avoir à relire toutes les conversations.

Une information peut être reliée à plusieurs projets ou conventions, ou rester indépendante de tout projet.

## 6.7. Espaces logiques

La séparation suivante constitue une orientation déjà présente dans la conception du système :

- **Atelier :** exploration, idées, propositions et questions ouvertes.
- **Référentiel :** connaissances établies, conventions et décisions suffisamment consolidées.
- **Journal :** historique, événements, changements et retours d'exécution.
- **Pilotage :** tâches, jalons, priorités et progression.

Ces espaces ne doivent pas être confondus avec des niveaux de validation.

Une information exploratoire ne devient pas automatiquement officielle parce qu'elle a été déplacée dans un espace.

---

# 7. Les mécanismes principaux

## 7.1. Capture

Capture assure la collecte des informations.

Responsabilités :

- Identifier les informations utiles dans les sources.
- Préserver les auteurs et la provenance.
- Extraire les unités d'information cohérentes.
- Conserver les nuances et le contexte.
- Identifier les premières relations possibles.
- Séparer les propositions, décisions, questions et demandes.
- Conserver les informations non validées sans les présenter comme des faits établis.

Capture ne doit pas :

- Transformer automatiquement une proposition en décision.
- Consolider prématurément toutes les informations.
- Supprimer les anciennes captures.
- Réécrire les sources originales.
- Déclarer une convention officielle sans justification.

## 7.2. Review

Review assure la consolidation des connaissances.

Responsabilités :

- Détecter les doublons.
- Relier les informations.
- Identifier les sujets maîtres.
- Faire émerger les convergences.
- Repérer les contradictions.
- Suivre les évolutions de réflexion.
- Consolider les informations suffisamment établies.
- Mettre à jour ou proposer des mises à jour documentaires.
- Préparer les éléments de pilotage pertinents.

Review doit préserver les traces historiques.

Une nouvelle compréhension ne doit pas effacer le cheminement ayant conduit à l'ancienne.

## 7.3. Search

Search permet de retrouver les informations pertinentes.

La recherche doit pouvoir s'appuyer sur :

- Le contenu.
- La nature de l'information.
- Le projet.
- Les sujets maîtres.
- Les relations.
- Les documents.
- Les fichiers.
- Les références techniques.
- Les historiques de décisions.
- Les sources originales.

L'objectif est de fournir un contexte précis et limité, plutôt que de transmettre systématiquement l'intégralité du registre.

## 7.4. Sync

Sync assure les échanges explicites avec les outils externes utilisés pour le pilotage ou la consultation.

Il doit distinguer les données de référence des vues de travail.

Aucune synchronisation destructive ou modification d'une source de vérité ne doit être effectuée sans autorisation adaptée.

La synchronisation avec des outils comme ClickUp peut être envisagée pour le pilotage, mais ne doit pas créer une seconde source de vérité concurrente.

---

# 8. Standardisation des projets

## 8.1. Considérer chaque projet comme un produit

Le système doit accompagner la conception et le cycle de vie des projets en considérant chacun d'eux comme un produit possédant :

- Une raison d'être.
- Une vision.
- Des objectifs.
- Un périmètre.
- Des utilisateurs ou bénéficiaires.
- Des exigences.
- Des contraintes.
- Une architecture.
- Des conventions.
- Des fonctionnalités.
- Un plan d'évolution.
- Un suivi de réalisation.

Cette approche doit permettre de commencer un projet avec une structure lisible, puis de l'enrichir progressivement.

## 8.2. Socle documentaire universel

Le projet doit disposer d'un ensemble de documents standardisés, communs à tous les projets qui utilisent le système.

Ces documents doivent avoir des responsabilités stables et complémentaires.

Le socle documentaire déjà défini dans le système constitue une base à préserver.

Il ne doit pas être supprimé, réduit ou remplacé par des documents spécifiques à un domaine.

Les projets peuvent recevoir des documents supplémentaires, mais ceux-ci doivent compléter le socle et non le déstructurer.

Le référentiel documentaire existant demeure la référence pour connaître la liste exacte des documents standardisés.

## 8.3. Conventions spécialisées

Le socle documentaire est complété par des conventions adaptées aux différents domaines.

Exemples :

- Convention Web.
- Convention Mobile.
- Convention de développement logiciel.
- Convention de design et direction artistique.

Ces conventions peuvent définir des documents supplémentaires, des règles, des skills, des agents et des méthodes adaptées.

Un projet Web doit pouvoir recevoir ses conventions techniques sans imposer ces règles à un projet créatif ou mobile.

## 8.4. Héritage des conventions

La hiérarchie recherchée comporte trois niveaux :

1. Conventions générales.
2. Conventions spécialisées.
3. Conventions propres au projet.

La propagation est descendante.

Les conventions générales s'appliquent aux domaines qui les utilisent.

Les conventions spécialisées héritent des règles générales et les précisent.

Les projets héritent des conventions pertinentes et peuvent ajouter des adaptations locales justifiées.

Une règle propre à un projet ne doit pas modifier automatiquement une convention générale.

Les conventions spécialisées doivent référencer les règles générales dont elles dépendent, plutôt que dupliquer leur contenu.

## 8.5. Standardiser sans sur-standardiser

Il est important de ne pas chercher à uniformiser artificiellement toute l'architecture des projets.

La standardisation doit se concentrer en priorité sur les éléments transversaux :

- Nommage.
- Taxonomie.
- Métadonnées.
- Responsabilités documentaires.
- Organisation de l'information.
- Traçabilité.
- Principes de structuration.

Les choix techniques et architecturaux internes doivent rester adaptés au produit et à ses contraintes.

Le système doit favoriser une cohérence naturelle plutôt que multiplier les règles obligatoires.

---

# 9. Conventions transversales

Plusieurs besoins de standardisation ont été identifiés au cours du cadrage.

Ils feront l'objet de documents spécialisés et ne doivent pas être intégralement redéfinis dans cette note.

## 9.1. Convention de nommage

Le principe recherché est de privilégier les noms courts, stables et basés sur les concepts et les responsabilités.

Préférences :

- Un seul mot lorsque le contexte suffit.
- Ne pas répéter les informations déjà présentes dans le chemin.
- Éviter les noms excessivement descriptifs.
- Éviter la multiplication des fichiers spécialisés.
- Centraliser les variantes lorsqu'elles appartiennent au même concept.
- Autoriser les noms composés et la séparation des fichiers lorsque cela améliore réellement la compréhension ou la maintenabilité.

Exemple : privilégier `card.tsx` avec des variantes cohérentes plutôt que créer systématiquement plusieurs fichiers indépendants pour chaque apparence d'une carte.

Cette préférence ne doit pas devenir une contrainte absolue.

Le document dédié `NAMING.md` doit formaliser les règles et leurs exceptions.

## 9.2. Convention des métadonnées

Les documents doivent pouvoir exposer des propriétés structurées facilitant leur compréhension par les humains et les agents IA.

Les propriétés envisagées incluent :

- Nom.
- Version.
- Description.
- Résumé.
- Type.
- Périmètre.
- Statut.
- Dates.
- Sources des dernières modifications.
- Dépendances documentaires.

La convention devra être adaptée aux formats.

Orientations techniques envisagées :

- Markdown : front matter YAML.
- TOML : configuration du système.
- JSON / JSONL : propriétés intégrées aux données structurées.
- Code source : commentaires et documentation adaptés lorsque cela présente une utilité.
- Formats binaires : métadonnées natives ou index externe lorsque nécessaire.

Le registre JSONL est conservé comme option privilégiée pour les entrées successives et append-only.

TOML est envisagé pour les configurations, mais le modèle définitif reste à formaliser.

Le document dédié `METADATA.md` doit définir la convention complète.

## 9.3. Généralisation raisonnée

Les conventions doivent être communes dans leurs principes, mais adaptées à la nature des fichiers.

Il ne faut pas imposer artificiellement des métadonnées ou des structures qui ne sont pas pertinentes pour un format donné.

L'objectif est d'améliorer la découvrabilité et la compréhension, pas d'ajouter des contraintes inutiles.

---

# 10. Registre : carte vivante du projet

## 10.1. Rôle du registre

Le registre ne doit pas être considéré comme une simple archive de conversations.

Il doit devenir une carte structurée permettant de comprendre l'histoire, les relations et les réalisations d'un projet.

Il doit permettre de répondre notamment à ces questions :

- Qu'a-t-on déjà envisagé ?
- Qu'a-t-on essayé ?
- Pourquoi ce choix a-t-il été fait ?
- Quelles alternatives existent ?
- Quelles décisions sont toujours pertinentes ?
- Quelles conventions s'appliquent ?
- Quels fichiers implémentent cette fonctionnalité ?
- Quels changements ont déjà été réalisés ?
- Quelles idées sont liées à ce sujet ?
- Qu'est-ce qui a évolué depuis la dernière intervention ?

## 10.2. Relier les connaissances à l'implémentation

Les captures doivent pouvoir référencer les éléments techniques pertinents :

- Fichiers.
- Dossiers.
- Composants.
- Fonctions.
- Classes.
- Symboles.
- Commits.
- État de réalisation.
- Dernière vérification connue.

Ces références doivent faciliter la recherche, sans prétendre remplacer le code réel.

Le registre ne doit pas recopier inutilement le contenu des fichiers.

Il doit surtout expliquer les raisons, les contraintes, les relations et le contexte qui ne sont pas toujours visibles dans le code.

## 10.3. Recherche progressive

L'agent ne doit pas devoir lire systématiquement l'intégralité du projet.

Le processus souhaité est :

1. Identifier le sujet de l'intervention.
2. Rechercher les informations pertinentes dans le registre.
3. Retrouver les captures et les relations importantes.
4. Identifier les documents et fichiers associés.
5. Lire les fichiers réellement concernés.
6. Vérifier l'état actuel du code et les éventuelles modifications récentes.
7. Préparer une proposition d'intervention cohérente.

La recherche doit être progressive et limiter le contexte transmis à l'agent.

Une recherche trop large dans les captures peut elle-même devenir coûteuse. Le registre doit donc être organisé et indexé de manière à fournir des résultats ciblés.

## 10.4. Ne pas confondre contexte historique et état actuel

Le registre peut indiquer qu'une fonctionnalité devait être créée, mais cela ne prouve pas qu'elle existe actuellement.

Il peut conserver une décision ancienne, mais cette décision peut avoir été remplacée.

Les informations historiques doivent être confrontées à l'état réel du projet avant de servir à une modification.

Cette distinction est centrale pour éviter les erreurs de contexte.

---

# 11. GitHub : source de vérité permanente du projet

## 11.1. Principe fondamental

GitHub demeure une source de vérité permanente pour l'état du projet.

L'historique des conversations ne constitue jamais une représentation exhaustive de son état réel.

Entre deux demandes, l'utilisateur peut librement modifier le dépôt :

- Ajouter une fonctionnalité.
- Corriger un problème.
- Réorganiser l'architecture.
- Renommer des fichiers.
- Modifier des conventions.
- Ajouter ou supprimer des éléments.
- Faire évoluer le code sans en informer les assistants IA.

Ces modifications restent valides même si aucune conversation ne les mentionne.

## 11.2. Autorité de l'état réel

Aucun agent ne peut considérer une information historique comme supérieure à l'état actuel du dépôt.

L'état du dépôt doit être vérifié aux endroits concernés avant une intervention.

Une information présente dans le registre ne peut pas justifier de restaurer une ancienne implémentation si le code a évolué depuis.

## 11.3. Protection contre les régressions

Les agents doivent respecter les règles suivantes :

- Ne pas supprimer une fonctionnalité existante sans demande explicite.
- Ne pas réintroduire une ancienne architecture simplement parce qu'elle apparaît dans le contexte historique.
- Ne pas écraser des modifications réalisées entre plusieurs conversations.
- Ne pas supprimer des fichiers ou documents sans justification et autorisation.
- Ne pas effectuer de retour arrière destructif sans demande humaine explicite.
- Ne pas considérer les modifications non poussées comme inexistantes.

Les modifications locales non commitées doivent également être protégées.

Le dépôt distant constitue la référence pour les états enregistrés et partagés, tandis que les modifications locales en cours représentent du travail réel qui ne doit pas être écrasé.

## 11.4. Vérification proportionnée

L'objectif n'est pas d'imposer la lecture complète du dépôt avant chaque modification.

La recherche dans le registre doit permettre d'identifier les zones pertinentes.

L'agent vérifie ensuite les fichiers concernés et les dépendances susceptibles d'être affectées.

Une exploration ou un audit global est réservé aux interventions dont le périmètre le justifie.

**Aucun agent ne possède l'autorité de faire régresser le projet au nom d'une connaissance historique incomplète.**

---

# 12. Production de prompts et accompagnement du développement

## 12.1. Finalité opérationnelle majeure

L'une des principales fonctions attendues du système est de produire des prompts de haute qualité pour les agents IA chargés de réaliser les modifications du projet.

Environ 98 % des modifications de code sont envisagées comme étant réalisées par une IA.

Le système doit donc améliorer la qualité du contexte transmis aux agents plutôt que simplement faciliter la consultation de documents.

## 12.2. Préparation d'une intervention

Lorsqu'une nouvelle amélioration est envisagée, le système doit pouvoir :

1. Comprendre la demande.
2. Identifier le sujet principal.
3. Rechercher les idées, décisions et travaux antérieurs.
4. Identifier les conventions applicables.
5. Retrouver les documents pertinents.
6. Identifier les fichiers et composants concernés.
7. Vérifier les éléments techniques dans le dépôt.
8. Définir le périmètre de la modification.
9. Identifier les contraintes et risques.
10. Définir les critères de réussite.
11. Produire un prompt adapté à l'agent et à son environnement.

## 12.3. Qualité attendue des prompts

Un prompt ne doit pas simplement être long.

Il doit contenir les informations réellement nécessaires :

- Contexte du problème.
- Objectif.
- État actuel connu.
- Références aux décisions.
- Conventions applicables.
- Périmètre.
- Fichiers ou zones concernés lorsque cela est établi.
- Contraintes de compatibilité.
- Comportements attendus.
- Critères de validation.
- Points de vigilance.
- Libertés laissées à l'agent.

Le système doit éviter de transmettre des informations inutiles ou obsolètes.

## 12.4. Boucle de retour

Les résultats d'exécution doivent pouvoir enrichir le registre.

Une modification réalisée peut produire de nouvelles informations :

- Implémentation effective.
- Résultats de tests.
- Problèmes rencontrés.
- Décisions techniques supplémentaires.
- Écarts avec les intentions initiales.
- Nouvelles possibilités d'amélioration.

La réalisation contribue ainsi au cycle de vie de l'information au lieu de rester isolée dans le code.

---

# 13. Interface conversationnelle et interactions humaines

## 13.1. Une interface qui structure sans interrompre

Une piste expérimentale importante consiste à faire évoluer l'expérience de conversation.

L'objectif est de permettre à l'utilisateur de travailler normalement avec un assistant tout en rendant les informations produites directement manipulables.

Les messages pourraient être analysés en blocs ou unités d'information possédant des propriétés.

Ces propriétés pourraient notamment indiquer :

- Nature de l'information.
- Sujet maître.
- Projet concerné.
- Domaine.
- Intention.
- Position.
- Niveau de confiance.
- Relations.
- Action possible.

## 13.2. Actions directement dans la conversation

Une interface future pourrait permettre de sélectionner une phrase ou un bloc et de modifier son état.

Exemples :

- Confirmer une proposition.
- La laisser en exploration.
- La relier à une convention existante.
- La transformer en tâche.
- La classer dans un projet.
- Signaler une contradiction.
- Identifier une décision.
- Demander une analyse complémentaire.

Une liste ou une réponse structurée pourrait également proposer des actions adaptées à son contenu, comme la création de tâches.

## 13.3. Relation avec Capture et Review

Cette interface ne doit pas créer un deuxième système de classification.

Elle doit utiliser les mêmes propriétés et règles que le registre.

Les actions humaines constituent des informations supplémentaires, conservées dans l'historique.

Capture peut identifier automatiquement les unités d'information, puis l'utilisateur peut intervenir sur leur classification.

Review assure ensuite la consolidation.

L'automatisation doit réduire le travail manuel, pas supprimer la capacité de l'utilisateur à contrôler les décisions.

## 13.4. Caractère expérimental

Cette expérience reste une orientation exploratoire.

Différents moyens d'intégration pourront être étudiés selon les environnements :

- Extensions propres aux assistants.
- Intégrations IDE.
- Plugins.
- Extensions navigateur.
- Interface de conversation indépendante.

Les mécanismes d'extension propres à certains outils, comme les Mods de Claude Code évoqués pendant les échanges, constituent des pistes d'adaptation.

Ils ne doivent pas devenir une dépendance du cœur du système.

Le moteur de classification, de capture et de gestion des relations doit rester indépendant de l'interface utilisée.

---

# 14. Principes fondamentaux de conception

Les principes suivants doivent guider les choix fonctionnels, documentaires et techniques.

## 14.1. Centralité de l'information

L'information traçable et évolutive est le cœur du système.

Les idées, décisions, projets, documents et tâches sont des formes ou des usages de cette information.

## 14.2. Préservation de l'historique

Les informations précédentes ne doivent pas disparaître lorsqu'une réflexion évolue.

Les corrections et enrichissements doivent conserver leur filiation.

## 14.3. Provenance et attribution

Chaque information doit pouvoir être rattachée à sa source et à son auteur lorsque cela est disponible.

La provenance ne doit pas être modifiée par une simple reformulation.

## 14.4. Séparation entre proposition et validation

Une proposition d'assistant ne constitue pas une décision humaine.

L'acceptation, le niveau de confiance, le statut et l'intention doivent être distingués.

## 14.5. GitHub comme référence de l'état du projet

Le registre et les conversations facilitent la compréhension du projet, mais ne remplacent pas son état réel.

Aucune opération destructive ne doit être déclenchée par une connaissance historique incomplète.

## 14.6. Standardisation par les concepts

Privilégier des conventions génériques et stables.

Éviter la multiplication des fichiers, catégories, documents et règles lorsque plusieurs éléments peuvent être organisés sous une même responsabilité cohérente.

## 14.7. Structure prévisible

Les mêmes grandes catégories doivent être retrouvées d'un projet à l'autre.

Le système doit diminuer le nombre de décisions organisationnelles nécessaires.

## 14.8. Simplicité progressive

La structure doit exister avant d'être intégralement remplie.

Un projet peut commencer avec un cadrage incomplet et évoluer naturellement.

## 14.9. Contextualisation avant intervention

Un agent doit rechercher les décisions et réalisations pertinentes avant de proposer une évolution.

Il doit ensuite vérifier les éléments réellement concernés.

## 14.10. Indépendance des outils

Le système doit pouvoir fonctionner avec différents assistants, IDE et outils de pilotage.

Ses données et conventions ne doivent pas dépendre d'une interface unique.

---

# 15. Périmètre du projet

## 15.1. Inclus dans le périmètre

Le projet doit couvrir progressivement :

- Gestion du cycle de vie de l'information.
- Collecte depuis différentes sources.
- Captures structurées.
- Préservation de la provenance.
- Relations entre informations.
- Historique et évolutions.
- Consolidation des connaissances.
- Recherche contextuelle.
- Standardisation documentaire.
- Conventions générales.
- Conventions spécialisées.
- Templates de projet.
- Skills et règles pour les agents.
- Accompagnement du cadrage et du brainstorming.
- Préparation des tâches et évolutions.
- Génération de prompts contextualisés.
- Référencement des fichiers et implémentations.
- Intégrations avec différents assistants et environnements.

## 15.2. Hors périmètre ou non retenu comme objectif central

Le système ne doit pas être conçu comme :

- Un simple gestionnaire de notes.
- Un simple gestionnaire de tâches.
- Un catalogue d'idées sans historique.
- Un assistant conversationnel supplémentaire sans mémoire structurée.
- Un remplacement de GitHub ou du code source.
- Un outil imposant une architecture technique identique à tous les projets.
- Un système qui transforme automatiquement toutes les idées en décisions.
- Un système de gestion autonome ayant le pouvoir de modifier ou supprimer les décisions et réalisations humaines.

Les outils existants peuvent rester utilisés lorsqu'ils remplissent correctement leur rôle.

Le système doit prioritairement organiser leur utilisation et maintenir un contexte commun.

---

# 16. Exigences non fonctionnelles

| Exigence              | Attendu                                                              |
| --------------------- | -------------------------------------------------------------------- |
| Simplicité            | Limiter les manipulations et les concepts inutiles                   |
| Prévisibilité         | Retrouver les mêmes repères dans chaque projet                       |
| Maintenabilité        | Éviter une architecture excessivement complexe                       |
| Traçabilité           | Comprendre l'origine et l'évolution des informations                 |
| Fiabilité             | Préserver les données et éviter les pertes d'information             |
| Extensibilité         | Ajouter de nouveaux domaines et conventions                          |
| Interopérabilité      | Fonctionner avec plusieurs assistants et outils                      |
| Efficacité            | Limiter les recherches et lectures redondantes                       |
| Efficacité des tokens | Transmettre un contexte ciblé plutôt que l'intégralité du projet     |
| Sécurité              | Protéger les sources de vérité et les modifications existantes       |
| Contrôlabilité        | Conserver la possibilité d'intervention et de validation humaine     |
| Lisibilité IA-first   | Rendre les documents et registres faciles à exploiter par les agents |

---

# 17. Risques et points de vigilance

## 17.1. Sur-standardisation

Un système trop rigide pourrait freiner les projets plutôt que les faciliter.

La standardisation doit se concentrer sur les responsabilités transversales et laisser les domaines spécialisés gérer leurs contraintes propres.

## 17.2. Surproduction d'informations

Une capture trop granulaire ou une automatisation excessive pourrait produire beaucoup de bruit.

Il faut trouver un équilibre entre conservation des informations utiles et charge de traitement.

## 17.3. Perte de nuances

Les agents pourraient interpréter une réflexion comme une décision ou attribuer à l'utilisateur une proposition formulée par l'assistant.

La provenance, l'auteur et le niveau de validation doivent rester explicitement distingués.

## 17.4. Registre obsolète

Les références vers les fichiers et implémentations peuvent devenir obsolètes après des modifications du code.

Elles doivent être vérifiées avec prudence et ne jamais être considérées comme une preuve de l'état actuel du dépôt.

## 17.5. Coût de recherche

Un registre mal structuré pourrait devenir aussi coûteux à consulter qu'une exploration directe du code.

La recherche doit être progressive, indexée et limitée aux informations pertinentes.

## 17.6. Régressions provoquées par les agents

Les agents peuvent intervenir avec un contexte incomplet.

La protection du dépôt et la vérification ciblée de l'état réel doivent être intégrées aux règles fondamentales de travail.

## 17.7. Complexité de l'interface

Une interface qui classe automatiquement chaque phrase peut devenir envahissante et interrompre la réflexion.

Il faudra permettre une capture discrète, des interactions contextuelles et une intervention humaine facultative lorsque la situation ne nécessite pas de décision immédiate.

## 17.8. Dépendance aux fournisseurs

Les fonctions d'interface spécifiques à Claude Code, ChatGPT ou d'autres outils peuvent évoluer.

Le cœur du système doit rester indépendant de leurs possibilités d'intégration.

---

# 18. Critères de réussite

Le projet pourra être considéré comme répondant à sa finalité lorsque les capacités suivantes seront suffisamment fiables.

## 18.1. Démarrage des projets

- Un nouveau projet peut être initialisé rapidement.
- Le socle documentaire est automatiquement disponible.
- Les conventions pertinentes peuvent être activées.
- La structure est compréhensible sans formation spécifique.
- Les documents peuvent être complétés progressivement.

## 18.2. Gestion de l'information

- Une conversation peut produire plusieurs captures indépendantes.
- Les sources et auteurs restent identifiables.
- Les propositions ne deviennent pas automatiquement des décisions.
- Les idées peuvent évoluer sans perdre leur historique.
- Les informations peuvent être reliées à plusieurs sujets.

## 18.3. Recherche et compréhension

- Un agent retrouve les décisions et travaux antérieurs d'un sujet.
- Il identifie les documents et fichiers pertinents.
- Il comprend pourquoi une implémentation existe.
- Il vérifie l'état réel du code avant d'intervenir.
- Il évite de relire inutilement l'ensemble du projet.

## 18.4. Développement assisté par IA

- Les prompts produits sont contextualisés.
- Les agents appliquent les conventions pertinentes.
- Les modifications respectent l'architecture et les décisions actuelles.
- Les changements déjà réalisés sont préservés.
- Les résultats d'exécution peuvent enrichir le registre.

## 18.5. Expérience de travail

- L'utilisateur retrouve les mêmes repères d'un projet à l'autre.
- Il peut reprendre facilement une réflexion.
- Le brainstorming peut évoluer sans perdre les idées antérieures.
- Il conserve une vision globale des projets.
- L'organisation facilite l'avancement plutôt que de le ralentir.

---

# 19. Orientations de réalisation

Cette section propose un ordre logique de développement. Elle ne constitue pas encore une roadmap validée.

## Phase 1 — Consolider le socle documentaire

Formaliser et vérifier :

- Les documents universels.
- Les responsabilités de chaque document.
- Les conventions de métadonnées.
- Les conventions de nommage.
- Les principes de taxonomie.
- Les conventions générales.
- Les règles de documentation.

Objectif : disposer d'un standard stable utilisable pour créer les projets.

## Phase 2 — Stabiliser le cycle de vie de l'information

Consolider les mécanismes :

- Capture.
- Relations.
- Provenance.
- Historique.
- Review.
- Recherche.

Objectif : disposer d'un registre fiable, compréhensible et exploitable.

## Phase 3 — Structurer les conventions spécialisées

Définir les extensions nécessaires :

- Web.
- Mobile.
- Développement logiciel.
- Autres domaines selon les besoins.

Objectif : pouvoir initialiser différents types de projets à partir du socle commun.

## Phase 4 — Améliorer la contextualisation des agents

Développer la recherche progressive et les relations avec le dépôt.

Objectif : retrouver rapidement les décisions et implémentations pertinentes et produire des prompts de qualité.

## Phase 5 — Améliorer le workflow de projet

Relier les réflexions, les tâches, le pilotage, les réalisations et les retours d'exécution.

Objectif : créer une continuité entre brainstorming, cadrage, préparation et réalisation.

## Phase 6 — Explorer les interfaces interactives

Étudier les intégrations permettant de classifier, confirmer, relier et transformer les informations directement dans les environnements de conversation.

Objectif : réduire les ruptures entre le travail conversationnel et la gestion des connaissances.

---

# 20. État des décisions et questions ouvertes

Cette section doit permettre de distinguer ce qui constitue déjà un engagement de conception de ce qui reste à approfondir.

## 20.1. Éléments explicitement retenus

Les éléments suivants ont été exprimés et confirmés par l'utilisateur pendant le cadrage :

| Sujet           | Orientation retenue                                                              |
| --------------- | -------------------------------------------------------------------------------- |
| Vision          | Système universel de gestion du cycle de vie des informations                    |
| Priorité        | Gestion et standardisation des projets                                           |
| Core            | Cycle de vie de l'information                                                    |
| Projets         | Considérés comme des produits                                                    |
| Documents       | Standardiser le démarrage des projets                                            |
| Extensions      | Ajouter des conventions et documents selon le domaine                            |
| Organisation    | Retrouver les mêmes repères d'un projet à l'autre                                |
| Brainstorming   | Conserver un contexte continu et des idées interconnectées                       |
| Prompts         | Améliorer fortement leur qualité et leur contextualisation                       |
| GitHub          | Source de vérité permanente de l'état du projet                                  |
| Protection      | Ne jamais annuler ou écraser des changements existants sans autorisation humaine |
| Nommage         | Préférer les noms courts, les concepts et les responsabilités                    |
| Convention      | Distinguer le socle général des conventions spécialisées                         |
| Standardisation | Éviter de sur-standardiser l'architecture interne des projets                    |

## 20.2. Orientations fortement établies

Les éléments suivants sont cohérents avec le cadrage, mais leurs modalités exactes restent à formaliser :

- Le registre comme carte vivante du projet.
- La recherche dans les captures avant la lecture ciblée du code.
- La séparation d'un message en plusieurs unités d'information.
- Les relations structurées entre idées, décisions, documents et fichiers.
- L'utilisation de métadonnées normalisées.
- La hiérarchie des conventions générales, spécialisées et locales.
- L'organisation en espaces Atelier, Référentiel, Journal et Pilotage.
- L'accompagnement du brainstorming par des agents spécialisés.
- L'intégration de la génération de prompts dans le workflow.

## 20.3. Propositions techniques à examiner

Ces pistes ont été discutées, mais ne doivent pas être considérées comme des décisions définitives :

- Maintenir JSONL pour le registre et employer TOML pour les configurations.
- Généraliser le front matter YAML dans les documents Markdown.
- Utiliser un index de recherche éventuellement construit à partir du registre.
- Référencer les fichiers, symboles et commits depuis les captures.
- Utiliser les capacités d'extension des assistants pour créer une interface interactive.
- Automatiser une partie de Capture et Review au fil des conversations.

## 20.4. Questions encore ouvertes

Les questions suivantes devront être approfondies avant de figer certaines parties de l'architecture :

1. Quel modèle de données définitif doit représenter les informations, leurs versions et leurs relations ?
2. Comment gérer précisément les modifications et les validations sans écraser l'historique ?
3. Quel mécanisme de recherche et d'indexation offre le meilleur équilibre entre précision et coût en tokens ?
4. Quelles propriétés doivent être obligatoires dans les captures ?
5. Comment automatiser la mise à jour des références entre captures et code ?
6. Comment gérer les conventions lorsqu'elles évoluent ou entrent en contradiction ?
7. Comment mesurer la qualité d'un prompt produit par le système ?
8. Quelle interface interactive peut être réalisée de manière durable sur plusieurs outils ?
9. Quel niveau d'automatisation de Capture et Review est souhaitable ?
10. Quel nom définitif correspond le mieux au produit ?

---

# 21. Conclusion du cadrage

Le projet a commencé avec l'ambition de construire un Second Brain capable de conserver le contexte des conversations et des projets.

La réflexion sur le « GitHub des idées » a ensuite permis de dépasser la simple conservation de notes en introduisant l'historique, l'évolution et les relations entre les informations.

Le cadrage a finalement abouti à une ambition plus large : construire un système universel dont le cœur est le cycle de vie de l'information, et dont l'application prioritaire est la standardisation et l'accompagnement des projets.

La finalité n'est pas de créer une bibliothèque documentaire toujours plus importante.

Elle est de disposer d'un environnement de travail stable dans lequel :

- Les projets démarrent avec des structures cohérentes.
- Les informations ne se perdent pas.
- Les idées restent interconnectées.
- Les décisions conservent leur historique.
- Les conventions sont réutilisables.
- Les agents comprennent le contexte avant d'intervenir.
- Les modifications respectent l'état réel du projet.
- Les réflexions peuvent être transformées en instructions précises et en réalisations concrètes.

Le système doit ainsi créer une continuité entre la réflexion, la connaissance, la conception, le pilotage et la réalisation.

**Son ambition fondamentale est de permettre de construire et faire évoluer des projets avec une organisation prévisible, une mémoire fiable et des agents IA capables d'agir avec une compréhension durable du contexte.**

Ce cadrage constitue une base de référence évolutive. Les futures modifications de vision, de périmètre ou de principes fondamentaux devront être examinées à la lumière de ce document, sans effacer l'historique des réflexions qui ont conduit à son évolution.