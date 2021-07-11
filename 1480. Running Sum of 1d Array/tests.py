from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        arr1 = [1, 2, 3, 4]
        arr2 = [1, 1, 1, 1, 1]
        arr3 = [3, 1, 2, 10, 1]
        self.assertEqual(self.instance.runningSum(arr1), [1, 3, 6, 10])
        self.assertEqual(self.instance.runningSum(arr2), [1, 2, 3, 4, 5])
        self.assertEqual(self.instance.runningSum(arr3), [3, 4, 6, 16, 17])
