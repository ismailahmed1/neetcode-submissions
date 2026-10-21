class Solution:
    def climbStairs(self, n: int) -> int:
        older = 0
        newer = 1

        for i in range (n - 1, -1, -1):
            totalSteps = older + newer
            older = newer
            newer = totalSteps
        
        return totalSteps

