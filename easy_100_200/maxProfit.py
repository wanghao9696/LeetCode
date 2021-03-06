class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                money = money + (prices[i] - prices[i - 1])
            else:
                continue
        return money
