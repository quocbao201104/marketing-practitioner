from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Sequence


def seal_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def redact_text(
    text: str, roots: Sequence[Path], secret_values: Sequence[str]
) -> str:
    redacted = text
    root_variants: set[str] = set()
    for root in roots:
        resolved = str(Path(root).resolve())
        root_variants.add(resolved)
        root_variants.add(resolved.replace("\\", "/"))
    for value in sorted(root_variants, key=len, reverse=True):
        if value:
            redacted = re.sub(re.escape(value), "<WORKSPACE>", redacted, flags=re.I)
    for secret in sorted(set(secret_values), key=len, reverse=True):
        if secret:
            redacted = redacted.replace(secret, "<REDACTED>")
    return redacted
