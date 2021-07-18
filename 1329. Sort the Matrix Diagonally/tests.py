from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        matrix1 = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
        matrix2 = [
            [11, 25, 66, 1, 69, 7],
            [23, 55, 17, 45, 15, 52],
            [75, 31, 36, 44, 58, 8],
            [22, 27, 33, 25, 68, 4],
            [84, 28, 14, 11, 5, 50],
        ]
        self.assertEqual(
            obj.diagonalSort(matrix1), [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]
        )
        self.assertEqual(
            obj.diagonalSort(matrix2),
            [
                [5, 17, 4, 1, 52, 7],
                [11, 11, 25, 45, 8, 69],
                [14, 23, 25, 44, 58, 15],
                [22, 27, 31, 36, 50, 66],
                [84, 28, 75, 33, 55, 68],
            ],
        )
