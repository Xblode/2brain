# -*- coding: utf-8 -*-
"""Tests autonomes du Bootstrap /brain (lot 2). Bibliothèque standard uniquement.

Usage : python brain-main/bootstrap/tests/run_bootstrap_tests.py
Tout se passe dans un dossier créé par tempfile.mkdtemp, hors du dépôt. La source
utilisée est une copie temporaire de brain-main/ ; le brain/ réel n'est jamais
écrit (le SCHEMA.md du dépôt n'est lu que pour comparaison). Rien n'est écrit dans ~/.claude :
les tests du compte utilisent --home avec un dossier temporaire.
Sortie : une ligne PASS/FAIL par contrôle. Code de sortie 0 si tout passe, 1 sinon.
"""

import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import traceback
from pathlib import Path

BOOT = Path(__file__).resolve().parent.parent
REPO = BOOT.parent.parent
SCRIPTS = BOOT / "scripts"
ACCOUNT = BOOT / "account"
EXPECTED_MESSAGE = (
    "Ce dossier est vide et 2brain n'y est pas installé. "
    "Dans cette situation, la première réponse de la session commence par la question : "
    "« Avant de commencer, souhaites-tu installer 2brain dans ce projet ? ». "
    "Si la réponse est oui, elle indique de taper /brain -i. "
    "Si la réponse est non, la session continue normalement et la question n'est pas reposée."
)
ANSWERS_FULL = {
    "nature": "Site web vitrine",
    "objectif": "Présenter l'activité de l'atelier",
    "modules": ["recherche", "revue"],
    "outils": "Next.js, Figma",
    "identite": "Atelier Test",
}
ANSWERS_NULL = {k: None for k in ANSWERS_FULL}

NL = chr(10)
RESULTS = []
TMP = None


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else "  :: " + str(detail)[:400]))


def rmtree(path):
    def onerror(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)

    shutil.rmtree(path, onerror=onerror)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tree(root, skip=()):
    out = {}
    root = Path(root)
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if any(rel == s or rel.startswith(s + "/") for s in skip):
            continue
        out[rel] = "dir" if p.is_dir() else sha(p)
    return out


def run(script, *args, cwd=None, inp=None):
    p = subprocess.run(
        [sys.executable, "-I", "-B", str(script), *[str(a) for a in args]],
        capture_output=True, text=True, encoding="utf-8", input=inp, cwd=cwd, timeout=180,
    )
    return p.returncode, p.stdout, p.stderr


def runj(script, *args, **kw):
    rc, out, err = run(script, *args, **kw)
    try:
        data = json.loads(out)
    except Exception:
        data = {"_raw": out, "_err": err}
    return rc, data


def mk(path, files):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    for rel, content in files.items():
        p = path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return path


def new_dir(name):
    d = Path(TMP) / name
    n = 0
    while d.exists():
        n += 1
        d = Path(TMP) / ("%s-%d" % (name, n))
    d.mkdir(parents=True)
    return d


def git(*args, cwd):
    subprocess.run(["git", *args], cwd=cwd, capture_output=True, check=True, stdin=subprocess.DEVNULL)


def fake_source_repo(name, with_lab=True, remote="https://github.com/Xblode/2brain.git"):
    d = new_dir(name)
    git("init", "-q", cwd=d)
    if remote:
        git("remote", "add", "origin", remote, cwd=d)
    if with_lab:
        mk(d, {"lab/x.txt": "x", "brain/registry/entries.jsonl": ""})
    return d


def copy_brain_main(dst_root):
    dst = Path(dst_root) / "brain-main"
    shutil.copytree(REPO / "brain-main", dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return dst


def hook(stdin_obj=None, raw=None, cwd=None):
    inp = raw if raw is not None else json.dumps(stdin_obj)
    rc, out, err = run(ACCOUNT / "session-start.py", inp=inp, cwd=cwd)
    return rc, out, err


# --------------------------------------------------------------------------- groupes


def test_hook():
    empty = new_dir("hook-empty")
    gitonly = new_dir("hook-git")
    (gitonly / ".git").mkdir()
    withfile = mk(new_dir("hook-file"), {"a.txt": "x"})
    withbm = mk(new_dir("hook-bm"), {"brain-main/README.md": "x"})
    rc, out, _ = hook({"cwd": str(empty), "source": "startup"})
    ctx = json.loads(out)["hookSpecificOutput"] if out else {}
    check("hook: dossier vide -> message exact, code 0",
          rc == 0 and ctx.get("additionalContext") == EXPECTED_MESSAGE and ctx.get("hookEventName") == "SessionStart", out)
    rc, out, _ = hook({"cwd": str(gitonly), "source": "startup"})
    check("hook: seulement .git -> message", rc == 0 and "installer 2brain" in out, out)
    rc, out, _ = hook({"cwd": str(withfile), "source": "startup"})
    check("hook: dossier avec fichier -> silence", rc == 0 and out == "", out)
    rc, out, _ = hook({"cwd": str(withbm), "source": "startup"})
    check("hook: brain-main présent -> silence", rc == 0 and out == "", out)
    rc, out, _ = hook({"cwd": str(empty), "source": "resume"})
    check("hook: source resume -> silence", rc == 0 and out == "", out)
    rc, out, _ = hook({"cwd": str(empty / "inexistant"), "source": "startup"})
    check("hook: cwd invalide -> silence, code 0", rc == 0 and out == "", out)
    rc, out, _ = hook({"source": "startup"})
    check("hook: cwd absent -> silence, code 0", rc == 0 and out == "")
    rc, out, err = hook(raw="pas du json {{")
    check("hook: entrée invalide -> silence, code 0, pas de trace", rc == 0 and out == "" and err == "", err)
    rc, out, err = hook(raw="")
    check("hook: entrée vide -> silence, code 0", rc == 0 and out == "")
    check("hook: aucun fichier créé dans le dossier vide", list(empty.iterdir()) == [])


def status(project, home, *extra):
    return runj(ACCOUNT / "status.py", "--project", project, "--home", home, "--json", "--offline", *extra)


def test_status():
    home = new_dir("home-status")
    p_abs = mk(new_dir("st-abs"), {"package.json": "{}", "src/a.js": "x"})
    rc, st = status(p_abs, home)
    check("status: absent", rc == 0 and st["brain_main"]["etat"] == "absent" and st["brain"]["etat"] == "absent"
          and st["dossier_vide"] is False and "package.json" in st["technologies"] and st["depot_source"] is False, st)
    check("status: version distante non vérifiée hors ligne", st["bootstrap"]["distante"] == "non vérifié", st["bootstrap"])
    p_empty = new_dir("st-empty")
    (p_empty / ".git").mkdir()
    rc, st = status(p_empty, home)
    check("status: dossier avec seulement .git = vide", st["dossier_vide"] is True, st)

    p_part = mk(new_dir("st-part"), {"brain-main/README.md": "x", "brain/docs/vision.md": "x"})
    rc, st = status(p_part, home)
    check("status: partiel", st["brain_main"]["etat"] == "partiel" and st["brain"]["etat"] == "partiel", st)

    p_full = mk(new_dir("st-full"), {
        "brain-main/README.md": "x", "brain-main/conventions/a.md": "x", "brain-main/skills/s.md": "x",
        "brain-main/bootstrap/VERSION": "0.1.0\n",
        "brain-main/manifest.json": json.dumps({"version": "0.1.0", "files": {}}),
        "brain/docs/vision.md": "x", "brain/docs/project.md": "x", "brain/docs/requirements.md": "x",
        "brain/docs/architecture.md": "x", "brain/docs/workflow.md": "x",
        "brain/registry/entries.jsonl": '{"id":"CAP-001"}\n{"id":"CAP-002"}\n\n',
    })
    rc, st = status(p_full, home)
    check("status: complet, 2 entrées, version installée",
          st["brain_main"]["etat"] == "complet" and st["brain"]["etat"] == "complet" and st["brain"]["entrees_registre"] == 2
          and st["brain_main"]["version_installee"] == "0.1.0" and st["bootstrap"]["projet"] == "0.1.0", st)

    src = fake_source_repo("st-src")
    rc, st = status(src, home)
    check("status: dépôt source reconnu", st["depot_source"] is True, st)
    nolab = fake_source_repo("st-nolab", with_lab=False)
    rc, st = status(nolab, home)
    check("status: remote 2brain sans lab/ -> pas dépôt source", st["depot_source"] is False, st)
    norem = fake_source_repo("st-norem", remote=None)
    rc, st = status(norem, home)
    check("status: sans remote -> pas dépôt source", st["depot_source"] is False, st)
    other = fake_source_repo("st-other", remote="https://github.com/autre/projet.git")
    rc, st = status(other, home)
    check("status: autre remote -> pas dépôt source", st["depot_source"] is False, st)

    # version du compte et message de mise à jour (fonction interne, sans réseau)
    mk(home, {".claude/skills/brain/VERSION": "0.0.9\n"})
    rc, st = status(p_abs, home)
    check("status: version du compte lue", st["bootstrap"]["compte"] == "0.0.9", st["bootstrap"])

    before = tree(p_full)
    before_home = tree(home)
    run(ACCOUNT / "status.py", "--project", p_full, "--home", home, "--offline")
    run(ACCOUNT / "status.py", "--project", p_full, "--home", home, "--offline", "--json")
    check("status: écriture nulle (projet et home inchangés)", tree(p_full) == before and tree(home) == before_home)
    rc, out, err = run(ACCOUNT / "status.py", "--project", p_abs, "--home", home, "--offline")
    check("status: sortie texte", rc == 0 and "brain-main : absent" in out, out)


def make_tar(path, members, pax_comment=None):
    """members : liste de (nom, contenu_bytes|None pour dossier|('link', cible))."""
    kwargs = {}
    if pax_comment:
        kwargs = {"format": tarfile.PAX_FORMAT, "pax_headers": {"comment": pax_comment}}
    with tarfile.open(path, "w:gz", **kwargs) as tf:
        for name, content in members:
            ti = tarfile.TarInfo(name)
            if content is None:
                ti.type = tarfile.DIRTYPE
                ti.mode = 0o755
                tf.addfile(ti)
            elif isinstance(content, tuple):
                ti.type = tarfile.SYMTYPE
                ti.linkname = content[1]
                tf.addfile(ti)
            else:
                ti.size = len(content)
                tf.addfile(ti, io.BytesIO(content))


def test_fetch():
    fetch = ACCOUNT / "fetch-source.py"
    repo_root = new_dir("fetch-src")
    copy_brain_main(repo_root)
    dest = new_dir("fetch-dest")
    rc, data = runj(fetch, "--dest", dest, "--source-dir", repo_root)
    prep = dest / "brain-main" / "bootstrap" / "scripts" / "prepare-install.py"
    check("fetch: copie locale", rc == 0 and data.get("ok") and prep.is_file(), data)
    check("fetch: commit source noté (inconnu pour une copie sans git)",
          (dest / "source-commit.txt").read_text(encoding="utf-8").strip() == "inconnu")
    check("fetch: pas de __pycache__ copié", not list(dest.rglob("__pycache__")))
    rc, data = runj(fetch, "--dest", dest, "--source-dir", repo_root)
    check("fetch: destination non vide refusée", rc == 2, data)

    # archive valide, avec commit dans l'en-tête pax
    good = new_dir("fetch-tar") / "good.tar.gz"
    members = [("2brain-master/", None), ("2brain-master/README.md", b"racine\n"), ("2brain-master/brain/x.md", b"hors brain-main\n")]
    for p in sorted((repo_root / "brain-main").rglob("*")):
        rel = p.relative_to(repo_root).as_posix()
        members.append(("2brain-master/" + rel, None if p.is_dir() else p.read_bytes()))
    make_tar(good, members, pax_comment="a" * 40)
    dest = new_dir("fetch-dest")
    rc, data = runj(fetch, "--dest", dest, "--source-url", good.as_uri())
    check("fetch: archive locale valide, seul brain-main/ extrait",
          rc == 0 and (dest / "brain-main" / "bootstrap" / "VERSION").is_file()
          and not (dest / "README.md").exists() and not (dest / "brain").exists(), data)
    check("fetch: commit lu dans l'archive", data.get("source_commit") == "a" * 40, data)

    # chemin malveillant
    evil = good.parent / "evil.tar.gz"
    make_tar(evil, [("2brain-master/brain-main/ok.md", b"ok"), ("2brain-master/brain-main/../../evil.txt", b"pwned")])
    dest = new_dir("fetch-dest-evil")
    rc, data = runj(fetch, "--dest", dest, "--source-url", evil.as_uri())
    check("fetch: chemin malveillant (..) refusé, rien écrit", rc == 4 and not (dest.parent / "evil.txt").exists()
          and not (dest / "brain-main").exists(), data)
    evil2 = good.parent / "evil2.tar.gz"
    make_tar(evil2, [("/abs/evil.txt", b"x"), ("2brain-master/brain-main/ok.md", b"ok")])
    dest = new_dir("fetch-dest-evil2")
    rc, data = runj(fetch, "--dest", dest, "--source-url", evil2.as_uri())
    check("fetch: chemin absolu refusé", rc == 4 and not (dest / "brain-main").exists(), data)
    link = good.parent / "link.tar.gz"
    make_tar(link, [("2brain-master/brain-main/ok.md", b"ok"), ("2brain-master/brain-main/l", ("l", "../../x"))])
    dest = new_dir("fetch-dest-link")
    rc, data = runj(fetch, "--dest", dest, "--source-url", link.as_uri())
    check("fetch: lien refusé", rc == 4 and not (dest / "brain-main").exists(), data)

    # archive sans Bootstrap
    nob = good.parent / "nobootstrap.tar.gz"
    make_tar(nob, [("2brain-master/brain-main/README.md", b"x"), ("2brain-master/brain-main/conventions/N.md", b"x")])
    dest = new_dir("fetch-dest-nob")
    rc, data = runj(fetch, "--dest", dest, "--source-url", nob.as_uri())
    check("fetch: archive sans Bootstrap -> message clair, code 3",
          rc == 3 and "ne contient pas encore le Bootstrap" in data.get("erreur", ""), data)
    nobm = good.parent / "nobrainmain.tar.gz"
    make_tar(nobm, [("2brain-master/README.md", b"x")])
    rc, data = runj(fetch, "--dest", new_dir("fetch-dest-nobm"), "--source-url", nobm.as_uri())
    check("fetch: archive sans brain-main/ refusée", rc == 4, data)
    rc, data = runj(fetch, "--dest", new_dir("fetch-dest-http"), "--source-url", "http://example.com/x.tgz")
    check("fetch: URL http refusée", rc == 2, data)


class Env:
    """Source récupérée (copie locale) partagée par les tests d'installation."""


def setup_fetched():
    root = new_dir("fetched-src")
    copy_brain_main(root)
    dest = new_dir("fetched")
    rc, data = runj(ACCOUNT / "fetch-source.py", "--dest", dest, "--source-dir", root)
    Env.source = dest / "brain-main"
    check("préparation: source récupérée", rc == 0, data)


def prepare(project, answers=ANSWERS_FULL, source=None):
    return runj(SCRIPTS / "prepare-install.py", "--source", source or Env.source, "--project", project,
                "--answers", json.dumps(answers))


def apply(project, sha_value):
    return runj(SCRIPTS / "apply-install.py", "--project", project, "--plan-sha256", sha_value)


def project_with_files(name="proj"):
    return mk(new_dir(name), {"README.md": "# Projet\n", "src/app.py": "print(1)\n", ".gitignore": "x\n", "CLAUDE.md": "perso\n"})


def test_prepare_cancel():
    proj = project_with_files("prep")
    before = tree(proj)
    rc, data = prepare(proj)
    emp = proj / "EMPLACEMENT"
    check("prévisualisation: EMPLACEMENT créé avec marqueur, plan, brain-main, brain",
          rc == 0 and (emp / ".2brain-emplacement").is_file() and (emp / "plan.json").is_file()
          and (emp / "brain-main" / "bootstrap" / "VERSION").is_file() and (emp / "brain" / "docs" / "VISION.md").is_file(), data)
    check("prévisualisation: plan_sha256 = empreinte de plan.json", data.get("plan_sha256") == sha(emp / "plan.json"), data)
    check("prévisualisation: projet inchangé hors EMPLACEMENT", tree(proj, skip=("EMPLACEMENT",)) == before)
    check("prévisualisation: AGENTS.md prévu car absent, CLAUDE.md existant non touché",
          (emp / "AGENTS.md").is_file() and data.get("agents_md_cree") is True and (proj / "CLAUDE.md").read_text(encoding="utf-8") == "perso\n", data)
    plan = json.loads((emp / "plan.json").read_text(encoding="utf-8"))
    check("prévisualisation: plan.json contient réponses, source, commit, conflits, adaptations, empreintes",
          plan["reponses"]["nature"] == "Site web vitrine" and plan["source_commit"] and "conflits" in plan
          and "adaptations" in plan and all(len(v) == 64 for v in plan["fichiers"].values()), plan.keys())
    check("prévisualisation: pas de manifeste prévu", "brain-main/manifest.json" not in plan["fichiers"])
    # nouvelle prévisualisation par-dessus la précédente
    rc, data2 = prepare(proj)
    check("prévisualisation: refaite sur EMPLACEMENT marqué", rc == 0 and data2["plan_sha256"] == data["plan_sha256"], data2)
    rc, out = runj(SCRIPTS / "cancel-install.py", "--project", proj)
    check("annulation: EMPLACEMENT supprimé, projet strictement identique",
          rc == 0 and out.get("supprime") is True and not emp.exists() and tree(proj) == before, out)
    rc, out = runj(SCRIPTS / "cancel-install.py", "--project", proj)
    check("annulation: rien à annuler = ok", rc == 0 and out.get("supprime") is False, out)

    # EMPLACEMENT étranger
    proj2 = mk(new_dir("prep-foreign"), {"EMPLACEMENT/perso.txt": "à moi\n", "a.txt": "x"})
    before2 = tree(proj2)
    rc, data = prepare(proj2)
    check("EMPLACEMENT étranger: prévisualisation refusée sans toucher", rc == 2 and tree(proj2) == before2, data)
    rc, out = runj(SCRIPTS / "cancel-install.py", "--project", proj2)
    check("EMPLACEMENT étranger: annulation refusée, jamais supprimé", rc == 2 and tree(proj2) == before2, out)
    rc, out = runj(SCRIPTS / "apply-install.py", "--project", proj2, "--plan-sha256", "0" * 64)
    check("EMPLACEMENT étranger: installation refusée", rc == 2 and tree(proj2) == before2, out)

    # AGENTS.md existant
    proj3 = mk(new_dir("prep-agents"), {"AGENTS.md": "# à moi\n", "a.txt": "x"})
    before3 = tree(proj3)
    rc, data = prepare(proj3)
    check("AGENTS.md existant: non prévu, adaptation signalée, fichier intact",
          rc == 0 and not (proj3 / "EMPLACEMENT" / "AGENTS.md").exists() and any("AGENTS.md existe" in a for a in data["adaptations"])
          and tree(proj3, skip=("EMPLACEMENT",)) == before3, data)

    # dépôt source
    src = fake_source_repo("prep-srcrepo")
    before4 = tree(src, skip=(".git",))
    rc, data = prepare(src)
    check("dépôt source: prévisualisation refusée, rien créé", rc == 2 and tree(src, skip=(".git",)) == before4, data)
    rc, data = apply(src, "0" * 64)
    check("dépôt source: installation refusée", rc == 2, data)

    # projet déjà équipé
    for name in ("brain-main", "brain"):
        pe = mk(new_dir("prep-equipped"), {name + "/x.md": "x"})
        b = tree(pe)
        rc, data = prepare(pe)
        check("projet déjà équipé (%s/): refus, rien créé" % name, rc == 2 and tree(pe) == b, data)
    rc, data = runj(SCRIPTS / "prepare-install.py", "--source", Env.source, "--project", project_with_files("prep-badans"),
                    "--answers", "{pas du json")
    check("réponses illisibles: refus", rc == 2, data)


def doc_text(proj, name):
    return (proj / "brain" / "docs" / name).read_text(encoding="utf-8")


def test_install():
    proj = project_with_files("inst")
    others = tree(proj)
    rc, prep = prepare(proj)
    rc, data = apply(proj, prep["plan_sha256"])
    check("installation validée: code 0, bilan", rc == 0 and data.get("ok") and data["bilan"]["validateur_registre"] == "ok", data)
    check("installation: brain-main/ et brain/ créés",
          (proj / "brain-main" / "ROUTER.md").is_file() and (proj / "brain" / "registry" / "entries.jsonl").is_file()
          and all((proj / "brain" / "docs" / n).is_file() for n in ("VISION.md", "PROJECT.md", "REQUIREMENTS.md", "ARCHITECTURE.md", "WORKFLOW.md")))
    check("installation: autres fichiers intacts",
          all(tree(proj).get(k) == v for k, v in others.items()))
    check("installation: EMPLACEMENT supprimé", not (proj / "EMPLACEMENT").exists())
    check("installation: AGENTS.md créé depuis le modèle", (proj / "AGENTS.md").is_file() and "brain-main/" in (proj / "AGENTS.md").read_text(encoding="utf-8"))
    man = json.loads((proj / "brain-main" / "manifest.json").read_text(encoding="utf-8"))
    check("installation: manifeste (version, commit, date, empreintes, sans lui-même)",
          man["version"] == (BOOT / "VERSION").read_text(encoding="utf-8").strip() and man["source_commit"] and man["installed"]
          and "manifest.json" not in man["files"] and all(sha(proj / "brain-main" / k) == v for k, v in man["files"].items())
          and len(man["files"]) > 10, list(man)[:6])
    rc, out, _ = run(proj / "brain-main/skills/brain-capture/scripts/validate-registry.py", proj / "brain/registry/entries.jsonl")
    check("installation: validateur de registre OK sur le registre généré", rc == 0 and "OK bloquant: oui" in out, out)
    check("installation: registre vide", (proj / "brain/registry/entries.jsonl").read_bytes() == b"")
    check("installation: SCHEMA.md de brain-main identique à celui du dépôt source (brain/registry/SCHEMA.md)",
          sha(REPO / "brain-main/registry/SCHEMA.md") == sha(REPO / "brain/registry/SCHEMA.md"))
    check("installation: SCHEMA.md installé dans brain-main/registry/, pas dans brain/",
          sha(proj / "brain-main/registry/SCHEMA.md") == sha(REPO / "brain/registry/SCHEMA.md") and not (proj / "brain/registry/SCHEMA.md").exists())
    check("installation: aucun __pycache__", not list(proj.rglob("__pycache__")))
    vision, project_md = doc_text(proj, "VISION.md"), doc_text(proj, "PROJECT.md")
    check("installation: front matter conforme METADATA (6 champs obligatoires)",
          all(doc_text(proj, n).startswith("---\nmetadata_version: 1\n") and all(("\n%s:" % k) in doc_text(proj, n).split("\n---\n")[0]
              for k in ("title", "type", "description", "status", "created", "updated")) for n in
              ("VISION.md", "PROJECT.md", "REQUIREMENTS.md", "ARCHITECTURE.md", "WORKFLOW.md")))
    check("installation: réponses reprises (objectif, nature, identité, outils)",
          "Présenter l'activité" in vision and "Site web vitrine" in project_md and "Atelier Test" in project_md
          and "Next.js" in doc_text(proj, "ARCHITECTURE.md"))
    check("installation: modules notés comme intention, sans activation",
          "- recherche" in project_md and "rien n'est activé" in project_md)
    check("installation: aucun placeholder restant", not any("{{" in p.read_text(encoding="utf-8") for p in (proj / "brain").rglob("*.md")))
    rc, prep2 = prepare(proj)
    check("installation: projet désormais équipé -> nouvelle prévisualisation refusée", rc == 2, prep2)

    # réponses nulles
    projn = project_with_files("inst-null")
    rc, prep = prepare(projn, ANSWERS_NULL)
    rc, data = apply(projn, prep["plan_sha256"])
    texts = "".join(doc_text(projn, n) for n in ("VISION.md", "PROJECT.md", "ARCHITECTURE.md"))
    check("réponses nulles: non bloquantes, « À compléter. » partout, rien d'inventé",
          rc == 0 and texts.count("À compléter.") >= 6 and "{{" not in texts and "None" not in texts, data)
    rc, prep = runj(SCRIPTS / "prepare-install.py", "--source", Env.source, "--project", project_with_files("inst-empty-json"), "--answers", "{}")
    check("réponses vides ({}): acceptées", rc == 0, prep)

    # plan altéré
    pa = project_with_files("inst-alt")
    rc, prep = prepare(pa)
    before = tree(pa)
    plan_path = pa / "EMPLACEMENT" / "plan.json"
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    plan["reponses"]["nature"] = "altéré"
    plan_path.write_text(json.dumps(plan), encoding="utf-8")
    rc, data = apply(pa, prep["plan_sha256"])
    check("plan altéré: refus code 3, rien écrit", rc == 3 and tree(pa) == {**before, "EMPLACEMENT/plan.json": sha(plan_path)}
          and not (pa / "brain-main").exists(), data)
    rc, prep = prepare(pa)
    rc, data = apply(pa, "f" * 64)
    check("empreinte validée incorrecte: refus code 3", rc == 3 and not (pa / "brain-main").exists(), data)
    (pa / "EMPLACEMENT" / "brain" / "docs" / "VISION.md").write_text("altéré", encoding="utf-8")
    rc, data = apply(pa, prep["plan_sha256"])
    check("arborescence EMPLACEMENT altérée: refus code 3", rc == 3 and not (pa / "brain-main").exists() and not (pa / "brain").exists(), data)
    (pa / "EMPLACEMENT" / "intrus.txt").write_text("x", encoding="utf-8")
    rc, prep = prepare(pa)
    check("EMPLACEMENT marqué: refait proprement (intrus supprimé)", rc == 0 and not (pa / "EMPLACEMENT" / "intrus.txt").exists())
    (pa / "EMPLACEMENT" / "intrus.txt").write_text("x", encoding="utf-8")
    rc, data = apply(pa, prep["plan_sha256"])
    check("fichier en trop dans EMPLACEMENT: refus code 3", rc == 3 and not (pa / "brain-main").exists(), data)

    # conflit apparu après validation
    for what in ("AGENTS.md", "brain", "brain-main"):
        pc = project_with_files("inst-conflict")
        rc, prep = prepare(pc)
        if what == "AGENTS.md":
            (pc / what).write_text("apparu\n", encoding="utf-8")
        else:
            (pc / what).mkdir()
            (pc / what / "x.md").write_text("apparu\n", encoding="utf-8")
        b = tree(pc)
        rc, data = apply(pc, prep["plan_sha256"])
        check("conflit apparu après validation (%s): code 4, rien écrit, EMPLACEMENT conservé" % what,
              rc == 4 and tree(pc) == b and (pc / "EMPLACEMENT" / "plan.json").is_file() and what in " ".join(data.get("conflits", [])), data)
    rc, data = apply(project_with_files("inst-noprep"), "0" * 64)
    check("installation sans prévisualisation: refus", rc == 2, data)


IMPORTS = ["brain-main/conventions/README.md", "brain-main/conventions/TAXONOMY.md", "brain-main/README.md"]
DOCS5 = ("VISION.md", "PROJECT.md", "REQUIREMENTS.md", "ARCHITECTURE.md", "WORKFLOW.md")


def import_lines(text):
    """Lignes d'import @chemin hors blocs de code (une ligne qui commence par @)."""
    out, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if not fence and line.strip().startswith("@"):
            out.append(line.strip()[1:])
    return out


def stray_at(text):
    """Arobases hors blocs et hors code en ligne, en dehors des lignes d'import (import involontaire possible)."""
    cleaned, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if not fence and not line.strip().startswith("@"):
            cleaned.append(re.sub(r"`[^`]*`", "", line))
    return re.findall(r"(?:^|\s)@[\w./-]+", "\n".join(cleaned))


def test_root_files():
    # CLAUDE.md et AGENTS.md absents : créés, affichés dans le plan
    pn = mk(new_dir("root-none"), {"README.md": "# P" + NL})
    rc, prep = prepare(pn)
    plan = json.loads((pn / "EMPLACEMENT" / "plan.json").read_text(encoding="utf-8"))
    check("racine absente: CLAUDE.md et AGENTS.md dans le plan et dans le résumé",
          rc == 0 and prep["racine_creee"] == ["AGENTS.md", "CLAUDE.md"] and "CLAUDE.md" in plan["fichiers"] and "AGENTS.md" in plan["fichiers"]
          and prep["adaptations"] == [] and prep["conflits"] == [], prep)
    rc, data = apply(pn, prep["plan_sha256"])
    claude = (pn / "CLAUDE.md").read_text(encoding="utf-8") if (pn / "CLAUDE.md").is_file() else ""
    agents = (pn / "AGENTS.md").read_text(encoding="utf-8") if (pn / "AGENTS.md").is_file() else ""
    check("racine absente: CLAUDE.md = ligne @AGENTS.md, AGENTS.md créé, bilan", rc == 0 and claude == "@AGENTS.md" + NL
          and agents.startswith("---" + NL) and data["bilan"]["claude_md"] and data["bilan"]["agents_md"], data)
    check("AGENTS.md installé: dates rendues, aucun placeholder", "{{" not in agents and "created: " in agents, agents[:300])
    check("AGENTS.md installé: les 3 imports, dans l'ordre, hors de tout bloc de code", import_lines(agents) == IMPORTS, import_lines(agents))
    check("AGENTS.md installé: chaque fichier importé existe dans le projet installé",
          all((pn / rel).is_file() for rel in import_lines(agents)), [r for r in import_lines(agents) if not (pn / r).is_file()])
    check("AGENTS.md installé: ordre répété en clair (sans arobase), consigne -o, séparation brain/brain-main",
          "dans le même ordre" in agents and "`/brain -o`" in agents and "une seule fois par session" in agents
          and "jamais dans `brain-main/`" in agents and "À compléter" in agents, agents)
    check("AGENTS.md installé: METADATA.md et NAMING.md non importés, consigne obligatoire présente (modèle et guide)",
          not any("METADATA" in x or "NAMING" in x for x in import_lines(agents))
          and all(w in agents for w in ("Obligatoire avant de créer ou modifier un document", "brain-main/conventions/NAMING.md", "brain-main/conventions/METADATA.md"))
          and "Obligatoire avant de créer ou modifier un document" in (pn / "brain-main/README.md").read_text(encoding="utf-8"))
    check("AGENTS.md installé: aucun arobase hors des imports", stray_at(agents) == [], stray_at(agents))
    check("fichiers importés: aucun arobase involontaire (pas d'import en chaîne)",
          all(stray_at((pn / rel).read_text(encoding="utf-8")) == [] for rel in IMPORTS + ["brain-main/conventions/METADATA.md", "brain-main/conventions/NAMING.md"]),
          [(r, stray_at((pn / r).read_text(encoding="utf-8"))) for r in IMPORTS])
    check("modèles: CLAUDE.md = @AGENTS.md ; AGENTS.md importe dans l'ordre",
          (BOOT / "templates/CLAUDE.md").read_text(encoding="utf-8").strip() == "@AGENTS.md"
          and import_lines((BOOT / "templates/AGENTS.md").read_text(encoding="utf-8")) == IMPORTS)

    # les deux existent : jamais modifiés, adaptation exacte
    pe = mk(new_dir("root-both"), {"CLAUDE.md": "perso claude" + NL, "AGENTS.md": "perso agents" + NL})
    before = tree(pe)
    rc, prep = prepare(pe)
    ad = prep["adaptations"]
    check("racine existante: rien créé à la racine, adaptations signalées avec les lignes exactes",
          rc == 0 and prep["racine_creee"] == [] and len(ad) == 2
          and all("@" + rel in ad[0] for rel in IMPORTS) and ad[0].index("@" + IMPORTS[0]) < ad[0].index("@" + IMPORTS[-1])
          and "/brain -o" in ad[0] and ad[1].endswith("@AGENTS.md"), ad)
    check("racine existante: la prévisualisation n'écrit que EMPLACEMENT", tree(pe, skip=("EMPLACEMENT",)) == before)
    rc, data = apply(pe, prep["plan_sha256"])
    check("racine existante: installation ok, CLAUDE.md et AGENTS.md jamais modifiés",
          rc == 0 and tree(pe, skip=("brain-main", "brain")) == before and data["bilan"]["adaptations"] == ad, data)

    # AGENTS.md existe seul : CLAUDE.md créé, AGENTS.md intact
    pa = mk(new_dir("root-agents"), {"AGENTS.md": "perso agents" + NL})
    before = tree(pa)
    rc, prep = prepare(pa)
    rc2, data = apply(pa, prep["plan_sha256"])
    check("AGENTS.md seul: CLAUDE.md créé, AGENTS.md intact, adaptation = lignes à ajouter à AGENTS.md",
          rc == 0 and rc2 == 0 and prep["racine_creee"] == ["CLAUDE.md"] and (pa / "CLAUDE.md").read_text(encoding="utf-8") == "@AGENTS.md" + NL
          and sha(pa / "AGENTS.md") == before["AGENTS.md"] and len(prep["adaptations"]) == 1 and "@" + IMPORTS[0] in prep["adaptations"][0], prep)

    # CLAUDE.md existe seul : AGENTS.md créé, CLAUDE.md intact, ligne @AGENTS.md à ajouter
    pc = mk(new_dir("root-claude"), {"CLAUDE.md": "perso claude" + NL})
    rc, prep = prepare(pc)
    rc2, data = apply(pc, prep["plan_sha256"])
    check("CLAUDE.md seul: AGENTS.md créé, CLAUDE.md intact, adaptation = ligne @AGENTS.md",
          rc == 0 and rc2 == 0 and prep["racine_creee"] == ["AGENTS.md"] and (pc / "CLAUDE.md").read_text(encoding="utf-8") == "perso claude" + NL
          and len(prep["adaptations"]) == 1 and prep["adaptations"][0].endswith("@AGENTS.md"), prep)

    # déjà conforme : aucune adaptation
    done = "".join("@" + r + NL for r in IMPORTS) + "- Si `brain/docs/` contient encore « À compléter », proposer `/brain -o` une seule fois par session." + NL
    pd = mk(new_dir("root-done"), {"CLAUDE.md": "@AGENTS.md" + NL, "AGENTS.md": done})
    rc, prep = prepare(pd)
    check("racine déjà conforme: aucune adaptation, rien créé", rc == 0 and prep["adaptations"] == [] and prep["racine_creee"] == [], prep)

    # conflit apparu après validation sur CLAUDE.md
    pk = mk(new_dir("root-conflict"), {"README.md": "x"})
    rc, prep = prepare(pk)
    (pk / "CLAUDE.md").write_text("apparu" + NL, encoding="utf-8")
    b = tree(pk)
    rc, data = apply(pk, prep["plan_sha256"])
    check("conflit apparu sur CLAUDE.md: code 4, rien écrit", rc == 4 and tree(pk) == b and "CLAUDE.md" in data.get("conflits", []), data)


def installed_project(name, answers):
    proj = mk(new_dir(name), {"README.md": "# P" + NL})
    rc, prep = prepare(proj, answers)
    rc, data = apply(proj, prep["plan_sha256"])
    assert rc == 0, data
    return proj


def test_generated_brain():
    forbidden = re.compile(r"2brain|brain-main|bootstrap|capture|cap-", re.I)
    for label, answers in (("réponses complètes", ANSWERS_FULL), ("réponses nulles", ANSWERS_NULL)):
        proj = installed_project("gen-" + label.split()[1], answers)
        files = sorted(p.relative_to(proj / "brain").as_posix() for p in (proj / "brain").rglob("*") if p.is_file())
        check("brain/ généré (%s): seulement les 5 documents et registry/entries.jsonl" % label,
              files == sorted(["docs/" + n for n in DOCS5] + ["registry/entries.jsonl"]), files)
        dirs = sorted(p.relative_to(proj / "brain").as_posix() for p in (proj / "brain").rglob("*") if p.is_dir())
        check("brain/ généré (%s): seulement docs/ et registry/" % label, dirs == ["docs", "registry"], dirs)
        hits = []
        for p in (proj / "brain").rglob("*"):
            rel = p.relative_to(proj / "brain").as_posix()
            if forbidden.search(rel):
                hits.append((rel, "chemin"))
            if p.is_file():
                for m in forbidden.finditer(p.read_text(encoding="utf-8")):
                    hits.append((rel, m.group(0)))
        check("brain/ généré (%s): aucune occurrence (insensible à la casse) de 2brain, brain-main, bootstrap, capture, CAP-" % label, not hits, hits[:5])
        texts = [p.read_text(encoding="utf-8") for p in (proj / "brain").rglob("*.md")]
        check("brain/ généré (%s): ni « créé à l'installation » ni renvoi au standard du dépôt" % label,
              not any("installation" in t.lower() or "dépôt" in t for t in texts))
    projn = installed_project("gen-fm", ANSWERS_NULL)
    check("brain/ généré: front matter METADATA, plan en 6 sections, réponses vides en « À compléter. »",
          all(doc_text(projn, n).startswith("---" + NL + "metadata_version: 1" + NL) and doc_text(projn, n).count(NL + "## ") == 6 for n in DOCS5)
          and doc_text(projn, "VISION.md").count("À compléter.") >= 4)
    check("brain/ généré: PROJECT.md note les modules comme intention seulement",
          "Modules envisagés (intention seulement ; rien n'est activé)" in doc_text(installed_project("gen-mod", ANSWERS_FULL), "PROJECT.md"))


def test_status_todo():
    home = new_dir("home-todo")
    proj = installed_project("todo-proj", ANSWERS_NULL)
    rc, st = status(proj, home)
    check("status: installation neuve -> 5 documents « À compléter », -o suggéré",
          st["brain"]["etat"] == "complet" and st["brain"]["documents_a_completer"] == 5
          and any("/brain -o" in n for n in st["notes"]), st)
    rc, out, _ = run(ACCOUNT / "status.py", "--project", proj, "--home", home, "--offline")
    check("status: sortie texte avec le nombre et la suggestion de -o", "encore « À compléter » : 5" in out and "/brain -o" in out, out)
    for n in ("VISION.md", "PROJECT.md"):
        path = proj / "brain" / "docs" / n
        path.write_text(path.read_text(encoding="utf-8").replace("À compléter", "Renseigné"), encoding="utf-8")
    rc, st = status(proj, home)
    check("status: 2 documents remplis -> 3 restants, noms listés",
          st["brain"]["documents_a_completer"] == 3
          and st["brain"]["documents_a_completer_noms"] == ["ARCHITECTURE.md", "REQUIREMENTS.md", "WORKFLOW.md"], st["brain"])
    for n in ("REQUIREMENTS.md", "ARCHITECTURE.md", "WORKFLOW.md"):
        path = proj / "brain" / "docs" / n
        path.write_text(path.read_text(encoding="utf-8").replace("À compléter", "Renseigné"), encoding="utf-8")
    before = tree(proj)
    rc, st = status(proj, home)
    check("status: 0 document « À compléter » -> aucune suggestion de -o, brain complet",
          st["brain"]["documents_a_completer"] == 0 and st["brain"]["etat"] == "complet" and not any("/brain -o" in n for n in st["notes"]), st)
    check("status: lecture seule", tree(proj) == before)
    rc, st = status(mk(new_dir("todo-abs"), {"a.txt": "x"}), home)
    check("status: brain absent -> 0 et pas de suggestion",
          st["brain"]["documents_a_completer"] == 0 and not any("/brain -o" in n for n in st["notes"]), st)


def test_onboarding_files():
    skill = REPO / "brain-main/skills/brain-onboarding/SKILL.md"
    text = skill.read_text(encoding="utf-8")
    head = text.split("---")[1]
    check("onboarding: SKILL.md existe, front matter sur le modèle de brain-capture", skill.is_file()
          and "name: brain-onboarding" in head and "disable-model-invocation: true" in head and "description:" in head
          and "version:" in head, head)
    check("onboarding: au plus 80 lignes", len(text.splitlines()) <= 80, len(text.splitlines()))
    forbidden = ("UPPER_SNAKE_CASE", "kebab-case", "metadata_version", "SemVer", "snake_case", "camelCase", "TAXONOMY.md")
    check("onboarding: aucune convention reprise", not any(w in text for w in forbidden))
    check("onboarding: marqueurs confirmé/hypothèse/à compléter, validation explicite, état par status.py, renvoi à /brain -i",
          all(w in text for w in ("`confirmé`", "`hypothèse`", "`à compléter`", "validation explicite", "status.py", "/brain -i")), text[:200])
    check("onboarding: ne modifie ni le registre ni brain-main/, ne décide rien, ne code rien",
          "ni le registre, ni `brain-main/`" in text and "Ne rien décider, ne rien coder" in text)
    check("onboarding: /compact absent", "/compact" not in text)
    proj = installed_project("onb-proj", ANSWERS_FULL)
    check("onboarding: présent dans le projet installé", sha(proj / "brain-main/skills/brain-onboarding/SKILL.md") == sha(skill))
    guide = (REPO / "brain-main/README.md").read_text(encoding="utf-8")
    check("guide: au plus 80 lignes", len(guide.splitlines()) <= 80, len(guide.splitlines()))
    check("guide: chaque commande présente", all(("`%s`" % c) in guide for c in
          ("/brain", "/brain -i", "/brain -u", "/brain -o", "/brain -c", "/brain -c <fichier>", "/brain -c 1", "/brain -s <sujet>", "/brain -r")))
    paths = re.findall(r"`(brain-main/[\w./-]+\.md)`", guide)
    check("guide: chemins de fichiers cités existent dans le projet installé (et skill d'onboarding et de capture cités)",
          bool(paths) and all((proj / p).is_file() for p in paths)
          and "brain-main/skills/brain-onboarding/SKILL.md" in paths and "brain-main/skills/brain-capture/SKILL.md" in paths,
          [p for p in paths if not (proj / p).is_file()])
    check("guide: règles (append only, proposition, locked, commit, convention avant création) et /compact absent",
          all(w in guide for w in ("append only", "Une proposition n'est pas une décision", "locked: true", "commit", "lire la convention concernée"))
          and "/compact" not in guide)
    check("guide: aucune copie de convention", not any(w in guide for w in ("UPPER_SNAKE_CASE", "kebab-case", "SemVer")))
    check("guide: aucune mention de documents inexistants", "COMMANDS.md" not in guide and "BOOTSTRAP.md" not in guide)


def pick(manifest_files, prefix_list):
    for p in prefix_list:
        if p in manifest_files:
            return p
    raise RuntimeError("fichier introuvable : %r" % prefix_list)


def test_update():
    upd = SCRIPTS / "update-brain-main.py"
    proj = project_with_files("upd")
    rc, prep = prepare(proj)
    rc, data = apply(proj, prep["plan_sha256"])
    bm = proj / "brain-main"
    man = json.loads((bm / "manifest.json").read_text(encoding="utf-8"))
    files = man["files"]
    names = [f for f in sorted(files) if f.endswith(".md") and not f.startswith("bootstrap/")]
    A, B, C, D, E, F, G = [pick(files, [n]) for n in names[:7]]
    # source 2 : copie modifiée
    s2root = new_dir("upd-src2")
    shutil.copytree(Env.source, s2root / "brain-main")
    s2 = s2root / "brain-main"
    (s2 / A).write_text((s2 / A).read_text(encoding="utf-8") + "\nmodif source A\n", encoding="utf-8")        # id / modifié
    (s2 / B).unlink()                                                                                          # id / supprimé
    (s2 / D).write_text("D version source\n", encoding="utf-8")                                                # mod / mod différemment
    (s2 / E).unlink()                                                                                          # mod / supprimé
    (s2 / G).write_text("G version source\n", encoding="utf-8")                                                # supprimé loc / modifié
    (s2 / "nouveau.md").write_text("nouveau\n", encoding="utf-8")                                              # absent / nouveau
    (s2 / "extra.md").write_text("extra source\n", encoding="utf-8")                                           # hors manifeste / autre contenu
    tpl = pick(files, ["bootstrap/templates/brain/docs/VISION.md"])
    (s2 / tpl).write_text((s2 / tpl).read_text(encoding="utf-8") + "\nmodèle changé\n", encoding="utf-8")
    (s2 / "bootstrap" / "VERSION").write_text("0.2.0\n", encoding="utf-8")
    # état local
    (bm / C).write_text("C modifié localement\n", encoding="utf-8")                                            # mod / identique
    (bm / D).write_text("D modifié localement\n", encoding="utf-8")
    (bm / E).write_text("E modifié localement\n", encoding="utf-8")
    (bm / F).unlink()                                                                                          # supprimé loc / identique
    (bm / G).unlink()
    (bm / "extra.md").write_text("extra local\n", encoding="utf-8")
    (bm / "perso.md").write_text("fichier local seulement\n", encoding="utf-8")

    brain_before = tree(proj / "brain")
    proj_before = tree(proj)
    rc, plan = runj(upd, "--source", s2, "--project", proj)
    paths = lambda k: sorted(e["path"] if isinstance(e, dict) else e for e in plan.get(k, []))
    check("mise à jour: plan sans écriture", rc == 0 and plan["ok"] and plan["ecrit"] is False and tree(proj) == proj_before, plan)
    check("mise à jour: identique/modifié -> mise à jour", A in paths("update") and tpl in paths("update") and "bootstrap/VERSION" in paths("update"), plan)
    check("mise à jour: identique/supprimé -> suppression proposée", paths("delete") == [B], plan)
    check("mise à jour: modifié/identique -> conservé", C in plan["kept"], plan)
    check("mise à jour: modifié/(modifié autrement|supprimé) -> conflits",
          {D, E} <= set(paths("conflicts")), plan["conflicts"])
    check("mise à jour: absent/nouveau -> ajout", "nouveau.md" in paths("add"), plan)
    check("mise à jour: hors manifeste avec autre contenu -> conflit", "extra.md" in paths("conflicts"), plan["conflicts"])
    check("mise à jour: supprimé localement/identique -> conservé supprimé, signalé", F in plan["kept_deleted"], plan)
    check("mise à jour: supprimé localement/modifié -> conflit", G in paths("conflicts"), plan["conflicts"])
    check("mise à jour: fichier local hors manifeste sans équivalent source -> signalé", "perso.md" in plan["local_only"], plan)
    check("mise à jour: adaptations_brain signalées (modèle changé)", any(a["path"] == tpl for a in plan["adaptations_brain"]), plan["adaptations_brain"])
    check("mise à jour: versions et plan_sha256", plan["versions"]["source"] == "0.2.0" and len(plan["plan_sha256"]) == 64, plan["versions"])

    rc, bad = runj(upd, "--source", s2, "--project", proj, "--apply", "--plan-sha256", "0" * 64)
    check("mise à jour: --apply avec empreinte erronée refusé (3), rien écrit", rc == 3 and tree(proj) == proj_before, bad)
    rc, bad = runj(upd, "--source", s2, "--project", proj, "--apply")
    check("mise à jour: --apply sans empreinte refusé", rc == 2 and tree(proj) == proj_before, bad)

    manifest_before = json.loads((bm / "manifest.json").read_text(encoding="utf-8"))
    rc, done = runj(upd, "--source", s2, "--project", proj, "--apply", "--plan-sha256", plan["plan_sha256"])
    check("mise à jour: --apply ok", rc == 0 and done.get("ok") and done["ecrit"], done)
    check("mise à jour: fichier mis à jour, ajout, suppression",
          (bm / A).read_bytes() == (s2 / A).read_bytes() and (bm / "nouveau.md").read_text(encoding="utf-8") == "nouveau\n" and not (bm / B).exists())
    check("mise à jour: modifications locales jamais écrasées (conservé, conflits, hors manifeste)",
          (bm / C).read_text(encoding="utf-8") == "C modifié localement\n" and (bm / D).read_text(encoding="utf-8") == "D modifié localement\n"
          and (bm / E).read_text(encoding="utf-8") == "E modifié localement\n" and (bm / "extra.md").read_text(encoding="utf-8") == "extra local\n"
          and (bm / "perso.md").is_file())
    check("mise à jour: supprimés localement restent supprimés (identique et conflit)", not (bm / F).exists() and not (bm / G).exists())
    man2 = json.loads((bm / "manifest.json").read_text(encoding="utf-8"))
    mf = man2["files"]
    check("mise à jour: manifeste mis à jour pour les seuls fichiers appliqués",
          mf[A] == sha(s2 / A) and mf["nouveau.md"] == sha(s2 / "nouveau.md") and B not in mf and man2["version"] == "0.2.0", man2["version"])
    check("mise à jour: fichiers en conflit gardent leur empreinte d'origine au manifeste",
          mf[D] == manifest_before["files"][D] and mf[E] == manifest_before["files"][E] and mf[G] == manifest_before["files"][G]
          and mf[C] == manifest_before["files"][C] and "extra.md" not in mf)
    check("mise à jour: brain/ strictement inchangé (empreintes)", tree(proj / "brain") == brain_before)
    check("mise à jour: rien écrit hors brain-main/", tree(proj, skip=("brain-main",)) == {k: v for k, v in proj_before.items() if not k.startswith("brain-main")})
    rc, plan2 = runj(upd, "--source", s2, "--project", proj)
    check("mise à jour: second plan sans mise à jour, mêmes conflits",
          rc == 0 and not plan2["update"] and not plan2["add"] and not plan2["delete"] and {D, E, G, "extra.md"} <= set(e["path"] for e in plan2["conflicts"]), plan2)

    # source modifiée entre le plan et l'application
    proj_b = project_with_files("upd-race")
    rc, prep = prepare(proj_b)
    apply(proj_b, prep["plan_sha256"])
    s3root = new_dir("upd-src3")
    shutil.copytree(Env.source, s3root / "brain-main")
    s3 = s3root / "brain-main"
    (s3 / "nouveau.md").write_text("v1\n", encoding="utf-8")
    rc, plan3 = runj(upd, "--source", s3, "--project", proj_b)
    (s3 / "nouveau.md").write_text("v2\n", encoding="utf-8")
    b = tree(proj_b)
    rc, out = runj(upd, "--source", s3, "--project", proj_b, "--apply", "--plan-sha256", plan3["plan_sha256"])
    check("mise à jour: plan recalculé différent -> refus (3), rien écrit", rc == 3 and tree(proj_b) == b, out)

    # refus
    srcrepo = fake_source_repo("upd-srcrepo")
    mk(srcrepo, {"brain-main/manifest.json": json.dumps({"version": "0", "files": {}})})
    b = tree(srcrepo, skip=(".git",))
    rc, out = runj(upd, "--source", s2, "--project", srcrepo)
    check("mise à jour: refus dans un faux dépôt source (même avec manifeste)", rc == 2 and tree(srcrepo, skip=(".git",)) == b, out)
    noman = mk(new_dir("upd-noman"), {"brain-main/README.md": "x"})
    b = tree(noman)
    rc, out = runj(upd, "--source", s2, "--project", noman)
    check("mise à jour: refus sans manifeste", rc == 2 and tree(noman) == b, out)
    nobm = mk(new_dir("upd-nobm"), {"a.txt": "x"})
    rc, out = runj(upd, "--source", s2, "--project", nobm)
    check("mise à jour: refus sans brain-main/", rc == 2, out)
    evil = project_with_files("upd-evil")
    rc, prep = prepare(evil)
    apply(evil, prep["plan_sha256"])
    mpath = evil / "brain-main" / "manifest.json"
    m = json.loads(mpath.read_text(encoding="utf-8"))
    m["files"]["../brain/docs/VISION.md"] = "0" * 64
    mpath.write_text(json.dumps(m), encoding="utf-8")
    b = tree(evil)
    rc, out = runj(upd, "--source", s3, "--project", evil)
    check("mise à jour: chemin sortant de brain-main/ dans le manifeste -> refus", rc == 2 and tree(evil) == b, out)


def settings_fixture(home, extra=None):
    data = {
        "permissions": {"allow": ["mcp__x"]},
        "env": {"A": "1"},
        "hooks": {
            "SessionStart": [{"hooks": [{"type": "command", "command": "echo", "args": ["autre"]}]}],
            "PostToolUse": [{"matcher": "Edit", "hooks": [{"type": "command", "command": "true"}]}],
        },
    }
    if extra:
        data.update(extra)
    p = home / ".claude" / "settings.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=4), encoding="utf-8")
    return data


def our_groups(settings):
    return [g for g in settings["hooks"]["SessionStart"]
            if any(str(a).replace("\\", "/").endswith("skills/brain/session-start.py") for h in g["hooks"] for a in h.get("args", []))]


def test_account():
    inst = SCRIPTS / "install-account.py"
    home = new_dir("home-acc")
    orig = settings_fixture(home)
    sp = home / ".claude" / "settings.json"
    orig_hash = sha(sp)
    rc, out = runj(inst, "--home", home, "--dry-run")
    check("compte: --dry-run n'écrit rien", rc == 0 and out["dry_run"] and out["actions"] and sha(sp) == orig_hash
          and not (home / ".claude/skills").exists() and not (home / ".claude/2brain-bootstrap").exists(), out)
    rc, out = runj(inst, "--home", home)
    s = json.loads(sp.read_text(encoding="utf-8"))
    check("compte: installation ok", rc == 0 and out["ok"], out)
    backups = list((home / ".claude/2brain-bootstrap/backups").glob("settings.*.json"))
    check("compte: sauvegarde de settings.json présente et identique à l'original",
          len(backups) == 1 and sha(backups[0]) == orig_hash, backups)
    check("compte: autres clés et autres hooks conservés",
          s["permissions"] == orig["permissions"] and s["env"] == orig["env"] and s["hooks"]["PostToolUse"] == orig["hooks"]["PostToolUse"]
          and s["hooks"]["SessionStart"][0] == orig["hooks"]["SessionStart"][0])
    groups = our_groups(s)
    check("compte: un groupe SessionStart, matcher startup, forme sans shell (command=python, args=[script])",
          len(groups) == 1 and groups[0]["matcher"] == "startup" and groups[0]["hooks"][0]["type"] == "command"
          and groups[0]["hooks"][0]["command"] == sys.executable and len(groups[0]["hooks"][0]["args"]) == 1
          and "shell" not in groups[0]["hooks"][0], groups)
    sd = home / ".claude/skills/brain"
    skill = (sd / "SKILL.md").read_text(encoding="utf-8")
    check("compte: __PYTHON__ remplacé par le chemin absolu de Python",
          "__PYTHON__" not in skill and Path(sys.executable).as_posix() in skill)
    check("compte: fichiers posés (SKILL.md, hook, status, fetch, VERSION)",
          all((sd / n).is_file() for n in ("SKILL.md", "session-start.py", "status.py", "fetch-source.py", "VERSION"))
          and (sd / "VERSION").read_text(encoding="utf-8").strip() == (BOOT / "VERSION").read_text(encoding="utf-8").strip())
    check("compte: le script de hook installé existe au chemin enregistré", Path(groups[0]["hooks"][0]["args"][0]).is_file())
    empty = new_dir("acc-empty")
    rc, o, e = run(Path(groups[0]["hooks"][0]["args"][0]), inp=json.dumps({"cwd": str(empty), "source": "startup"}))
    check("compte: le hook installé répond dans un dossier vide", rc == 0 and "installer 2brain" in o, o)
    # réinstallation
    rc, out = runj(inst, "--home", home)
    s2 = json.loads(sp.read_text(encoding="utf-8"))
    check("compte: réinstallation sans doublon", rc == 0 and len(our_groups(s2)) == 1 and len(s2["hooks"]["SessionStart"]) == 2, s2["hooks"])
    check("compte: deuxième sauvegarde distincte", len(list((home / ".claude/2brain-bootstrap/backups").glob("settings.*.json"))) == 2)

    # désinstallation
    rc, out = runj(inst, "--home", home, "--uninstall")
    s3 = json.loads(sp.read_text(encoding="utf-8"))
    check("compte: --uninstall retire son groupe et son dossier, garde le reste",
          rc == 0 and not sd.exists() and not our_groups(s3) and s3["hooks"]["SessionStart"] == orig["hooks"]["SessionStart"]
          and s3["hooks"]["PostToolUse"] == orig["hooks"]["PostToolUse"] and s3["permissions"] == orig["permissions"], out)
    check("compte: --uninstall garde les sauvegardes et affiche ce qui est retiré",
          len(list((home / ".claude/2brain-bootstrap/backups").glob("settings.*.json"))) >= 3 and any("suppression" in a for a in out["actions"]), out)
    rc, out = runj(inst, "--home", home, "--uninstall")
    check("compte: --uninstall répété sans effet", rc == 0 and "rien à retirer" in out["actions"], out)

    # skill étranger
    home2 = new_dir("home-foreign")
    settings_fixture(home2)
    mk(home2 / ".claude/skills/brain", {"SKILL.md": "étranger\n"})
    b = tree(home2)
    rc, out = runj(inst, "--home", home2)
    check("compte: refus d'écraser un skills/brain étranger, rien écrit", rc == 2 and tree(home2) == b, out)
    rc, out = runj(inst, "--home", home2, "--uninstall")
    check("compte: --uninstall ne supprime pas un skills/brain étranger", rc == 0 and (home2 / ".claude/skills/brain/SKILL.md").is_file(), out)

    # remplacement de la sonde
    home3 = new_dir("home-probe")
    probe_settings = {
        "model": "x",
        "hooks": {"SessionStart": [
            {"hooks": [{"type": "command", "command": sys.executable,
                        "args": [str(home3 / ".claude/2brain-sonde/session_start.py")]}]},
            {"hooks": [{"type": "command", "command": "echo", "args": ["garde"]}]},
        ]},
    }
    mk(home3 / ".claude", {"settings.json": json.dumps(probe_settings), "2brain-sonde/session_start.py": "pass\n",
                           "2brain-sonde/hook.log": "log\n", "2brain-sonde/settings.json.avant-sonde": "{\n    \"avant\": \"é\"\n}", "skills/brain/SKILL.md": "sonde\n", "skills/autre/SKILL.md": "autre\n"})
    rc, out = runj(inst, "--home", home3)
    check("sonde: sans --replace-probe, refus", rc == 2 and (home3 / ".claude/2brain-sonde").exists(), out)
    rc, out = runj(inst, "--home", home3, "--replace-probe", "--dry-run")
    check("sonde: --dry-run annonce la copie de la sauvegarde d'avant-sonde, sans écrire",
          rc == 0 and any("settings.avant-sonde.json" in a for a in out["actions"]) and not (home3 / ".claude/2brain-bootstrap").exists(), out)
    check("sonde: --replace-probe --dry-run n'écrit rien", rc == 0 and (home3 / ".claude/2brain-sonde").exists()
          and (home3 / ".claude/skills/brain/SKILL.md").read_text(encoding="utf-8") == "sonde\n", out)
    probe_bytes = (home3 / ".claude/2brain-sonde/settings.json.avant-sonde").read_bytes()
    rc, out = runj(inst, "--home", home3, "--replace-probe")
    s4 = json.loads((home3 / ".claude/settings.json").read_text(encoding="utf-8"))
    flat = json.dumps(s4)
    check("sonde: --replace-probe retire groupe de la sonde, skills/brain et 2brain-sonde, installe /brain",
          rc == 0 and "2brain-sonde" not in flat and not (home3 / ".claude/2brain-sonde").exists()
          and (home3 / ".claude/skills/brain/VERSION").is_file() and "sonde" not in (home3 / ".claude/skills/brain/SKILL.md").read_text(encoding="utf-8").lower().split("---")[1]
          and len(our_groups(s4)) == 1 and any("garde" in json.dumps(g) for g in s4["hooks"]["SessionStart"])
          and s4["model"] == "x" and (home3 / ".claude/skills/autre/SKILL.md").is_file(), out)

    kept = home3 / ".claude/2brain-bootstrap/backups/settings.avant-sonde.json"
    check("sonde: sauvegarde d'avant-sonde conservée à l'identique après --replace-probe",
          kept.is_file() and kept.read_bytes() == probe_bytes and "é".encode("utf-8") in probe_bytes
          and any("settings.avant-sonde.json" in a for a in out["actions"]), out)
    home3b = new_dir("home-probe-over")
    mk(home3b / ".claude", {"settings.json": "{}", "2brain-sonde/settings.json.avant-sonde": "nouveau", "skills/brain/SKILL.md": "sonde\n",
                            "2brain-bootstrap/backups/settings.avant-sonde.json": "ancien"})
    rc, out = runj(inst, "--home", home3b, "--replace-probe")
    bdir = home3b / ".claude/2brain-bootstrap/backups"
    check("sonde: copie d'avant-sonde déjà présente jamais écrasée (suffixe)",
          rc == 0 and (bdir / "settings.avant-sonde.json").read_text(encoding="utf-8") == "ancien"
          and (bdir / "settings.avant-sonde-1.json").read_text(encoding="utf-8") == "nouveau", out)

    # format de settings.json conservé
    home7 = new_dir("home-format")
    fixture = {"model": "é", "permissions": {"allow": ["a"]}, "hooks": {"PostToolUse": [{"hooks": [{"type": "command", "command": "true"}]}]}}
    raw7 = json.dumps(fixture, indent=4, ensure_ascii=False)
    (home7 / ".claude").mkdir()
    (home7 / ".claude/settings.json").write_bytes(raw7.encode("utf-8"))
    rc, out = runj(inst, "--home", home7)
    new7 = (home7 / ".claude/settings.json").read_bytes().decode("utf-8")
    d7 = json.loads(new7)
    ours7 = d7.pop("hooks")
    orig7 = dict(fixture)
    orig7.pop("hooks")
    check("format: 4 espaces, LF, sans retour final conservés (é non échappé)",
          rc == 0 and new7.split("\n")[1].startswith('    "') and "\r" not in new7
          and not new7.endswith("\n") and "é" in new7 and "\\u00e9" not in new7, new7[:120])
    check("format: seul le bloc hooks diffère, ordre des clés conservé",
          d7 == orig7 and list(json.loads(new7)) == ["model", "permissions", "hooks"]
          and ours7["PostToolUse"] == fixture["hooks"]["PostToolUse"] and len(ours7["SessionStart"]) == 1, out)
    home8 = new_dir("home-format-crlf")
    (home8 / ".claude").mkdir()
    (home8 / ".claude/settings.json").write_bytes((json.dumps({"a": 1}, indent="\t").replace("\n", "\r\n") + "\r\n").encode("utf-8"))
    rc, out = runj(inst, "--home", home8)
    new8 = (home8 / ".claude/settings.json").read_bytes().decode("utf-8")
    check("format: tabulations, CRLF et retour final conservés",
          rc == 0 and new8.endswith("\r\n") and '\r\n\t"a"' in new8 and "\n" not in new8.replace("\r\n", ""), repr(new8[:60]))

    # JSON invalide
    home4 = new_dir("home-badjson")
    mk(home4 / ".claude", {"settings.json": "{ pas du json"})
    b = tree(home4)
    rc, out = runj(inst, "--home", home4)
    check("compte: settings.json invalide -> refus, rien écrit", rc == 2 and tree(home4) == b, out)
    rc, out = runj(inst, "--home", home4, "--uninstall")
    check("compte: settings.json invalide -> --uninstall refuse aussi", rc == 2 and tree(home4) == b, out)
    home5 = new_dir("home-badshape")
    mk(home5 / ".claude", {"settings.json": json.dumps({"hooks": {"SessionStart": "oops"}})})
    b = tree(home5)
    rc, out = runj(inst, "--home", home5)
    check("compte: hooks.SessionStart mal formé -> refus, rien écrit", rc == 2 and tree(home5) == b, out)

    # sans settings.json
    home6 = new_dir("home-nosettings")
    rc, out = runj(inst, "--home", home6)
    s6 = json.loads((home6 / ".claude/settings.json").read_text(encoding="utf-8"))
    check("compte: sans settings.json, créé avec le seul hook", rc == 0 and len(our_groups(s6)) == 1 and set(s6) == {"hooks"}, s6)


def test_skill():
    text = (ACCOUNT / "SKILL.md").read_text(encoding="utf-8")
    head = text.split("---")[1]
    check("SKILL.md: front matter (name, argument-hint, disable-model-invocation: true)",
          "name: brain" in head and "argument-hint: [-i | -u | -o | -c | -c fichier | -c 1 | -s sujet | -r]" in head and "disable-model-invocation: true" in head, head)
    check("SKILL.md: pas de syntaxe !", "!`" not in text and "```!" not in text)
    check("SKILL.md: aiguille -c -s -r vers les scripts et vers brain-capture (plus de renvoi au lot 3)", "lot 3" not in text and "read-session.py" in text and "brain-main/skills/brain-capture/SKILL.md" in text)
    check("SKILL.md: règles de validation, délégation worker-sonnet, jamais de simulation",
          "worker-sonnet" in text and "Jamais de simulation" in text and "validation" in text)
    forbidden = ("UPPER_SNAKE_CASE", "kebab-case", "metadata_version", "SemVer", "snake_case", "TAXONOMY")
    check("SKILL.md: aucune copie de convention", not any(w in text for w in forbidden))
    check("SKILL.md: léger (au plus 70 lignes)", len(text.splitlines()) <= 70, len(text.splitlines()))
    check("SKILL.md: -o aiguille vers le skill d'onboarding, fin de -i propose -o et une nouvelle conversation",
          "brain-main/skills/brain-onboarding/SKILL.md" in text and "/brain -o" in text and "nouvelle conversation" in text)
    check("SKILL.md: /compact seulement pour l'interdire", all(re.search(r"jamais|Jamais|interdit", ln) for ln in text.splitlines() if "/compact" in ln))
    check("SKILL.md: __PYTHON__ présent avant installation", "__PYTHON__" in text)
    check("VERSION: 0.3.0", (BOOT / "VERSION").read_text(encoding="utf-8").strip() == "0.3.0")
    # chaque script est autonome : aucun import local
    local_names = {p.stem.replace("-", "_") for p in list(SCRIPTS.glob("*.py")) + list(ACCOUNT.glob("*.py"))}
    bad = []
    for p in list(SCRIPTS.glob("*.py")) + list(ACCOUNT.glob("*.py")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith(("import ", "from ")):
                mod = line.split()[1].split(".")[0]
                if mod in local_names:
                    bad.append((p.name, line))
    check("scripts: aucun import local (autonomes)", not bad, bad)


def main():
    global TMP
    sys.stdout.reconfigure(encoding="utf-8")
    TMP = tempfile.mkdtemp(prefix="2brain-bootstrap-tests-")
    try:
        for name, fn in (("hook", test_hook), ("status", test_status), ("fetch", test_fetch)):
            try:
                fn()
            except Exception:
                check("exception dans le groupe " + name, False, traceback.format_exc()[-600:])
        try:
            setup_fetched()
        except Exception:
            check("exception dans la préparation de la source", False, traceback.format_exc()[-600:])
        for name, fn in (("prepare/cancel", test_prepare_cancel), ("installation", test_install),
                         ("racine", test_root_files), ("brain généré", test_generated_brain),
                         ("status -o", test_status_todo), ("onboarding", test_onboarding_files),
                         ("mise à jour", test_update), ("compte", test_account), ("skill", test_skill)):
            try:
                fn()
            except Exception:
                check("exception dans le groupe " + name, False, traceback.format_exc()[-600:])
    finally:
        rmtree(TMP)
    ok = sum(1 for _, r in RESULTS if r)
    print("\nRÉSULTAT : %d PASS, %d FAIL sur %d" % (ok, len(RESULTS) - ok, len(RESULTS)))
    return 0 if ok == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
