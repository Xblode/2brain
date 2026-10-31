# FINAL_ASSESSMENT — Test de capacité Brain Capture 0.1.3

| | |
| --- | --- |
| Date | 2026-10-31 |
| Question | Une IA qui n’a que les captures peut-elle retrouver l’essentiel, comprendre l’évolution, et reconstruire assez pour poursuivre le développement ? |
| Captures | `20261031-000600-ref{1,2,3}` (349 CAP) |
| Reconstruction | `reconstruction-20261031/` |
| Audits | `PHASE2_VERIFICATION.md`, `PHASE4_COMPARATIVE_AUDIT.md` |

**Verdict court** : **partiellement**. Capture 0.1.3 conserve assez pour *raconter* Second Brain et son atelier Capture ; **pas assez** pour *reprendre* le développement comme un collègue qui connaît le dépôt et l’état livré.

---

## A. Résultats des captures

| Run | Source | CAP | Relations | User / Assistant | Validateur |
| --- | --- | --- | --- | --- | --- |
| `20261031-000600-ref1` | conversation-reference-1 | 117 | 165 | 49 / 68 | OK bloquant (16 WARN) |
| `20261031-000600-ref2` | conversation-reference-2 | 120 | 114 | 30 / 90 | OK bloquant (37 WARN) |
| `20261031-000600-ref3` | conversation-reference-3 | 112 | 152 | 21 / 91 | OK bloquant |

### Répartition intention (agrégée indicative)

Convention / orientation / suggestion / feedback / requirement / observation / question / task / milestone / decision / risk / preference / idea — densités élevées en **convention** (ref1/ref3) et **feedback/risk** (ref2).

### Grounding

Majoritairement `source_explicit` (~326/349) ; peu d’`uncertain` ; quelques `source_interpreted` (ref1).

### Validation

`explicit_user_approval` rare (6 / 6 / 12) ; reste en `none` — anti-faux-explicit **globalement respecté**.

### Localisateurs

Tous les CAP ont `origin.locators[]` non vides ; cohérence mécanique OK. Qualité sémantique des plages : variable (ex. CAP-036 sur une seule ligne multi-thèmes).

### Artefacts par run

`entries.jsonl`, `validate.json`, `AUDIT.md`, `COMPARISON.md`, `CAPTURE_NOTE.md` présents.

### Limite protocole Phase 1

Scripts temporaires de sérialisation utilisés puis retirés sur ref1/ref2 — écart au « skill-direct pur » noté ; JSONL final revalidé.

---

## B. Résultats de reconstruction

### Retrouvées correctement

- Vision / problème (vibecode, perte d’intentions, multi-chatbots).
- Séparation conceptuelle Brain-main / brain / ClickUp = visualiseur, local = SoT.
- Philosophie Capture vs Review vs Sync.
- Taxonomie intention / position / validation + `approval_global_partial`.
- Chronologie V1 → 0.1.1 → 0.1.2 → décision 0.1.3 ; abandons (045232, pause 0.1.2).
- Contradictions : B/C, Inbox, updates modules, « pas de 0.1.3 » puis faire 0.1.3.
- Roadmap 6 couches et 7 sujets de cadrage comme **ouverts / partiels**.
- Review = graphe (validé comme direction, hors scope Capture).

### Partiellement retrouvées

- Architecture Core/Modules/Instance (proposée, partiellement retenue).
- Table des commandes, pipeline, 4 espaces.
- Métriques des anciens test-runs (tendances OK, chiffres non vérifiables depuis CAP seules).
- Détails ops Inbox / onboarding / brief 500 mots.

### Perdues (source → CAP ou CAP → reconstruction)

- **URL ClickUp** (source L1277) absente de `ref1:CAP-087` malgré « lien fourni ».
- Naming / conventions projets web (source L22–23) mal porté.
- Grille des **6 risques** atomisés en CAP puis non remontés comme grille en reconstruction.
- Exemples Minecraft / Rust / CardCarousel dilués ou oubliés en docs reconstruits.
- Contenu réel des docs, code Skill, schéma filesystem — absents des sources (non pénalisable) mais **indispensables** pour développer.

### Mal interprétées

- `type: decision` / libellés « DÉCISION » sur orientations `validation: none` (B/C, updates, CAP-024).
- `space: referentiel` pour propositions non approuvées.
- CAP-086 formulation trop absolue vs hésitation source.

### Inventées

Peu de fiction de features. Biais dominant = **surclassement de statut**, pas invention d’architecture fantôme. Gaps documentés honnêtement.

### Fonctionnalités reconstruites vs impossibles

| Reconstruit (design) | Impossible depuis CAP seules |
| --- | --- |
| Rôle Capture / Review / Sync | Skill 0.1.3 livré + chemins `.cursor/skills/` |
| Fenêtres, 4 passes, audit | Validateur `--require-intention`, bilan template |
| Registre entries comme capture | État living `brain/registry/entries.jsonl` |
| ClickUp arbo conceptuelle | Sync API / IDs réels / URL folder |
| Modules type mods (décision) | Dossier Brain-main/ réel sur disque |

---

## C. Évaluation par axe (/10)

| Axe | Note | Justification |
| ---: | ---: | --- |
| **Couverture des informations** | **6.5** | Grands thèmes couverts (AUDITS OK) ; détails ops critiques perdus (URL ClickUp, naming web). |
| **Fidélité historique** | **8** | Chronologie versions, abandons, contradictions (045232, 0.1.3 vs « pas de refonte ») bien préservés et reconstruits. |
| **Qualité de l’attribution** | **7** | Auteurs user/assistant cohérents ; sources sans labels gérées ; déséquilibre assistant croissant reflète les sessions. |
| **Préservation nuances / approbations** | **6** | Anti-`explicit` réussi ; dérive via `type`/`space`/libellés reconstruction (« DÉCISION » sur orientations). |
| **Qualité des relations** | **5** | Intra-run utile (surtout ref3) ; ref2 très asymétrique ; **inter-runs nul** — 3 îlots. |
| **Autonomie des captures** | **7** | Contenus généralement compréhensibles hors source ; 2 CAP trop larges (ref3 CAP-009/096) ; fusions ponctuelles (CAP-036). |
| **Capacité de recherche** | **4** | Pas d’index métier ; collision CAP-NNN ; requête « règle Inbox actuelle ? » = grep + jugement humain. |
| **Capacité de reconstruction** | **6.5** | Excellent brief d’atelier ; mauvais inventaire produit ; Phase 3 nécessaire pour exploiter 349 CAP. |
| **Cohérence avec le dépôt actuel** | **3.5** | Concept aligné ; MVP Capture 0.1.3 + docs provisoires **non déductibles** ; risque confondre conçu et livré. |

**Moyenne indicative** ≈ **6.0 / 10** — mémoire de conception utilisable, pas encore mémoire opérationnelle de projet.

---

## D. Diagnostic des problèmes

| Problème | Catégorie | Exemple |
| --- | --- | --- |
| URL ClickUp non capturée | **Capture** | Source L1277 vs CAP-087 |
| Naming web non porté | **Capture** | Source L22–23 |
| `type: decision` sur orientation B/C | **Structure** | CAP-019 |
| Propositions en `space: referentiel` | **Structure** | CAP-023 et similaires |
| 6 risques non reliés en grille exploitable en reconstruction | **Relations** + **Reconstruction** | CAP-006…017 ref2 |
| Thèmes répétés ref1↔ref2 sans lien machine | **Relations** | 7 cadrages, 6 couches |
| CardCarousel / Minecraft absents des docs reconstruits | **Reconstruction** | CAP-013, CAP-036 présents mais non indexés |
| Sur-étiquetage « DÉCISION » en Phase 3 | **Reconstruction** | VISION §3, ARCH updates |
| Contenu Skill / docs / disque | **Source** (hors conversations) | Non pénalisable |
| AUDIT.md « couverture OK » trop optimiste | **Documentation** | vs PHASE4 axe 1 |
| Double taxonomie type × intention | **Structure** / **Documentation** | Lecteurs confondent statut |
| 349 CAP sans Search/Review | **Documentation** | Exploitation = re-synthèse |

---

## E. Verdict

### Brain Capture conserve-t-il suffisamment d’informations ?

**Oui pour la trajectoire et les principes ; non pour les détails opérationnels et l’état livré.** 0.1.3 n’est plus un trou noir (progrès net vs V1/0.1.1), mais « suffisamment » dépend de l’usage : *comprendre l’atelier* ≠ *continuer le code*.

### Les captures sont-elles exploitables sans les conversations originales ?

**Partiellement.** Une IA peut produire un brief fidèle (Phase 3 le montre). Elle ne peut pas répondre efficacement à des questions ponctuelles sans re-synthèse coûteuse, ni récupérer ce qui n’a pas été capturé (URL).

### Une IA peut-elle reconstruire l’architecture du projet ?

**L’architecture *conçue* : oui, avec nuances.**  
**L’architecture *du dépôt* : non.**

### Une IA peut-elle retrouver les décisions et leur historique ?

**Oui, mieux que sur les versions antérieures** — surtout les contradictions et remplacements. Attention au piège selected/orientation = décision.

### Le format actuel est-il suffisamment structuré ?

**Pour stocker : oui (0.1.3 valide).**  
**Pour retrouver et trancher le statut vivant : non** — manque index, relations inter-runs, discipline type/space, et couche Review.

### Trois problèmes les plus importants à corriger

1. **Perte de détails signalés comme précieux** (ex. URL ClickUp) — règle de capture « ne rien perdre » non tenue sur les ancres opérationnelles.
2. **Statut poreux** (`type`/`space`/lecture « DÉCISION ») malgré anti-`explicit` — le risque de déformation des intentions persiste à l’exploitation.
3. **Trois îlots sans Search/Review** — 349 CAP atomiques retombent en agrégat documentaire ; pas de graphe inter-conversations.

### Améliorer Capture, ou plutôt Review et Search ?

**Les deux, mais le levier critique pour *poursuivre le développement* est Review + Search (et relations inter-runs), pas seulement plus de CAP.**  
Capture doit encore corriger pertes de détails et statut (`type`/`space`) ; sans Review/Search, même une capture parfaite reste une archive difficile à interroger.

### Réponse à la question du test

> Une IA qui ne dispose que des captures peut-elle retrouver l’ensemble des informations importantes, comprendre l’évolution, et reconstruire assez pour poursuivre le développement ?

| Sous-question | Réponse |
| --- | --- |
| Ensemble des infos importantes | **Non** (détails ops + hors-sources dépôt) |
| Comprendre l’évolution | **Oui** |
| Reconstruire architecture/fonctionnalités *conçues* | **Oui, avec discipline** |
| Poursuivre le développement *du dépôt réel* | **Non sans le dépôt (ou captures post-implémentation)** |

**Note globale du système mémoire pour cet objectif : 5.5 / 10.**

---

## Limites de l’expérience

1. Captures déléguées à des agents (fenêtrage réel ~4–6 fenêtres) — possible under/over-segmentation vs process humain long.
2. Scripts de sérialisation temporaires (ref1/ref2) — écart protocole skill-direct.
3. Reconstruction et audit Phase 4 aussi délégués — la « séparation stricte » capture/reconstruction est simulée par consignes, pas par isolation machine totale.
4. Corpus = 3 conversations déjà centrées sur Second Brain / Capture — pas un test de généralisation (conforme au brief).
5. Pas de commit/push ; production non touchée.
