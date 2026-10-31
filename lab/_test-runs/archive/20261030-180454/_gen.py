# -*- coding: utf-8 -*-
"""Fresh /brain-capture 0.1.2 from conversation-reference-1.txt — NOT a transform of prior JSONL."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
OUT = OUT_DIR / "entries.jsonl"
STORAGE = "brain/registry/_test-runs/20261030-180454/entries.jsonl"
CREATED = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
ORIGIN = {
    "source": "brain/sources/conversation-reference-1.txt",
    "url": "https://chatgpt.com/share/6ae3fb90-b6bc-83ed-b432-22f8963f96d8",
}
N = 0
E: list[dict] = []


def add(
    *,
    type: str,
    intention: str,
    author: str,
    title: str,
    content: str,
    evidence: str,
    position=None,
    space: str = "atelier",
    validation: str = "none",
    approval_scope=None,
    confidence: str = "high",
    relations: list | None = None,
    feeds_doc: str | None = None,
    clickup_ref: str | None = None,
    tags: list | None = None,
) -> str:
    global N
    N += 1
    cid = f"CAP-{N:03d}"
    if validation == "explicit_user_approval":
        assert approval_scope in ("item", "set")
        ab = "user"
    else:
        assert approval_scope is None
        ab = None
    if author == "user" and type in ("observation", "event", "idea"):
        assert validation == "none"
    E.append(
        {
            "id": cid,
            "type": type,
            "intention": intention,
            "position": position,
            "status": "extracted",
            "space": space,
            "validation": validation,
            "author": author,
            "approved_by": ab,
            "approval_scope": approval_scope,
            "title": title,
            "content": content,
            "evidence": evidence,
            "confidence": confidence,
            "origin": ORIGIN,
            "project": "2brain",
            "created_at": CREATED,
            "storage": STORAGE,
            "relations": relations or [],
            "clickup_ref": clickup_ref,
            "feeds_doc": feeds_doc,
            "tags": tags or [],
        }
    )
    return cid


def by_id(cid: str) -> dict:
    return next(e for e in E if e["id"] == cid)


def link(a: str, rel: str, b: str) -> None:
    by_id(a)["relations"].append({"rel": rel, "to": b})


# ===== Fenêtre 1 : brief =====
add(
    type="idea",
    intention="idea",
    position="exploring",
    author="user",
    feeds_doc="vision.md",
    tags=["brief"],
    title="Second cerveau multi-chatbots pour suivre idées et projets",
    content="L'utilisateur veut un second cerveau qui trie code, idées et flux issus de plusieurs chatbots ; stocke idées et avancées ; assure un suivi facile ; connaît son workflow et ses logiciels ; range l'information dans différentes boîtes/outils ; et fournit des agents capables de retrouver, traiter et faire valider une information. Outils IA prévus : Skills, MCP, Rules, Agents. L'UX doit rester simple.",
    evidence="User brief initial : « Je voudrais me lancer dans un projet de second cerveau… »",
)
add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    feeds_doc="architecture.md",
    title="Distinction Brain/ (instance projet) vs Brain-main/ (moteur installable)",
    content="Brain/ est l'instance conventionnée par projet : même structure/docs, stockage des tâches, décisions, registres et connaissances du projet activé. Brain-main/ est le dossier d'installation (conventions, règles, skills, Agents.md, subagents) que l'utilisateur place dans son projet pour donner le contexte commun aux modèles.",
    evidence="User : « On aura deux dossier centraux Brain/ et Brain-main/ » + descriptions.",
)
add(
    type="idea",
    intention="preference",
    position="selected",
    author="user",
    feeds_doc="integrations.md",
    title="SoT locale JSONL/SQL et ClickUp comme interface humaine prioritaire",
    content="Archiver localement idées, tâches et fonctionnalités dans des fichiers lisibles par IA (SQL, JSONL), légers et riches. Les logiciels tiers (ClickUp, Notion, GitHub, Drive) servent à la mise en page humaine. ClickUp est privilégié pour exploiter les capacités gratuites comme interface qualitative du second cerveau.",
    evidence="User : « tout archiver en local… SQL, JSONL » ; « utiliser clickup principalement ».",
)
add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    feeds_doc="vision.md",
    tags=["pain"],
    title="Problème vécu : idées perdues et contextes chat saturés",
    content="L'utilisateur travaille souvent en désordre, note beaucoup d'idées dans des chatbots, vibecode, fait confiance au code IA sans tout relire. Il perd des idées en passant du coq à l'âne et quand les contextes chatbots saturent ou se modifient. Il veut documenter l'avancement même non prévu et suivre ce qui est décidé ou non, tout en restant créatif.",
    evidence="User : « Souvent je travaille en désordre… je veux surtout… qu'il documentes l'avancement ».",
)
add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    space="pilotage",
    feeds_doc="integrations.md",
    title="ClickUp existant : espaces Mon organisation et Projets",
    content="Constat factuel : le ClickUp personnel a déjà deux espaces — « Mon organisation » (docs/listes vie, projets rapides, idées) et « Projets » (un dossier par projet, logique commune). Cela lui sert déjà à retrouver et centraliser. Ce n'est pas en soi l'adoption d'une nouvelle convention Brain.",
    evidence="User : « tu peux déjà regarder mon ClickUP il y a deux espace… »",
)
add(
    type="idea",
    intention="idea",
    position="exploring",
    author="user",
    feeds_doc="vision.md",
    title="Périmètre transverse web, Minecraft, Rust, auto-entreprise",
    content="Le second cerveau doit accompagner des projets de natures très différentes (site web, serveur Minecraft, mod manager Rust, gestion d'auto-entreprise/clients/factures) via une façon générique de démarrer, indépendante de la stack finale.",
    evidence="User : « un jour je ferais un serveur minecraft… mod manager en Rust… auto entreprise ».",
)
add(
    type="decision",
    intention="requirement",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    title="Exigence UX : peu de commandes (~10 à 15 max)",
    content="Contrainte utilisateur explicite : l'UX est ultra importante ; viser le moins de commandes possible, de l'ordre de 10 à 15 maximum, avec un rangement et un naming soignés sans complexifier l'usage.",
    evidence="User : « l'UX est ULTRA IMPORTANTE… » puis « 10/15 max ».",
)

# ===== Fenêtre 2 : Q1-3 =====
q_role = add(
    type="open_question",
    intention="question",
    position="proposed",
    author="assistant",
    title="Quel rôle quotidien : A automatique, B à la demande, C combinaison ?",
    content="L'assistant propose trois modes de rôle quotidien pour le Second Brain. Mode A : observe et organise automatiquement échanges IA, idées et modifications de projets. Mode B : fonctionne à la demande via quelques commandes simples (capture, organize, review, sync). Mode C : combine les deux — capture automatique quand possible, mais validation et organisation pilotées (orchestrateur). La question reste ouverte jusqu'à la réponse utilisateur.",
    evidence="Assistant Q1 : « Quel rôle doit jouer le Second Brain au quotidien ? »",
)
a_role = add(
    type="decision",
    intention="orientation",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    tags=["ambiguous-b-or-c"],
    title="Orientation B ou C : valider le cadrage, pas chaque expérimentation",
    content="L'utilisateur choisit entre les modes B (commandes à la demande) et C (combinaison auto + pilotage), sans trancher strictement B vs C. Il veut pouvoir brainstormer et tester avant validation dans le cadrage. Il ne veut pas valider chaque expérimentation ; il veut valider ce qui entre (ou non) dans le cadrage, les conflits et les doublons. En fin de session, une commande doit comprendre les changements faits (tous modèles, local SoT + ClickUp), noter les mises à jour et préparer des tâches. Les différences opérationnelles exactes restantes entre B et C ne sont pas encore figées dans la source.",
    evidence="User : « pour la réponse 1 je dirais B ou C car je veux pas avoir a valdier ce qui est test mais valider ce qui rentre… »",
)
link(q_role, "answered_by", a_role)
link(a_role, "answers", q_role)

q_cu = add(
    type="open_question",
    intention="question",
    position="proposed",
    author="assistant",
    title="ClickUp : interface de pilotage synchronisée ou simple miroir ?",
    content="L'assistant demande si ClickUp doit être une véritable interface de pilotage synchronisée avec le cerveau local, ou seulement un miroir des informations importantes. Il pose aussi le local comme source de vérité potentielle (JSONL/SQL) et GitHub pour le versionnement.",
    evidence="Assistant Q2 sur la place de ClickUp.",
)
a_cu = add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="integrations.md",
    title="Décision : local = SoT ; ClickUp = visualiseur synchronisé",
    content="Choix utilisateur explicite : tout ce qui est créé est stocké localement dans brain/ (peu lisible humain). ClickUp sert de visualisateur métier. Une commande de sync analyse les données locales et rend le projet lisible dans ClickUp. Ce n'est pas un simple miroir passif : il y a synchronisation pilotée.",
    evidence="User réponse 2 : stocker en local ; ClickUp visualisateur ; syncro avec le cerveau local.",
)
link(q_cu, "answered_by", a_cu)
link(a_cu, "answers", q_cu)

add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="architecture.md",
    title="Décision : socle universel + modules spécialisés",
    content="Réponse à la question de standardisation : l'utilisateur retient un socle universel pour tous les projets, plus des modules selon la nature (web, Rust, SaaS, DA, Minecraft…). Non bloquant ; conventions par module ; onboarding projet modulaire. La stack technique est choisie par l'IA de code, guidée par la base commune.",
    evidence="User : « Pour 3. oui un socle universel… des modules… »",
)

# ===== Principes assistant + bonne base (partial) =====
add(
    type="convention",
    intention="convention",
    position="proposed",
    author="assistant",
    feeds_doc="workflow.md",
    confidence="medium",
    title="Principe proposé : séparer exploratoire et référentiel officiel",
    content="L'assistant formule que le Second Brain ne doit pas empêcher l'expérimentation et qu'il faut distinguer travail exploratoire et référentiel officiel. L'utilisateur ne valide pas chaque expérimentation, seulement l'entrée officielle. Aligné conceptuellement avec l'orientation B/C, mais cette formulation n'a pas d'approbation nommément isolée.",
    evidence="Assistant : « le Second Brain ne doit pas empêcher l'expérimentation… distinction fondamentale ».",
)
c_spaces = add(
    type="proposition",
    intention="suggestion",
    position="endorsed",
    author="assistant",
    feeds_doc="architecture.md",
    tags=["approval_global_partial"],
    title="Suggestion : quatre espaces Atelier, Référentiel, Journal, Pilotage",
    content="Proposition assistant : (1) Atelier/Inbox exploratoire — idées et expérimentations non officielles ; (2) Référentiel projet officiel — décisions et conventions validées ; (3) Journal d'activité — historique de ce qui a été fait ; (4) Pilotage — tâches et sujets actionnables (ex. ClickUp). L'utilisateur a plus tard cité ce bloc dans un exercice et dit que cela fait une « bonne base de travail » : signal d'endossement / pertinence du segment, pas une validation formelle item-par-item de chaque sous-point.",
    evidence="Assistant « quatre espaces logiques » ; user plus tard « bonne base de travail » en citant un large bloc.",
)
c_capture_modes = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="Suggestion : capture passive et/ou par session (brain review)",
    content="L'assistant propose une capture passive (règles agents déposent dans l'Atelier), une capture par session via commande du type brain review (analyse dépôt + Atelier), ou une combinaison. Il souligne qu'une fin de session ne voit pas les idées purement conversationnelles hors dépôt. Pas d'approbation formelle isolée à ce stade.",
    evidence="Assistant : Capture passive / par session / combinaison.",
)
c_pipeline = add(
    type="proposition",
    intention="suggestion",
    position="endorsed",
    author="assistant",
    feeds_doc="workflow.md",
    tags=["approval_global_partial"],
    title="Suggestion : chaîne Sources → Capture → Orchestrateur → Agents → Réf+ClickUp",
    content="Proposition d'une chaîne de traitement continue : sources multi-IA et dépôt → registre JSONL → orchestrateur (analyse, classif, dédup) → agents spécialisés → référentiel local + ClickUp. Distinguer événements bruts, informations extraites et informations officielles. Inclus dans le segment ultérieurement traité comme « bonne base » (endossement partiel, pas validation formelle de chaque maillon).",
    evidence="Assistant « tout capturer, puis traiter » ; user « bonne base de travail ».",
)
add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    tags=["cli", "non-definitive"],
    title="Liste candidate de commandes brain * (explicitement non définitive)",
    content="Table de travail proposée : brain init, capture, review, process, validate, status, search, sync, audit, session, help. L'assistant précise que la liste n'est pas définitive et que certaines commandes pourront être regroupées. Même si le bloc apparaît dans la citation « bonne base », l'élément non définitif n'hérite pas d'une approbation formelle.",
    evidence="Assistant table commandes + « pas encore une liste définitive ».",
)
c_contract = add(
    type="proposition",
    intention="suggestion",
    position="endorsed",
    author="assistant",
    feeds_doc="architecture.md",
    tags=["approval_global_partial"],
    title="Suggestion : contrat commun d'information par entrée",
    content="Proposition : chaque information devrait porter type, origine, projet, statut, date, emplacement de stockage et relations, pour que les agents n'improvisent pas le rangement. Présenté comme cœur potentiel de Brain-main. Endossement partiel via « bonne base », sans validation formelle isolée.",
    evidence="Assistant champs obligatoires ; user « bonne base de travail ».",
)

# ===== Décisions user capture/validation/agents =====
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    title="Capture automatique sélective avec consolidation (pas tout archiver)",
    content="Décision user : ne pas tout garder de ce que l'agent « se dit » ; mettre en place une capture automatique avec un mécanisme de consolidation pour limiter le bruit ; à standardiser.",
    evidence="User : « capture automatique avec un mécanisme de consolidation ».",
)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    title="Entrée au référentiel : proposition complète + accord ; conflits challengés",
    content="Pour faire entrer une information officielle dans le référentiel : préparer une proposition de traitement complète et attendre l'accord. En cas de conflit (ex. Card vs CardCarousel), ne pas supprimer/remplacer unilatéralement : comprendre pourquoi le changement a été fait et viser une compatibilité (variant) plutôt qu'un écrasement. L'utilisateur demande aussi de challenger cet exemple avec d'autres cas.",
    evidence="User Q2 validation + exemple card/carrousel.",
)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="architecture.md",
    title="Agents spécialisés maîtrisant logique, structure et conventions",
    content="L'utilisateur veut une série d'agents spécialisés pour certaines tâches, connaissant par cœur logique, structure et conventions. Il n'a pas explicitement tranché ici entre orchestrateur central permanent et file d'agents indépendants (reco assistant non reprise comme décision).",
    evidence="User Q3 : agents spécialisés.",
)
add(
    type="convention",
    intention="convention",
    position="proposed",
    author="assistant",
    title="Taxonomie proposée : Observation / Proposition / Décision / Convention",
    content="L'assistant propose de ne jamais confondre observation (constat), proposition (évolution envisagée), décision (direction choisie) et convention (règle durable). Une proposition ne devient pas décision parce qu'un agent la trouve pertinente.",
    evidence="Assistant quatre notions.",
)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    title="Conflits : proposer plusieurs solutions comparées",
    content="Lorsqu'un agent détecte une incohérence, l'utilisateur veut qu'il puisse proposer plusieurs solutions comparées (avantages, inconvénients, risques, coût de migration), pas seulement signaler le problème.",
    evidence="User : « 1. oui » à la Q conflits.",
)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    title="Conserver l'historique des décisions remplacées",
    content="L'utilisateur veut conserver toutes les anciennes décisions même remplacées, avec raison du changement et conséquences (traçabilité type DEC-014 remplacée par DEC-027).",
    evidence="User : « 2. Oui » historique.",
)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="architecture.md",
    title="Trois niveaux de conventions ; modules comme mods",
    content="L'utilisateur accepte les conventions universelles SB, les conventions propres à chaque projet, et un troisième niveau de conventions de modules réutilisables. Il précise que les modules doivent être comme des mods : stockés dans brain-main, vivant réellement dans brain une fois activés.",
    evidence="User : « 3. Oui… modules un peu comme des mods… »",
)

c_core = add(
    type="proposition",
    intention="suggestion",
    position="endorsed",
    author="assistant",
    feeds_doc="architecture.md",
    tags=["approval_global_partial"],
    title="Suggestion : architecture Core / Modules / Instance",
    content="Proposition assistant de trois niveaux : Core universel (capture, registres, décisions, tâches, agents, validation, sync ClickUp) ; Modules métier activables ; Instance Brain du projet (identité, modules activés, config, connaissances, historique, état réel). L'utilisateur, après citation du bloc, dit que cela « doit servir de base » : endossement de segment, pas validation formelle de chaque détail.",
    evidence="Assistant architecture conceptuelle ; user « ca doit servir de base ».",
)
add(
    type="convention",
    intention="convention",
    position="endorsed",
    author="assistant",
    feeds_doc="architecture.md",
    tags=["approval_global_partial"],
    title="Modules = extensions autonomes, pas systèmes parallèles",
    content="Un module ne doit pas être un simple dossier de docs : extension autonome (conventions, agents, skills, templates, rules, workflows) qui n'invente pas la gestion Core des décisions/tâches/idées. Définition dans Brain-main ; vie dans Brain ; versionnement. Même segment « servir de base ».",
    evidence="Assistant fonctionnement modules + user « servir de base ».",
)

# Onboarding
c_onb = add(
    type="proposition",
    intention="suggestion",
    position="favorable",
    author="assistant",
    feeds_doc="workflow.md",
    validation="explicit_user_approval",
    approval_scope="item",
    title="Onboarding progressif : ne pas remplir dix docs d'un coup",
    content="Proposition assistant : brain init ne doit pas simplement copier des dossiers et demander de remplir dix documents. Il doit lancer un onboarding intelligent et progressif (nature, objectif, modules, outils, identité, init Brain, infos manquantes sans bloquer). L'utilisateur reprend explicitement : « effectivement brain init ne doit pas bêtement demander… intelligent et progressif » — approbation formelle de ce point précis (item).",
    evidence="User : « effectivement brain init ne doit pas betement demander… »",
)
add(
    type="decision",
    intention="convention",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    tags=["ambiguity-silence"],
    title="Onboarding : questions sans coder/valider sauf explicite ; registre d'idées d'abord",
    content="Règle user : n'importe quel chatbot doit pousser à compléter les docs par Q/R sans coder ni valider sauf instruction explicite ; proposer en cas de doute. Les idées vont d'abord au registre pour trier plus tard. Nuance : l'utilisateur dit que souvent son silence signifie que « ça lui va » — risque de perte d'info ; le silence ne doit pas être traité automatiquement comme validation formelle.",
    evidence="User onboarding : sans coder/valider sauf explicite ; silence parfois = OK.",
)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    title="Activation modules : proposition IA et/ou ajout manuel",
    content="L'IA peut proposer/choisir les modules nécessaires ; les modules peuvent aussi être ajoutés manuellement dans le projet.",
    evidence="User : « Oui l'IA pourra choisir les modules… aussi etre ajouter manuellement »",
)
reco_mod = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="Reco initiale : MàJ modules des projets existants proposées, pas auto",
    content="Recommandation/question assistant : si un module évolue dans brain-main, les projets existants reçoivent des mises à jour proposées sans application automatique.",
    evidence="Assistant Q2 modules : mises à jour proposées, pas auto.",
)
dec_mod = add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    title="MàJ modules : auto si dans brain-main ; pas d'auto si local-only",
    content="Décision user qui tranche la reco précédente pour le cas brain-main : les modules déjà dans brain-main peuvent se mettre à jour automatiquement sur les projets ; un module uniquement local à brain ne se met pas à jour automatiquement ; si ajouté dans brain-main, la version brain-main est maître.",
    evidence="User réponse MàJ modules auto vs local-only.",
)
link(dec_mod, "resolves", reco_mod)
add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    title="Démarrage possible avec une phrase ; ~500 mots = repère non bloquant",
    content="On peut démarrer un projet avec seulement une phrase ; le système pose des questions pour cadrer. Un brief d'environ 500 mots est un repère de qualité, pas une condition bloquante.",
    evidence="User : commencer par une phrase ; 500 mots pas obligatoire.",
)
q_init = add(
    type="open_question",
    intention="question",
    position="uncertain",
    author="user",
    title="brain init : une fois par projet ou par session ?",
    content="Question user non tranchée par lui-même : brain init s'utilise-t-il une seule fois par projet (voire une conversation) ou à chaque session ?",
    evidence="User : « brain init pourra etre utiliser 1 seul fois… ou par session ? »",
)
a_init = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="Proposition : brain init unique ; onboarding = processus continu",
    content="Réponse assistant (non décision user) : brain init crée l'instance une fois ; l'onboarding progressif dure plusieurs conversations/sessions ; capture/review restent permanents. Donc brain init ne devrait pas être relancé à chaque session.",
    evidence="Assistant : brain init non relancé à chaque session.",
)
link(q_init, "answered_by", a_init)
link(a_init, "answers", q_init)

add(
    type="observation",
    intention="observation",
    position=None,
    author="assistant",
    title="Verdict atelier : GO cadrage moteur ; pas encore créer Brain/ Brain-main/",
    content="L'assistant estime qu'il y a assez de matière pour définir le moteur universel, mais pas pour figer l'architecture technique ni créer les dossiers Brain/ et Brain-main/. Il recommande une spécification fonctionnelle d'abord.",
    evidence="Assistant GO cadrage moteur ; pas créer dossiers encore.",
)

# Six milestones individuels
layers = [
    ("Core minimal", "Capture, registres, classification, historique et validation."),
    ("Orchestration", "Agents spécialisés et workflows."),
    ("Onboarding", "Création et enrichissement progressif des projets."),
    ("Modules", "Extensions métier indépendantes."),
    ("Connecteurs", "ClickUp, GitHub et autres outils."),
    ("Automatisation", "Consolidation, audits et synchronisation."),
]
milestone_ids = []
for name, detail in layers:
    mid = add(
        type="task",
        intention="milestone",
        position="proposed",
        author="assistant",
        space="pilotage",
        tags=["potential", "roadmap-layer"],
        title=f"Jalon potentiel : couche {name}",
        content=f"Couche de construction recommandée par l'assistant : {name}. Contenu : {detail} L'utilisateur indique que cette trame en couches donne déjà une première base pour jalons/tâches, sans en faire une roadmap officiellement validée.",
        evidence="Assistant couches 1–6 ; user « première base pour les jalon/taches ».",
    )
    milestone_ids.append(mid)

# ClickUp structure
add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    space="pilotage",
    feeds_doc="integrations.md",
    title="Organisation ClickUp projet observée : docs, Inbox, Cadrage, Roadmap",
    content="Description factuelle par l'utilisateur de l'arborescence sous un dossier projet ClickUp : docs ; Inbox (idées hors chatbot, une tâche par idée) ; Cadrage (sujets à voir) ; Roadmap (trame du projet, ex. couches). Cette observation fournit la matière pour une éventuelle convention, mais n'est pas en soi une validation formelle d'une convention Brain déjà adoptée.",
    evidence="User arbo ClickUp docs/Inbox/Cadrage/Roadmap.",
)
add(
    type="convention",
    intention="convention",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    title="Convention : Capture écrit les registres ; Review range vers docs sans supprimer",
    content="Règle énoncée par l'utilisateur : /brain-capture enregistre dans les registres ; /brain-review range vers les docs nécessaires sans rien supprimer ni trop empiler. Même en phase de cadrage non définitif, il veut déjà une trame à suivre.",
    evidence="User : capture → registres ; review → docs sans supprimer/empiler.",
)

# Formalisation capture/review — global partial
add(
    type="proposition",
    intention="suggestion",
    position="favorable",
    author="assistant",
    feeds_doc="workflow.md",
    tags=["approval_global_partial"],
    title="Formalisation proposée de /brain-capture et /brain-review",
    content="L'assistant formalise Capture (identifier infos → registres locaux avec origine/statut ; signaler sujets sans modifier le référentiel officiel) et Review (relations, doublons, contradictions → propositions docs/tâches/jalons ; validation humaine avant officiel ; rien ne disparaît). L'utilisateur dit être « d'accord globalement avec ton workflow » tout en réservant le cadrage des documents : approbation partielle de segment, pas validation formelle de chaque détail.",
    evidence="Assistant formalise commandes ; user « d'accord globalement… par contre les documents… ».",
)
cap_auto = add(
    type="decision",
    intention="decision",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    title="Capture automatique après chaque message pertinent",
    content="Décision user : après chaque message pertinent, analyser, répondre, puis faire un /brain-capture. Le comportement normal vise l'automatisation par intégration ; une commande manuelle peut rester disponible. Évolution du modèle par rapport à la seule capture passive/session.",
    evidence="User : capture auto après chaque message.",
)
cap_selective = next(e["id"] for e in E if "sélective" in e["title"])
link(cap_auto, "related", c_capture_modes)
link(cap_auto, "related", cap_selective)

add(
    type="decision",
    intention="orientation",
    position="selected",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    tags=["ambiguous-validation-scope"],
    title="Review : consolider, dédupliquer ; « valider certaines choses » (portée ambiguë)",
    content="L'utilisateur veut que /brain-review consolide le registre, enlève les doublons, et « valide certaines choses ». Trois idées coexistent dans la source et doivent rester distinctes conceptuellement : (1) consolidation/entretien des données ; (2) déduplication ; (3) validation de certains éléments. La portée exacte de « valide » vs validation explicite uniquement n'est pas entièrement figée — à ne pas élargir abusivement.",
    evidence="User : review consolide, dédup, « validée certaine choses ».",
)
add(
    type="convention",
    intention="convention",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="workflow.md",
    title="Entretien continu de la mémoire pour éviter l'explosion registres/docs",
    content="Principe user : il faut entretenir la mémoire en continu ; sinon registres et docs explosent. L'entretien doit rester simple et cadré pour ne rien perdre.",
    evidence="User : entretenir la mémoire… sinon explosion.",
)
add(
    type="convention",
    intention="convention",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="integrations.md",
    title="Inbox ClickUp = notes externes manuelles ; pas d'inbox registre local miroir",
    content="L'Inbox ClickUp sert aux notes prises hors ordinateur. En local, l'utilisateur ne prévoit pas d'inbox miroir : les registres d'idées sont plus adaptés. /brain-review peut récupérer l'Inbox ClickUp pour la convertir en entrées structurées.",
    evidence="User précisions Inbox ClickUp vs local.",
)
add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="user",
    feeds_doc="integrations.md",
    title="Proposition : idées validées en sous-tâches Roadmap sans docs/code encore",
    content="Lors des reviews, si une roadmap existe déjà, on pourrait ajouter des sous-tâches et sous-sous-tâches pour stocker des idées validées sans forcément les documenter ni les coder encore. Formulation « on pourrait » : suggestion opérationnelle, pas décision définitive ni création ClickUp.",
    evidence="User : sous-tâches roadmap pour idées validées pas encore codées.",
)

# Sept sujets de cadrage individuels
cadrage = [
    ("Modèle de données et registres", "Définir précisément types d'informations, identifiants, relations et statuts."),
    ("Capture multi-IA", "Déterminer comment Claude Code, Cursor, ChatGPT et autres communiquent avec le même registre."),
    ("Cycle de vie des informations", "Parcours d'une idée de sa capture à son éventuelle validation."),
    ("Gestion des conflits", "Préserver code réel, conventions, décisions et évolutions sans écrasement abusif."),
    ("Modules et versions", "Dépendances, mises à jour et compatibilité entre versions de modules."),
    ("Synchronisation ClickUp", "Sync bidirectionnelle, correspondances et gestion des conflits ClickUp."),
    ("Permissions des agents", "Droits lecture/capture/proposition/validation/sync/modification ; un agent docs ne modifie pas arbitrairement le référentiel."),
]
for title, detail in cadrage:
    add(
        type="task",
        intention="milestone",
        position="proposed",
        author="assistant",
        space="pilotage",
        tags=["potential", "cadrage"],
        title=f"Sujet de cadrage : {title}",
        content=f"Sujet encore à concevoir, listé par l'assistant comme point structurant avant architecture technique. Détail : {detail} L'utilisateur a déjà créé manuellement des tâches Cadrage correspondantes dans ClickUp ; ne pas les recréer ici — capturer le contenu pour la mémoire locale.",
        evidence="Assistant table « points encore à concevoir » + user structure Cadrage.",
    )

add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    space="pilotage",
    title="Réf. ClickUp : liste Cadrage déjà peuplée (ne pas recréer)",
    content="Observation : la liste Cadrage du projet 2nd Brain contient déjà les sujets de cadrage créés manuellement (constat ultérieur : 7). Référencer seulement ; aucune écriture ClickUp demandée dans cette capture.",
    evidence="User + constat 7 sujets Cadrage ; ne rien rajouter dans ClickUp.",
    clickup_ref="ClickUp Projets/2nd Brain/Cadrage (7 sujets existants)",
)
add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    space="pilotage",
    title="Réf. ClickUp : Roadmap déjà peuplée (ne pas recréer)",
    content="Observation : la Roadmap contient déjà les jalons de couches (constat : 6). Référencer seulement.",
    evidence="User couches + constat 6 jalons.",
    clickup_ref="ClickUp Projets/2nd Brain/Roadmap (6 jalons existants)",
)
add(
    type="event",
    intention="observation",
    position=None,
    author="user",
    space="journal",
    feeds_doc="integrations.md",
    title="Événement : peuplement manuel ClickUp ; consigne de ne rien y écrire",
    content="L'utilisateur a appliqué manuellement l'exercice de review sur ClickUp et demande explicitement de ne rien ajouter dans ClickUp pour le moment (hors discussion sur les docs).",
    evidence="User : peuplement manuel + « ne rajoute rien dans le clickup ».",
)

# Docs model
c_op1 = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    feeds_doc="architecture.md",
    title="Proposition initiale : créer operating-model.md dédié",
    content="Première proposition documentaire : un operating-model.md pour capture, consolidation, validation et agents.",
    evidence="Assistant liste docs initiale : operating-model.md",
)
c_op2 = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    feeds_doc="architecture.md",
    title="Évolution : ne pas standardiser operating-model.md — répartir",
    content="Évolution de la proposition : ne pas en faire un document standard ; répartir le contenu entre architecture.md et workflow.md.",
    evidence="Assistant recommandation operating-model.md",
)
link(c_op1, "evolves_to", c_op2)
link(c_op2, "evolves_from", c_op1)
c_ob1 = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="Proposition initiale : créer onboarding.md dédié",
    content="Première proposition : document onboarding.md dédié à l'initialisation et à l'accompagnement progressif.",
    evidence="Assistant liste : onboarding.md",
)
c_ob2 = add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    feeds_doc="workflow.md",
    title="Évolution : onboarding comme chapitre de workflow.md",
    content="Évolution : ne pas faire d'onboarding.md standard ; traiter l'onboarding comme chapitre de workflow.md.",
    evidence="Assistant recommandation onboarding.md",
)
link(c_ob1, "evolves_to", c_ob2)
link(c_ob2, "evolves_from", c_ob1)

add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="Socle documentaire candidat (vision, project, architecture, workflow…)",
    content="Proposition non définitive : documents standards candidats vision.md, project.md, architecture.md, workflow.md (obligatoires) ; design.md et integrations.md selon besoin. L'assistant précise que la liste n'est pas encore définitive.",
    evidence="Assistant proposition de socle documentaire.",
)
add(
    type="decision",
    intention="decision",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    space="referentiel",
    feeds_doc="vision.md",
    title="vision.md validé comme document standard généraliste",
    content="L'utilisateur valide vision.md à 100% comme document généraliste retrouvé dans tous les projets. Cela ne fige pas encore le reste du catalogue documentaire (toujours en discussion).",
    evidence="User : « Vison.md c'est valider a 100%… »",
)
add(
    type="open_question",
    intention="question",
    position="exploring",
    author="user",
    title="Quels docs standard ? Accumuler puis standardiser plus tard",
    content="Question/orientation ouverte : doutes sur operating-model.md et onboarding.md (chapitre vs doc). Pour l'instant choisir des docs standard, y mettre le contenu en vrac, puis standardiser plus tard quand il y aura assez de matière.",
    evidence="User : docs standard puis vrac puis standardiser.",
)
add(
    type="convention",
    intention="convention",
    position="confirmed",
    author="user",
    validation="explicit_user_approval",
    approval_scope="item",
    feeds_doc="vision.md",
    title="Pas d'écrasement silencieux des docs en cas de contradiction",
    content="Si un apport est contradictoire avec un document existant (ex. vision.md), ne pas écraser : proposer plusieurs solutions d'adaptation.",
    evidence="User : ne pas écraser vision ; proposer adaptations.",
)
add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="AGENTS.md comme point d'entrée IA, pas doc métier complet",
    content="Proposition : AGENTS.md à la racine guide les IA (où trouver Brain, conventions, capture, agents/skills, règles de validation) sans contenir toute la documentation.",
    evidence="Assistant section AGENTS.md.",
)
add(
    type="proposition",
    intention="suggestion",
    position="proposed",
    author="assistant",
    title="Documentation en deux phases : accumulation puis standardisation",
    content="Phase 1 : remplir les docs existants même provisoires. Phase 2 : analyser redondances, mauvais classement, docs trop longs, sujets méritant un document indépendant.",
    evidence="Assistant méthode en deux temps.",
)
add(
    type="task",
    intention="task",
    position="proposed",
    author="user",
    space="pilotage",
    tags=["potential"],
    title="Tâche potentielle : standardiser le contenu des docs après accumulation",
    content="L'utilisateur veut garder une trace qu'après accumulation de matière dans les docs, une future tâche consistera à standardiser leur contenu.",
    evidence="User : futur tâche standardiser contenu docs.",
)
add(
    type="convention",
    intention="convention",
    position="proposed",
    author="assistant",
    feeds_doc="workflow.md",
    confidence="medium",
    title="Trois niveaux proposés : Capture / Organisation / Validation",
    content="Proposition assistant : Capture enregistre ; Organisation classe/relie/prépare docs et tâches provisoires ; Validation fait entrer officiellement. Vise la proactivité sans décider à la place de l'utilisateur. Pas d'approbation formelle isolée nommément.",
    evidence="Assistant trois niveaux de traitement.",
)
add(
    type="convention",
    intention="convention",
    position="proposed",
    author="assistant",
    feeds_doc="architecture.md",
    confidence="medium",
    title="Registres = historique ; docs = état actuel ; ClickUp = pilotage",
    content="Règle proposée : les registres conservent l'historique ; les documents présentent l'état actuel ; ClickUp pilote. Consolider sans empiler/dupliquer.",
    evidence="Assistant séparation registres/docs/ClickUp.",
)
add(
    type="convention",
    intention="convention",
    position="proposed",
    author="assistant",
    feeds_doc="vision.md",
    confidence="medium",
    title="Documenter dès le flux sans attendre un cadrage fini",
    content="Principe proposé : le Second Brain ne doit pas attendre qu'un projet soit cadré pour commencer à documenter ; il transforme continuellement le flux en structure provisoire, évolutive et traçable. Les informations écartées restent retrouvables.",
    evidence="Assistant : ne pas attendre cadrage fini.",
)
add(
    type="task",
    intention="task",
    position="proposed",
    author="assistant",
    space="pilotage",
    tags=["potential"],
    title="Tâche potentielle : contrat commun + adaptateurs capture multi-IA",
    content="Limite technique : la capture après chaque message devra être implémentée par des intégrations propres à chaque environnement. Un skill seul ne garantit pas l'écriture automatique dans le dépôt local. Il faudra un contrat commun et des adaptateurs.",
    evidence="Assistant : contrat commun et adaptateurs.",
)
add(
    type="open_question",
    intention="question",
    position="proposed",
    author="assistant",
    title="Périmètre du modèle documentaire universel à approfondir",
    content="Prochain travail recommandé : quels docs sont obligatoires ; quelles infos appartiennent à chaque doc ; lesquelles restent aux registres ; quels docs viennent des modules ; comment éviter les doublons docs/registres/ClickUp — sans créer les fichiers tout de suite.",
    evidence="Assistant recommandation prochain travail.",
)
add(
    type="observation",
    intention="observation",
    position=None,
    author="user",
    space="journal",
    tags=["test-noise", "meta-test"],
    title="Méta : exercice de simulation de ce que le SB aurait capturé",
    content="L'utilisateur simule ce qu'un second cerveau aurait déjà dû enregistrer en citant des blocs assistant. Cet événement décrit un exercice de test/atelier, pas une connaissance métier durable du produit. Les endossements « bonne base » / « servir de base » qui l'accompagnent sont traités via approval_global_partial sur les suggestions concernées, pas comme décisions formelles.",
    evidence="User exercice pratique + « bonne base de travail ».",
)

assert len(E) == N
OUT.write_text(
    "\n".join(json.dumps(e, ensure_ascii=False, separators=(", ", ": ")) for e in E) + "\n",
    encoding="utf-8",
)
from collections import Counter

print("count", len(E))
print("intention", Counter(e["intention"] for e in E))
print("validation", Counter(e["validation"] for e in E))
print("milestones", sum(1 for e in E if e["intention"] == "milestone"))
print("cadrage tags", sum(1 for e in E if "cadrage" in e["tags"]))
print("global_partial", sum(1 for e in E if "approval_global_partial" in e["tags"]))
