class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.search(nums[1:]), self.search(nums[:-1]))

    
    def search(self, nums):
        rob_old, rob_new = 0, 0

        for n in nums:
            temp = max(rob_old + n, rob_new)
            rob_old = rob_new
            rob_new = temp
        
        return rob_new