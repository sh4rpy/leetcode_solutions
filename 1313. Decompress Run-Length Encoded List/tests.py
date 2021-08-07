from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        nums1 = [1, 2, 3, 4]
        nums2 = [1, 1, 2, 3]
        self.assertEqual(obj.decompressRLElist(nums1), [2, 4, 4, 4])
        self.assertEqual(obj.decompressRLElist(nums2), [1, 3, 3])
