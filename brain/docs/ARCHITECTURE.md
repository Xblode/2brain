# Architecture

> **Provisoire** — synthèse légère issue de la capture. Détail : `brain/registry/entries.jsonl`.
> Sources : CAP-002, CAP-009, CAP-010, CAP-016, CAP-019, CAP-022–CAP-026, CAP-043–CAP-044, CAP-058.
> **Attention : références obsolètes.** Les `CAP-xxx` de ce document viennent de l'ancien registre de 69 captures (commit `45ba05d`). Le registre actuel réutilise ces numéros pour d'autres contenus : ne pas les y chercher. Pour les lire : `git show 45ba05d:brain/registry/entries.jsonl`.

## Brain / Brain-main (provisoire)

- **Brain/** : instance projet (connaissances, registres, état).
- **Brain-main/** : moteur (conventions, agents, skills, modules de référence).

## Directions retenues en atelier (≠ officielles figées)

- Socle universel + modules spécialisés — CAP-009.
- Quatre espaces logiques : Atelier, Référentiel, Journal, Pilotage — CAP-010.
- Core / Modules / Instance — CAP-024 ; modules type « mods » — CAP-023, CAP-025.
- Contrat d’information commun (type, origine, statut, relations…) — CAP-016.
- Agents spécialisés (+ orchestrateur en reco) — CAP-019.
- Historique des décisions conservé — CAP-022.

## Point non décidé : operating-model.md

1. Proposition initiale : document `operating-model.md` dédié — CAP-043.
2. Évolution : **ne pas** en faire un standard ; répartir vers `architecture.md` + `workflow.md` — CAP-044.
3. État actuel : **découpage non définitivement décidé** (à trancher en review).
