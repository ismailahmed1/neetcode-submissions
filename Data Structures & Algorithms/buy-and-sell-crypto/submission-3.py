class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        max_P = 0
        profit = 0

        while (r < len(prices)):
            print (prices[r])
            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                max_P = max(profit, max_P)
            else:
                l = r
            r+=1
        return max_P
