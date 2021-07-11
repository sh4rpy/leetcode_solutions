class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest_candies_number = max(candies)
        return [candy + extraCandies >= greatest_candies_number for candy in candies]
