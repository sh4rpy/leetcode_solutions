from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        encoded1 = [1, 2, 3]
        first1 = 1
        encoded2 = [6, 2, 7, 3]
        first2 = 4
        self.assertEqual(obj.decode(encoded1, first1), [1, 0, 2, 1])
        self.assertEqual(obj.decode(encoded2, first2), [4, 2, 0, 7, 4])
