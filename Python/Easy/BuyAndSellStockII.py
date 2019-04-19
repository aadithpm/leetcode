class Solution:
    def maxProfit(self, prices):
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx - 1] < prices[idx]:
                print("Val:", prices[idx])
                print("Prev Val:", prices[idx - 1])
                profit += prices[idx] - prices[idx - 1]
                print("P:", profit)
        return profit