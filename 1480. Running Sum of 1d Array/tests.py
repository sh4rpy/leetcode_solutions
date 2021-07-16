from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        arr1 = [1, 2, 3, 4]
        arr2 = [1, 1, 1, 1, 1]
        arr3 = [3, 1, 2, 10, 1]
        self.assertEqual(obj.runningSum(arr1), [1, 3, 6, 10])
        self.assertEqual(obj.runningSum(arr2), [1, 2, 3, 4, 5])
        self.assertEqual(obj.runningSum(arr3), [3, 4, 6, 16, 17])
