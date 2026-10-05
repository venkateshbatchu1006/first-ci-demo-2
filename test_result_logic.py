import unittest
from result_logic import check_result


class TestResultLogic(unittest.TestCase):

    def test_fail_due_to_attendance(self):
        self.assertEqual(check_result(60, 80), "Fail")

    def test_fail_due_to_marks(self):
        self.assertEqual(check_result(80, 30), "Fail")

    def test_pass_case(self):
        self.assertEqual(check_result(80, 80), "Pass")


if __name__ == "__main__":
    unittest.main()
