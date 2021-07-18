from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        candies1 = [2, 3, 5, 1, 3]
        extra_candies1 = 3
        candies2 = [4, 2, 1, 1, 2]
        extra_candies2 = 1
        candies3 = [12, 1, 12]
        extra_candies3 = 10
        self.assertEqual(
            obj.kidsWithCandies(candies1, extra_candies1),
            [True, True, True, False, True],
        )
        self.assertEqual(
            obj.kidsWithCandies(candies2, extra_candies2),
            [True, False, False, False, False],
        )
        self.assertEqual(
            obj.kidsWithCandies(candies3, extra_candies3), [True, False, True]
        )
