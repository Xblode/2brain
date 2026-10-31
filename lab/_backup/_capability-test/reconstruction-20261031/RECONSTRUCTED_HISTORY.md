# Historique de développement (reconstruit)

> Chronologie **telle qu’elle apparaît dans les trois conversations-sources capturées** (ref1 ≈ conception initiale ; ref2 ≈ critique long terme + audits 0.1.1 + conception Capture ; ref3 ≈ 0.1.2 / audits / 0.1.3).  
> Les runs sont indépendants : les `id` CAP-NNN se répètent — toujours citer `capture_ref`.

## Phase A — Cadrage vision et moteur (ref1 / conversation-reference-1)

1. **Vision initiale** multi-chatbots + stack Skills/MCP/Rules/Agents.  
   `20261031-000600-ref1:CAP-001` · `CAP-002`
2. **Proposition** dossiers Brain / Brain-main + interfaces ClickUp etc.  
   `CAP-003`–`CAP-006` · `CAP-004`
3. **Constat** workflow chaotique ; exigences SoT locale, garde-fous, UX, générique multi-types projets.  
   `CAP-007`–`CAP-013`
4. **Méthode d’abord** (assistant) ; 3 questions A/B/C, ClickUp sync, socle+modules.  
   `CAP-015`–`CAP-018`
5. **Orientations user** B/C ; local SoT ; socle+modules.  
   `CAP-019`–`CAP-021`
6. **Propositions** 4 espaces, pipeline, commandes, contrat, couches registre.  
   `CAP-022`–`CAP-031`
7. **Orientations** capture auto sélective ; validation = proposition complète avant officiel (oppose reco auto-classer) ; agents spécialisés.  
   `CAP-035`–`CAP-037`
8. **Décisions explicites** : conflits solutions comparées ; historique décisions ; modules type mods.  
   `CAP-044`–`CAP-046`
9. **Architecture conceptuelle** Core/Modules/Instance ; onboarding ; updates modules.  
   `CAP-047`–`CAP-057`
10. **Bilan** : assez pour cadrage moteur, pas archi technique.  
    `CAP-059`–`CAP-065`
11. **Feedback user** « bonne base » (partial) sur espaces/pipeline/commandes/contrat + Core/modules + principes.  
    `CAP-066`–`CAP-068`
12. **ClickUp** arbo confirmée ; cadrage 7 sujets + roadmap 6 couches simulés.  
    `CAP-071`–`CAP-080` · `CAP-103`–`CAP-115`
13. **Workflow** capture/review ; docs candidats ; vision.md 100 % ; doutes operating-model/onboarding.  
    `CAP-074`–`CAP-100`
14. **Décision** ClickUp appliqué manuellement — ne rien ajouter.  
    `CAP-087`
15. **Mode atelier** poursuivi.  
    `CAP-116`–`CAP-117`

## Phase B — Viabilité long terme + Skill 0.1.1 (ref2 / conversation-reference-2)

1. **Événement** : implémentation « 1.1 » (capture) lancée sur Cursor.  
   `20261031-000600-ref2:CAP-001`
2. **Question** long terme ; réponse : concept solide, 6 risques, ordre de construction, 5 étapes.  
   `CAP-002`–`CAP-028`
3. **Audit test Skill v0.1.1** (run `20261030-045232`) : amélioration réelle, pas assez fiable.  
   `CAP-030`–`CAP-042`
4. **Re-audit** `20261030-061941` : vraie re-capture source ; progrès + P1/P2 restants.  
   `CAP-043`–`CAP-053`
5. **Reco assistant** V0.1.2 ciblée — **contredite** ensuite par user.  
   `CAP-054` ← `contradicted_by` `CAP-074`
6. **Précisions user** autonomie, multi-infos, fenêtres, approval_partial, ClickUp SoT local, filtrage bruit.  
   `CAP-055`–`CAP-073`
7. **Décisions** : pas de 0.1.2 tout de suite (mode conception) ; jeter 045232.  
   `CAP-074` · `CAP-075`
8. **Conception Capture** : taxonomies, fenêtres, registres, archive, Review/Sync.  
   `CAP-076`–`CAP-120`
9. **Décisions** : une intention principale ; Review local / Sync ClickUp ; archivage D.  
   `CAP-097` · `CAP-098` · `CAP-101`

## Phase C — V0.1.2, audits, bascule 0.1.3 (ref3 / conversation-reference-3)

1. **Décision** lancer conception V0.1.2 via prompt Cursor ; ajouter source 2 ; échantillons 1 vs 2.  
   `20261031-000600-ref3:CAP-001`–`CAP-003`
2. **Spec 0.1.2** (prompt assistant) : fenêtres, 4 passes, taxonomies, anti-agrégat, COMPARISON, scénarios A–H.  
   `CAP-004`–`CAP-032`
3. **Plan Cursor** partagé ; feedback favorable + 5 ajustements ; feu vert après précisions.  
   `CAP-033`–`CAP-044`
4. **Audit 180454** : progression structurelle ; P1 `_gen.py` ne prouve pas le Skill.  
   `CAP-045`–`CAP-055`
5. **Audit 184105** : sans `_gen.py` ; méthode crédible ; P1 explicit injustifiés persistent ; prêt sample 2.  
   `CAP-056`–`CAP-064`  
   *Orientation assistant « pas de refonte 0.1.3 » (`CAP-063`) — plus tard contredite.*
6. **Audit 194948** (sample 2) : succès structurel hors sample 1 ; P1 CAP-031 trop large.  
   `CAP-065`–`CAP-074`
7. **Feedback user** : lier propositions ; séparer captures ; signatures ; ne pas comparer CAP-N inter-sources ; sources 1–2 officielles.  
   `CAP-075`–`CAP-083`
8. **Architecture Review** graphe + hiérarchie : **validées user**.  
   `CAP-084`–`CAP-094`
9. **Décision** faire **0.1.3** avant cross-conversation (contredit `CAP-063`).  
   `CAP-095` · `CAP-097`
10. **Protocole test** Q1–Q5 répondues ; axes A–F 0.1.3 ; Tests A/B ; Capture seul, pas Review.  
    `CAP-096` · `CAP-100`–`CAP-111`

## Abandons / remplacements explicites

| Élément | Statut | Réf. |
|---------|--------|------|
| Test run `20261030-045232` | **Abandonné** (pas vraie re-capture) | `ref2:CAP-075` · `ref3:CAP-026` |
| « Faire 0.1.2 tout de suite » (pendant ref2) | **Remplacé** par mode conception | `ref2:CAP-074` vs `ref2:CAP-054` |
| Puis 0.1.2 est relancée | **Réactivée** en début ref3 | `ref3:CAP-001` |
| « Pas de refonte 0.1.3 » post-184105 | **Remplacé** par décision 0.1.3 | `ref3:CAP-063` vs `ref3:CAP-095` |
| Reco auto-classer après session | **Opposée** par user (proposition complète) | `ref1:CAP-033` vs `CAP-036` |
| Updates modules « proposées sans auto » | **Opposée** par auto brain-main | `ref1:CAP-052` vs `CAP-056` |
| Espace Inbox local (4 espaces) | **Nuancé / conflictuel** avec « pas d’inbox locale » | `ref1:CAP-023` vs `CAP-086` |
| Docs `operating-model` / `onboarding` standard | **En doute** ; reco assistant : ne pas standardiser | `ref1:CAP-090` · `CAP-097` |

## Versions Skill Capture évoquées

| Version | Événements capturés |
|---------|---------------------|
| « 1.1 » / V1.0 | Implémentation lancée ; baseline avant 0.1.1 |
| V0.1.1 | Audits 045232 (rejeté) / 061941 (baseline sémantique) |
| V0.1.2 | Spec + plan Cursor + runs 180454 / 184105 / 194948 |
| V0.1.3 | Décidée ; axes définis ; **non décrite comme livrée** dans les CAP |
