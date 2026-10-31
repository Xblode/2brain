import json, collections, pathlib
base = pathlib.Path("brain/registry/_capability-test")
for run in ["20261031-000600-ref1", "20261031-000600-ref2", "20261031-000600-ref3"]:
    p = base / run / "entries.jsonl"
    rows = []
    ids = set()
    dups = []
    bad = []
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            o = json.loads(line)
        except Exception as e:
            bad.append((i, str(e)))
            continue
        rows.append(o)
        if o.get("id") in ids:
            dups.append(o.get("id"))
        ids.add(o.get("id"))
    authors = collections.Counter(r.get("author") for r in rows)
    intentions = collections.Counter(r.get("intention") for r in rows)
    grounding = collections.Counter(r.get("grounding") for r in rows)
    validation = collections.Counter(r.get("validation") for r in rows)
    nrel = sum(len(r.get("relations") or []) for r in rows)
    short = [r["id"] for r in rows if len((r.get("content") or "")) < 40]
    no_loc = [r["id"] for r in rows if not ((r.get("origin") or {}).get("locators"))]
    missing_req = []
    req = [
        "id", "run_id", "capture_ref", "type", "intention", "position", "status",
        "space", "validation", "author", "author_confidence", "approved_by",
        "approval_scope", "title", "content", "evidence", "confidence", "grounding",
        "origin", "project", "created_at", "storage",
    ]
    for r in rows:
        for k in req:
            if k not in r:
                missing_req.append((r.get("id"), k))
        cref = f"{r.get('run_id')}:{r.get('id')}"
        if r.get("capture_ref") != cref:
            missing_req.append((r.get("id"), "capture_ref_mismatch"))
    idset = {r["id"] for r in rows}
    bad_rel = []
    for r in rows:
        for rel in r.get("relations") or []:
            if rel.get("to") not in idset:
                bad_rel.append((r["id"], rel))
    multi_topicish = [
        r["id"] for r in rows
        if (r.get("content") or "").count(";") >= 3 and len(r.get("content") or "") > 400
    ]
    print("RUN", run)
    print(" N", len(rows), "rels", nrel, "dups", dups, "json_bad", bad)
    print(" authors", dict(authors))
    print(" intentions", dict(intentions))
    print(" grounding", dict(grounding))
    print(" validation", dict(validation))
    print(" short_content_count", len(short), "sample", short[:15])
    print(" no_locators", no_loc)
    print(" missing_or_mismatch_count", len(missing_req), "sample", missing_req[:10])
    print(" bad_rel_count", len(bad_rel), "sample", bad_rel[:5])
    print(" long_multi_semicolon", multi_topicish[:15], "count", len(multi_topicish))
    print()
