---
name: brain
description: Commande unique 2brain. État et aide, installation (-i), mise à jour de brain-main (-u), remplissage de brain/docs/ (-o), capture de la session (-c) ou d'un fichier (-c fichier), annulation de la dernière capture (-c 1), recherche (-s), Review en rapport seulement (-r).
argument-hint: [-i | -u | -o | -c | -c fichier | -c 1 | -s sujet | -r]
disable-model-invocation: true
---

# /brain

Skill léger du compte. Il aiguille, il ne contient ni convention ni modèle : les conventions et les mécanismes sont dans `brain-main/` du projet, les modèles dans le dépôt récupéré par `fetch-source.py`.

Arguments reçus : `$ARGUMENTS` (premier : `$0`).

## Règles

- **Pas d'écriture sans validation.** Aucune écriture dans le projet sans réponse explicite de l'utilisateur, donnée dans le message qui suit immédiatement la présentation du plan. Une approbation générale ou passée ne compte pas. `-o` écrit seulement ce que l'utilisateur valide, document par document. Exception : `-c` (hors `-c 1`) vaut demande d'écrire l'extrait puis d'ajouter au registre, par les scripts du skill de capture. `-s` et `-r` n'écrivent rien.
- **Jamais de simulation.** Ne jamais inventer le résultat d'une commande.
- **Sans Bash** (session orchestrateur, cas normal d'un projet installé : ni Bash, ni Write, ni Edit) : lancer la commande exacte par l'agent `worker-sonnet`, telle quelle, relire sa sortie brute et la restituer sans la réécrire ; sans cet agent, dire que la commande ne peut pas s'exécuter ici. Le worker ne voit pas la conversation : le brief donne tout, soit les commandes exactes avec l'identifiant de session `${CLAUDE_SESSION_ID}` déjà substitué, les chemins, le dossier de travail, le contenu validé mot pour mot, et le rappel que `brain/registry/entries.jsonl` est en append only. Questions, validation et jugement restent chez l'orchestrateur.
- **Autorisations expresses dans le brief** (`worker-sonnet` s'interdit sinon d'écrire dans `brain/registry/`, dans `.claude/` et de committer) : le brief **autorise expressément** l'écriture que la commande implique, et elle seule. `-c` et `-c <fichier>` : `brain/registry/` par `append-captures.py` et le staging prévu par le skill de capture, et `brain/sources/sessions/`. `-c 1` : le rollback par `rollback-captures.py`. `-i` : l'écriture de `.claude/` par `apply-install.py`, si le plan le prévoit. Le brief rappelle l'append only (ni réécriture, ni renumérotation) et interdit tout commit et tout push.
- Scripts : `"__PYTHON__" -I <script>`. Leur sortie se lit, elle ne se réécrit pas.
- Capturer n'est pas réduire le contexte : ne jamais lancer `/compact`.

## Aiguillage

- **Vide** : `"__PYTHON__" -I "${CLAUDE_SKILL_DIR}/status.py" --project "<dossier de travail>"`. Restituer l'état et rappeler les options `-i -u -o -c -s -r`. Si des documents contiennent encore « À compléter », suggérer `-o`. Lecture seule.
- **`-i`**, **`-u`** : parcours ci-dessous. **`-o`** : parcours `-o`. **`-c`**, **`-s`**, **`-r`** : parcours `-c`, `-s`, `-r`. **Autre** : afficher l'aide (options, une ligne chacune).

## Parcours `-i`

1. `status.py --json`. Si `depot_source` est vrai : refuser. Si `brain-main/` ou `brain/` existe : présenter leur état et s'arrêter.
2. Analyser : type de projet, technologies, conventions et documentation existantes, d'après `status.py` et une lecture ciblée.
3. Poser les questions d'accueil : nature du projet, objectif, modules, outils, identité. Une réponse manquante ne bloque pas (valeur nulle). La réponse sur les modules note seulement une intention.
4. `"__PYTHON__" -I "${CLAUDE_SKILL_DIR}/fetch-source.py" --dest <dossier temporaire vide>`. Si le dépôt distant n'a pas le Bootstrap, relayer l'erreur et s'arrêter.
5. `"__PYTHON__" -I <temp>/brain-main/bootstrap/scripts/prepare-install.py --source <temp>/brain-main --project <dossier de travail> --answers <json>` (`nature`, `objectif`, `modules`, `outils`, `identite`, chacun éventuellement nul).
6. Présenter : emplacement, arborescence, fichiers créés (dont `CLAUDE.md`, `AGENTS.md` et l'adaptateur `.claude/` du routeur s'ils sont absents ; s'ils existent ils ne sont jamais modifiés, y compris `.claude/settings.json`), conflits, adaptations, et le `routeur` (actif ou non, avec la raison). Demander la validation.
7. Oui explicite : `apply-install.py --project <dossier de travail> --plan-sha256 <valeur du résumé>` (même dossier `scripts/`). Non : `cancel-install.py --project <dossier de travail>`, puis continuer. Code 4 : redemander la validation après une nouvelle préparation.
8. Fin : afficher le bilan du script (fichiers posés, `CLAUDE.md`, `AGENTS.md` et `.claude/` créés ou non, `routeur`, adaptations à faire). Indiquer si le routeur est `actif à la prochaine conversation` ou `non activé` (et la raison), et dire de **démarrer une nouvelle conversation** pour que le contexte se charge. Proposer `/brain -o` pour remplir `brain/docs/`.

## Parcours `-u`

1. Refuser dans le dépôt source (`status.py --json`, `depot_source`). `fetch-source.py` vers un dossier temporaire vide.
2. `"__PYTHON__" -I <temp>/brain-main/bootstrap/scripts/update-brain-main.py --source <temp>/brain-main --project <dossier de travail>` : sans `--apply`, n'écrit rien et imprime le plan.
3. Présenter : versions, mises à jour, ajouts, suppressions, conflits (jamais écrasés), adaptations de `brain/` et de l'adaptateur (`adaptations_claude` : `.claude/` n'est pas modifié), signalées seulement. Après validation explicite : même commande avec `--apply --plan-sha256 <valeur>`.
4. `-u` ne met pas à jour le compte : si `status.py` signale un Bootstrap plus récent, relancer `install-account.py`.

## Parcours `-o`

Si `brain-main/` ou `brain/` est absent : dire de faire `/brain -i` et s'arrêter. Sinon `status.py --json`, puis suivre `brain-main/skills/brain-onboarding/SKILL.md`. Aucune écriture sans validation, même dans le dépôt source 2brain. Le registre et `brain-main/` ne sont pas modifiés.

## Parcours `-c`, `-s`, `-r`

Si `brain-main/` ou `brain/registry/entries.jsonl` est absent : dire de faire `/brain -i` et s'arrêter. Les chemins ci-dessous partent du dossier de travail.

- **`-c`** : `"__PYTHON__" -I brain-main/skills/brain-capture/scripts/read-session.py --session-id ${CLAUDE_SESSION_ID} --project "<dossier de travail>" --out-dir brain/sources/sessions`. Relayer le résumé : plages par rôle, retraits, masquages, dernier horodatage, avertissements. Code 3 : relayer le message et s'arrêter. Sinon suivre `brain-main/skills/brain-capture/SKILL.md` avec cet extrait pour source (`origin.source` = son chemin, `locators` = plages de lignes ; seul `[USER]` est humain), mode `production` sauf autre demande. Extraction utile et structurée, sans recopier de blocs entiers de conversation. Rappeler de relire l'extrait avant tout commit. Sous orchestrateur : le brief de `worker-sonnet` demande de suivre `brain-main/skills/brain-capture/SKILL.md`, avec l'extrait, le mode et les validations de l'utilisateur recopiés mot pour mot, et rappelle l'append only ; il dit de s'arrêter en `blocked` plutôt que d'inventer.
- **`-c <fichier>`** : vérifier que le fichier existe (sinon refuser), puis même skill de capture avec ce fichier pour source.
- **`-c 1`** : ne rien capturer. Lire le dernier `manifest.json` committed de `brain/registry/_capture-history/` et présenter ce qui sera annulé (ids, source, date). Après confirmation explicite : `"__PYTHON__" -I brain-main/skills/brain-capture/scripts/rollback-captures.py --n 1`, selon `brain-main/skills/brain-capture/references/rollback.md`. Refus du script : ne rien supprimer.
- **`-c` avec un autre argument** (ni `1`, ni fichier existant) : refuser.
- **`-s <sujet> [filtres]`** : `"__PYTHON__" -I brain-main/skills/brain-search/scripts/search-registry.py <mots> --project "<dossier de travail>" [filtres]` (`--help` liste les filtres). Restituer le résultat sans le réécrire, avec l'id et la validation de chaque entrée. Lecture seule.
- **`-r`** : `"__PYTHON__" -I brain-main/skills/brain-review/scripts/review-registry.py --project "<dossier de travail>"`. Présenter ensuite l'analyse comme des propositions à valider, fondées sur le rapport, avec ses limites. Aucune écriture, aucun changement de statut.
