class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxStock = 0 

        while r < len(prices):
            stock = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            
            r += 1

            maxStock = max(maxStock, stock)

        return maxStock