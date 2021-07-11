from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        arr1 = [1, 2, 1]
        arr2 = [1, 3, 2, 1]
        self.assertEqual(self.instance.getConcatenation(arr1), [1, 2, 1, 1, 2, 1])
        self.assertEqual(self.instance.getConcatenation(arr2), [1, 3, 2, 1, 1, 3, 2, 1])
