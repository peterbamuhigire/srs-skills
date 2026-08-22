import json
import unittest
from pathlib import Path


class ApprovalAdapterTests(unittest.TestCase):
    def test_adapter_declares_fail_closed_actions(self):
        payload = json.loads((Path(__file__).parents[1] / "docs" / "approval-adapter.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["engine"], "srs")
        self.assertGreaterEqual(len(payload["actions"]), 5)
        for action in payload["actions"]:
            if action["class"] in {"L2", "L3"}:
                self.assertTrue(action["preview_required"])
                self.assertTrue(action["idempotency_required"])
                self.assertTrue(action["rollback"])
                self.assertTrue(action["verification"])


if __name__ == "__main__":
    unittest.main()
