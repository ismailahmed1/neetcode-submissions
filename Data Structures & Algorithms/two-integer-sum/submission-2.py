class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indicesMap = {}

        for i,n in enumerate(nums):
            diff = target - n 
            if diff in indicesMap:
                return [indicesMap[diff], i]
            indicesMap[n] = i 
        
        return False