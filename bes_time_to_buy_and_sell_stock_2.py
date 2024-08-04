class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        prices.append(0)
        min_price=prices[0]
        profit=0
        for i in range(n):
            if min_price>prices[i]:
                min_price=prices[i]
            elif min_price<prices[i] and prices[i]>prices[i+1]:
                profit+=prices[i]-min_price
                min_price=float('inf')
        return profit
        