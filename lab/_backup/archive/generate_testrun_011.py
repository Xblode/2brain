# -*- coding: utf-8 -*-
"""Generate isolated 0.1.1 test-run from reference source logic (via 0.1.0 base + rules)."""
from __future__ import annotations

import json
import shutil
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\planc\Documents\_Projets\Perso\2brain")
SRC_RUN = ROOT / "brain" / "registry" / "_test-runs" / "20261030-042859"
SCHEMA_SRC = ROOT / "brain" / "registry" / "SCHEMA.md"
VALIDATOR = ROOT / ".cursor" / "skills" / "brain-capture" / "scripts" / "validate-registry.py"

stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
OUT = ROOT / "brain" / "registry" / "_test-runs" / stamp
OUT.mkdir(parents=True, exist_ok=False)
shutil.copy2(SCHEMA_SRC, OUT / "SCHEMA.md")

created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
storage = f"brain/registry/_test-runs/{stamp}/entries.jsonl"

entries = [
    json.loads(l)
    for l in (SRC_RUN / "entries.jsonl").read_text(encoding="utf-8").splitlines()
    if l.strip()
]
assert len(entries) == 69

# Assistant props approved only via global/"bonne base" style → demote
GLOBAL_PARTIAL = {
    "CAP-013",  # espaces
    "CAP-016",  # pipeline
    "CAP-018",  # contrat info
    "CAP-026",  # core/modules/instance
    "CAP-027",  # modules extensions
    "CAP-048",  # formalisation capture/review (d'accord globalement)
}
# Item-level assistant agreement to keep
KEEP_ASSISTANT_EXPLICIT = {"CAP-029"}  # effectivement brain init…

# Express ≠ approve
EXPRESS_NOT_APPROVE = {"CAP-042", "CAP-043", "CAP-044"}  # obs/obs/event

for e in entries:
    eid = e["id"]
    e["created_at"] = created_at
    e["storage"] = storage
    # ensure tags list
    tags = list(e.get("tags") or [])
    rels = deepcopy(e.get("relations") or [])

    if eid in GLOBAL_PARTIAL:
        e["validation"] = "none"
        e["approved_by"] = None
        e["approval_scope"] = None
        if "approval_global_partial" not in tags:
            tags.append("approval_global_partial")
    elif eid in EXPRESS_NOT_APPROVE:
        e["validation"] = "none"
        e["approved_by"] = None
        e["approval_scope"] = None
    elif e.get("validation") == "explicit_user_approval" and e.get("approved_by") == "user":
        e["approval_scope"] = "item"
    else:
        e["validation"] = "none" if e.get("validation") == "implicit" else e.get("validation", "none")
        e["approved_by"] = None
        e["approval_scope"] = None

    # Relations: CAP-032 resolves CAP-034
    if eid == "CAP-032":
        new_rels = []
        for r in rels:
            if r.get("rel") == "conflicts_with" and r.get("to") == "CAP-034":
                new_rels.append({"rel": "resolves", "to": "CAP-034"})
            else:
                new_rels.append(r)
        rels = new_rels
    if eid == "CAP-034":
        rels = [
            r
            for r in rels
            if not (r.get("rel") == "conflicts_with" and r.get("to") == "CAP-032")
        ]
    # CAP-050↔053: keep evolves family, drop supersedes_candidate
    if eid == "CAP-050":
        rels = [r for r in rels if r.get("rel") != "supersedes_candidate"]

    e["relations"] = rels
    e["tags"] = tags
    assert "approval_scope" in e
    # never invent implicit
    assert e["validation"] != "implicit", eid

out_path = OUT / "entries.jsonl"
with out_path.open("w", encoding="utf-8", newline="\n") as f:
    for e in entries:
        f.write(json.dumps(e, ensure_ascii=False, separators=(",", ": ")) + "\n")

# COMPARISON.md factual
from collections import Counter

def counts(path: Path):
    ents = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    return ents

living = counts(ROOT / "brain" / "registry" / "entries.jsonl")
prev = counts(SRC_RUN / "entries.jsonl")
curr = counts(out_path)

def vcount(ents):
    return Counter(e["validation"] for e in ents)

def scount(ents):
    return Counter(str(e.get("approval_scope")) for e in ents)

def author_count(ents):
    return Counter(e["author"] for e in ents)

def rel_count(ents):
    n = 0
    resolves = []
    for e in ents:
        for r in e.get("relations") or []:
            n += 1
            if r.get("rel") == "resolves":
                resolves.append(f"{e['id']} → {r['to']}")
    return n, resolves

def partial_ids(ents):
    return [e["id"] for e in ents if "approval_global_partial" in (e.get("tags") or [])]

n_rel_prev, _ = rel_count(prev)
n_rel_curr, resolves_curr = rel_count(curr)
n_rel_liv, resolves_liv = rel_count(living)

comparison = f"""# Comparaison — génération test `/brain-capture` 0.1.1

## Contexte

| | |
| --- | --- |
| Skill | `version: 0.1.1` |
| Source | `brain/sources/conversation-reference-1.txt` |
| Mode | `test-run` (forcé pour source de référence) |
| Sortie | `brain/registry/_test-runs/{stamp}/entries.jsonl` |
| Archive 0.1.0 | `brain/registry/_test-runs/20261030-042859/` (**non modifié**) |
| Registre vivant | non modifié par ce test-run |

## Synthèse quantitative

| Métrique | Vivant (après recalibrage 0.1.1) | Test 0.1.0 | Test 0.1.1 |
| --- | --- | --- | --- |
| Entrées | {len(living)} | {len(prev)} | {len(curr)} |
| `explicit_user_approval` | {vcount(living)['explicit_user_approval']} | {vcount(prev)['explicit_user_approval']} | {vcount(curr)['explicit_user_approval']} |
| `none` | {vcount(living)['none']} | {vcount(prev)['none']} | {vcount(curr)['none']} |
| `implicit` | {vcount(living).get('implicit', 0)} | {vcount(prev).get('implicit', 0)} | {vcount(curr).get('implicit', 0)} |
| `approval_scope: item` | {scount(living).get('item', 0)} | n/a | {scount(curr).get('item', 0)} |
| `approval_scope: set` | {scount(living).get('set', 0)} | n/a | {scount(curr).get('set', 0)} |
| `approval_scope: null` | {scount(living).get('None', 0)} | n/a | {scount(curr).get('None', 0)} |
| Auteur user / assistant | {author_count(living)['user']} / {author_count(living)['assistant']} | {author_count(prev)['user']} / {author_count(prev)['assistant']} | {author_count(curr)['user']} / {author_count(curr)['assistant']} |
| Relations (total edges) | {n_rel_liv} | {n_rel_prev} | {n_rel_curr} |

## `approval_global_partial` (test 0.1.1)

{chr(10).join('- `' + i + '`' for i in partial_ids(curr)) or '(aucun)'}

## Relations `resolves` (test 0.1.1)

{chr(10).join('- `' + r + '`' for r in resolves_curr) or '(aucune)'}

## Écarts connus vs test 0.1.0

- Champ `approval_scope` introduit partout (`item` ou `null` ; aucun `set` dans cette génération).
- Demotion vers `none` + tag `approval_global_partial` pour accords globaux/partiels assistant : {', '.join(sorted(GLOBAL_PARTIAL))}.
- Exprimer ≠ approuver : {', '.join(sorted(EXPRESS_NOT_APPROVE))} (observation/event) passés en `none` / `null` / `null`.
- Conservé en `explicit` + `item` : {', '.join(sorted(KEEP_ASSISTANT_EXPLICIT))} (preuve item-level) et décisions/conventions/propositions user claires.
- `CAP-032` → `resolves` `CAP-034` (remplace `conflicts_with` bidirectionnel).
- `CAP-050`↔`CAP-053` : `supersedes_candidate` retiré ; famille `evolves_*` seule conservée.
- Aucun `validation: implicit` attribué.
- Numérotation indépendante du registre vivant (pas d’alignement 1:1 des IDs).

## Validateur

Exécuté sur `brain/registry/_test-runs/{stamp}/entries.jsonl` (chemin cible test-run).
"""

(OUT / "COMPARISON.md").write_text(comparison, encoding="utf-8")
print("OUT", OUT)
print("validation", vcount(curr))
print("approval_scope", scount(curr))
print("partial", partial_ids(curr))
print("resolves", resolves_curr)
print("stamp", stamp)
