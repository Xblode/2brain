---
metadata_version: 1
title: Adaptateur Claude Code de l'Agent Router
description: Décrit la correspondance entre les profils de l'Agent Router et les agents Claude Code, leurs limites vérifiées et la procédure de test.
version: "0.1.2"
status: draft
created: "2026-11-05"
updated: "2026-11-06"
type: reference
scope:
  level: domain
  targets: [claude-code]
depends_on:
  - "brain-main/ROUTER.md"
updated_from:
  - "https://code.claude.com/docs/en/sub-agents.md"
  - "https://code.claude.com/docs/en/model-config.md"
  - "https://code.claude.com/docs/en/permission-modes.md"
---

# Adaptateur Claude Code

Cet adaptateur applique `brain-main/ROUTER.md`. Les règles (rôles, sélection, brief, rapport, contrôle, trace) n'y sont pas recopiées : voir ce document. Les résultats des tests de la section « Vérification » ne sont pas consignés ici ; l'état réel (non vérifié en session réelle) est dans `brain-main/adapters/claude-code/README.md`.

## Correspondance

| Profil | Agent | Modèle |
| --- | --- | --- |
| `strategic` | `orchestrator` | `opus` |
| `standard` | `worker-sonnet` | `sonnet` |
| `light` | `worker-haiku` | `haiku` |

## Outils

| Agent | `tools` |
| --- | --- |
| `orchestrator` | `Read, Grep, Glob, Agent(worker-sonnet, worker-haiku), SendMessage, TaskStop, AskUserQuestion` |
| `worker-sonnet` | `Read, Grep, Glob, Edit, Write, Bash` |
| `worker-haiku` | `Read, Grep, Glob, Edit, Bash` |

- Workers : `omitClaudeMd: true`, `disallowedTools: mcp__*`, sans `Agent` ni `SendMessage`.
- `worker-haiku` n'a pas `Write` : créer un fichier demande un jugement, donc le profil `standard`.
- L'orchestrateur n'a pas de mode plan : ce mode exige d'écrire un fichier de plan. Les plans sont présentés dans la conversation et validés par `AskUserQuestion`.
- `settings.json` : `{"agent": "orchestrator"}` seulement, sans `permissions.deny` (clé active). Aucun hook, plugin, MCP, skill, Agent Teams ni dépendance : cette phrase concerne cet adaptateur des agents, pas le Bootstrap (documenté dans `brain-main/bootstrap/README.md`).

## Ce que `model` ne garantit pas

L'ordre documenté est : paramètre `model` de l'appel, puis frontmatter, puis `CLAUDE_CODE_SUBAGENT_MODEL`, puis modèle du parent. L'orchestrateur pourrait donc surcharger un worker, y compris vers Opus. `availableModels` limite l'ensemble mais ne lie pas un worker à un modèle, et Opus doit y rester. `deniedModels` est réservé aux managed settings. L'effet de `/model` sur l'agent de session n'est pas documenté. V1 : consigne de ne jamais passer `model`, et contrôle dans la mesure.

## Version cible

Claude Code 2.1.317 ou plus (version embarquée dans Desktop). Le CLI du PATH est en 2.1.22 : à mettre à jour avant tout usage en terminal.

## Limites de la V1

1. `Bash` chez les workers contourne les `deny` (écriture dans `.claude/`, `git commit`). Seules la consigne et le mode de permission s'y opposent, les hooks étant exclus. Le `deny` bloque aussi une session ordinaire : `.claude/` se modifie alors à la main ou après retrait temporaire de l'interdiction.
2. Modèles non verrouillés par worker (voir plus haut).
3. Trois points non documentés, à tester : prise en charge de `agent` par Desktop, `Agent(a, b)` avec le setting (documenté pour `--agent`), MCP chez un subagent en arrière-plan (la doc dit qu'il les garde, d'où `disallowedTools`).
4. Le worker ne peut pas interroger l'orchestrateur en cours de mission : il s'arrête, et la reprise a un coût.
5. Claude Code conserve les transcriptions des subagents dans `~/.claude/`, hors du dépôt. La règle « pas de raisonnement interne » vaut pour le Second Brain, pas pour ces fichiers.
6. Le prompt de l'orchestrateur remplace le prompt par défaut : perte possible de consignes natives. Les outils propres à Desktop (liste de tâches, etc.) peuvent aussi disparaître de sa liste blanche.
7. Un routeur par défaut modifie les conditions du test de reprise de la remise à niveau : à signaler lors de la comparaison avec la mesure de départ.
8. CLI 2.1.22 : comportement inconnu avec cette configuration, probablement un orchestrateur sans délégation.

## Vérification

À faire avant d'activer la clé `agent`. Résultats non encore consignés.

| Test | Attendu |
| --- | --- |
| Orchestrateur : demander une écriture, une commande | Refus par absence d'outil, délégation proposée |
| Orchestrateur : appeler `Explore` ou un autre agent | Impossible ; sinon, repli natif `permissions.deny` sur `Agent(nom)` |
| Workers : tenter un subagent | Impossible |
| Modèle effectif de chaque agent | `opus`, `sonnet`, `haiku` dans les métadonnées de sortie |
| Worker en arrière-plan : lister les outils MCP | Aucun |
| Worker `blocked`, puis reprise avec `SendMessage` | Reprise avec son historique ; vérifier si `ToolSearch` est nécessaire à l'orchestrateur |
| Worker : écrire dans `.claude/` avec `Edit` | Refusé par `deny` |
| Parallèle, deux workers en arrière-plan | Pas de blocage sur une demande de permission |
| Front matter METADATA dans les agents | Agents chargés sans erreur |
| `python brain-main/skills/brain-capture/scripts/validate-registry.py brain/registry/entries.jsonl` et `git status` | Registre intact |
| Nouvelle session Desktop avec la clé `agent` | Opus orchestrateur au démarrage ; `/status` confirme |

Si Claude Code refuse les champs de métadonnées ajoutés au front matter des agents, une exception sera documentée (METADATA §10.1).

## Retour arrière

Retirer la clé `agent` de `settings.json` rend le comportement antérieur.

## Exception de nommage

- **Règle concernée** : NAMING §2.1 (nommer selon le concept et la responsabilité, ici le profil plutôt que le modèle).
- **Périmètre** : `.claude/agents/` uniquement (`worker-sonnet`, `worker-haiku`).
- **Justification** : les noms portent le modèle à la demande de l'humain (NAMING §11.3).
- **Comportement attendu** : si le modèle d'un profil change, le nom du fichier est réexaminé ; l'exception ne s'étend à aucun autre dossier.

## Maintenance de `.claude/`

Le `deny` sur `.claude/**` bloque les modifications par les agents (voir Limites, point 1). Pour modifier ces fichiers : à la main, ou après retrait temporaire de l'interdiction dans `settings.json`, puis rétablissement.
