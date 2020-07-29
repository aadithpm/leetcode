class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0
        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)
        
        return max(sold, reset)
