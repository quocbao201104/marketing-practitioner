from __future__ import annotations

import hashlib
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .models import ArmProfile, CaseContract


IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache"}
FORBIDDEN_ANSWER_NAMES = {"golden-answer", "expected-answer", "reference-answer"}


class WorkspaceError(RuntimeError):
    """Raised when an isolated run workspace cannot be built safely."""


@dataclass(frozen=True)
class WorkspaceBinding:
    root: Path
    profile_id: str
    skill_mode: str
    skill_path: Path | None
    expected_skill_sha256: str | None


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _iter_tree_files(root: Path):
    if not root.is_dir():
        raise WorkspaceError(f"tree does not exist: {root}")
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        relative = path.relative_to(root)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.is_symlink():
            target = path.resolve()
            if not _is_within(target, root.resolve()):
                raise WorkspaceError(f"symlink escapes source tree: {relative.as_posix()}")
        if path.is_file():
            yield relative, path


def hash_tree(root: Path) -> str:
    root = Path(root).resolve()
    digest = hashlib.sha256()
    for relative, path in _iter_tree_files(root):
        encoded_path = relative.as_posix().encode("utf-8")
        data = path.read_bytes()
        digest.update(len(encoded_path).to_bytes(8, "big"))
        digest.update(encoded_path)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def _resolve_repo_input(repo_root: Path, relative: str) -> Path:
    candidate = (repo_root / relative).resolve()
    if not _is_within(candidate, repo_root):
        raise WorkspaceError(f"input path escapes repository root: {relative}")
    if not candidate.is_file():
        raise WorkspaceError(f"input file does not exist: {relative}")
    return candidate


def _initialize_git(root: Path) -> None:
    try:
        completed = subprocess.run(
            ["git", "init", "--quiet", str(root)],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        raise WorkspaceError(f"cannot launch git init: {exc}") from exc
    if completed.returncode:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise WorkspaceError(f"git init failed: {detail}")


def build_run_workspace(
    case: CaseContract,
    profile: ArmProfile,
    repo_root: Path,
    destination: Path,
) -> WorkspaceBinding:
    repo_root = Path(repo_root).resolve()
    destination = Path(destination).resolve()
    if destination.exists() and any(destination.iterdir()):
        raise WorkspaceError(f"destination is not empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    _initialize_git(destination)

    case_root = destination / "case"
    inputs_root = case_root / "inputs"
    inputs_root.mkdir(parents=True)
    (case_root / "prompt.txt").write_text(case.prompt + "\n", encoding="utf-8")
    for relative in case.input_files:
        source = _resolve_repo_input(repo_root, relative)
        target = inputs_root / Path(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    skill_path: Path | None = None
    expected_hash: str | None = None
    if profile.skill_mode == "workspace-copy":
        source_text = profile.skill_source
        if source_text is None:
            raise WorkspaceError("workspace-copy profile has no skill source")
        source = (repo_root / source_text).resolve()
        if not _is_within(source, repo_root):
            raise WorkspaceError("skill source escapes repository root")
        source_hash = hash_tree(source)
        expected_hash = (
            source_hash
            if profile.expected_skill_sha256 == "computed-at-run-bind"
            else profile.expected_skill_sha256
        )
        skill_path = (
            destination / ".agents" / "skills" / "marketing-practitioner"
        )
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            source,
            skill_path,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        )

    return WorkspaceBinding(
        root=destination,
        profile_id=profile.profile_id,
        skill_mode=profile.skill_mode,
        skill_path=skill_path,
        expected_skill_sha256=expected_hash,
    )


def preflight_workspace(binding: WorkspaceBinding) -> list[str]:
    errors: list[str] = []
    discovered_skill = (
        binding.root / ".agents" / "skills" / "marketing-practitioner"
    )
    if binding.skill_mode == "none":
        if discovered_skill.exists():
            errors.append("baseline contains marketing-practitioner")
    elif not discovered_skill.is_dir():
        errors.append("skill arm is missing marketing-practitioner")
    elif binding.expected_skill_sha256 is None:
        errors.append("skill arm has no bound SHA-256")
    else:
        try:
            actual = hash_tree(discovered_skill)
        except WorkspaceError as exc:
            errors.append(str(exc))
        else:
            if actual != binding.expected_skill_sha256:
                errors.append("skill copy SHA-256 differs from bound hash")

    if not (binding.root / ".git").is_dir():
        errors.append("run workspace is not a Git workspace")

    for path in binding.root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        lowered = path.name.lower()
        if any(token in lowered for token in FORBIDDEN_ANSWER_NAMES):
            errors.append(
                f"workspace contains answer-bearing material: {path.relative_to(binding.root).as_posix()}"
            )
    return errors
