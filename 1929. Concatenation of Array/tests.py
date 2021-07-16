from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        arr1 = [1, 2, 1]
        arr2 = [1, 3, 2, 1]
        self.assertEqual(obj.getConcatenation(arr1), [1, 2, 1, 1, 2, 1])
        self.assertEqual(obj.getConcatenation(arr2), [1, 3, 2, 1, 1, 3, 2, 1])
