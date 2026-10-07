#!/usr/bin/env python3
"""Verificador de la bóveda IstpetDev y de las skills del equipo.

Uso (desde cualquier carpeta):
    python .agents/skills/istpetdev-docs/scripts/check_vault.py
    python .agents/skills/istpetdev-docs/scripts/check_vault.py --sync-skills

Errores (salida 1): enlaces internos rotos, nombres de nota duplicados, frontmatter
incompleto, estados no válidos, IDs definidos fuera de su nota dueña o repetidos,
rutas personales, bloques de código sin cerrar, conteos desactualizados en
«Fuente y control documental», skills con formato no portable y copia de skills
para Claude Code desincronizada.

Avisos (no bloquean): lenguaje absoluto en notas de propuesta.

Solo usa la biblioteca estándar de Python 3.9+.
"""
from __future__ import annotations

import argparse
import filecmp
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents" / "skills"
CLAUDE_SKILLS = ROOT / ".claude" / "skills"

# Archivos en la raíz que leen los asistentes; no son notas de Obsidian con frontmatter.
AGENT_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"}
ATTACHMENTS = {"Manual oficial.pdf"}
REQUIRED_FIELDS = ("tipo", "estado", "actualizado", "tags")
VALID_STATES = {"vigente", "propuesta", "pendiente", "aceptado", "validado", "reemplazado", "plantilla"}

# Prefijo de ID -> nota dueña (única nota donde se define en una fila de tabla).
ID_OWNERS = {
    "RF": "Requisitos y aceptacion",
    "RNF": "Requisitos y aceptacion",
    "V": "Plan de validacion",
    "B": "Backlog",
    "S": "Dataset y escenarios",
    "ADR": "Decisiones de arquitectura",
    "O": "Consultas para la organizacion",
    "R": "Riesgos y decisiones pendientes",
    "EXP": "Simulador y metricas",
    "WF": "n8n e IA",
}
ID_ROW = re.compile(r"^\|\s*(RF|RNF|V|B|S|ADR|O|R|EXP|WF)-(\d+)\s*\|")
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
PERSONAL_PATH = re.compile(r"/home/[A-Za-z0-9_.-]+|[A-Za-z]:[\\/]+Users[\\/]+[A-Za-z0-9_.-]+", re.IGNORECASE)
ABSOLUTE = re.compile(r"\b(garantiz\w*|instant[áa]ne\w*|imposible|perfectamente|absolut\w*|nivel senior)\b", re.IGNORECASE)
NEGATION = re.compile(r"\b(no|sin|nunca|ni)\b", re.IGNORECASE)
COUNT_NOTES = re.compile(r"\*\*(\d+) notas Markdown\*\*")
COUNT_LINKS = re.compile(r"\*\*(\d+) enlaces internos resueltos\*\*")
SKILL_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
BACKTICK_MD = re.compile(r"`([^`\s][^`]*?\.md)`")
MD_LINK = re.compile(r"\]\(([^)#\s]+\.md)\)")


def vault_notes() -> list[Path]:
    """Notas visibles para Obsidian: Markdown fuera de carpetas ocultas."""
    notes = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts[:-1]):
            continue
        notes.append(path)
    return sorted(notes)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def check_vault(errors: list[str], warnings: list[str]) -> tuple[int, int]:
    notes = vault_notes()
    names: dict[str, Path] = {}
    for note in notes:
        if note.stem in names:
            errors.append(f"Nombre de nota duplicado: {note.relative_to(ROOT)} y {names[note.stem].relative_to(ROOT)}")
        names[note.stem] = note
    valid_targets = set(names) | ATTACHMENTS

    links = 0
    definitions: dict[str, list[str]] = {}
    for note in notes:
        rel = note.relative_to(ROOT).as_posix()
        text = read(note)

        if note.name not in AGENT_FILES or note.parent != ROOT:
            fields = frontmatter(text)
            if fields is None:
                errors.append(f"{rel}: falta frontmatter")
            else:
                missing = [f for f in REQUIRED_FIELDS if not fields.get(f)]
                if missing:
                    errors.append(f"{rel}: faltan campos de frontmatter {missing}")
                state = fields.get("estado")
                if state and state not in VALID_STATES:
                    errors.append(f"{rel}: estado «{state}» no válido ({', '.join(sorted(VALID_STATES))})")

        if note.parent == ROOT and note.name in AGENT_FILES - {"README.md"} and WIKILINK.search(text):
            errors.append(f"{rel}: usa [[wikilinks]]; los asistentes fuera de Obsidian no los resuelven. Usa rutas relativas")

        for target in WIKILINK.findall(text):
            links += 1
            if target.strip() not in valid_targets:
                errors.append(f"{rel}: enlace roto [[{target}]]")

        if text.count("```") % 2:
            errors.append(f"{rel}: bloque de código sin cerrar")

        for match in PERSONAL_PATH.finditer(text):
            errors.append(f"{rel}: ruta personal «{match.group(0)}»")

        in_code = False
        fields = frontmatter(text) or {}
        for number, line in enumerate(text.splitlines(), 1):
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            row = ID_ROW.match(line)
            if row:
                prefix, num = row.groups()
                key = f"{prefix}-{num}"
                definitions.setdefault(key, []).append(f"{rel}:{number}")
                owner = ID_OWNERS[prefix]
                if note.stem != owner:
                    errors.append(f"{rel}:{number}: {key} se define fuera de su nota dueña «{owner}»")
            if fields.get("estado") == "propuesta":
                for word in ABSOLUTE.findall(line):
                    if not NEGATION.search(line):
                        warnings.append(f"{rel}:{number}: lenguaje absoluto «{word}»")

    for key, places in definitions.items():
        if len(places) > 1:
            errors.append(f"{key} definido más de una vez: {', '.join(places)}")

    control = names.get("Fuente y control documental")
    if control:
        text = read(control)
        noted = COUNT_NOTES.findall(text)
        linked = COUNT_LINKS.findall(text)
        if not noted or int(noted[-1]) != len(notes):
            errors.append(f"Fuente y control documental: el último conteo de notas no es {len(notes)}")
        if not linked or int(linked[-1]) != links:
            errors.append(f"Fuente y control documental: el último conteo de enlaces no es {links}")
    return len(notes), links


def check_skills(errors: list[str]) -> int:
    if not SKILLS.is_dir():
        errors.append(".agents/skills no existe")
        return 0
    count = 0
    for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        count += 1
        main = skill / "SKILL.md"
        rel = main.relative_to(ROOT).as_posix()
        if not main.is_file():
            errors.append(f"{skill.relative_to(ROOT).as_posix()}: falta SKILL.md")
            continue
        text = read(main)
        fields = frontmatter(text)
        if fields is None:
            errors.append(f"{rel}: falta frontmatter")
            continue
        extra = set(fields) - {"name", "description"}
        if extra:
            errors.append(f"{rel}: campos no portables en frontmatter {sorted(extra)}; usa solo name y description")
        name = fields.get("name", "")
        if name != skill.name or not SKILL_NAME.match(name) or len(name) > 64:
            errors.append(f"{rel}: name «{name}» debe ser igual a la carpeta, en minúsculas con guiones y de hasta 64 caracteres")
        description = fields.get("description", "")
        if not description or len(description) > 1024:
            errors.append(f"{rel}: description vacía o de más de 1024 caracteres")
        for file in skill.rglob("*.md"):
            body = read(file)
            frel = file.relative_to(ROOT).as_posix()
            if WIKILINK.search(body):
                errors.append(f"{frel}: usa [[wikilinks]]; usa rutas relativas")
            for match in PERSONAL_PATH.finditer(body):
                errors.append(f"{frel}: ruta personal «{match.group(0)}»")
            for target in BACKTICK_MD.findall(body) + MD_LINK.findall(body):
                if "/" not in target or "<" in target or "*" in target:
                    continue
                if not ((ROOT / target).exists() or (file.parent / target).exists()):
                    errors.append(f"{frel}: la ruta «{target}» no existe")
    return count


def check_mirror(errors: list[str]) -> None:
    if not CLAUDE_SKILLS.exists():
        errors.append(".claude/skills no existe; ejecuta este script con --sync-skills")
        return
    def files(base: Path) -> set[str]:
        return {p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    source, mirror = files(SKILLS), files(CLAUDE_SKILLS)
    different = sorted(source ^ mirror)
    different += sorted(f for f in source & mirror if not filecmp.cmp(SKILLS / f, CLAUDE_SKILLS / f, shallow=False))
    if different:
        errors.append(".claude/skills no coincide con .agents/skills (" + ", ".join(different[:5]) + "); ejecuta con --sync-skills")


def sync_skills() -> None:
    if CLAUDE_SKILLS.exists():
        shutil.rmtree(CLAUDE_SKILLS)
    shutil.copytree(SKILLS, CLAUDE_SKILLS, ignore=shutil.ignore_patterns("__pycache__"))
    print(f"Copiadas las skills de {SKILLS.relative_to(ROOT).as_posix()} a {CLAUDE_SKILLS.relative_to(ROOT).as_posix()}")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Verifica la bóveda y las skills de IstpetDev.")
    parser.add_argument("--sync-skills", action="store_true", help="copia .agents/skills a .claude/skills antes de verificar")
    parser.add_argument("--quiet-warnings", action="store_true", help="no muestra los avisos de lenguaje absoluto")
    args = parser.parse_args()
    if args.sync_skills:
        sync_skills()

    errors: list[str] = []
    warnings: list[str] = []
    notes, links = check_vault(errors, warnings)
    skills = check_skills(errors)
    check_mirror(errors)

    if warnings and not args.quiet_warnings:
        print(f"Avisos ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print(f"Errores ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")
    print(f"Resumen: {notes} notas Markdown, {links} enlaces internos, {skills} skills, "
          f"{len(errors)} errores, {len(warnings)} avisos.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
