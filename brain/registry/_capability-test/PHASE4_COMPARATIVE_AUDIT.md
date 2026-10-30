# Phase 4 — Audit comparatif (capability test)

| | |
| --- | --- |
| Date | 2026-10-31 |
| Reconstruction figée | `brain/registry/_capability-test/reconstruction-20261031/` |
| Captures | `20261031-000600-ref{1,2,3}/` |
| Sources | `brain/sources/conversation-reference-{1,2,3}.txt` |
| Phase 2 | `PHASE2_VERIFICATION.md` |
| Dépôt confronté | `brain/docs/*`, `.cursor/skills/brain-capture/**`, `brain/registry/*` |

**Règle appliquée** : une absence n’est **pas** une faute si l’info n’est pas dans les conversations sources.  
**Méthode** : confrontation reconstruction ↔ CAP ↔ sources ↔ dépôt réel. Sans complaisance.

---

## Synthèse exécutive

La reconstruction Phase 3 est **honnête sur les gaps** et **bonne sur la trajectoire** (vision, contradictions, versions Capture, roadmap proposée). Elle **ne reconstitue pas** le dépôt réel (Skill 0.1.3 livré, arborescence, docs provisoires, validateur). Les captures 0.1.3 sont **techniquement solides** mais **perdent des détails exploitables** (URL ClickUp, naming web, risques long terme non remontés) et **polluent le statut** (`type: decision` / `space: referentiel` / libellés « DÉCISION » sur des orientations `validation: none`). Le graphe **intra-run** est utile ; le graphe **inter-runs** est inexistant — la reconstruction doit le inventer thématiquement.

**Verdict capacité « mémoire exploitable »** : **partielle**. Suffisante pour raconter *pourquoi* et *dans quel ordre* le projet a pensé Capture ; insuffisante pour reprendre le travail comme un collègue qui connaît le dépôt et l’état livré.

---

## Axe 1 — Infos dans les sources absentes des captures

### CAP (perte réelle)

| Manque | Source | Preuve capture | Gravité |
|--------|--------|----------------|---------|
| **URL folder ClickUp** | `conversation-reference-1.txt` L1277 (`https://app.clickup.com/90151633729/...`) | `ref1:CAP-087` : « Lien fourni vers le folder » ; `clickup_ref: null` ; URL absente du `content` | **Haute** — détail « à ne plus perdre » (L1275) justement perdu |
| **Convention naming / workflow projets web** | L22–23 (« projets web… workflow défini, conventionner, naming » + `agent.md` / `design.md`) | `COMPARISON.md` ref1 prétend une fusion dans CAP-013/009 ; **ni CAP-009 ni CAP-013** ne portent le naming web | **Moyenne** |
| **Exigence « me comprendre, mon workflow »** | L24 | Diluée dans CAP-001 (vision large) sans CAP dédiée | **Moyenne** |
| **Collage intégral prompt Cursor 0.1.2** | ref3 ~L6–683 | `AUDIT.md` ref3 : « Partiel — règles structurantes capturées ; pas une CAP par sous-paragraphe » | **Acceptable** (volume) mais des micro-règles ops peuvent manquer |

### Non-pénalisé (absent des sources)

- Texte intégral de `vision.md` / docs ClickUp — user valide le *document*, pas son contenu dans le chat.
- Code `SKILL.md` / `validate-registry.py` / inventaire filesystem — hors conversations.
- Résultats bruts des anciens `_test-runs` — seuls des *résumés d’audit* sont dans les sources (correctement noté dans `RECONSTRUCTION_GAPS.md` §1).

### Verdict axe 1

Couverture thématique large (AUDITS auto-OK) **≠** fidélité des détails opérationnels. Le cas Inbox/ClickUp URL est le contre-exemple le plus clair du brief user.

---

## Axe 2 — Capturées mais mal interprétées

| Cas | Problème | Preuve |
|-----|----------|--------|
| **`ref1:CAP-019`** | `type: decision` + `position: selected` pour « B **ou** C » non tranché ; `intention: orientation`, `validation: none` — OK sémantique intention, **mauvais type** | Source L94–98 ; CAP-019 ; reconstruction reprend pourtant « **DÉCISION** (orientation…) » (`RECONSTRUCTED_VISION.md` §3) |
| **`ref1:CAP-086`** | `grounding: source_interpreted` + formulation absolue « pas d’inbox locale » alors que la source hésite (« je n’aurais jamais… **je crois** ») | L1273–1275 vs content CAP-086 |
| **`ref1:CAP-036`** | Fusion dans une même CAP de (a) politique de validation référentiel, (b) exemple CardCarousel, (c) demande d’autres exemples | Source L331 (réponse multi-points) ; content CAP-036 |
| **`space: referentiel` + `validation: none`** | 15 CAP ref1 (ex. CAP-023 « Quatre espaces ») placées en référentiel alors que ce sont des propositions non approuvées | PHASE2 point 2 ; CAP-023 |
| **`ref3:CAP-024`** | `type: decision` / `intention: decision` alors que `position: proposed`, `validation: none` (périmètre assistant 0.1.2) | CAP-024 ; reconstruction ARCH §7 l’étiquette encore « **DÉCISION** » avec note contradictoire |

### Verdict axe 2

Anti-faux-`explicit` globalement respecté (peu d’`explicit_user_approval` abusifs). La dérive se fait via **`type` / `space` / libellés de reconstruction**, pas via `validation` — plus insidieuse.

---

## Axe 3 — Correctement capturées mais impossibles / difficiles à retrouver en reconstruction

| Info bien dans les CAP | Où dans la reconstruction ? | Problème |
|------------------------|----------------------------|----------|
| **6 risques long terme** `ref2:CAP-006`…`017` (dette mémoire, déformation IA, orchestration, maintenance, contrainte, outils) | `RECONSTRUCTED_HISTORY.md` : mention « 6 risques » sans liste ; 1–2 risques cités isolément dans VISION/ARCH | **Non reconstitués comme grille** |
| **Exemples multi-projets** Minecraft / Rust / auto-entreprise `ref1:CAP-013` | Absents de `RECONSTRUCTED_VISION.md` (seul « multi-projets » générique CAP-001) | Perte de concrétude |
| **CardCarousel / conflits composants** `ref1:CAP-036`/`038` | Non repris dans ARCH/VISION | Cas d’usage oublié |
| **Table ~11 commandes** `ref1:CAP-030` | Présente ARCH §5 / ROADMAP « proposé » | Retrouvable mais noyée |
| **Détails ops Inbox / brief 500 / fusion** (agrégat `ref2:CAP-052`) | GAPS §2.x ; pas d’unité claire | COMPARISON ref2 avoue le partial |

Les registres sont **navigables par ID**, pas par *question métier*. Sans savoir le `capture_ref`, « où est le risque orchestration ? » = grep manuel sur 120 lignes JSONL.

### Verdict axe 3

La reconstruction **synthétise** mieux qu’elle **indexe**. Ce qui est atomisé dans les CAP (forces 0.1.3) **retombe en agrégat** au moment de la mémoire documentaire.

---

## Axe 4 — Correctement reconstruites

Exemples solides (CAP → doc reconstruite fidèle, nuances conservées) :

1. **Problème / vision** — désordre chatbots, vibecode, perte d’intentions (`ref1:CAP-007`, `ref2:CAP-005`) → `RECONSTRUCTED_VISION.md` §1–2.
2. **Ambiguïté B/C** — taguée, non tranchée → VISION §3 + GAPS §2.2.
3. **Local = SoT / ClickUp visualiseur** — `ref1:CAP-020`, `ref2:CAP-068` → VISION + ARCH §3.
4. **Contradiction Inbox** Atelier vs pas d’inbox locale — `conflicts_with` CAP-023↔086 → ARCH §4 + GAPS §2.4.
5. **Chronologie versions / abandons** — jeter `045232`, pause puis relance 0.1.2, 0.1.3 contredit « pas de refonte » → `RECONSTRUCTED_HISTORY.md` + table abandons.
6. **Hiérarchie Capture→…→projets + Review = graphe** — `ref3:CAP-093`/`094` → ARCH §8 / ROADMAP.
7. **0.1.3 décidée, Review hors scope, Tests A/B non exécutés dans les CAP** — ROADMAP §4 + HISTORY versions.
8. **Discipline proposition vs décision** sur beaucoup de blocs (commandes, AGENTS.md, 6 couches = piste) + `RECONSTRUCTION_GAPS.md` lucide.

### Verdict axe 4

Cœur conceptuel et **histoire des décisions/contradictions** : **réussite nette** de la Phase 3 sous contrainte « CAP only ».

---

## Axe 5 — Inventées / extrapolées dans la reconstruction

| Élément | Statut |
|---------|--------|
| Contenu technique MCP / SQL final / arbo disque | **Non inventé** — listé en gaps |
| « Hybride B/C probable » | Explicitement **HYPOTHÈSE** (GAPS §2.2) — OK |
| « FAIT schéma observé dans les JSONL » (`grounding`…) | Meta-lecture des artefacts de test, **pas** du `content` métier — frontière grise, signalée |
| Élévation massive en « **DÉCISION** » d’orientations `validation: none` | **Sur-étiquetage narratif** (pas invention de faits, mais invention de *statut*) — voir axe 6 |
| Affirmer que 0.1.3 est **livrée** | **Évité** correctement |

Pas d’invention grossière de features fantômes. Le biais dominant est le **surclassement de statut**, pas la fiction.

---

## Axe 6 — Décisions historiques confondues avec propositions (ou inverse)

### Captures

- **Bien** : `explicit_user_approval` rare et souvent justifié (`ref1:CAP-044`–`046`, `071`, `087`, `089` ; `ref3:CAP-095`, `096`).
- **Mal** : 9 CAP ref1 en `type: decision` avec `validation: none` (CAP-019…057) — le schéma `type` contredit la taxonomie intention/validation.
- **Mal** : propositions assistant en `space: referentiel` (CAP-023, etc.).

### Reconstruction

| Libellé reconstruction | Réalité CAP | Jugement |
|------------------------|-------------|----------|
| « **DÉCISION** » mode B/C | orientation, ambiguous, none | **Trop fort** |
| « **DÉCISION** » updates auto brain-main | CAP-056 orientation + tag ambiguous + conflicts_with CAP-052 | **Trop fort** (orientation conflictuelle) |
| « **DÉCISION** » Review local / Sync | `ref2:CAP-098` (choix user clair) | **Juste** |
| « **DÉCISION (pour 0.1.2)** » entries.jsonl seul | CAP-024 proposed / none | **Confusion** (note correctrice insuffisante) |
| « bonne base » / partial → non verrouillé | ROADMAP §5 | **Juste** |

### Verdict axe 6

Le skill a progressé sur l’anti-`explicit` ; la **lecture humaine / reconstruction** réintroduit le piège « selected = décidé ». C’est exactement le risque `ref2:CAP-008`.

---

## Axe 7 — Fonctionnalités actuelles absentes de la reconstruction

**Non pénalisable si hors sources** — mais l’audit doit dire ce qu’une IA « CAP-only » **ne peut pas savoir** du dépôt réel :

| Réalité dépôt (2026-10-31) | Dans CAP / reconstruction ? |
|----------------------------|-----------------------------|
| Skill `.cursor/skills/brain-capture/` **version 0.1.3** livré (`SKILL.md`, 4 références, `validate-registry.py`) | Axes A–F **décidés/proposés** ; **pas** « livré / chemins / bilan template / ordre workflow strict » |
| Modes `production` vs `test-run` + forçage test sur `conversation-reference-*.txt` | Partiel (test-runs évoqués) ; **pas** le contrat opérationnel SKILL |
| `brain/registry/SCHEMA.md` + champs `author_confidence`, locators kinds, `--require-intention` | Grounding observé ; **schéma officiel non reconstruit** |
| `brain/docs/*` **provisoires** légers (vision/project/architecture/workflow/integrations) | Socle candidats `ref1:CAP-096` ; **pas** l’état « provisoire /brain-capture » ni les CAP living cités dans les docs |
| `brain/docs/README.md` standardisation V1 (5 docs obligatoires dont `requirements.md`, `locked: true`) | **Absent** des 3 sources → non pénalisable ; invisible à la reconstruction |
| Pas de dossier `Brain-main/` ni `AGENTS.md` à la racine | ARCH parle Brain-main conceptuel ; **écart disque non détectable** via CAP |
| Pas de skill `/brain-review` | Correctement hors scope 0.1.3 |
| Registre living `brain/registry/entries.jsonl` + historique `_test-runs/` | GAPS : « ne pas assumer production » — **juste**, donc état living inconnu |

### Verdict axe 7

Reconstruction = **mémoire de conception**, pas **inventaire produit**. Pour reprendre le code/skill, il faudrait le dépôt (ou une capture post-implémentation).

---

## Axe 8 — Fonctionnalités anciennes présentées à tort comme actuelles

| Risque | Observation |
|--------|-------------|
| Présenter 0.1.1 / runs `_gen.py` comme pratique courante | **Évité** — HISTORY/TESTS marquent 045232 abandonné, 180454 non crédible |
| Présenter 4 espaces / 11 commandes / orchestrateur comme archi live | **Majoritairement évité** (PROPOSITION / partial) |
| Présenter Capture auto « après chaque message » comme fait | ARCH/CAPTURE tracent l’**évolution** + risque skill≠auto (`ref1:CAP-101`) — **OK** |
| Présenter Review/Sync/graphe comme implémentés | ROADMAP : Review **hors scope** 0.1.3 — **OK** |
| Docs dépôt `workflow.md` qui citent encore « capture auto sélective / après chaque message » comme mode provisoire | État docs **en avance / flou** vs skill manuel `/brain-capture` — la reconstruction CAP-only est ici *plus prudente* que les docs light |

Peu de « vieux = actuel » dans la reconstruction figée. Le danger est plutôt **« conçu = déployé »** (axe 7).

---

## Axe 9 — Relations manquantes entre captures

### Intra-run

| Run | Relations | Réciprocité manquante (échant. answers/clarifies/contradicts/…) | Commentaire |
|-----|-----------|-----------------------------------------------------------------|-------------|
| ref1 | 165 | ~15 sur 53 arcs « spéciaux » | Tensions majeures liées (033↔036, 052↔056, 023↔086) |
| ref2 | 114 | ~32 / 40 | **Graphe le plus asymétrique** (PHASE2 : 37 WARN) |
| ref3 | 152 | ~0 / 45 | Meilleure discipline 0.1.3 |

`ref3:CAP-095` ↔ `CAP-063` (`contradicts`) : **excellent** signal d’évolution.

### Inter-runs

- **Aucune** relation native (contrat 0.1.3 : `relations[].to` local).
- Thèmes répétés sans lien machine : 7 sujets cadrage (`ref1:CAP-103`…`109` ↔ `ref2:CAP-112`…`118`) ; 6 couches roadmap ; philosophie Capture ref2→ref3.
- `capture_ref` prépare l’identité ; **Brain Review** (non livré) est requis pour en faire un graphe.
- Reconstruction HISTORY fait le lien **thématique** — utile, mais **non prouvable** comme relation CAP.

### Verdict axe 9

Mémoire = **3 îlots**. Exploitation cross-conversation = travail humain / Phase 3, pas propriété du registre.

---

## Axe 10 — Infos trop dispersées pour exploitation efficace

Facteurs cumulés :

1. **349 CAP** (117+120+112) pour 3 conversations — densité haute, signal dilué.
2. **Collision d’IDs** `CAP-NNN` → obligation permanente de `capture_ref`.
3. **Double taxonomie** `type` (0.1.1) × `intention` (0.1.3) — lecteurs reconstruisent mal le statut (axe 6).
4. **Même idée × N runs** sans index (cadrage, couches, Inbox).
5. **Reconstruction éclatée** en 6 fichiers + GAPS : bonne pour lecture humaine linéaire, mauvaise pour requête « quelle est la règle Inbox *actuelle* ? » (CAP-023 vs 086 vs 100 + docs integrations).
6. **Agrégats résiduels** : `ref3:CAP-096` (Q1–Q5), `ref2:CAP-052` (liste ops audit).

Résultat : un agent « reprise projet » doit soit **relire les sources**, soit **rejouer une Phase 3**. Les CAP seules ne sont pas encore une API de connaissance.

---

## Comparaison dépôt

Question : *l’IA n’ayant que les CAP (et la reconstruction) aurait-elle pu reconstruire… ?*

| Cible | Possible ? | Commentaire |
|-------|------------|-------------|
| **Architecture actuelle** | **Partielle (conceptuelle)** | Brain / Brain-main / ClickUp SoT : oui en intention. Disque réel = seulement `brain/` + `.cursor/skills/` : **non**. |
| **Features implémentées** | **Non** | Saurait que Capture est prioritaire et 0.1.3 *décidée* ; pas que le Skill 0.1.3, le validateur et le protocole de test sont **shippés**. |
| **Conventions** | **Partielle** | Taxonomies intention/position, fenêtres, anti-agrégat : oui. Standard doc V1 (`README.md`), `locked`, chemins skills : **non** (hors sources ou post-sources). |
| **Responsabilités agents / skills** | **Partielle** | Capture vs Review vs Sync bien séparés *en design*. Pas d’agents spécialisés réels ; `AGENTS.md` proposé (`ref1:CAP-098`) **absent du dépôt**. |
| **Fonctionnement réel Capture** | **Partielle** | Philosophie + fenêtres + 4 passes + audit final : oui. Ordre strict SKILL, bilan template, isolation `_capability-test` / `_test-runs`, flags validateur : **non**. |
| **Évolutions faites** | **Oui (récit)** / **Non (artefacts)** | Trajectoire V1→0.1.1→0.1.2→0.1.3 et défauts d’audit : oui. Contenu des `_test-runs` et diffs skill : non (volontairement hors CAP). |
| **Futures envisagées** | **Oui** | Tests A/B, Review graphe, registres spécialisés, sync ClickUp, modules, 6 couches : bien cartographiés comme ouverts/proposés. |

**Écart critique** : la reconstruction décrit un **atelier de conception abouti** ; le dépôt est un **MVP Capture 0.1.3 + docs provisoires**. Confondre les deux serait une erreur d’exploitation — et les CAP actuelles n’empêchent pas cette confusion sans discipline de lecture (statuts, gaps).

---

## Notes sur les AUDIT/COMPARISON de capture

Les `AUDIT.md` des trois runs déclarent une couverture « OK » quasi totale. Phase 2 avait prévenu : **ne pas confondre audit de capture et vérité**. Phase 4 confirme :

- OK **thématique** (les grands blocs sont représentés).
- Pas OK **granularité exploitable** (URL, naming, risques non indexés).
- Les COMPARISON sont plus honnêtes que les AUDIT (ref2 « Partiel » ops ; ref3 « Partiel » prompt).

---

## Scores indicatifs (0–5)

| Axe | Score | Lecture courte |
|-----|------:|----------------|
| 1 Absences source→CAP | 2.5 | Gros thèmes OK ; détails ops perdus |
| 2 Mal interprétées | 3 | Anti-explicit OK ; type/space/statut faibles |
| 3 CAP OK → reconstruite KO | 2.5 | Synthèse perd l’index atomique |
| 4 Correctement reconstruites | 4 | Vision/histoire/contradictions fortes |
| 5 Inventées | 4 | Peu de fiction ; sur-étiquetage |
| 6 Décision ↔ proposition | 2.5 | Piège récurrent malgré 0.1.3 |
| 7 Features actuelles absentes | n/a* | *Hors sources : écart dépôt majeur |
| 8 Ancien comme actuel | 4 | Prudence versions globalement bonne |
| 9 Relations manquantes | 2 | Intra inégal ; inter nul |
| 10 Dispersion | 2 | 349 CAP / 3 îlots / double taxonomie |

\*Pour l’axe 7, le score de *capacité mémoire* (savoir ce qui est live) est **1.5/5** si on juge l’objectif « reprendre le projet » ; **5/5** si on juge le respect de la règle « pas hors sources ».

---

## Conclusions Phase 4

1. **Capture 0.1.3** valide structurellement (Phase 2) et **couvre** les conversations — ce n’est plus le trou noir V1/0.1.1.
2. Elle **ne garantit pas** la conservation des détails que le user a explicitement signalés comme précieux (URL ClickUp).
3. La **reconstruction** est un bon **brief d’atelier** ; un mauvais **miroir du dépôt**.
4. Le prochain levier n’est pas seulement plus de CAP : c’est **Review / index / relations inter-runs / discipline de statut** — exactement le backlog déjà capturé mais non livré.
)
