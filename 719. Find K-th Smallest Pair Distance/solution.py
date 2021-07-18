class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        low, high, n = 0, nums[-1] - nums[0], len(nums)
        while low < high:
            mid, count, i, j = (low + high) // 2, 0, 0, 0
            while i < n:
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
                i += 1

            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
