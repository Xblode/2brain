# -*- coding: utf-8 -*-
"""Met à jour `AGENTS.md` et `CLAUDE.md` d'un projet (écritures de `/brain -a`, une opération à la fois).

Usage : python -I sync-agents.py --project DOSSIER --op claude|2brain|projet [--section-file FICHIER] [--dry-run]

- `claude`  : si `CLAUDE.md` a un contenu autre que `@AGENTS.md`, ce contenu passe mot pour mot dans `AGENTS.md`
              (section délimitée), puis `CLAUDE.md` devient `@AGENTS.md`. `CLAUDE.md` absent : créé. Déjà conforme : inchangé.
              Seule la ligne `@AGENTS.md` (import circulaire) n'est pas reprise. `AGENTS.md` absent : créé.
- `2brain`  : ajoute à `AGENTS.md` le contenu du modèle `brain-main/bootstrap/templates/AGENTS.md` (sans front matter),
              dans une section délimitée, sauf s'il y est déjà (délimiteurs ou imports `brain-main/`). Rien n'est remplacé.
- `projet`  : ajoute à `AGENTS.md` le texte de `--section-file` (déjà validé par l'humain), mot pour mot, dans une section
              délimitée. Une section déjà présente n'est jamais remplacée : texte identique = aucune action, sinon refus.
Ne modifie jamais autre chose que `AGENTS.md` et `CLAUDE.md`. Refus dans le dépôt source 2brain. UTF-8, fins de ligne conservées.
Sortie JSON. Codes : 0 ok (y compris « rien à écrire »), 2 refus ou erreur (rien n'est écrit).
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

IMPORT_LINE = "@AGENTS.md"
M_CLAUDE = ("<!-- 2brain:claude-md:debut -->", "<!-- 2brain:claude-md:fin -->")
M_BRAIN = ("<!-- 2brain:2brain:debut -->", "<!-- 2brain:2brain:fin -->")
M_PROJET = ("<!-- 2brain:projet:debut -->", "<!-- 2brain:projet:fin -->")


class Refused(Exception):
    pass


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


def read_text(path):
    """Lit en UTF-8 sans toucher aux fins de ligne. None si absent."""
    if os.path.lexists(path) and (path.is_symlink() or not path.is_file()):
        raise Refused("`%s` n'est pas un fichier ordinaire, rien n'est écrit" % path.name)
    if not path.is_file():
        return None
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refused("`%s` n'est pas de l'UTF-8 valide, rien n'est écrit" % path.name)


def write_text(path, text):
    tmp = path.with_name(path.name + ".tmp-2brain")
    tmp.write_bytes(text.encode("utf-8"))
    os.replace(tmp, path)


def eol_of(text):
    return "\r\n" if text and "\r\n" in text else "\n"


def is_conform(claude):
    return claude is not None and claude.lstrip("﻿").strip() == IMPORT_LINE


def append_block(agents, block, eol):
    """Ajoute le bloc à la fin, séparé par une ligne vide."""
    if not agents:
        return block
    if not agents.endswith(("\n", "\r")):
        agents += eol
    if not agents.endswith(eol + eol) and not agents.endswith("\n\n"):
        agents += eol
    return agents + block


def mk_block(markers, body, eol):
    body_nl = body if body.endswith("\n") else body + eol
    return markers[0] + eol + body_nl + markers[1] + eol


def op_claude(project, dry_run):
    cpath, apath = project / "CLAUDE.md", project / "AGENTS.md"
    claude, agents = read_text(cpath), read_text(apath)
    out = {"ok": True, "op": "claude", "dry_run": dry_run, "ecrit": False, "fichiers": []}
    if claude is None:
        out.update(action="création de CLAUDE.md", message="`CLAUDE.md` absent : créé avec `@AGENTS.md`.")
        if not dry_run:
            write_text(cpath, IMPORT_LINE + "\n")
            out.update(ecrit=True, fichiers=["CLAUDE.md"])
        return out
    if is_conform(claude):
        out.update(action="aucune", message="`CLAUDE.md` est déjà conforme (`@AGENTS.md`) : rien à écrire.")
        return out
    # contenu à reprendre : tout, sauf la ligne d'import circulaire
    kept = [ln for ln in claude.splitlines(keepends=True) if ln.strip() != IMPORT_LINE]
    content = "".join(kept)
    if not content.strip():
        # contenu vide (espaces) : seul le modèle manque
        out.update(action="CLAUDE.md remis au modèle", message="`CLAUDE.md` sans contenu : remis au modèle `@AGENTS.md`.")
        if not dry_run:
            write_text(cpath, IMPORT_LINE + "\n")
            out.update(ecrit=True, fichiers=["CLAUDE.md"])
        return out
    base = agents if agents is not None else ""
    eol = eol_of(base) if base else eol_of(content)
    body = "## Contenu repris de l'ancien CLAUDE.md" + eol + eol + content
    block = mk_block(M_CLAUDE, body, eol)
    files = []
    new_agents = base
    if block in base:
        out["note"] = "Contenu déjà présent dans `AGENTS.md` (reprise interrompue) : pas de duplication."
    else:
        if agents is None:
            new_agents = "# Instructions agents" + eol + eol + block
        else:
            new_agents = append_block(base, block, eol)
        files.append("AGENTS.md")
    files.append("CLAUDE.md")
    out.update(action="contenu de CLAUDE.md repris dans AGENTS.md, CLAUDE.md remis au modèle",
               message=("Simulation : rien n'est écrit. " if dry_run else "") +
               "Le contenu de `CLAUDE.md` (%d caractères) est repris mot pour mot dans `AGENTS.md`, puis `CLAUDE.md` devient `@AGENTS.md`." % len(content),
               a_ecrire=files, contenu_repris=content)
    if not dry_run:
        if "AGENTS.md" in files:
            write_text(apath, new_agents)  # d'abord AGENTS.md : en cas d'échec, CLAUDE.md garde son contenu
        write_text(cpath, IMPORT_LINE + "\n")
        out.update(ecrit=True, fichiers=files)
    return out


def op_2brain(project, dry_run):
    apath = project / "AGENTS.md"
    agents = read_text(apath)
    out = {"ok": True, "op": "2brain", "dry_run": dry_run, "ecrit": False, "fichiers": []}
    if agents is not None and (M_BRAIN[0] in agents or "@brain-main/conventions/README.md" in agents):
        out.update(action="aucune", message="`AGENTS.md` contient déjà les informations 2brain : rien à écrire.")
        return out
    tpl_path = project / "brain-main" / "bootstrap" / "templates" / "AGENTS.md"
    tpl = read_text(tpl_path)
    if tpl is None:
        raise Refused("modèle `brain-main/bootstrap/templates/AGENTS.md` introuvable : faire `/brain -i` ou `/brain -u`. Rien n'est écrit.")
    tpl = tpl.replace("\r\n", "\n").lstrip("﻿")
    if tpl.startswith("---\n"):
        end = tpl.find("\n---\n", 4)
        if end != -1:
            tpl = tpl[end + 5:]
    lines = []
    for ln in tpl.strip("\n").split("\n"):
        if ln.startswith("# "):
            ln = "## 2brain"  # le titre du modèle devient le titre de la section
        elif ln.startswith("#"):
            ln = "#" + ln
        lines.append(ln)
    eol = eol_of(agents) if agents else "\n"
    block = mk_block(M_BRAIN, eol.join(lines), eol)
    new_agents = append_block(agents, block, eol) if agents is not None else "# Instructions agents" + eol + eol + block
    out.update(action="ajout des informations 2brain" + (" (AGENTS.md créé)" if agents is None else ""),
               message=("Simulation : rien n'est écrit. " if dry_run else "") + "Section 2brain (repères, imports, règles) ajoutée à la fin de `AGENTS.md`, sans rien remplacer.",
               a_ecrire=["AGENTS.md"])
    if not dry_run:
        write_text(apath, new_agents)
        out.update(ecrit=True, fichiers=["AGENTS.md"])
    return out


def op_projet(project, section_file, dry_run):
    if not section_file:
        raise Refused("`--section-file` est requis pour l'opération `projet`")
    sp = Path(section_file)
    if not sp.is_file():
        raise Refused("fichier de section introuvable : %s" % section_file)
    try:
        text = sp.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refused("la section n'est pas de l'UTF-8 valide, rien n'est écrit")
    text = text.lstrip("﻿")
    if not text.strip():
        raise Refused("la section est vide, rien n'est écrit")
    if "<!-- 2brain:" in text:
        raise Refused("la section contient un délimiteur 2brain, rien n'est écrit")
    apath = project / "AGENTS.md"
    agents = read_text(apath)
    eol = eol_of(agents) if agents else "\n"
    text = text.replace("\r\n", "\n").replace("\n", eol)
    block = mk_block(M_PROJET, text, eol)
    out = {"ok": True, "op": "projet", "dry_run": dry_run, "ecrit": False, "fichiers": []}
    if agents is not None and block in agents:
        out.update(action="aucune", message="Cette section est déjà dans `AGENTS.md` : rien à écrire.")
        return out
    if agents is not None and M_PROJET[0] in agents:
        raise Refused("`AGENTS.md` a déjà une section projet différente : elle n'est jamais remplacée. Proposer une adaptation à part. Rien n'est écrit.")
    new_agents = append_block(agents, block, eol) if agents is not None else "# Instructions agents" + eol + eol + block
    out.update(action="ajout de la section projet" + (" (AGENTS.md créé)" if agents is None else ""),
               message=("Simulation : rien n'est écrit. " if dry_run else "") + "Section projet ajoutée à la fin de `AGENTS.md`, mot pour mot.",
               a_ecrire=["AGENTS.md"])
    if not dry_run:
        write_text(apath, new_agents)
        out.update(ecrit=True, fichiers=["AGENTS.md"])
    return out


def run(project, op, section_file, dry_run):
    if is_source_repo(project):
        raise Refused("dépôt source 2brain : refus, son `AGENTS.md` est celui du projet lui-même ; cette écriture se fait dans un projet installé")
    if not project.is_dir():
        raise Refused("dossier de projet introuvable : %s" % project)
    if op == "claude":
        return op_claude(project, dry_run)
    if op == "2brain":
        return op_2brain(project, dry_run)
    return op_projet(project, section_file, dry_run)


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Met à jour AGENTS.md et CLAUDE.md (/brain -a).")
    ap.add_argument("--project", required=True)
    ap.add_argument("--op", required=True, choices=["claude", "2brain", "projet"])
    ap.add_argument("--section-file")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    try:
        out = run(Path(args.project).resolve(), args.op, args.section_file, args.dry_run)
        code = 0
    except Refused as exc:
        out, code = {"ok": False, "ecrit": False, "erreur": str(exc)}, 2
    sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    return code


if __name__ == "__main__":
    sys.exit(main())
