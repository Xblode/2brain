# AUDIT — capture production : conversation-reference-5

| | |
| --- | --- |
| Source | lab/sources/conversation-reference-5.txt (5 265 lignes, lues 1 à 5 265 sans trou) |
| Cible | brain/registry/entries.jsonl (append via append-captures.py, opération ref5-20261106) |
| run_id | production ; capture_ref production:CAP-NNN |
| Plage | CAP-420 à CAP-476 (57 captures, sans trou) |
| Couche | Audit de capture (distinct de la validation technique et de l'évaluation humaine) |

## Fenêtres (12, par échanges ; 4 passes appliquées à chaque fenêtre)

| Fenêtre (lignes) | Contenu | Captures |
| --- | --- | --- |
| 1–602 | Demande de prompt 0.1.5 ; prompt de l'assistant (non recopié) | 420 |
| 603–1352 | Décision « pas de test isolé » ; demande de retour arrière ; design rollback (assistant) | 421–426 |
| 1353–2144 | Question sur les protections append-only ; réponse de l'assistant ; prompt (non recopié) | 427–428 |
| 2145–2565 | GitHub des idées ; réponse de l'assistant ; cinq niveaux ; choix de la vision C | 429–435 |
| 2566–2688 | Cycle de vie ; conventions par type ; brainstorming ; prompts de qualité | 436–440 |
| 2689–2887 | Finalité de standardisation ; rangement stable ; GitHub source de vérité | 441–443 |
| 2888–2983 | Préférence de nommage ; accord partiel | 444–445 |
| 2984–3005 | TOML ; message multi-infos ; feedback ; coûts ; interface ; conventions ; front matter | 446, 448, 450–453, 455, 456, 459–463 |
| 3006–3499 | Analyse de l'assistant (TOML, multi-infos, coûts, Mods, héritage) | 447, 449, 454, 457, 458 |
| 3500–4823 | Demande de cadrage ; cadrage rédigé (CADRAGE non découpé) | 464–465 |
| 4824–4911 | Question sur les conventions ; tableau de l'assistant | 466–467 |
| 4912–5265 | Usage personnel ; skills ; Graphify ; UI/UX ; DA ; design system ; second cerveau ; rôles des skills | 468–476 |

Couverture : aucune tranche omise. Les messages humains ont été examinés ligne à ligne. Les propositions de l'assistant ont été retenues quand elles répondent à une question ou posent une règle.

## Couverture source↔brouillon

| Zone / thème | Statut | CAP |
| --- | --- | --- |
| Demandes et décisions humaines (prompt, test, rollback) | Complet | 420, 421, 422 |
| Questions humaines (protections, GitHub des idées, TOML, coûts, faisabilité, conventions, cadrage) | Complet | 427, 429, 446, 453, 456, 466, 464 |
| Vision (choix C, priorité, cycle de vie, finalité, TDAH) | Complet | 433, 434, 436, 441, 442 |
| Standardisation, nommage, conventions, héritage | Complet | 444, 459, 460, 461, 462, 463 |
| Source de vérité GitHub | Complet (règle humaine) | 443 |
| Rollback et protections (propositions de l'assistant) | Partiel : garde-fous et IDs retenus ; historique _capture-history/ et liste de garanties non retenus | 423–426, 428 |
| Skills, Graphify, UI/UX, DA, design system (humain) | Complet | 470–475 |
| Rôles des skills (assistant) | Complet | 476 |
| Propositions de structure de l'assistant (briques, cinq couches, 01–06, index, propriétés, six axes) | Partiel : voir Exclusions | 431 seulement |
| CADRAGE (3512–4809) | Non découpé : fait de rédaction seulement | 465 |

## Exclusions motivées (propositions de l'assistant et répétitions)

- Prompts Cursor (lignes 6–602, 643–1350, 1429–2137) : versions successives du prompt 0.1.5, longues, non recopiées (consigne). Les règles P0 (attribution, space, atomicité, intention) reprennent CAP-384 à CAP-387 et CAP-417 ; non recapturées.
- Premier prompt (test isolé sur la source 4, lignes 6–14) : remplacé par la décision humaine de la ligne 603, donc non capturé à part.
- Ligne 2145 : « j'ai plus de crédit sur cursor donc j'ai pas lancé le correctif » : état d'avancement, non capturé (faible valeur de connaissance). À rouvrir si besoin.
- Ligne 2566 : « On continuera après » : sans contenu.
- Lignes 2288–2299 (rôles de Brain Capture, Review, Search et Sync dans la nouvelle vision) : tableau de correspondance non capturé.
- Lignes 2268–2282 (alternatives A, B, C conservées, distinguer évolution et fusion) : non capturées ; le principe est repris comme question (432).
- Lignes 2363 (formulation du modèle universel), 2373–2401 (trois dimensions), 2403–2442 (cycle non linéaire), 2444–2464 (information versionnée au centre), 2466–2492 (analogie Git), 2494–2523 (deux niveaux universel et domaines), 2549–2561 (hypothèse de travail), 2671–2683 (vision consolidée) : propositions de l'assistant qui développent la vision. Non capturées, faute de place. La vision humaine est captée par 433, 434, 436 et 441.
- Lignes 2761–2785 (structure commune 01 à 06) : non capturée. À reprendre si l'humain la retient.
- Lignes 2822–2882 (règle GitHub détaillée, trois niveaux de vérité, principe « aucun agent ne peut faire régresser le projet ») : non capturées. La règle humaine (443) est captée.
- Lignes 2897–2958 (quatre principes de nommage) : non capturées ; la préférence humaine est captée (444).
- Lignes 3144–3159 (propriétés proposées pour une capture : subject, project, domain, concepts, relations, files, symbols, implementation_status, commit, verified_at) : non capturées. À décider.
- Lignes 3340–3424 (maquette d'interface, trois temps A, B, C, limite ChatGPT) : non capturées. L'idée humaine est captée (455, 456).
- Lignes 3006–3008 et 3091–3097 (registre comme index intelligent, reformulations) : non capturées.
- Lignes 4937–4943 (personnalisation profonde, axe de pilotage transversal) : non capturées.
- Lignes 4962–4994 (briques : environnement, moteur, projets, créative, activités, agents, interfaces) : non capturées.
- Lignes 5049–5129 (DA libre, UX sélectif, design system obligatoire) : non capturées. Les points humains 472 à 474 sont captés.
- Lignes 5164–5188 (Graphify, point de vue de l'assistant) : non capturées ; la position humaine est captée (471).
- Lignes 5190–5206 (nouvelles conventions : WORKFLOW.md, ORCHESTRATION.md, SKILLS.md, etc.) : non capturées. Le tableau de conventions des lignes 4834–4904 l'est (467).
- Lignes 5210–5225 (philosophie du projet personnel), 5227–5263 (six axes), 5265 (recommandation suivante) : non capturées.
- Liens d'images et de titres (images.openai.com en lignes 5071–5101 et 5168 ; favicons google.com/s2/favicons) : non repris. Les URL des outils d'inspiration cités par l'humain sont captées (473).
- Lignes 2185–2205 (approches existantes : GitLab, Creative Version Control, Brain Vault, mymir) : non capturées. Le texte n'a que des favicons ou des noms de domaine partiels ; aucune URL complète n'est disponible.
- Marqueurs d'artefacts `【turn…】` aux lignes 3059, 3314, 3332 et 3336 : non repris.

## Atomicité et richesse

- Splits : CAP-423, 424, 425 (rollback : transaction, garde-fous, IDs) ; CAP-433 et 434 (vision et priorité, deux choix distincts) ; CAP-436 à 440 (cinq exigences humaines séparées) ; CAP-448 et 449 (message multi-infos : demande humaine et proposition de l'assistant) ; CAP-455 et 456 (idée et question de faisabilité).
- Fusions évitées : la préférence de nommage (444) est séparée de la règle de convention ; l'accord de principe (445) est séparé de la question des conventions.
- Volume : 57 captures, au-dessus du repère 30 à 50. Raison : 40 captures sont des paroles humaines (demandes, décisions, questions, préférences, exigences), et la consigne donne la priorité à ces paroles. Les propositions de l'assistant ont été réduites (17 captures, voir Exclusions).
- Captures courtes : 425, 436, 438, 439, 440, 451, 474 (une phrase humaine, la source n'ayant rien de plus).

## Provenance et refs

- Locators : oui. Numéros de ligne 1-indexés (équivalents à `sed -n`). Chaque evidence est vérifiée par check_cit.py contre ses locators.
- URL et refs : toutes les URL non favicon présentes dans les lignes captées sont dans refs[] et dans content, en entier. CAP-457 : lien de la ligne 3314. CAP-470 : six skills (lignes 4915 à 4920). CAP-471 : Graphify (4924). CAP-473 : Refero, Recent Design, Mobbin (4927). CAP-476 : six URL avec `?utm_source=chatgpt.com` (5008 à 5015).
- Note sur CAP-457 : le libellé du lien (« … | Medium », article sur une fuite de code) ne correspond pas au domaine réel (images.openai.com). L'URL est reprise telle quelle. Non vérifiée (pas d'accès web).
- Note sur CAP-476 : les URL gardent le paramètre `?utm_source=chatgpt.com` présent dans la source.
- Multi-passages : oui (CAP-431 : lignes 2217 et 2219–2251 ; CAP-465 : lignes 3506 et 3512–4809).

## Grounding, mapping, space, approbation

- intention→type : appliqué par build.py selon TAXONOMY.md (orientation et suggestion vers proposition ; question vers open_question ; decision vers decision ; requirement et preference vers observation ; idea vers idea ; task vers task ; convention vers convention).
- Anti-faux-explicit : une seule approbation explicite, CAP-421. Les accords partiels portent `approval_global_partial` et `validation: none` (CAP-445, CAP-462). Les choix humains (CAP-433, CAP-434) portent `position: selected` sans validation.
- Space : `referentiel` seulement pour CAP-421 (décision explicite), CAP-443 (règle que l'humain présente comme fondamentale, sans approbation formelle : signal REVIEW à trancher), CAP-468 (statut de projet personnel exprimé comme fait, sans approbation : signal REVIEW). Les propositions de l'assistant sont en `atelier`, sauf CAP-465 (fait de rédaction, `journal`).
- Tags : `ambiguous` (433), `approval_global_partial` (445, 462), `à-revoir` (442), `vérification-à-faire` (457).

## Contradictions, tensions et relations

- Relations posées : 61 liens au total, dont 46 internes au lot (réciproques posées pour chaque paire `answers`, `clarifies`, `evolves_from` interne) et 15 vers des anciennes CAP (un seul sens).
- Vers les anciennes captures (un seul sens, comme prévu par les règles) : CAP-433 vers CAP-001 (evolves_from), CAP-436 et CAP-441 vers CAP-389 (clarifies), CAP-420 vers CAP-416 (related), CAP-421 vers CAP-376 et CAP-416 (related), CAP-429 et CAP-430 vers CAP-001 (related), CAP-431 vers CAP-390 et CAP-405 (related), CAP-464 et CAP-465 vers CAP-403 et CAP-412 (related), CAP-466 vers CAP-380 (related), CAP-468 vers CAP-407 (related).
- Le validateur signale trois réciproques absentes vers des anciennes CAP (CAP-433, CAP-436, CAP-441) : attendu, car une seule direction est possible.
- Contradictions posées : aucune. Tensions possibles à relire par l'humain : CAP-443 (GitHub source de vérité) et CAP-187 (local = source de vérité, pour ClickUp) ; CAP-468 (projet personnel) et CAP-407 (Second Brain doit cadrer tout projet) ; CAP-467 (TAXONOMY.md proposé en premier) et le fichier brain-main/conventions/TAXONOMY.md qui existe déjà (version 1.0.2).
- CAP-380 proposait `taxonomy.md` ; le fichier existant est `TAXONOMY.md` (même nom, casse différente). Non traité ici.

## Corrections avant clôture

- Transcriptions corrigées avant le contrôle final : CAP-439 (« Notre projet » et non « projets »), CAP-454 (« à une condition »), CAP-462 (« sujets global »). Contrôle final : 107 morceaux conformes, 0 écart.
- Notes de travail retirées du content : CAP-444 (« écrit ainsi dans la source ») et CAP-465 (phrase sur le périmètre de la capture).
- CAP-432 : libellé des options aligné sur la source.
- Réciprocité ajoutée : CAP-433 `clarified_by` CAP-434. Le validateur ne signale plus de WARN interne au lot.
- Registre réel : non modifié. SHA-256 avant et après : 0ae3c9777258cd418a04e5579e2c996b4a5baedb6bb7eabbbd17dd0cdd69c4a3.

## Points à décider par l'humain

- CAP-442 (TDAH déclaré) : information personnelle sensible. Garder dans le registre ou non ?
- CAP-421 : seule approbation explicite. Confirmer qu'une consigne de procédure (pas de test isolé) vaut approbation de la décision.
- CAP-433 : choix de la vision C, présenté comme « à approfondir » ; classé en `orientation`, `selected`, sans validation. Confirmer ce classement.
- CAP-443 et CAP-468 : `referentiel` sans validation (signal REVIEW).
- CAP-457 : affirmations de l'assistant sur les Mods de Claude Code, non vérifiées ; lien à contrôler.
- CAP-422 : la commande est écrite « /brain-capture 1 » dans la source ; le Skill utilise « /brain -c 1 ». Le contenu reprend la source ; l'écart de nom est signalé ici.
- Propositions de l'assistant non capturées (voir Exclusions) : à capturer ou non dans un lot ultérieur.
- Volume : 57 captures, au-dessus du repère 30 à 50 : à trancher.
- Ligne 2145 (correctif non lancé faute de crédit) : non capturée, à confirmer.

## Bilan `/brain -c`

| | |
| --- | --- |
| Source | lab/sources/conversation-reference-5.txt |
| Mode | production |
| Cible | brain/registry/entries.jsonl (non écrit : brouillon seul) |
| run_id | production |
| IDs ajoutés (brouillon) | CAP-420 → CAP-476 (57) |
| Validateur | OK sur copie + brouillon (`--require-intention`, `--json-out`) : 0 erreur, 26 avertissements dont 3 liens one-sided attendus, 65 revues humaines (dont 5 dans le lot) |
| validate.json | oui (copie) |
| AUDIT.md | oui |
| Production touchée | non |

**Couches** : technique OK · audit capture fait (partiel sur propositions assistant) · éval. humaine en attente.

**Comptes** : total 57 · explicit 1 · none 56 · set 0 · partiel (tag approval_global_partial) 2 · position null 37.

**Auteurs** : user 40 · assistant 17.

**Intentions** : requirement 18 ; suggestion 12 ; question 8 ; preference 5 ; observation 4 ; feedback 3 ; orientation 2 ; task 2 ; decision 1 ; convention 1 ; idea 1.

**Grounding** : explicit 54 · contextual 3 · interpreted 0 · uncertain 0.

**Refs** : URL conservées 17 (sur 5 captures ; favicons non retenus) ; formulation « lien fourni » évitée : oui.

**Actionnable** : tâches 2 (420, 464) ; jalons 0 ; cadrage individuel 441, 465 (le cadrage lui-même n'est pas découpé).

**Relations** : 61 liens (46 internes, 15 vers anciennes CAP) ; réciproques internes posées : oui ; doubles évités : oui.

**Ambigus** : CAP-433 (orientation, choix non figé), CAP-443 et CAP-468 (referentiel sans validation), CAP-442 (donnée sensible), CAP-457 (affirmations non vérifiées).

**Bruit exclu** : prompts Cursor non recopiés ; artefacts `【turn…】` ; favicons Google ; URL d'images openai.com.

**Fenêtres** : 12 traitées ; mémoire globale : oui.

**Couverture** : messages pertinents humains : OK ; propositions assistant conservées : partiel (voir Exclusions) ; nuances : OK ; locators : OK ; refs : OK.

## Captures

| id | Titre | Intention | Auteur | Validation | Espace |
| --- | --- | --- | --- | --- | --- |
| CAP-420 | Demande du prompt Brain Capture 0.1.5 après la source 4 | task | user | none | pilotage |
| CAP-421 | Décision utilisateur : capturer la source 4 directement dans le registre de production, sans test isolé | decision | user | explicit_user_approval | referentiel |
| CAP-422 | Demande utilisateur : pouvoir annuler la dernière exécution de Capture avec /brain-capture 1 | requirement | user | none | atelier |
| CAP-423 | Proposition assistant : rollback transactionnel d'une exécution complète, et non un git reset | suggestion | assistant | none | atelier |
| CAP-424 | Proposition assistant : garde-fous du retour arrière (point de restauration, contrôle, archive) | suggestion | assistant | none | atelier |
| CAP-425 | Proposition assistant : un identifiant annulé reste réservé, les trous de numérotation sont acceptés | suggestion | assistant | none | atelier |
| CAP-426 | Proposition assistant : écriture du registre par un seul script à ajout, avec contrôle avant et après | suggestion | assistant | none | atelier |
| CAP-427 | Question utilisateur : Capture écrit-il à la suite sans rien supprimer, et faut-il des protections globales en 0.1.5 ? | question | user | none | atelier |
| CAP-428 | Constat assistant : règle append-only seulement déclarative, pas de garantie technique | observation | assistant | none | atelier |
| CAP-429 | Question utilisateur : un « GitHub des idées » plutôt qu'un « second cerveau » ? | question | user | none | atelier |
| CAP-430 | Réponse assistant : « GitHub des idées » décrit mieux le fonctionnement, mais c'est le modèle mental qui doit changer | suggestion | assistant | none | atelier |
| CAP-431 | Proposition assistant : cinq niveaux (sources, registre, graphe, structure du projet, exploitation) | suggestion | assistant | none | atelier |
| CAP-432 | Question assistant : GitHub des idées, GitHub des projets ou versionnement universel des connaissances ? | question | assistant | none | atelier |
| CAP-433 | Choix utilisateur : vision C, versionnement universel des connaissances (à approfondir) | orientation | user | none | atelier |
| CAP-434 | Choix utilisateur : « les trois », avec une priorité aux projets | orientation | user | none | atelier |
| CAP-435 | Questions ouvertes de l'assistant : cinq sujets à trancher avant de modifier l'architecture | question | assistant | none | atelier |
| CAP-436 | Utilisateur : le cycle de vie des informations sera le cœur du projet | requirement | user | none | atelier |
| CAP-437 | Utilisateur : relier plus tard chaque projet à des conventions par type (web, mobile, autres) | requirement | user | none | atelier |
| CAP-438 | Utilisateur : lancer vite un projet et brainstormer régulièrement pour préparer correctifs et updates | requirement | user | none | atelier |
| CAP-439 | Utilisateur : le projet doit surtout produire des prompts de qualité pour les correctifs et updates | requirement | user | none | atelier |
| CAP-440 | Utilisateur : épauler le brainstorming en gardant un contexte d'idées interconnectées par projet | requirement | user | none | atelier |
| CAP-441 | Finalité utilisateur : standardiser les documents de démarrage, puis conventionner les documents spécialisés | requirement | user | none | atelier |
| CAP-442 | Besoin utilisateur : ranger dans des boîtes toujours identiques pour avancer (TDAH déclaré) | requirement | user | none | atelier |
| CAP-443 | Règle utilisateur : GitHub reste la source de vérité, ce qui est poussé ne doit pas être retiré sans demande humaine | convention | user | none | referentiel |
| CAP-444 | Préférence utilisateur : noms de documents d'un seul mot, variantes dans card.tsx plutôt que fichiers multiples | preference | user | none | atelier |
| CAP-445 | Accord utilisateur : voir les projets comme des produits à standardiser (accord global, non validé point par point) | feedback | user | none | atelier |
| CAP-446 | Question utilisateur : passer le registre en TOML ? | question | user | none | atelier |
| CAP-447 | Réponse assistant : garder JSONL pour le registre, utiliser TOML pour la configuration | suggestion | assistant | none | atelier |
| CAP-448 | Problème utilisateur : un même message mêle une idée structurante, une vision et une petite modification | requirement | user | none | atelier |
| CAP-449 | Proposition assistant : séparer dans un message les unités d'information, en gardant la source commune | suggestion | assistant | none | atelier |
| CAP-450 | Retour utilisateur : l'assistant ne peut pas tout vérifier à chaque modification, d'où le suivi des idées | feedback | user | none | atelier |
| CAP-451 | Observation utilisateur : environ 98 % des modifications seront codées par une IA | observation | user | none | atelier |
| CAP-452 | Exigence utilisateur : chercher dans le registre ce qui a déjà été fait avant de proposer une implémentation | requirement | user | none | atelier |
| CAP-453 | Question utilisateur : chercher dans le registre est-il moins coûteux que vérifier directement dans le code ? | question | user | none | atelier |
| CAP-454 | Réponse assistant : la recherche dans le registre peut coûter moins cher si elle reste progressive | suggestion | assistant | none | atelier |
| CAP-455 | Idée utilisateur : interface expérimentale qui rend les réponses annotables et actionnables | idea | user | none | atelier |
| CAP-456 | Question utilisateur : comment adapter l'interface expérimentale aux propriétés et réglages de Capture ? | question | user | none | atelier |
| CAP-457 | Affirmation de l'assistant : Claude Code Mods sont des extensions JS/TS, pas une modification du binaire | observation | assistant | none | atelier |
| CAP-458 | Proposition assistant : trois niveaux de conventions (générales, spécialisées, projet), héritage descendant | suggestion | assistant | none | atelier |
| CAP-459 | Utilisateur : conventions générales (naming, taxonomie) pour tous les projets, conventions spécialisées sans effet vers le haut | requirement | user | none | atelier |
| CAP-460 | Utilisateur : la convention Web doit utiliser la convention générale sans dupliquer l'information | requirement | user | none | atelier |
| CAP-461 | Exigence utilisateur : Capture et Review doivent aboutir seuls au même rangement de convention | requirement | user | none | atelier |
| CAP-462 | Retour utilisateur : standardiser les projets eux-mêmes, mais sans impact trop lourd, sur des sujets globaux | feedback | user | none | atelier |
| CAP-463 | Préférence utilisateur : propriétés en en-tête de la plupart des fichiers, comme SKILL.md | preference | user | none | atelier |
| CAP-464 | Demande utilisateur : rédiger la note de cadrage (cadrage.md) dans cette conversation, en représentant son évolution | task | user | none | pilotage |
| CAP-465 | Note de cadrage rédigée par l'assistant dans la conversation (version 0.1, en cours de consolidation) | observation | assistant | none | journal |
| CAP-466 | Question utilisateur : quels autres documents de convention peut-on déjà avancer ? | question | user | none | atelier |
| CAP-467 | Proposition assistant : tableau de conventions à rédiger, en commençant par TAXONOMY.md | suggestion | assistant | none | atelier |
| CAP-468 | Précision utilisateur : projet pour un usage personnel, un espace de travail adapté à lui | requirement | user | none | referentiel |
| CAP-469 | Utilisateur : plusieurs briques autour du système pour piloter ses activités depuis n'importe où | requirement | user | none | atelier |
| CAP-470 | Utilisateur : six skills externes retenus comme sources, à intégrer au workflow sans refaire leur travail | requirement | user | none | atelier |
| CAP-471 | Préférence utilisateur : Graphify comme source d'inspiration, sans l'intégrer au projet | preference | user | none | atelier |
| CAP-472 | Préférence utilisateur : pas de skills UI pour l'instant, UX possible plus tard ; garder dimensional drawing | preference | user | none | atelier |
| CAP-473 | Utilisateur : outils d'inspiration pour la DA, qui doit rester libre et ne jamais s'enfermer dans la copie | requirement | user | none | atelier |
| CAP-474 | Exigence utilisateur : un Design System suivant un code standardisé, toujours | requirement | user | none | atelier |
| CAP-475 | Préférence utilisateur : chacun doit créer son propre second cerveau, avec ses conventions et ses règles | preference | user | none | atelier |
| CAP-476 | Proposition assistant : rôle de chaque skill externe, et séparation système / skills / outils | suggestion | assistant | none | atelier |

## Ajout au registre réel et contrôles

- Registre réel touché : oui. 419 -> 476 lignes (525510 -> 612255 octets). SHA-256 avant 0ae3c9777258cd418a04e5579e2c996b4a5baedb6bb7eabbbd17dd0cdd69c4a3, après 1af706b3a1e59e7ada0d9fb413f91a2b520dc1ae7c244db75736a2c963b641c6. Les 525510 premiers octets donnent 0ae3c977… (append only prouvé) ; les 57 dernières lignes sont identiques au brouillon.
- Contrôle mécanique des citations (check_cit.py) : 107 morceaux conformes, 0 écart, aucune correction nécessaire.
- Validateur (--require-intention) : 0 erreur bloquante, 26 avertissements (réciproques de relations), 476 ids uniques.
- Aucune correction de contenu dans ce lot.

## Limites de méthode

- Rédaction des captures par un worker haiku ; le contrôle des citations est mécanique, le jugement sémantique n'a pas été refait.
- Évaluation humaine en attente.
