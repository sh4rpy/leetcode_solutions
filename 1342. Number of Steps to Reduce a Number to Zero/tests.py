from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        num1 = 14
        num2 = 8
        num3 = 123
        self.assertEqual(obj.numberOfSteps(num1), 6)
        self.assertEqual(obj.numberOfSteps(num2), 4)
        self.assertEqual(obj.numberOfSteps(num3), 12)
