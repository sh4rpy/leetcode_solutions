from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        s1 = 'codeleet'
        indices1 = [4, 5, 6, 7, 0, 2, 1, 3]
        s2 = 'abc'
        indices2 = [0, 1, 2]
        s3 = 'aiohn'
        indices3 = [3, 1, 4, 2, 0]
        s4 = 'aaiougrt'
        indices4 = [4, 0, 2, 6, 7, 3, 1, 5]
        s5 = 'art'
        indices5 = [1, 0, 2]
        self.assertEqual(obj.restoreString(s1, indices1), 'leetcode')
        self.assertEqual(obj.restoreString(s2, indices2), 'abc')
        self.assertEqual(obj.restoreString(s3, indices3), 'nihao')
        self.assertEqual(obj.restoreString(s4, indices4), 'arigatou')
        self.assertEqual(obj.restoreString(s5, indices5), 'rat')
