class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        i = 0
        j = 1
        ans = 0
        while i < len(nums) - 1:
            if nums[i] == nums[j]:
                ans += 1
            if j == len(nums) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        return ans
