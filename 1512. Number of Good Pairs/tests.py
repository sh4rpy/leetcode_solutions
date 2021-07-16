from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        arr1 = [1, 2, 3, 1, 1, 3]
        arr2 = [1, 1, 1, 1]
        arr3 = [1, 2, 3]
        self.assertEqual(self.instance.numIdenticalPairs(arr1), 4)
        self.assertEqual(self.instance.numIdenticalPairs(arr2), 6)
        self.assertEqual(self.instance.numIdenticalPairs(arr3), 0)
