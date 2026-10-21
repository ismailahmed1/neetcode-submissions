class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        repeat = []

        for i in nums: 
            if i in repeat:
                return True
            repeat.append(i)
        
        return False