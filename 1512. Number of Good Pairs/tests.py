from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        arr1 = [1, 2, 3, 1, 1, 3]
        arr2 = [1, 1, 1, 1]
        arr3 = [1, 2, 3]
        self.assertEqual(obj.numIdenticalPairs(arr1), 4)
        self.assertEqual(obj.numIdenticalPairs(arr2), 6)
        self.assertEqual(obj.numIdenticalPairs(arr3), 0)
