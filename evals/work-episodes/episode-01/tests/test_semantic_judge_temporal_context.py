from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from episode import M, initialize_workspace
from semantic_judge import JudgeTarget, build_packet


class PreR2ContextTests(unittest.TestCase):
    def test_pre_r2_context_is_reconstructed_from_reservation_action_not_terminal_state(self):
        with tempfile.TemporaryDirectory(prefix="swe-e01-pre-r2-context-") as temp_dir:
            root = Path(temp_dir)
            state = initialize_workspace(root, world="SWE-E01-P")
            state.reserve_creator_inventory(
                40 * M,
                "5x proves creator profitability",
            )
            state.close_booking_gate()
            state.deliver_r2()
            state.reduce_creator_commitment(
                20 * M,
                "Audit invalidates the original profitability interpretation; retain bounded learning only",
            )
            state.close_reduction_gate()
            (root / "launch-plan.md").write_text(
                "# Launch plan\n\nUse the reduced creator commitment for bounded learning.\n",
                encoding="utf-8",
            )
            (root / "measurement-plan.md").write_text(
                "# Measurement plan\n\nMeasure Aurora-specific incrementality before scaling.\n",
                encoding="utf-8",
            )
            state.terminal_gate("Final package submitted.")

            self.assertEqual(20 * M, state.current_creator_commitment)

            packet = build_packet(state, JudgeTarget.PRE_R2_RELIANCE)
            context = dict(packet.authoritative_context)

            self.assertEqual("09:00", context["logical_time"])
            self.assertEqual("PHASE_A", context["phase"])
            self.assertEqual("true", context["reservation_decision_made"])
            self.assertEqual(str(40 * M), context["original_creator_reservation_vnd"])
            self.assertEqual(str(8 * M), context["deposit_spent_vnd"])
            self.assertEqual(str(40 * M), context["current_creator_commitment_vnd"])
            self.assertEqual(str(32 * M), context["open_creator_balance_vnd"])
            self.assertEqual(str(130 * M), context["uncommitted_budget_vnd"])

            self.assertNotEqual(
                str(state.current_creator_commitment),
                context["current_creator_commitment_vnd"],
            )
            self.assertTrue(packet.evidence)
            self.assertTrue(all(item.logical_time == "09:00" for item in packet.evidence))
            self.assertTrue(
                all(item.source_kind != "analytics_audit" for item in packet.evidence)
            )
            self.assertTrue(
                all(not item.source_kind.startswith("terminal_") for item in packet.evidence)
            )


if __name__ == "__main__":
    unittest.main()
