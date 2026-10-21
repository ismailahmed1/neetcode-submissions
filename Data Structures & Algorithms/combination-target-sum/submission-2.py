class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol, subset = [], []

        def dfs(i, total):
            if total == target:
                sol.append(subset.copy())
                return
            elif i >= len(nums) or total > target:
                return 
            
            #choosing to include the same element
            subset.append(nums[i])
            dfs(i, total + nums[i])

            subset.pop()
            dfs(i + 1, total)

        
        dfs(0, 0)
        return sol

        
