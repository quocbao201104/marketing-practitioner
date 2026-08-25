from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import ArmProfile, CaseContract, ValidationError


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_document(path: Path, collection_key: str) -> list[Any]:
    try:
        text = Path(path).read_text(encoding="utf-8")
        document = json.loads(text, object_pairs_hook=_reject_duplicate_keys)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"cannot load {path}: {exc}") from exc
    if not isinstance(document, dict):
        raise ValidationError("contract document must be an object")
    expected = {"schema_version", collection_key}
    unknown = sorted(set(document) - expected)
    missing = sorted(expected - set(document))
    if unknown:
        raise ValidationError(f"unknown document fields: {', '.join(unknown)}")
    if missing:
        raise ValidationError(f"missing document fields: {', '.join(missing)}")
    if document["schema_version"] != 1:
        raise ValidationError("schema_version must equal 1")
    collection = document[collection_key]
    if not isinstance(collection, list) or not collection:
        raise ValidationError(f"{collection_key} must be a non-empty array")
    return collection


def load_cases(path: Path) -> list[CaseContract]:
    cases = [CaseContract.from_dict(item) for item in _load_document(path, "cases")]
    seen: set[str] = set()
    for case in cases:
        if case.identity in seen:
            raise ValidationError(f"duplicate case identity: {case.identity}")
        seen.add(case.identity)
    return cases


def load_profiles(path: Path, *, live: bool = False) -> list[ArmProfile]:
    profiles = [
        ArmProfile.from_dict(item, live=live)
        for item in _load_document(path, "profiles")
    ]
    seen: set[str] = set()
    for profile in profiles:
        if profile.profile_id in seen:
            raise ValidationError(f"duplicate profile id: {profile.profile_id}")
        seen.add(profile.profile_id)
    return profiles


__all__ = ["ValidationError", "load_cases", "load_profiles"]
