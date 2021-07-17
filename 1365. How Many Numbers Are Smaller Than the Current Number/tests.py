from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        arr1 = [8, 1, 2, 2, 3]
        arr2 = [6, 5, 4, 8]
        arr3 = [7, 7, 7, 7]
        self.assertEqual(obj.smallerNumbersThanCurrent(arr1), [4, 0, 1, 1, 3])
        self.assertEqual(obj.smallerNumbersThanCurrent(arr2), [2, 1, 0, 3])
        self.assertEqual(obj.smallerNumbersThanCurrent(arr3), [0, 0, 0, 0])
