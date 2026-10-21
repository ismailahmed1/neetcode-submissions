class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0 

        for i in nums:
            length = 1
            if (i - 1) not in nums:
                while (i + length) in nums:
                    length += 1
            
            max_length = max(max_length, length)
        
        return max_length

        