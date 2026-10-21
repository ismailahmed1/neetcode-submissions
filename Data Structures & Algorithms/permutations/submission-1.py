class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol, subset = [], []

        def backtrack():
            if len(subset) == len(nums):
                sol.append(subset.copy())
                return
            
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    backtrack()
                    subset.pop()
            
            return sol
    
        return backtrack()