class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices_map = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in indices_map:
                return [indices_map[diff], i]

            indices_map[n] = i 
        
        