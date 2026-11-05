# -*- coding: utf-8 -*-
"""Prévisualisation de l'installation de 2brain : crée EMPLACEMENT/ à la racine du projet.

Usage : python -I prepare-install.py --source DOSSIER_BRAIN_MAIN --project DOSSIER --answers JSON_OU_FICHIER
Ne touche à aucun autre fichier du projet. Crée EMPLACEMENT/ avec la copie prévue de
brain-main/ et de brain/, un plan.json et le marqueur .2brain-emplacement.
Sortie JSON (avec plan_sha256). Codes : 0 ok, 2 refus ou erreur.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

EMPLACEMENT = "EMPLACEMENT"
MARKER = ".2brain-emplacement"
MANIFEST = "manifest.json"
ANSWER_KEYS = ("nature", "objectif", "modules", "outils", "identite")
TODO = "À compléter."
PLACEHOLDER = re.compile(r"\{\{([a-z_]+)\}\}")


class Refused(Exception):
    pass


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def is_source_repo(project):
    """Dépôt source 2brain : remote origin Xblode/2brain, lab/ et le registre présents."""
    try:
        out = subprocess.run(
            ["git", "-C", str(project), "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=10, stdin=subprocess.DEVNULL,
        )
        if out.returncode != 0 or "Xblode/2brain" not in out.stdout:
            return False
    except Exception:
        return False
    return (project / "lab").is_dir() and (project / "brain" / "registry" / "entries.jsonl").is_file()


def rmtree(path):
    def onerror(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)

    shutil.rmtree(path, onerror=onerror)


def skipped(rel_parts):
    return "__pycache__" in rel_parts or rel_parts[-1].endswith(".pyc")


def list_files(root):
    """Fichiers réguliers sous root (chemins relatifs posix). Refuse les liens."""
    out = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if skipped(rel.parts):
            continue
        if path.is_symlink():
            raise Refused("lien refusé : %s" % path)
        if path.is_file():
            out[rel.as_posix()] = path
    return out


def fmt(value):
    """Texte d'une réponse ; une réponse nulle ou vide donne « À compléter. »."""
    if value is None:
        return TODO
    if isinstance(value, (list, tuple)):
        items = [str(v).strip() for v in value if str(v).strip()]
        return "\n".join("- " + i for i in items) if items else TODO
    text = str(value).strip()
    return text if text else TODO


def render(text, values):
    return PLACEHOLDER.sub(lambda m: values.get(m.group(1), m.group(0)), text)


def load_answers(raw):
    try:
        text = raw if raw.lstrip().startswith("{") else Path(raw).read_text(encoding="utf-8")
        data = json.loads(text)
    except Exception as exc:
        raise Refused("réponses illisibles (JSON attendu) : %s" % exc)
    if not isinstance(data, dict):
        raise Refused("les réponses doivent être un objet JSON")
    return {k: data.get(k) for k in ANSWER_KEYS}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True)
    ap.add_argument("--project", required=True)
    ap.add_argument("--answers", required=True)
    args = ap.parse_args()
    emplacement = None
    created = False
    try:
        project = Path(args.project).resolve()
        source = Path(args.source).resolve()
        if not project.is_dir():
            raise Refused("projet introuvable : %s" % project)
        if is_source_repo(project):
            raise Refused("refus : ce dossier est le dépôt source 2brain")
        for name in ("brain-main", "brain"):
            if os.path.lexists(project / name):
                raise Refused(
                    "%s/ existe déjà : 2brain est déjà (partiellement) installé ici, rien n'est créé. "
                    "Utilise /brain pour voir l'état ou /brain -u pour mettre à jour brain-main/." % name
                )
        if not (source / "bootstrap" / "templates" / "brain").is_dir() or not (source / "bootstrap" / "VERSION").is_file():
            raise Refused("source invalide : bootstrap/templates/brain ou bootstrap/VERSION absent dans %s" % source)
        answers = load_answers(args.answers)
        emplacement = project / EMPLACEMENT
        if os.path.lexists(emplacement):
            if emplacement.is_dir() and not emplacement.is_symlink() and (emplacement / MARKER).is_file():
                rmtree(emplacement)
            else:
                raise Refused("%s/ existe déjà sans son marqueur %s : refus, rien n'y est touché" % (EMPLACEMENT, MARKER))

        version = (source / "bootstrap" / "VERSION").read_text(encoding="utf-8").strip()
        commit_file = source.parent / "source-commit.txt"
        commit = commit_file.read_text(encoding="utf-8").strip() if commit_file.is_file() else "inconnu"

        emplacement.mkdir()
        created = True
        (emplacement / MARKER).write_text(
            json.dumps({"outil": "prepare-install", "cree": datetime.now().isoformat(timespec="seconds")}) + "\n",
            encoding="utf-8",
        )

        # brain-main/ : copie de la source (sans manifeste ni caches).
        for rel, path in list_files(source).items():
            if rel == MANIFEST:
                continue
            target = emplacement / "brain-main" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)

        # brain/ : généré depuis les modèles et les réponses.
        values = {k: fmt(v) for k, v in answers.items()}
        values["date"] = date.today().isoformat()
        templates = source / "bootstrap" / "templates"
        for rel, path in list_files(templates / "brain").items():
            target = emplacement / "brain" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if rel.endswith(".md"):
                text = render(path.read_text(encoding="utf-8"), values)
                target.write_text(text, encoding="utf-8", newline="\n")
            else:
                shutil.copyfile(path, target)

        # CLAUDE.md et AGENTS.md : créés seulement s'ils sont absents, jamais modifiés.
        adaptations = []
        conflicts = []
        agents_template = templates / "AGENTS.md"
        claude_template = templates / "CLAUDE.md"
        agents_exists = os.path.lexists(project / "AGENTS.md")
        claude_exists = os.path.lexists(project / "CLAUDE.md")
        agents_text = render(agents_template.read_text(encoding="utf-8"), values) if agents_template.is_file() else ""
        if not agents_exists and agents_text:
            (emplacement / "AGENTS.md").write_text(agents_text, encoding="utf-8", newline="\n")
        if not claude_exists and claude_template.is_file():
            shutil.copyfile(claude_template, emplacement / "CLAUDE.md")
        if agents_exists:
            current = (project / "AGENTS.md").read_text(encoding="utf-8", errors="replace")
            present = {line.strip() for line in current.splitlines()}
            wanted = [l.rstrip() for l in agents_text.splitlines() if l.startswith("@brain-main/") or l.startswith("- Si `brain/docs/`")]
            missing = [l for l in wanted if l not in present]
            if missing:
                adaptations.append(
                    "AGENTS.md existe : il n'est pas modifié. Pour charger 2brain à chaque session, ajouter exactement ces lignes "
                    "(les imports dans cet ordre, hors de tout bloc de code) :\n" + "\n".join(missing)
                )
        if claude_exists:
            current = (project / "CLAUDE.md").read_text(encoding="utf-8", errors="replace")
            if "@AGENTS.md" not in {line.strip() for line in current.splitlines()}:
                adaptations.append(
                    "CLAUDE.md existe : il n'est pas modifié. Pour qu'il charge AGENTS.md, ajouter exactement la ligne :\n@AGENTS.md"
                )

        files = {}
        for rel, path in list_files(emplacement).items():
            if rel in (MARKER,):
                continue
            files[rel] = sha256_file(path)
        for rel in files:
            if os.path.lexists(project / rel):
                conflicts.append(rel)
        plan = {
            "plan_version": 1,
            "projet": str(project),
            "source": str(source),
            "source_commit": commit,
            "bootstrap_version": version,
            "reponses": answers,
            "fichiers": dict(sorted(files.items())),
            "conflits": conflicts,
            "adaptations": adaptations,
        }
        plan_bytes = (json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
        (emplacement / "plan.json").write_bytes(plan_bytes)
        plan_sha = hashlib.sha256(plan_bytes).hexdigest()

        dirs = sorted({str(Path(r).parent.as_posix()) for r in files if "/" in r})
        summary = {
            "ok": True,
            "emplacement": str(emplacement),
            "plan_sha256": plan_sha,
            "source_commit": commit,
            "bootstrap_version": version,
            "reponses": answers,
            "arborescence": dirs,
            "fichiers_brain_main": sum(1 for r in files if r.startswith("brain-main/")),
            "fichiers_brain": sorted(r for r in files if r.startswith("brain/")),
            "racine_creee": sorted(r for r in files if r in ("CLAUDE.md", "AGENTS.md")),
            "agents_md_cree": "AGENTS.md" in files,
            "claude_md_cree": "CLAUDE.md" in files,
            "conflits": conflicts,
            "adaptations": adaptations,
        }
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        return 0
    except Refused as exc:
        if created and emplacement is not None:
            rmtree(emplacement)
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(json.dumps({"ok": False, "erreur": str(exc)}, ensure_ascii=False, indent=2) + "\n")
        return 2
    except Exception as exc:
        if created and emplacement is not None:
            rmtree(emplacement)
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(json.dumps({"ok": False, "erreur": "échec : %r" % exc}, ensure_ascii=False, indent=2) + "\n")
        return 2


if __name__ == "__main__":
    sys.exit(main())
