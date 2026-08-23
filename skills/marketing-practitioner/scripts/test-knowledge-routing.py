#!/usr/bin/env python3
"""Small deterministic smoke tests for knowledge-route extraction mechanics."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

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


def main() -> int:
    fixture = """# Fixture\n\n## A\nA intro\n\n### A.1\nA1 body\n\n#### A.1.1\nA11 body\n\n### A.2\nA2 body\n\n## B\nB body\n\n<!-- route:start fixture.marker -->\nMARKER BODY\n\n### nested marker heading\nstill marker\n<!-- route:end fixture.marker -->\n\n## C\nC body\n"""

    a = module.extract_heading_section(fixture, "## A")
    assert "### A.1" in a and "### A.2" in a
    assert "## B" not in a

    a1 = module.extract_heading_section(fixture, "### A.1")
    assert "#### A.1.1" in a1
    assert "### A.2" not in a1

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
                "# Amazon evidence\n\n## [A03] Source A03\nA03 body\n\n## [A04] Source A04\nA04 body\n",
                encoding="utf-8",
            )

            source_path, source_content = module.get_source("a03")
            assert source_path == "references/commerce/amazon.md"
            assert source_content.startswith("## [A03] Source A03")
            assert "## [A04]" not in source_content

            # Evidence lookup must remain independent of the semantic manifest.
            assert not module.MANIFEST_PATH.exists()
            _, independent_source = module.get_source("R23")
            assert independent_source.startswith("### [R23] Source R23")

            assert module.validate_sources() == []
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

    print("PASS\t16 routing-mechanics smoke checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
