from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        grid1 = [[1, 2, 3], [3, 2, 1]]
        grid2 = [[1, 5], [7, 3], [3, 5]]
        grid3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        self.assertEqual(self.instance.maximumWealth(grid1), 6)
        self.assertEqual(self.instance.maximumWealth(grid2), 10)
        self.assertEqual(self.instance.maximumWealth(grid3), 17)
