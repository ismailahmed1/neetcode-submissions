class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0 
        minLen = float('inf')
        total = 0  

        while r < len(nums):
            total += nums[r]
            while total >= target:
                minLen = min(minLen, r - l + 1)
                total -= nums[l]
                l += 1
            
            r += 1
        
        return minLen if minLen != float('inf') else 0 