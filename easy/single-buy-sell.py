# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# assumption: stock price is never negative

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)

        # greatest element to the right of a given index, for each index
        greatest = [-1 for _ in prices]
        greatest[-1] = -1
        for i in range(len(prices)-2, -1, -1):
            greatest[i] = max(greatest[i+1], prices[i+1])

        # and our answer follows
        return max(0, max(g - price for price, g in zip(prices, greatest)))

# simpler: store min price so far, max profit so far
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 1e10
        max_ = 0
        for price in prices:
            if price < min_:
                min_ = price
            elif price - min_ > max_:
                max_ = price - min_
        return max_
