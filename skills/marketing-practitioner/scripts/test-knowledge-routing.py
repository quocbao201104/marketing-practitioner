#!/usr/bin/env python3
"""Small deterministic smoke tests for knowledge-route extraction mechanics."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace

SCRIPT_PATH = Path(__file__).with_name("get-knowledge.py")
spec = importlib.util.spec_from_file_location("get_knowledge", SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def expect_error(fn, contains: str) -> None:
    try:
        fn()
    except module.RoutingError as exc:
        assert contains in str(exc), str(exc)
    else:
        raise AssertionError(f"expected RoutingError containing {contains!r}")


def cli_args(**overrides):
    values = {
        "route_ids": [],
        "source": None,
        "list": False,
        "namespace": None,
        "namespaces": False,
        "validate": False,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


def main() -> int:
    expected_routes = {
        "content.consequential-strategy": "## 12. Deeper path for consequential content strategy",
        "content.job-measurement": "## 13. Measurement follows the marketing job",
        "content.performance-diagnosis": "## 15. Diagnostic record for weak or changing performance",
        "commerce.fact-provenance": "### 5.5 Preserve fact provenance",
        "commerce.discovery-modality": "### 7.1 Query modality ≠ retrieval-model modality",
        "commerce.content-commerce-measurement": "### 10.2 Content metrics and commerce metrics can share an object history without sharing causal meaning",
        "commerce.shopper-representation-jobs": "### 11.1 Selection and evaluation representations have different jobs",
        "commerce.observation-interpretation": "## 12. Observation records for commerce",
        "email.core": "## 1. Scope: decide whether, when, and how email should carry resolved strategy",
        "email.send-decision": "## 2. Communication-relevant state and the send decision",
        "email.send-state": "## 3. Authority, reachability, suppression, and scoped send state",
        "email.sequence": "## 4. Time, history, sequence, branching, waiting, and exit",
        "email.allocation": "## 5. Inbox, message, and optional action allocation",
        "email.continuity": "## 6. Continuity and representation robustness",
        "email.observation": "## 7. Observation semantics and causal boundary",
        "email.decision-record": "## 8. Compact email decision record",
        "email.invariants": "## 9. Anti-folklore invariants",
    }
    for route_id, expected_heading in expected_routes.items():
        _, content = module.get_knowledge(route_id)
        assert content.startswith(expected_heading)

    email_source_path, email_source_content = module.get_source("EM03")
    assert email_source_path == "references/email-communication-evidence.md"
    assert email_source_content.startswith("## [EM03] Apple — Mail Privacy Protection")

    fixture = """# Fixture\n\n## A\nA intro\n\n### A.1\nA1 body\n\n#### A.1.1\nA11 body\n\n### A.2\nA2 body\n\n## B\nB body\n\n<!-- route:start fixture.marker -->\nMARKER BODY\n\n### nested marker heading\nstill marker\n<!-- route:end fixture.marker -->\n\n## C\nC body\n"""

    a = module.extract_heading_section(fixture, "## A")
    assert "### A.1" in a and "### A.2" in a
    assert "## B" not in a

    a1 = module.extract_heading_section(fixture, "### A.1")
    assert "#### A.1.1" in a1
    assert "### A.2" not in a1

    fenced = """## Routed section\nIntro.\n\n```text\n## Example heading\nexample body\n```\n\n~~~markdown\n## Another example heading\nother example\n~~~\n\nCritical guardrail after examples.\n\n## Next section\nnext body\n"""
    fenced_section = module.extract_heading_section(fenced, "## Routed section")
    assert "## Example heading" in fenced_section
    assert "## Another example heading" in fenced_section
    assert "Critical guardrail after examples." in fenced_section
    assert "## Next section" not in fenced_section

    marker = module.extract_marker_section(fixture, "fixture.marker")
    assert marker.startswith("MARKER BODY")
    assert "nested marker heading" in marker
    assert "route:end" not in marker

    expect_error(
        lambda: module.extract_marker_section(
            "<!-- route:end reversed -->\nbody\n<!-- route:start reversed -->",
            "reversed",
        ),
        "precedes start marker",
    )

    expect_error(
        lambda: module.extract_heading_section("## X\none\n## X\ntwo\n", "## X"),
        "found 2",
    )

    manifest = {
        "version": 2,
        "namespaces": {
            "fixture": {
                "path": "fixture.md",
                "sections": {
                    "heading": "## A",
                    "marker": {"marker": "fixture.marker"},
                },
            }
        },
    }

    with tempfile.TemporaryDirectory() as tmp:
        old_root = module.ROOT
        old_manifest_path = module.MANIFEST_PATH
        try:
            module.ROOT = Path(tmp)
            module.MANIFEST_PATH = Path(tmp) / "missing-routing-index.json"
            (Path(tmp) / "fixture.md").write_text(fixture, encoding="utf-8")

            _, heading_content = module.get_knowledge("fixture.heading", manifest)
            assert heading_content == a

            _, marker_content = module.get_knowledge("fixture.marker", manifest)
            assert marker_content == marker

            assert module.validate_manifest(manifest) == []
            assert list(module.iter_route_ids(manifest, "fixture")) == [
                "fixture.heading",
                "fixture.marker",
            ]

            expect_error(lambda: module.resolve_path("../escape.md"), "escapes skill root")
            expect_error(
                lambda: module.get_knowledge("missing.route", manifest),
                "unknown knowledge namespace",
            )
            expect_error(
                lambda: module.get_knowledge("fixture.missing", manifest),
                "unknown knowledge route",
            )

            references = Path(tmp) / "references"
            (references / "commerce").mkdir(parents=True)
            (references / "bibliography.md").write_text(
                "# Bibliography\n\n### [R23] Source R23\nR23 body\n\n### [R24] Source R24\nR24 body\n",
                encoding="utf-8",
            )
            (references / "commerce" / "amazon.md").write_text(
                "# Amazon evidence\n\n## [A03] Source A03\nA03 body\n\n```text\n## [A03] Example source heading only\nnot evidence\n```\n\n~~~text\n## [A99] Another example only\nnot evidence either\n~~~\n\n## [A04] Source A04\nA04 body\n",
                encoding="utf-8",
            )

            source_path, source_content = module.get_source("a03")
            # Logical source paths must remain POSIX-style on every host OS.
            assert source_path == "references/commerce/amazon.md"
            assert source_content.startswith("## [A03] Source A03")
            assert "## [A04]" not in source_content

            # Evidence lookup must remain independent of the semantic manifest.
            assert not module.MANIFEST_PATH.exists()
            _, independent_source = module.get_source("R23")
            assert independent_source.startswith("### [R23] Source R23")

            assert module.validate_sources() == []
            scanned = module.scan_sources()
            assert len(scanned["A03"]) == 1
            assert "A99" not in scanned
            expect_error(lambda: module.get_source("ZZ99"), "found 0")

            (references / "duplicate.md").write_text(
                "## [A03] Duplicate\nother body\n",
                encoding="utf-8",
            )
            expect_error(lambda: module.get_source("A03"), "found 2")
            source_errors = module.validate_sources()
            assert len(source_errors) == 1
            assert source_errors[0].startswith("A03: evidence source ID appears 2 times")
        finally:
            module.ROOT = old_root
            module.MANIFEST_PATH = old_manifest_path

    expect_error(
        lambda: json.loads(
            '{"namespaces": {}, "namespaces": {}}',
            object_pairs_hook=module.reject_duplicate_keys,
        ),
        "duplicate JSON key",
    )

    expect_error(
        lambda: module.select_mode(
            cli_args(route_ids=["commerce.resolvability"], validate=True)
        ),
        "choose exactly one mode",
    )
    expect_error(
        lambda: module.select_mode(cli_args(list=True, namespaces=True)),
        "choose exactly one mode",
    )
    expect_error(
        lambda: module.select_mode(cli_args(namespace="shopee")),
        "--namespace is only valid with --list",
    )

    print("PASS\t40 routing-mechanics smoke checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
