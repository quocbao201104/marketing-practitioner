from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from episode import EpisodeState, M, Phase, initialize_workspace


class EpisodeStateTests(unittest.TestCase):
    def test_reservation_ledger_tracks_full_commitment(self):
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(40 * M, "bounded learning")
        self.assertEqual(8 * M, state.deposit_spent)
        self.assertEqual(32 * M, state.open_creator_balance)
        self.assertEqual(40 * M, state.current_creator_commitment)
        self.assertEqual(130 * M, state.uncommitted_budget)

    def test_70m_is_technically_reachable(self):
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(70 * M, "test technical capability")
        self.assertEqual(70 * M, state.original_reservation_amount)
        self.assertEqual(14 * M, state.deposit_spent)

    def test_reduction_preserves_deposit(self):
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(70 * M, "initial")
        state.close_booking_gate()
        state.deliver_r2()
        state.reduce_creator_commitment(50 * M, "recovery")
        self.assertEqual(14 * M, state.deposit_spent)
        self.assertEqual(36 * M, state.open_creator_balance)
        self.assertEqual(50 * M, state.current_creator_commitment)
        self.assertEqual(120 * M, state.uncommitted_budget)

    def test_scheduler_delivers_r2_before_phase_b(self):
        state = EpisodeState("SWE-E01-C")
        state.reserve_creator_inventory(0, "explicit zero")
        state.close_booking_gate()
        event = state.deliver_r2()
        self.assertTrue(state.r2_delivered)
        self.assertEqual("11:00", event.logical_time)
        self.assertEqual(Phase.B, state.phase)

    def test_action_seals_artifact_hashes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            state = initialize_workspace(root)
            (root / "planning.md").write_text("R1 is ambiguous", encoding="utf-8")
            state.reserve_creator_inventory(30 * M, "bounded access")
            self.assertIn("planning.md", state.actions[-1].artifact_hashes)
            sealed_hash = state.actions[-1].artifact_hashes["planning.md"]
            (root / "planning.md").write_text("rewritten later", encoding="utf-8")
            self.assertEqual(sealed_hash, state.actions[-1].artifact_hashes["planning.md"])

    def test_early_terminal_is_not_supported(self):
        state = EpisodeState("SWE-E01-P")
        with self.assertRaises(ValueError):
            state.terminal_gate()


if __name__ == "__main__":
    unittest.main()
