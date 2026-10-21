class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l <= r:
            m = (l + r) // 2
            total_hours = sum(math.ceil(p/m) for p in piles)

            if total_hours <= h: 
                result = m 
                r = m - 1
            else:
                l = m + 1
        
        return result
        