from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        nums1 = [1, 3, 1]
        k1 = 1
        nums2 = [1, 1, 1]
        k2 = 2
        nums3 = [1, 6, 1]
        k3 = 3
        self.assertEqual(obj.smallestDistancePair(nums1, k1), 0)
        self.assertEqual(obj.smallestDistancePair(nums2, k2), 0)
        self.assertEqual(obj.smallestDistancePair(nums3, k3), 5)
