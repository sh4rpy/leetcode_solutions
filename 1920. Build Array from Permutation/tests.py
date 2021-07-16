from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        arr1 = [0, 2, 1, 5, 3, 4]
        arr2 = [5, 0, 1, 2, 3, 4]
        self.assertEqual(obj.buildArray(arr1), [0, 1, 2, 4, 5, 3])
        self.assertEqual(obj.buildArray(arr2), [4, 5, 0, 1, 2, 3])
