class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol, subset = [], []

        candidates.sort()
        def dfs(i, total):
            if total == target:
                sol.append(subset.copy())
                return
            elif i >= len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0,0)
        return sol