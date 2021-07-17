class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        amount = 0
        product = 1
        while n:
            amount += n % 10
            product *= n % 10
            n //= 10
        return product - amount
