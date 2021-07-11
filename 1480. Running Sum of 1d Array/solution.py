class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        summand = 0
        ans = []
        for el in nums:
            summand += el
            ans.append(summand)
        return ans
