class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         numCount = {}

         for i in nums:
            numCount[i] = 1 + numCount.get(i, 0)
            if numCount[i] > 1:
                return True

        
         return False