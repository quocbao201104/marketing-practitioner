#!/usr/bin/env python3
"""Validate the stable, repository-owned Marketing Practitioner skill contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STRING_FIELD_RE = re.compile(r'^\s{2}([a-z_]+):\s*("(?:[^"\\]|\\.)*")\s*$')


class SkillValidationError(ValueError):
    """Raised when a validation input cannot be parsed safely."""


def _read_utf8(path: Path) -> str:
    try:
        data = path.read_bytes()
        text = data.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SkillValidationError(f"{path}: cannot read strict UTF-8: {exc}") from exc
    if text.startswith("\ufeff"):
        raise SkillValidationError(f"{path}: UTF-8 BOM is not supported")
    return text


def _decode_scalar(value: str, key: str) -> str:
    value = value.strip()
    if not value:
        raise SkillValidationError(f"frontmatter field {key!r} is empty")
    if value.startswith('"'):
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError as exc:
            raise SkillValidationError(
                f"frontmatter field {key!r} has invalid quoted text"
            ) from exc
        if not isinstance(decoded, str):
            raise SkillValidationError(f"frontmatter field {key!r} must be text")
        return decoded
    if value.startswith("'") and value.endswith("'") and len(value) >= 2:
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(text: str) -> dict[str, str]:
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0] != "---":
        raise SkillValidationError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise SkillValidationError("SKILL.md frontmatter is not closed") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace() or line.startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise SkillValidationError(f"invalid frontmatter line: {line!r}")
        key = key.strip()
        if key in fields:
            raise SkillValidationError(f"duplicate frontmatter field: {key}")
        fields[key] = "" if not value.strip() else _decode_scalar(value, key)
    return fields


def _validate_openai_yaml(path: Path, skill_name: str) -> list[str]:
    try:
        text = _read_utf8(path)
    except SkillValidationError as exc:
        return [str(exc)]

    normalized = text.replace("\r\n", "\n")
    lines = normalized.splitlines()
    if not lines or lines[0] != "interface:":
        return ["agents/openai.yaml must start with interface:"]

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = STRING_FIELD_RE.fullmatch(line)
        if not match:
            return [f"agents/openai.yaml has unsupported or unquoted line: {line!r}"]
        key, encoded = match.groups()
        if key in fields:
            return [f"agents/openai.yaml has duplicate interface field: {key}"]
        fields[key] = json.loads(encoded)

    errors: list[str] = []
    for key in ("display_name", "short_description", "default_prompt"):
        if not fields.get(key):
            errors.append(f"agents/openai.yaml is missing interface.{key}")
    short_description = fields.get("short_description", "")
    if short_description and not 25 <= len(short_description) <= 64:
        errors.append("interface.short_description must contain 25-64 characters")
    if f"${skill_name}" not in fields.get("default_prompt", ""):
        errors.append(
            f"interface.default_prompt must mention ${skill_name} explicitly"
        )
    return errors


def validate_skill(skill_root: Path) -> list[str]:
    skill_root = Path(skill_root)
    skill_path = skill_root / "SKILL.md"
    if not skill_path.is_file():
        return ["SKILL.md is missing"]

    try:
        fields = parse_frontmatter(_read_utf8(skill_path))
    except SkillValidationError as exc:
        return [str(exc)]

    errors: list[str] = []
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        errors.append("frontmatter name is required")
    elif not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("skill name must be <=64 lowercase letters, digits, or hyphens")
    elif name != skill_root.name:
        errors.append(
            f"skill name {name!r} does not match directory {skill_root.name!r}"
        )
    if not description:
        errors.append("frontmatter description is required")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")

    openai_yaml = skill_root / "agents" / "openai.yaml"
    if openai_yaml.exists():
        errors.extend(_validate_openai_yaml(openai_yaml, name))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Codex skill package.")
    parser.add_argument("skill_root", type=Path)
    args = parser.parse_args(argv)
    errors = validate_skill(args.skill_root)
    for error in errors:
        print(f"FAIL\t{error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS\tskill package")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
