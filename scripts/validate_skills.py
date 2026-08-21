#!/usr/bin/env python3
"""Validate the repository's portable Skill profile."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
FRONTMATTER_RE = re.compile(r"\A---\r?\n(?P<content>.*?)\r?\n---\r?\n", re.DOTALL)
FIELD_RE = re.compile(r"^(?P<key>[a-z][a-z-]*):\s*(?P<value>\S.*)$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_PATTERNS = {
    "Claude Code argument substitution": re.compile(r"\$ARGUMENTS(?:\[\d+\])?|\$\d+"),
    "Claude Code environment substitution": re.compile(r"\$\{CLAUDE_[A-Z0-9_]+\}"),
    "Claude Code inline shell injection": re.compile(r"(?m)^\s*!`[^`]+`\s*$"),
    "Claude Code fenced shell injection": re.compile(r"(?m)^```!\s*$"),
}


def validate_skill(skill_md: Path) -> list[str]:
    errors: list[str] = []
    content = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    relative_path = skill_md.relative_to(ROOT)

    if not match:
        return [f"{relative_path}: missing or malformed YAML frontmatter"]

    fields: dict[str, str] = {}
    for line in match.group("content").splitlines():
        field_match = FIELD_RE.match(line)
        if not field_match:
            errors.append(f"{relative_path}: unsupported frontmatter line: {line}")
            continue
        key = field_match.group("key")
        if key in fields:
            errors.append(f"{relative_path}: duplicate frontmatter key: {key}")
        fields[key] = field_match.group("value")

    if set(fields) != {"name", "description"}:
        errors.append(
            f"{relative_path}: portable frontmatter must contain only name and description"
        )

    name = fields.get("name", "")
    if len(name) > 64:
        errors.append(f"{relative_path}: name must contain at most 64 characters")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{relative_path}: name must be lowercase hyphen-case")
    elif skill_md.parent.name != name:
        errors.append(f"{relative_path}: parent directory must match name: {name}")

    description = fields.get("description", "")
    if not description or len(description) > 1024:
        errors.append(f"{relative_path}: description must contain 1 to 1024 characters")

    body = content[match.end() :]
    for label, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(body):
            errors.append(f"{relative_path}: contains {label}")

    return errors


def main() -> int:
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("No skills found in skills/", file=sys.stderr)
        return 1

    errors = [error for skill_md in skill_files for error in validate_skill(skill_md)]
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} portable skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
