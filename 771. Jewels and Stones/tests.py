from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        jewels1 = 'aA'
        stones1 = 'aAAbbbb'
        jewels2 = 'z'
        stones2 = 'ZZ'
        self.assertEqual(obj.numJewelsInStones(jewels1, stones1), 3)
        self.assertEqual(obj.numJewelsInStones(jewels2, stones2), 0)
