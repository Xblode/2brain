# -*- coding: utf-8 -*-
"""One-shot recalibration living registry → 0.1.1 metadata/relations only."""
from __future__ import annotations

import json
import shutil
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\planc\Documents\_Projets\Perso\2brain")
REG = ROOT / "brain" / "registry"
ENTRIES = REG / "entries.jsonl"
SCHEMA = REG / "SCHEMA.md"
BACKUP = REG / "_backup"
BACKUP.mkdir(exist_ok=True)

stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
backup_entries = BACKUP / f"entries.jsonl.pre-brain-capture-0.1.1.{stamp}.jsonl"
backup_schema = BACKUP / f"SCHEMA.md.pre-brain-capture-0.1.1.{stamp}.md"

# SCHEMA may already be 0.1.1; still snapshot current + entries before correction
shutil.copy2(ENTRIES, backup_entries)
# Prefer pre-v1 schema if present for archival, else current
pre_v1 = BACKUP / "SCHEMA.md.pre-brain-capture-v1.md"
if pre_v1.exists() and not (BACKUP / "SCHEMA.md.pre-brain-capture-0.1.1-from-v1.md").exists():
    shutil.copy2(pre_v1, BACKUP / "SCHEMA.md.pre-brain-capture-0.1.1-from-v1.md")
shutil.copy2(SCHEMA, backup_schema)
print("backup_entries:", backup_entries)
print("backup_schema:", backup_schema)

entries = [json.loads(l) for l in ENTRIES.read_text(encoding="utf-8").splitlines() if l.strip()]
assert len(entries) == 69, len(entries)

integrity = {
    e["id"]: {"title": e["title"], "content": e["content"], "evidence": e["evidence"]}
    for e in entries
}

GLOBAL_PARTIAL = {"CAP-010", "CAP-014", "CAP-016", "CAP-024", "CAP-025", "CAP-041"}
EXPRESS_NOT_APPROVE = {"CAP-035", "CAP-036", "CAP-055"}
IMPLICIT_TO_NONE = {"CAP-005", "CAP-011", "CAP-040", "CAP-058", "CAP-061", "CAP-065"}

changes: list[dict] = []


def record(eid: str, field: str, old, new) -> None:
    if old != new:
        changes.append({"id": eid, "field": field, "old": old, "new": new})


for e in entries:
    eid = e["id"]
    old_val = e.get("validation")
    old_ab = e.get("approved_by")
    old_scope = e.get("approval_scope", "<missing>")
    old_tags = list(e.get("tags") or [])
    old_rels = deepcopy(e.get("relations") or [])

    if eid in GLOBAL_PARTIAL:
        e["validation"] = "none"
        e["approved_by"] = None
        e["approval_scope"] = None
        tags = list(e.get("tags") or [])
        if "approval_global_partial" not in tags:
            tags.append("approval_global_partial")
        e["tags"] = tags
    elif eid in EXPRESS_NOT_APPROVE:
        e["validation"] = "none"
        e["approved_by"] = None
        e["approval_scope"] = None
    elif eid in IMPLICIT_TO_NONE or old_val == "implicit":
        e["validation"] = "none"
        e["approved_by"] = None
        e["approval_scope"] = None
    elif old_val == "explicit_user_approval" and old_ab == "user":
        e["approval_scope"] = "item"
    elif old_val == "none":
        e["approved_by"] = None
        e["approval_scope"] = None
    else:
        e["approval_scope"] = None if old_val != "explicit_user_approval" else "item"

    if eid == "CAP-030":
        new_rels = []
        for r in e.get("relations") or []:
            if r.get("rel") == "conflicts_with" and r.get("to") == "CAP-063":
                new_rels.append({"rel": "resolves", "to": "CAP-063"})
            else:
                new_rels.append(r)
        e["relations"] = new_rels
    if eid == "CAP-063":
        e["relations"] = [
            r
            for r in (e.get("relations") or [])
            if not (r.get("rel") == "conflicts_with" and r.get("to") == "CAP-030")
        ]
    if eid == "CAP-042":
        e["relations"] = [
            r
            for r in (e.get("relations") or [])
            if not (r.get("rel") == "supersedes_candidate" and r.get("to") == "CAP-056")
        ]

    record(eid, "validation", old_val, e["validation"])
    record(eid, "approved_by", old_ab, e["approved_by"])
    record(eid, "approval_scope", old_scope, e["approval_scope"])
    if list(e.get("tags") or []) != old_tags:
        record(eid, "tags", old_tags, list(e.get("tags") or []))
    if e.get("relations") != old_rels:
        record(eid, "relations", old_rels, e.get("relations"))

assert len(entries) == 69
for e in entries:
    snap = integrity[e["id"]]
    assert e["title"] == snap["title"], e["id"]
    assert e["content"] == snap["content"], e["id"]
    assert e["evidence"] == snap["evidence"], e["id"]
    assert "approval_scope" in e

with ENTRIES.open("w", encoding="utf-8", newline="\n") as f:
    for e in entries:
        f.write(json.dumps(e, ensure_ascii=False, separators=(",", ": ")) + "\n")

val_changes = [c for c in changes if c["field"] == "validation"]
ab_changes = [c for c in changes if c["field"] == "approved_by"]
scope_changes = [c for c in changes if c["field"] == "approval_scope"]
tag_changes = [c for c in changes if c["field"] == "tags"]
rel_changes = [c for c in changes if c["field"] == "relations"]

summary = {
    "version": "0.1.1",
    "backup_entries": str(backup_entries.relative_to(ROOT)).replace("\\", "/"),
    "backup_schema": str(backup_schema.relative_to(ROOT)).replace("\\", "/"),
    "entries": 69,
    "change_records": len(changes),
    "counts": {
        "validation_changed": len(val_changes),
        "approved_by_changed": len(ab_changes),
        "approval_scope_changed": len(scope_changes),
        "tags_changed": len(tag_changes),
        "relations_changed": len(rel_changes),
    },
    "validation_changed": val_changes,
    "approved_by_changed": ab_changes,
    "approval_scope_changed": scope_changes,
    "tags_changed": tag_changes,
    "relations_changed": rel_changes,
    "all_changes": changes,
}
diff_path = BACKUP / "correction-diff-0.1.1.json"
diff_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

print("validation", Counter(e["validation"] for e in entries))
print("approval_scope", Counter(str(e["approval_scope"]) for e in entries))
print("approved_by", Counter(str(e["approved_by"]) for e in entries))
print("counts", summary["counts"])
print("diff:", diff_path)
