from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        arr1 = [0, 2, 1, 5, 3, 4]
        arr2 = [5, 0, 1, 2, 3, 4]
        self.assertEqual(self.instance.buildArray(arr1), [0, 1, 2, 4, 5, 3])
        self.assertEqual(self.instance.buildArray(arr2), [4, 5, 0, 1, 2, 3])
