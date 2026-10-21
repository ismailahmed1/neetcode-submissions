class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if heights[r] > heights[l]:
                l += 1
            else: 
                r -= 1
            
            maxArea = max(maxArea, area)
        
        return maxArea