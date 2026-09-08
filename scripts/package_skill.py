#!/usr/bin/env python3
"""Build a portable skill ZIP from tracked runtime files and current file bytes."""

import argparse
from pathlib import Path
import subprocess
import sys
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New ZIP path (never overwritten)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    skill = root / "skills" / "marketing-practitioner"
    output = args.output.resolve()
    if output.suffix.lower() != ".zip":
        parser.error("output must have a .zip extension")
    if output.exists() or output.is_relative_to(skill):
        parser.error("choose a new output path outside the skill directory")
    subprocess.run(
        [sys.executable, "-B", str(root / "scripts" / "validate_skill.py"), str(skill)],
        check=True,
    )
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z", "--", "skills/marketing-practitioner"], cwd=root
    ).decode("utf-8").split("\0")
    entries = {}
    for name in sorted(filter(None, tracked)):
        source = root / name
        if source.is_symlink() or not source.resolve().is_relative_to(skill):
            raise ValueError(f"Runtime file is outside the skill: {name}")
        archive_name = "marketing-practitioner/" + source.relative_to(skill).as_posix()
        entries[archive_name] = source.read_bytes()
    for name in ("LICENSE", "THIRD_PARTY_NOTICES.md"):
        entries["marketing-practitioner/" + name] = (root / name).read_bytes()
    if "marketing-practitioner/SKILL.md" not in entries:
        raise ValueError("Tracked skill entrypoint is missing")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        assert set(archive.namelist()) == set(entries)
        assert all(archive.read(name) == content for name, content in entries.items())
    print(f"PASS: {len(entries)} files, preserved bytes: {output}")


if __name__ == "__main__":
    main()
