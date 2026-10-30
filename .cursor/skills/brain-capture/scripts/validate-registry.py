#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validateur déterministe du registre Brain (lecture seule).

Ne modifie jamais les entrées. Catégories : errors / warnings / human_review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ALLOWED_TYPES = {
    "idea",
    "observation",
    "proposition",
    "decision",
    "convention",
    "task",
    "open_question",
    "event",
}
ALLOWED_STATUS = {"extracted"}
ALLOWED_SPACES = {"atelier", "referentiel", "journal", "pilotage"}
ALLOWED_VALIDATION = {"none", "implicit", "explicit_user_approval"}
ALLOWED_AUTHOR = {"user", "assistant"}
ALLOWED_APPROVED_BY = {"user", None}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_REL = {
    "related",
    "evolves_from",
    "evolves_to",
    "answers",
    "answered_by",
    "conflicts_with",
    "supersedes_candidate",
    "parent_of",
    "child_of",
}
FORBIDDEN_REL = {"feeds_doc", "refers_clickup"}
REQUIRED_FIELDS = {
    "id",
    "type",
    "status",
    "space",
    "validation",
    "author",
    "approved_by",
    "title",
    "content",
    "evidence",
    "confidence",
    "origin",
    "project",
    "created_at",
    "storage",
}
KNOWN_FIELDS = REQUIRED_FIELDS | {"relations", "clickup_ref", "feeds_doc", "tags"}
ID_RE = re.compile(r"^CAP-\d{3,}$")
CAP_TARGET_RE = re.compile(r"^CAP-\d{3,}$")


def is_iso_datetime(value: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    candidates = [value]
    if value.endswith("Z"):
        candidates.append(value[:-1] + "+00:00")
    for c in candidates:
        try:
            datetime.fromisoformat(c)
            return True
        except ValueError:
            continue
    return False


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.human_review: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def review(self, msg: str) -> None:
        self.human_review.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_entries(path: Path, report: Report) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        report.warn("Fichier vide.")
        return entries
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            report.warn(f"Ligne {i}: ligne vide ignorée.")
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            report.error(f"Ligne {i}: JSON invalide ({exc}).")
            continue
        if not isinstance(obj, dict):
            report.error(f"Ligne {i}: l'entrée doit être un objet JSON.")
            continue
        entries.append(obj)
    return entries


def validate_entry(
    entry: dict[str, Any],
    line_no: int,
    ids: set[str],
    report: Report,
) -> None:
    eid = entry.get("id", f"<ligne {line_no}>")

    unknown = set(entry.keys()) - KNOWN_FIELDS
    if unknown:
        report.error(f"{eid}: champs inconnus: {sorted(unknown)}")

    for field in REQUIRED_FIELDS:
        if field not in entry:
            report.error(f"{eid}: champ obligatoire manquant: {field}")

    if "id" in entry:
        if not isinstance(entry["id"], str) or not ID_RE.match(entry["id"]):
            report.error(f"{eid}: id doit matcher CAP-NNN.")
        elif entry["id"] in ids:
            report.error(f"{eid}: id dupliqué.")
        else:
            ids.add(entry["id"])

    def check_enum(field: str, allowed: set[Any]) -> None:
        if field not in entry:
            return
        if entry[field] not in allowed:
            report.error(f"{eid}: {field}={entry[field]!r} non autorisé.")

    check_enum("type", ALLOWED_TYPES)
    check_enum("status", ALLOWED_STATUS)
    check_enum("space", ALLOWED_SPACES)
    check_enum("validation", ALLOWED_VALIDATION)
    check_enum("author", ALLOWED_AUTHOR)
    check_enum("confidence", ALLOWED_CONFIDENCE)

    if "approved_by" in entry and entry["approved_by"] not in ALLOWED_APPROVED_BY:
        report.error(f"{eid}: approved_by={entry['approved_by']!r} non autorisé (user|null).")

    for text_field in ("title", "content", "evidence", "project", "storage"):
        if text_field in entry and not isinstance(entry[text_field], str):
            report.error(f"{eid}: {text_field} doit être une string.")
        elif text_field in entry and not entry[text_field].strip():
            report.error(f"{eid}: {text_field} ne doit pas être vide.")

    if entry.get("status") != "extracted":
        report.error(f"{eid}: status doit être 'extracted' pour une capture.")

    if "created_at" in entry and not is_iso_datetime(entry["created_at"]):
        report.error(f"{eid}: created_at n'est pas une date ISO valide.")

    origin = entry.get("origin")
    if origin is not None:
        if not isinstance(origin, dict):
            report.error(f"{eid}: origin doit être un objet.")
        else:
            if "source" not in origin or not isinstance(origin.get("source"), str):
                report.error(f"{eid}: origin.source (string) obligatoire.")
            if "url" in origin and origin["url"] is not None and not isinstance(origin["url"], str):
                report.error(f"{eid}: origin.url doit être string ou absent.")

    # author / approved_by / validation coherence
    validation = entry.get("validation")
    approved_by = entry.get("approved_by")
    if validation == "explicit_user_approval" and approved_by != "user":
        report.error(
            f"{eid}: validation=explicit_user_approval exige approved_by=user "
            f"(reçu {approved_by!r})."
        )
    if validation in ("none", "implicit") and approved_by not in (None,):
        report.error(
            f"{eid}: validation={validation} exige approved_by=null (reçu {approved_by!r})."
        )
    if validation == "implicit":
        report.review(
            f"{eid}: validation=implicit (historique) — réexaminer la preuve avant conversion."
        )

    # space soft checks
    if entry.get("type") == "task" and entry.get("space") not in ("pilotage", "atelier"):
        report.warn(f"{eid}: type=task habituellement dans pilotage ou atelier.")
    if entry.get("space") == "referentiel" and validation != "explicit_user_approval":
        report.review(
            f"{eid}: space=referentiel sans explicit_user_approval — vérifier le placement."
        )

    # optional fields types
    if "relations" in entry and entry["relations"] is not None:
        if not isinstance(entry["relations"], list):
            report.error(f"{eid}: relations doit être une liste.")
    if "tags" in entry and entry["tags"] is not None and not isinstance(entry["tags"], list):
        report.error(f"{eid}: tags doit être une liste.")
    if "clickup_ref" in entry and entry["clickup_ref"] is not None and not isinstance(
        entry["clickup_ref"], str
    ):
        report.error(f"{eid}: clickup_ref doit être string ou null.")
    if "feeds_doc" in entry and entry["feeds_doc"] is not None and not isinstance(
        entry["feeds_doc"], str
    ):
        report.error(f"{eid}: feeds_doc doit être string ou null.")


def validate_relations(
    entries: list[dict[str, Any]],
    report: Report,
) -> None:
    by_id = {e["id"]: e for e in entries if isinstance(e.get("id"), str)}
    all_ids = set(by_id)

    for entry in entries:
        eid = entry.get("id", "?")
        relations = entry.get("relations") or []
        if not isinstance(relations, list):
            continue
        for idx, rel in enumerate(relations):
            if not isinstance(rel, dict):
                report.error(f"{eid}: relations[{idx}] doit être un objet.")
                continue
            r = rel.get("rel")
            to = rel.get("to")
            if r in FORBIDDEN_REL:
                report.error(
                    f"{eid}: rel={r!r} interdit dans relations "
                    f"(utiliser feeds_doc / clickup_ref)."
                )
            elif r not in ALLOWED_REL:
                report.error(f"{eid}: rel={r!r} non autorisé.")
            if not isinstance(to, str):
                report.error(f"{eid}: relations[{idx}].to doit être une string.")
                continue
            if not CAP_TARGET_RE.match(to):
                report.error(
                    f"{eid}: cible de relation non-capture {to!r} "
                    f"(documents/ClickUp interdits dans relations)."
                )
            elif to not in all_ids:
                report.error(f"{eid}: relation vers capture inexistante {to}.")

    # soft reciprocal checks
    def has_rel(src: str, rel: str, dst: str) -> bool:
        e = by_id.get(src)
        if not e:
            return False
        for r in e.get("relations") or []:
            if isinstance(r, dict) and r.get("rel") == rel and r.get("to") == dst:
                return True
        return False

    pairs = [
        ("answered_by", "answers"),
        ("answers", "answered_by"),
        ("evolves_from", "evolves_to"),
        ("evolves_to", "evolves_from"),
        ("parent_of", "child_of"),
        ("child_of", "parent_of"),
    ]
    seen: set[tuple[str, str, str]] = set()
    for entry in entries:
        eid = entry.get("id")
        if not eid:
            continue
        for r in entry.get("relations") or []:
            if not isinstance(r, dict):
                continue
            rel, to = r.get("rel"), r.get("to")
            if rel == "conflicts_with" and isinstance(to, str) and to in all_ids:
                if not has_rel(to, "conflicts_with", eid):
                    report.warn(
                        f"{eid}: conflicts_with → {to} sans réciproque "
                        f"(recommandé mais non bloquant)."
                    )
            for a, b in pairs:
                if rel == a and isinstance(to, str) and to in all_ids:
                    key = (min(eid, to), max(eid, to), a)
                    if key in seen:
                        continue
                    seen.add(key)
                    if not has_rel(to, b, eid):
                        report.warn(
                            f"{eid}: {a} → {to} sans réciproque {b} "
                            f"(recommandé si les deux côtés sont connus)."
                        )


def validate_registry(path: Path) -> Report:
    report = Report()
    if not path.exists():
        report.error(f"Fichier introuvable: {path}")
        return report
    entries = load_entries(path, report)
    ids: set[str] = set()
    for i, entry in enumerate(entries, 1):
        validate_entry(entry, i, ids, report)
    validate_relations(entries, report)
    report.warn(f"Résumé: {len(entries)} entrées chargées, {len(ids)} ids uniques.")
    return report


def print_report(report: Report, as_json: bool) -> None:
    if as_json:
        print(
            json.dumps(
                {
                    "ok": report.ok,
                    "errors": report.errors,
                    "warnings": report.warnings,
                    "human_review": report.human_review,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return
    print("=== Validateur registre Brain (lecture seule) ===")
    print(f"OK bloquant: {'oui' if report.ok else 'non'}")
    print(f"\nErreurs bloquantes ({len(report.errors)}):")
    for m in report.errors:
        print(f"  [ERROR] {m}")
    if not report.errors:
        print("  (aucune)")
    print(f"\nAvertissements ({len(report.warnings)}):")
    for m in report.warnings:
        print(f"  [WARN] {m}")
    if not report.warnings:
        print("  (aucun)")
    print(f"\nVérification humaine ({len(report.human_review)}):")
    for m in report.human_review:
        print(f"  [REVIEW] {m}")
    if not report.human_review:
        print("  (aucun)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valide entries.jsonl sans modification (mode lecture seule)."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="brain/registry/entries.jsonl",
        help="Chemin vers entries.jsonl",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Sortie JSON machine-readable",
    )
    args = parser.parse_args(argv)
    report = validate_registry(Path(args.path))
    print_report(report, args.json)
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
