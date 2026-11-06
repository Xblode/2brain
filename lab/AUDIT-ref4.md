# AUDIT - capture production : conversation-reference-4

| | |
| --- | --- |
| Source | lab/sources/conversation-reference-4.txt (4 464 lignes) |
| Cible | brain/registry/entries.jsonl (production, append via append-captures.py, opération ref4-20261106) |
| Couche | Audit de capture (distinct de la validation technique et de l'évaluation humaine) |
| Mode | production (run_id production), choisi explicitement par la mission |

## Résumé

- 69 captures, CAP-351 à CAP-419. Validateur sur la copie (registre + brouillon) : 0 erreur bloquante, avec --require-intention.
- 47 exclusions motivées (tableau ci-dessous). Volume supérieur au repère 35 à 50 : voir Atomicité et richesse.
- Registre réel touché : oui. 350 -> 419 lignes. SHA-256 avant a48a5498180ed818987194ca59ead860d331756183aa228649195e0ff1622f54, après 0ae3c9777258cd418a04e5579e2c996b4a5baedb6bb7eabbbd17dd0cdd69c4a3. Préfixe de 417200 octets inchangé (append only prouvé). Validateur final : 0 erreur bloquante, 23 avertissements.
- Contrôle mécanique des citations (script check_cit.py) : 88 morceaux de evidence, 0 écart après correction (15 captures corrigées, voir Corrections).


## Couverture source-registre (tranches lues : 1-4464, sans trou)

| Tranche | Thèmes | CAP du brouillon |
| --- | --- | --- |
| 1-500 | Prompt Cursor 0.1.3 ; audit 0.1.3 ; Test A/B | 351, 352, 353 |
| 501-1000 | Plan 0.1.3 (review, ajustements, verdict) ; Test A ; tâches | 354 |
| 1001-1500 | Audit du dernier push ; smoke test ; capability-test ; verdict | 355, 356, 357, 358, 359, 360, 361 |
| 1501-2000 | Audit capability-test (pertes, modes, isolation, référentiel) ; décisions | 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372 |
| 2001-2500 | Conventions générales ; brain-main ; décisions 0.1.3 correctif | 373, 374, 375, 376, 377, 378, 379, 380, 381 |
| 2501-3000 | Audit 0.1.4 (attribution, referentiel, composites) ; prompt 0.1.4.1 | 382, 383, 384, 385, 386, 387, 388 |
| 3001-3500 | Finalité du projet ; état de Second Brain ; vision Review | 389, 390, 391, 392, 393, 394, 395, 396, 397 |
| 3501-4000 | Note de cadrage ; Inbox ; décisions 0.1.5 / tasks.jsonl | 398, 399, 400, 401, 402, 403, 404, 405 |
| 4001-4464 | Suite note de cadrage ; agents ; Inbox ; synthèse | 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419 |

Numérotation abrégée : chiffres = CAP-NNN (ex. 351 = CAP-351). Une capture est rangée par la ligne de début de son premier locator.

## Exclusions motivées (sélection, 47 passages/éléments)

| Clé | Passage (titre de travail) | Motif |
| --- | --- | --- |
| k2 | Prompt Cursor 0.1.3 — analyse et plan sans modifier le dépôt | Contrainte d'analyse seule déjà captée (CAP-239, CAP-268) ; énoncé du prompt non repris. |
| k5 | Process 0.1.3 - présenter le plan à l'humain avant tout code Cursor | Process « présenter le plan avant code » déjà couvert par CAP-270 et CAP-277. |
| k6 | Localisateur window pour conversation Cursor live sans numéros de ligne | Détail de schéma (localisateur window) ; pas de décision utilisateur. Sélection. |
| k7 | Schéma 0.1.3 - ne pas ajouter commented_by, validated.jsonl ni statut Review | Non-ajouts de champs : détail de schéma, proche de CAP-205. Sélection. |
| k8 | 0.1.3 - retirer les scénarios A-H comme grille universelle de test | Retrait des scénarios A-H : détail de protocole, proche de CAP-266/CAP-267. Sélection. |
| k9 | Test B - accès partiel à la conversation = échec d'accès, pas échec de capture | Accès partiel = échec d'accès : règle proche de CAP-353 (Test B). Sélection. |
| k10 | Question ouverte - format exact de AUDIT.md et source du smoke-test 0.1.3 | Question de plan (format AUDIT.md, source smoke) : faible priorité ; à rouvrir si besoin. |
| k11 | Critères de passage au Test A pour Brain Capture 0.1.3 | Critères de passage au Test A : redondants avec CAP-344 et CAP-345 (registre vivant). |
| k12 | Review du plan - plusieurs localisateurs par capture (origin.locators) | Localisateurs multiples : déjà couvert par CAP-284 et CAP-219. |
| k14 | Review du plan - distinguer source_explicit, source_contextual et source_interpreted | source_interpreted : déjà présent dans TAXONOMY.md section 8. |
| k15 | Review du plan - auteur principal et contributions séparés | Auteur principal vs contributions : déjà dans source-attribution.md (CAP-317). |
| k16 | Review du plan - relations contradicts / contradicted_by pour deux propositions | Exemple contradicts : principe déjà dans TAXONOMY.md section 7 et CAP-034/CAP-154. |
| k20 | Principe 0.1.3 : références, provenance et qualité des relations à anticiper dès maintenant | Principe références/provenance : redondant avec CAP-312 (registre vivant) et CAP-389. |
| k21 | Ok j'ai push la mise à jour 0.1.3 sur le dépôt (déclaration utilisateur) | Push 0.1.3 (événement) : secondaire ; la demande d'audit reste captée (CAP-357). |
| k23 | Audit de la 0.1.3 poussée : architecture cohérente, corrections ciblées avant test | Synthèse d'audit 0.1.3 redondante avec CAP-358 et CAP-359. |
| k26 | Conventions des localisateurs 0.1.3 : lines 1-based inclusif, offset 0-based fin exclue | Conventions lines/offset/window : détail technique ; origine du contrôle captée par CAP-359. |
| k28 | Test A - procédure : environnement isolé, Skill User figé, sources 1 à 3 exclues | Procédure Test A détaillée : couverte par CAP-341 (registre vivant) ; remplacée par CAP-376. |
| k29 | Test A - ne pas donner à Cursor la liste des captures attendues | Consigne « ne pas donner la liste attendue » : consigne de test proche de CAP-331 (registre vivant). |
| k31 | Prompt de corrections 0.1.3 : ciblé, sans refonte ni Test A | Cadrage du prompt de corrections 0.1.3 : redondant avec CAP-377 et CAP-357. |
| k32 | Demande prompt de corrections 0.1.3 à donner à Cursor | Demande de prompt de corrections : secondaire, couverte par CAP-377. |
| k33 | Vérifications techniques après corrections 0.1.3 : fichier vide, rétrocompatibilité, fixture valide | Vérifications techniques post-correctif : redondantes avec CAP-358 et CAP-359. |
| k34 | Ok j'ai push le correctif 0.1.3 sur le dépôt (déclaration utilisateur) | Push du correctif (événement) : secondaire ; la demande d'audit reste captée (CAP-362). |
| k38 | Audit P1 validateur : rejouer la validation après le correctif et rejeter proprement les JSON malformés | Validateur : rejeu et JSON malformés : détail technique ; à rouvrir si besoin. |
| k42 | Test de reconstruction en trois phases : capture brute, reconstruction isolée, audit comparatif | Test de reconstruction en trois phases : objectif abandonné par l'utilisateur (CAP-378). |
| k43 | Trois catégories de problèmes révélées par le test : capture, compréhension, reconstruction | Trois catégories de problèmes : redondantes avec CAP-367 et CAP-368. |
| k44 | Demande de prompt Cursor pour le test de reconstruction | Demande de prompt Cursor (reconstruction) : secondaire ; objectif abandonné (CAP-378). |
| k46 | Résultats vérifiés du commit 8b43fcc : 349 captures, 431 relations, validate ok, réciprocité à améliorer | Chiffres détaillés du commit 8b43fcc : verdict et commit conservés (CAP-368) ; à rouvrir si besoin. |
| k49 | Audit P0 - isolation de la reconstruction non démontrée (sources et reconstruction dans le même dépôt) | Isolation de la reconstruction : objectif de reconstruction abandonné (CAP-378). |
| k52 | Audit P1 - espace referentiel reçoit trop de propositions non validées (runs ref1, ref2, ref3) | Référentiel (runs de test) : constat sur runs de test ; la version production est captée (CAP-384 et CAP-385). |
| k53 | Relations inégales et trois registres indépendants : pas de liens inter-runs pour une mémoire transversale | Relations inégales (runs de test) : constat sur runs de test, non repris. |
| k54 | Audit de la reconstruction : restitution conceptuelle utile, statuts parfois faux | Évaluation des documents reconstruits : objectif abandonné (CAP-378). |
| k55 | Évaluation de la reconstruction : 6/10 pour la mémoire de conception, pas encore mémoire opérationnelle | Note 6/10 de la reconstruction : objectif abandonné (CAP-378). Sélection. |
| k56 | Priorités recommandées : fiabiliser la capture, puis Review et Search, puis reconstruction isolée | Priorités 0.1.4 : en partie couvertes par CAP-388 et CAP-390 ; sélection. |
| k60 | Rangement local : dossiers backup et test-runs déplacés dans des dossiers archive | Rangement local des archives : fait non vérifiable ; l'état local est signalé en CAP-381. |
| k65 | Convention : séparer conventions du moteur, conventions du projet et règles internes de Brain Capture | Séparation des trois niveaux de conventions : couverte par CAP-404 et CAP-381. |
| k67 | Conventions candidates (metadata, naming, provenance, lifecycle, atomicity, clickup) : seulement taxonomy.md pour commencer | Liste de conventions candidates : en partie couverte par CAP-380 ; reste de conception. |
| k69 | Test séquentiel proposé : clone isolé, registre vide, mode production, vérifier l'append-only sur trois captures | Protocole séquentiel en clone isolé : remplacé par la décision CAP-376. |
| k70 | Prompt Cursor correctif : audit local préalable obligatoire avant toute modification | Audit local préalable dans le prompt : consigne de prompt, couverte par CAP-376. |
| k74 | Audit 0.1.4 : 531 relations sans cible invalide, related représente près de la moitié | Relations de la production (531, related proche de la moitié) : constat chiffré non capturé ; à reprendre si besoin. |
| k79 | Limites de l'audit 0.1.4 : restitution non testée, pas de hashes intermédiaires, AUDIT-CUMUL absent | Limites de l'audit 0.1.4 : restitution non testée captée par CAP-383 ; hashes et AUDIT-CUMUL non captés. |
| k83 | Correctif 0.1.4.1 P0 : l'auteur est celui de l'information originale, et seule une expression explicite de l'utilisateur vaut approbation | Règles d'attribution 0.1.4.1 : redondantes avec CAP-384 et CAP-387. |
| k84 | Correctif 0.1.4.1 : ne pas réécrire les 350 captures, corriger les règles pour les captures suivantes | Contrainte « ne pas réécrire les 350 captures » : prompt ; principe append-only déjà au protocole. |
| k87 | Ce qui est indispensable selon l'assistant : provenance, historique, consolidation, récupération avec source | Éléments indispensables (avis) : partiellement couverts par CAP-390 et CAP-405. |
| k89 | Approche just-in-time proposée : cinq étapes de récupération de contexte par un agent | Just-in-time en cinq étapes : proposition d'usage, à rouvrir lors de Review/Search. |
| k102 | Documentation : cadrage.md facultatif, pas de sixième document obligatoire | cadrage.md facultatif : proposition remplacée par CAP-412 (évolution non reliée, k102 non capturé). |
| k105 | Documents impactés par cette réflexion : enrichir les documents propriétaires existants, pistes non validées | Pistes d'impact documentaires : non validées ; à rouvrir lors de la consolidation. |
| k106 | Pas de refonte immédiate : ajouter la source 4 sans modifier les trois autres, puis Review sur les quatre | Ordre d'étapes après la source 4 : partiellement couvert par CAP-405 et CAP-419. |

Relations abandonnées (cible exclue, non créées) : 11 (CAP-356->k12, CAP-357->k21, CAP-362->k34, CAP-368->k42, CAP-377->k52, CAP-378->k55, CAP-391->k87, CAP-392->k84, CAP-396->k67, CAP-402->k84, CAP-404->k102).


## Atomicité et richesse

- Splits : audit 0.1.3 origin / workflow (CAP-358, CAP-359) ; audit 0.1.4 en quatre constats (CAP-384 attribution, CAP-385 referentiel, CAP-386 composites, CAP-387 états d'approbation) ; décisions de l'utilisateur séparées de ses préférences (CAP-376, CAP-378, CAP-402 d'un côté ; CAP-413 de l'autre) ; exigence de cadrage séparée de l'exigence d'additivité (CAP-407, CAP-408).
- Captures liées : CAP-357 (demande d'audit 0.1.3) lié à CAP-382 (demande d'audit 0.1.4) et CAP-362 (audit du dernier push).
- Volume : 69 captures pour un repère 35 à 50. Justification : la source contient une longue suite de décisions explicites de l'utilisateur (0.1.3, 0.1.4, 0.1.4.1, 0.1.5), d'audits de production et de réflexions de cadrage, chacune portant une information distincte. Exclus : doublons de CAP déjà présentes, prompts Cursor, répétitions, détails de schéma. Le contrôleur peut retirer des lignes avant append.
- Incomplet signalé : relations de la production (531, dont related proche de la moitié) non captées ; hashes et AUDIT-CUMUL absents (constat non capturé) ; restitution non testée (partiellement captée, CAP-383) ; détails de schéma 0.1.3 ; procédure Test A détaillée (synthétisée par CAP-341 registre vivant et CAP-376).
- Champs non renseignés faute de source : origin.url = null partout ; clickup_ref et feeds_doc = null.

## Provenance et refs

- Locators : 76 au total, plages entre 1 et 4464, vérifiées. 6 captures ont plusieurs passages (grounding source_contextual).
- URLs : la source 4 ne contient aucune URL de page complète. Les seules chaînes de type domaine sont dans des liens d'icône (google s2 favicons), non conservés en tant que tels. Les domaines cités sont dans refs[] et dans content : platform.claude.com, aclanthology.org, help.openai.com, www.anthropic.com (CAP-390) ; www.francecompetences.fr, numerique.francetravail.fr, www.pmi.org (CAP-403) ; recrutement.creditmutuel.fr (CAP-410) ; promptotheque-dsfr-bebd50.gitlab-pages.din.developpement-durable.gouv.fr (CAP-412).
- Le lien ClickUp de la source 1 n'est pas dans la source 4 : il n'est pas recopié. CAP-371 signale seulement sa perte dans le run ref1, sans adresse.
- Commits et run : c8da3dc (CAP-363), 678c62a (CAP-383), 8b43fcc (CAP-368), run 20261030-220724 (CAP-364). Les trois commits existent dans l'historique local (git cat-file -t).

## Grounding, mapping, space, approbation

- intention vers type : conforme (validateur, 0 erreur). Répartition des types : observation 37, proposition 15, open_question 5, decision 5, task 4, convention 3.
- Anti-faux-explicit : 5 explicit_user_approval, toutes sur des décisions de l'utilisateur formulées sans ambiguïté (CAP-376, CAP-378, CAP-402, CAP-415, CAP-416), approval_scope item. Aucun set ni partial. Les formulations de l'assistant (Feu vert, Je valide, Direction validée en CAP-356, Oui à une question en CAP-367) ne sont pas converties en approbation. Les accords de l'utilisateur sur des citations de l'assistant (CAP-399, CAP-409) restent validation none.
- space : atelier 58, referentiel 4 (CAP-376, CAP-378, CAP-415, CAP-416), pilotage 7 (CAP-402 repassée de referentiel à pilotage).
- Position : proposed 30, favorable 13, selected 13, None 12, uncertain 1. Positions nulles : CAP-351, CAP-357, CAP-362, CAP-373, CAP-374, CAP-375, CAP-382, CAP-389, CAP-395, CAP-398, CAP-406, CAP-418.
- Grounding : source_explicit 63, source_contextual 6. Confidence : high 57, medium 12.
- author_confidence : medium 67, low 2. Basse : CAP-354, CAP-356.
- Validateur : REVIEW « position selected + explicit » sur les décisions de l'utilisateur (intentionnel). Pas d'approval_global_partial.

## Contradictions, tensions et relations

- Tension préservée : l'utilisateur veut beaucoup de documents standardisés (CAP-396) ; l'assistant mettait en garde contre leur multiplication (CAP-391). Relation related, sans trancher.
- Évolution : cadrage.md facultatif (proposition CAP-102 exclue) devient document standard (CAP-412, sans relation évolutive vers la proposition exclue).
- Décision de l'utilisateur sur le protocole (CAP-376) : evolves_from CAP-345 (registre vivant). Inbox : CAP-401 evolves_from CAP-086 (registre vivant). Aucun remplacement implicite.
- Relations : 107 au total (related 97, answered_by 3, evolves_from 4, answers 3). 11 relations vers des captures exclues abandonnées (liste ci-dessus).
- Les relations answers et evolves_from vers le registre vivant n'ont pas de réciproque possible (append-only) : avertissements acceptés.

## Corrections appliquées avant append

Lot de corrections demandé par l'humain, appliqué au brouillon (sauvegarde : entries.avant-corrections.jsonl) :
- CAP-411 : note parasite retirée de content (« Espace referentiel alors que la validation formelle n'est pas établie : la règle est formulée comme établie par l'utilisateur, à confirmer. »).
- CAP-415 : content ramené à « Décision de l'utilisateur : le fichier tasks.jsonl sera créé en même temps que Brain Review. » (deux phrases hors propos retirées).
- CAP-402 : space referentiel -> pilotage (étape de séquence). CAP-416 : relation related -> evolves_from vers CAP-402 (acceptée par le validateur, avertissement de réciproque seulement).
- Autres notes retirées : CAP-409, « , à confirmer » (fin de phrase ; « approbation formelle non établie » conservé, il décrit la source) ; CAP-419, « , à confirmer par l'utilisateur » (l'assistant ne demande pas de confirmation dans la source).
- Citations : 15 evidence réalignées mot pour mot sur la source (CAP-354, 356, 360, 361, 363, 366, 371, 381, 395, 398, 407, 409, 411 « enlever », 413, 419) et CAP-416 (`mon "Go"`). 0 capture retirée.

Corrections antérieures du brouillon :

- CAP-377 (périmètre du petit correctif) : explicit_user_approval retiré (demande de périmètre, pas approbation formelle d'items) ; validation none.
- Wording : suppression de « URL ClickUp » et de « lien fourni » (le validateur signale ces formulations sans URL littérale) dans CAP-371, CAP-379, CAP-383 ; remplacement par « adresse » ou « référence ».
- Relations réciproques ajoutées dans le lot : answered_by de CAP-373 vers CAP-380, CAP-375 vers CAP-381, CAP-398 vers CAP-403.
- Grounding source_contextual pour les captures à plusieurs passages ; confidence high si un passage court (30 lignes ou moins), medium sinon.

## Points à décider ou à relire par le contrôleur

1. Volume au-dessus du repère : accepter ou retirer des captures avant append.
2. Décisions CAP-376, CAP-378, CAP-402, CAP-415, CAP-416 : explicit_user_approval posé sur une formulation claire de l'utilisateur. À confirmer.
3. CAP-399 et CAP-409 : accords sur des formulations citées de l'assistant ; validation none retenue.
4. CAP-412 : la proposition cadrage.md facultatif (CAP-102 exclue) n'est pas reliée.
5. Le Go pour le prompt 0.1.5 n'est pas donné dans la source ; CAP-416 le note.

## Limites de méthode

- Les fenêtres de lecture ont été faites par tranches de 500 lignes (et non ~5 échanges user/assistant).
- Les 4 passes (informations, actionnable, relations, contexte/refs) n'ont pas été documentées séparément.
- Rédaction des captures par un worker haiku ; contrôle mécanique des citations ajouté après coup, jugement sémantique non refait.
- Évaluation humaine en attente.
