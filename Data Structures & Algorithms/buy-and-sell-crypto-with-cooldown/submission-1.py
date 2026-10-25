class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, lookingToBuy):
            if i >= len(prices):
                return 0 
            if ((i, lookingToBuy) in dp):
                return dp[(i, lookingToBuy)]
            
            if lookingToBuy:
                buy = dfs(i + 1, not lookingToBuy) - prices[i]
                cooldown = dfs(i + 1, lookingToBuy)
                dp[(i, lookingToBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not lookingToBuy) + prices[i]
                cooldown = dfs(i + 1, lookingToBuy)
                dp[(i, lookingToBuy)] = max(sell, cooldown)
            
            return dp[(i, lookingToBuy)]
        
        return dfs(0, True)

