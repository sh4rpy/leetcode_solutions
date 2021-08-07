from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        nums1 = [0, 1, 2, 3, 4]
        index1 = [0, 1, 2, 2, 1]
        nums2 = [1, 2, 3, 4, 0]
        index2 = [0, 1, 2, 3, 0]
        nums3 = [1]
        index3 = [0]
        self.assertEqual(obj.createTargetArray(nums1, index1), [0, 4, 1, 3, 2])
        self.assertEqual(obj.createTargetArray(nums2, index2), [0, 1, 2, 3, 4])
        self.assertEqual(obj.createTargetArray(nums3, index3), [1])
