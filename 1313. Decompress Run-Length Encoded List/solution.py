class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        decompressed = []
        for i in range(0, len(nums) - 1, 2):
            freq, value = nums[i], nums[i + 1]
            decompressed += [value] * freq
        return decompressed
