import unittest
from unittest.mock import patch

from capstone_agent import AgentState, plan


class FrameworkTests(unittest.TestCase):
    @patch("capstone_agent.generate", return_value="1. Learn\n2. Practise\n3. Review")
    def test_plan_has_three_steps(self, _mock_generate):
        state = AgentState("Learn agents")
        plan(state)
        self.assertEqual(len(state.plan), 3)
        self.assertEqual(state.status, "planned")


if __name__ == "__main__":
    unittest.main()
