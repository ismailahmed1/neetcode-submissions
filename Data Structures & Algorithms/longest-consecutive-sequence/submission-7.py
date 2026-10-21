class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop through the list
        # check if (n - 1) present in nums set
        # if yes, skip 
        # if not keep incrementing length as long as we have n + 1 in set
        # store max length

        nums = set(nums)
        maxLength = 0

        for i in nums:
            if (i - 1) in nums:
                continue
            
            length = 0 
            while (i + length) in nums:
                length += 1
            
            maxLength = max(maxLength, length)
        

        return maxLength
        
        