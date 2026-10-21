class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output_filter = []

        for i in range (len(nums)):
            output_filter.append(nums[:i] + nums [i + 1:len(nums)])

        output = []
        for outputs in output_filter:
            res = 1
            for i in outputs:
                res *= i 
            output.append(res)
        
        return output
                
            