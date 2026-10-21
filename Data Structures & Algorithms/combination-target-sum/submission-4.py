class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output, subset = [], []

        def dfs(i, total):
            if total == target:
                output.append(subset.copy())
                return
            elif i >= len(nums) or total > target:
                return 
            
            subset.append(nums[i])
            dfs(i, total + nums[i])

            subset.pop()
            dfs(i + 1, total)
        
        dfs(0,0)
        return output