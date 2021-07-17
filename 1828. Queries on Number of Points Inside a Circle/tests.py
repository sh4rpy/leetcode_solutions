from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        points1 = [[1, 3], [3, 3], [5, 3], [2, 2]]
        queries1 = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        points2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        queries2 = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
        self.assertEqual(obj.countPoints(points1, queries1), [3, 2, 2])
        self.assertEqual(obj.countPoints(points2, queries2), [2, 3, 2, 4])
