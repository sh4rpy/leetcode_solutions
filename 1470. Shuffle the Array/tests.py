from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        arr1 = [2, 5, 1, 3, 4, 7]
        n1 = 3
        arr2 = [1, 2, 3, 4, 4, 3, 2, 1]
        n2 = 4
        arr3 = [1, 1, 2, 2]
        n3 = 2
        self.assertEqual(self.instance.shuffle(arr1, n1), [2, 3, 5, 4, 1, 7])
        self.assertEqual(self.instance.shuffle(arr2, n2), [1, 4, 2, 3, 3, 2, 4, 1])
        self.assertEqual(self.instance.shuffle(arr3, n3), [1, 2, 1, 2])
