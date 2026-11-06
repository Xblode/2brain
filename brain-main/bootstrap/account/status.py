# -*- coding: utf-8 -*-
"""État d'un projet vis-à-vis de 2brain. Lecture seule.

Usage : python -I status.py [--project DOSSIER] [--json] [--offline] [--home DOSSIER]
Codes de sortie : 0 normal, 2 dossier invalide.
"""

import argparse
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

REMOTE_VERSION_URL = "https://raw.githubusercontent.com/Xblode/2brain/master/brain-main/bootstrap/VERSION"
MANIFEST = "manifest.json"
DOCS = ("vision.md", "project.md", "requirements.md", "architecture.md", "workflow.md")
BRAIN_MAIN_REQUIRED = ("README.md", "conventions", "skills", "bootstrap")
TECH_HINTS = (
    "package.json", "pnpm-lock.yaml", "yarn.lock", "tsconfig.json", "pyproject.toml",
    "requirements.txt", "setup.py", "Cargo.toml", "go.mod", "pom.xml", "build.gradle",
    "Gemfile", "composer.json", "Dockerfile", "docker-compose.yml", "Makefile",
    "next.config.js", "vite.config.ts", "README.md", "AGENTS.md", "CLAUDE.md",
)


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


def parse_version(text):
    try:
        return tuple(int(p) for p in text.strip().split("."))
    except Exception:
        return None


def read_text(path):
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return None


def brain_main_state(project):
    root = project / "brain-main"
    if not root.exists():
        return {"etat": "absent", "manifeste": False, "version_installee": None}
    missing = [n for n in BRAIN_MAIN_REQUIRED if not (root / n).exists()]
    version = None
    manifest = (root / MANIFEST).is_file()
    if manifest:
        try:
            version = json.loads((root / MANIFEST).read_text(encoding="utf-8")).get("version")
        except Exception:
            version = None
    return {
        "etat": "complet" if not missing else "partiel",
        "manquants": missing,
        "manifeste": manifest,
        "version_installee": version,
    }


TODO_MARK = "À compléter"
AGENT_NAMES = ("orchestrator", "worker-sonnet", "worker-haiku")


def router_state(project):
    """Routeur Claude Code : `actif` (clé agent = orchestrator et trois agents), `absent` (ni l'un ni l'autre), sinon `partiel`."""
    try:
        data = json.loads((project / ".claude" / "settings.json").read_text(encoding="utf-8"))
        key = isinstance(data, dict) and data.get("agent") == "orchestrator"
    except Exception:
        key = False
    present = [n for n in AGENT_NAMES if (project / ".claude" / "agents" / (n + ".md")).is_file()]
    if key and len(present) == len(AGENT_NAMES):
        return {"etat": "actif", "raison": "`.claude/settings.json` : agent = orchestrator, trois agents présents"}
    if not key and not present:
        return {"etat": "absent", "raison": "ni la clé `agent` ni les agents dans `.claude/`"}
    parts = []
    parts.append("clé `agent` = orchestrator présente" if key else "clé `agent` = orchestrator absente de `.claude/settings.json`")
    missing = [n for n in AGENT_NAMES if n not in present]
    parts.append("agents : %s" % ("complets" if not missing else "manquants : " + ", ".join(missing)))
    return {"etat": "partiel", "raison": "; ".join(parts)}


def docs_to_complete(docs_dir):
    """Documents de brain/docs/ contenant encore « À compléter » (noms triés)."""
    out = []
    if docs_dir.is_dir():
        for p in sorted(docs_dir.glob("*.md")):
            text = read_text(p)
            if text and TODO_MARK in text:
                out.append(p.name)
    return out


def brain_state(project):
    root = project / "brain"
    if not root.exists():
        return {"etat": "absent", "entrees_registre": 0, "documents_a_completer": 0, "documents_a_completer_noms": []}
    docs_dir = root / "docs"
    present = {p.name.lower() for p in docs_dir.iterdir()} if docs_dir.is_dir() else set()
    missing = [d for d in DOCS if d not in present]
    todo = docs_to_complete(docs_dir)
    registry = root / "registry" / "entries.jsonl"
    count = 0
    if registry.is_file():
        try:
            with registry.open(encoding="utf-8") as fh:
                count = sum(1 for line in fh if line.strip())
        except Exception:
            count = 0
    else:
        missing.append("registry/entries.jsonl")
    return {
        "etat": "complet" if not missing else "partiel",
        "manquants": missing,
        "entrees_registre": count,
        "documents_a_completer": len(todo),
        "documents_a_completer_noms": todo,
    }


def remote_version(offline):
    if offline:
        return None
    try:
        with urllib.request.urlopen(REMOTE_VERSION_URL, timeout=3) as resp:
            if resp.status != 200:
                return None
            text = resp.read(64).decode("utf-8").strip()
        return text if parse_version(text) else None
    except Exception:
        return None


def build(project, home, offline):
    entries = sorted(p.name for p in project.iterdir())
    account = read_text(home / ".claude" / "skills" / "brain" / "VERSION")
    in_project = read_text(project / "brain-main" / "bootstrap" / "VERSION")
    remote = remote_version(offline)
    notes = []
    a, r, p = parse_version(account or ""), parse_version(remote or ""), parse_version(in_project or "")
    if remote is None:
        notes.append("Version distante : non vérifié.")
    elif a is None:
        notes.append("Version du Bootstrap sur le compte inconnue.")
    elif r and r > a:
        notes.append(
            "Une version plus récente du Bootstrap existe (%s > %s). Relance l'installation "
            "sur le compte (install-account.py) : /brain -u ne met pas à jour le compte." % (remote, account)
        )
    if a and p and p > a:
        notes.append(
            "Une version plus récente du Bootstrap existe : le projet embarque %s, le compte a %s. "
            "Relance install-account.py (brain-main/bootstrap/scripts/) pour mettre à jour le compte." % (in_project, account)
        )
    brain = brain_state(project)
    if brain["etat"] != "absent" and brain["documents_a_completer"] > 0:
        notes.append(
            "%d document(s) de brain/docs/ contiennent encore « %s » : /brain -o propose de les remplir (rien n'est écrit sans validation)."
            % (brain["documents_a_completer"], TODO_MARK)
        )
    router = router_state(project)
    if router["etat"] == "partiel":
        notes.append("Routeur partiel (%s) : il n'est pas actif." % router["raison"])
    return {
        "racine": str(project),
        "premier_niveau": entries,
        "dossier_vide": all(e == ".git" for e in entries),
        "brain_main": brain_main_state(project),
        "brain": brain,
        "depot_source": is_source_repo(project),
        "routeur": router["etat"],
        "routeur_raison": router["raison"],
        "technologies": [h for h in TECH_HINTS if (project / h).exists()],
        "bootstrap": {
            "compte": account or "inconnue",
            "projet": in_project or "absent",
            "distante": remote or "non vérifié",
        },
        "notes": notes,
    }


def as_text(st):
    bm, br = st["brain_main"], st["brain"]
    lines = [
        "Projet : %s" % st["racine"],
        "Dossier vide : %s" % ("oui" if st["dossier_vide"] else "non"),
        "Premier niveau : %s" % (", ".join(st["premier_niveau"]) or "(rien)"),
        "brain-main : %s%s" % (bm["etat"], " (version %s)" % bm["version_installee"] if bm.get("version_installee") else ""),
        "brain : %s (%d entrées au registre)" % (br["etat"], br["entrees_registre"]),
        "Documents contenant encore « %s » : %d" % (TODO_MARK, br["documents_a_completer"]),
        "Dépôt source 2brain : %s" % ("oui" if st["depot_source"] else "non"),
        "Routeur (orchestrateur et workers) : %s (%s)" % (st["routeur"], st["routeur_raison"]),
        "Technologies (indices) : %s" % (", ".join(st["technologies"]) or "aucun"),
        "Bootstrap : compte %s, projet %s, distante %s" % (
            st["bootstrap"]["compte"], st["bootstrap"]["projet"], st["bootstrap"]["distante"]),
    ]
    lines += st["notes"]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--offline", action="store_true", help="ne pas interroger la version distante")
    ap.add_argument("--home", default=None, help="home à lire pour la version du compte (défaut : réel)")
    args = ap.parse_args()
    project = Path(args.project).resolve()
    if not project.is_dir():
        sys.stderr.write("Dossier invalide : %s\n" % project)
        return 2
    home = Path(args.home) if args.home else Path.home()
    st = build(project, home, args.offline)
    if args.json:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(json.dumps(st, ensure_ascii=False, indent=2) + "\n")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(as_text(st) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
