from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        grid1 = [[1, 2, 3], [3, 2, 1]]
        grid2 = [[1, 5], [7, 3], [3, 5]]
        grid3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        self.assertEqual(obj.maximumWealth(grid1), 6)
        self.assertEqual(obj.maximumWealth(grid2), 10)
        self.assertEqual(obj.maximumWealth(grid3), 17)
