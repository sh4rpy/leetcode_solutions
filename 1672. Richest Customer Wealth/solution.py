class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            current_amount = sum(account)
            if current_amount > max_wealth:
                max_wealth = current_amount
        return max_wealth
