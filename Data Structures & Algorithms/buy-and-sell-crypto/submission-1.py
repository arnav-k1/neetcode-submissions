class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 101
        
        for price in (prices):
            if price < buy:
                buy = price
            if (price - buy) > profit:
                profit = price - buy

        return profit