class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        output = [0] * len(nums)

        #prefix
        prefix_num = 1
        for i in range(len(nums)):
            prefix[i] = prefix_num
            prefix_num *= nums[i]
        
        suffix_num = 1
        for i in range (len(nums) -1, -1, -1):
            suffix[i] = suffix_num
            suffix_num *= nums[i]

        for i in range (len(nums)):
            output[i] = suffix[i] * prefix[i]
        
        return output