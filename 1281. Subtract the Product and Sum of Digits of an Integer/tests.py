from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        n1 = 234
        n2 = 4421
        self.assertEqual(obj.subtractProductAndSum(n1), 15)
        self.assertEqual(obj.subtractProductAndSum(n2), 21)
