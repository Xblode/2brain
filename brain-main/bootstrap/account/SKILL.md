---
name: brain
description: Commande unique 2brain. État du projet et aide, installation (-i), mise à jour de brain-main (-u).
argument-hint: [-i | -u | -c | -s | -r]
disable-model-invocation: true
---

# /brain

Skill léger du compte. Il aiguille, il ne contient ni convention ni modèle : les conventions sont dans `brain-main/` du projet, les modèles dans le dépôt récupéré par `fetch-source.py`.

Arguments reçus : `$ARGUMENTS` (premier : `$0`).

## Règles

- **Pas d'écriture sans validation.** Aucune écriture dans le projet sans réponse explicite de l'utilisateur, donnée dans le message qui suit immédiatement la présentation du plan. Une approbation générale ou passée ne compte pas.
- **Jamais de simulation.** Ne jamais inventer le résultat d'une commande.
- **Sans Bash** (cas de l'orchestrateur du dépôt 2brain) : déléguer la commande exacte à l'agent `worker-sonnet` s'il existe, en lui donnant la commande telle quelle ; sinon dire clairement que la commande ne peut pas s'exécuter ici.
- Les scripts sont lancés avec `"__PYTHON__" -I <script>`. Leur sortie JSON se lit, elle ne se réécrit pas.

## Aiguillage

- **Vide** : lancer `"__PYTHON__" -I "${CLAUDE_SKILL_DIR}/status.py" --project "<dossier de travail>"`. Restituer l'état et rappeler : `-i` installer, `-u` mettre à jour brain-main/, `-c` `-s` `-r` prévus au lot 3. Lecture seule.
- **`-i`** : parcours d'installation ci-dessous.
- **`-u`** : parcours de mise à jour ci-dessous.
- **`-c`, `-s`, `-r`** : répondre que c'est prévu au lot 3 et pas encore construit. En attendant, la capture se fait en lisant `brain-main/skills/brain-capture/SKILL.md` s'il est présent.
- **Autre** : afficher l'aide (les cinq options ci-dessus).

## Parcours `-i`

1. `status.py --json`. Si `depot_source` est vrai : refuser. Si `brain-main/` ou `brain/` existe : présenter leur état et s'arrêter.
2. Analyser : type de projet, technologies, conventions et documentation existantes, d'après `status.py` et une lecture ciblée.
3. Poser les questions d'accueil : nature du projet, objectif, modules, outils, identité. Une réponse manquante ne bloque pas (valeur nulle). La réponse sur les modules note seulement une intention.
4. Récupérer la source : `"__PYTHON__" -I "${CLAUDE_SKILL_DIR}/fetch-source.py" --dest <dossier temporaire vide>`. Si le dépôt distant n'a pas encore le Bootstrap, relayer le message d'erreur et s'arrêter.
5. Préparer : `"__PYTHON__" -I <temp>/brain-main/bootstrap/scripts/prepare-install.py --source <temp>/brain-main --project <dossier de travail> --answers <json>` (`nature`, `objectif`, `modules`, `outils`, `identite`, chacun éventuellement nul).
6. Présenter : emplacement, arborescence, fichiers créés, conflits, adaptations proposées. Demander la validation.
7. Réponse explicite oui : `apply-install.py --project <dossier de travail> --plan-sha256 <valeur du résumé>` (même dossier `scripts/`). Réponse non : `cancel-install.py --project <dossier de travail>`, puis continuer normalement. Code 4 (conflit apparu) : redemander la validation après une nouvelle préparation.

## Parcours `-u`

1. Refuser dans le dépôt source (`status.py --json`, `depot_source`).
2. `fetch-source.py` vers un dossier temporaire vide.
3. `"__PYTHON__" -I <temp>/brain-main/bootstrap/scripts/update-brain-main.py --source <temp>/brain-main --project <dossier de travail>` : sans `--apply`, n'écrit rien et imprime le plan.
4. Présenter : versions, mises à jour, ajouts, suppressions, conflits (jamais écrasés), adaptations de `brain/` (signalées seulement).
5. Après validation explicite : même commande avec `--apply --plan-sha256 <valeur>`.
6. Rappeler que `-u` ne met pas à jour le compte : si `status.py` signale une version plus récente du Bootstrap, relancer `install-account.py`.
