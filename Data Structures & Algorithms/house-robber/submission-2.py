class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_old, rob_new = 0, 0

        for n in nums:
            temp = max(n + rob_old, rob_new)
            rob_old = rob_new
            rob_new = temp
        
        return rob_new

        
            