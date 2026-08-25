from __future__ import annotations

import re
from pathlib import Path


def controller_metrics(skill_root: Path) -> dict[str, int]:
    path = Path(skill_root) / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    return {
        "bytes": len(text.encode("utf-8")),
        "words": len(re.findall(r"\S+", text)),
        "lines": len(text.splitlines()),
    }
