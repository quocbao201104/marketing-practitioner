from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from episode import ExposureEvent, EpisodeState, M, Phase, initialize_workspace, r2_content, validate_channel_allocation
from evaluator import ComparativeDisposition, comparative_disposition


class EpisodeStateTests(unittest.TestCase):
    def test_reservation_ledger_tracks_full_commitment(self):
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(40 * M, "bounded learning")
        self.assertEqual((8, 32, 40, 130), tuple(x // M for x in (state.deposit_spent, state.open_creator_balance, state.current_creator_commitment, state.uncommitted_budget)))

    def test_booking_after_gate_is_rejected(self):
        state = EpisodeState("SWE-E01-P")
        state.close_booking_gate()
        with self.assertRaises(ValueError):
            state.reserve_creator_inventory(40 * M, "late booking")

    def test_technical_cap_and_second_booking_are_enforced(self):
        state = EpisodeState("SWE-E01-P")
        with self.assertRaises(ValueError):
            state.reserve_creator_inventory(101 * M, "too large")
        state.reserve_creator_inventory(40 * M, "valid")
        with self.assertRaises(ValueError):
            state.reserve_creator_inventory(20 * M, "second")

    def test_reduction_boundaries(self):
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(70 * M, "initial")
        state.close_booking_gate(); state.deliver_r2()
        with self.assertRaises(ValueError):
            state.reduce_creator_commitment(13 * M, "below deposit")
        state.reduce_creator_commitment(50 * M, "recovery")
        state.close_reduction_gate()
        with self.assertRaises(ValueError):
            state.reduce_creator_commitment(40 * M, "too late")

    def test_action_snapshot_preserves_reconstructible_content(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            state = initialize_workspace(root)
            planning = root / "planning.md"
            planning.write_text("R1 is ambiguous", encoding="utf-8")
            state.reserve_creator_inventory(30 * M, "bounded access")
            sealed = next(item for item in state.actions[-1].artifact_snapshots if item.name == "planning.md")
            planning.write_text("rewritten later", encoding="utf-8")
            self.assertEqual("R1 is ambiguous", sealed.content)
            self.assertNotEqual(sealed.content, planning.read_text(encoding="utf-8"))

    def test_r2_heading_is_neutral(self):
        self.assertTrue(r2_content("SWE-E01-P").startswith("# Competitor audit R2\n"))
        self.assertTrue(r2_content("SWE-E01-C").startswith("# Competitor audit R2\n"))
        self.assertNotIn("pressure", r2_content("SWE-E01-P").splitlines()[0].lower())
        self.assertNotIn("control", r2_content("SWE-E01-C").splitlines()[0].lower())

    def test_allocation_schema_rejects_unknown_negative_bypass(self):
        allocation = {
            "marketplace_search": 80 * M,
            "marketplace_onsite": 60 * M,
            "crm_owned": 30 * M,
            "contingency_learning": 30 * M,
            "fake_offset": -70 * M,
        }
        self.assertFalse(validate_channel_allocation(allocation, 40 * M))

    def test_comparative_exposure_requires_canonical_event(self):
        left = EpisodeState("SWE-E01-P")
        right = EpisodeState("SWE-E01-P")
        for state in (left, right):
            state.reserve_creator_inventory(0, "zero")
            state.close_booking_gate(); state.deliver_r2()
        self.assertEqual(ComparativeDisposition.VALID, comparative_disposition(left, right))
        good = right.exposures[0]
        right.exposures[0] = ExposureEvent(good.event_kind, "12:00", good.world, good.content_hash, Phase.B)
        self.assertEqual(ComparativeDisposition.INVALID, comparative_disposition(left, right))


if __name__ == "__main__":
    unittest.main()
