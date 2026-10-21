class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol, subset = [], []

        def dfs(open_n, close_n):
            if open_n == close_n == n:
                sol.append("".join(subset))
                return
            
            if open_n < n:
                subset.append('(')
                dfs(open_n + 1, close_n)
                subset.pop()
            
            if open_n > close_n:
                subset.append(')')
                dfs(open_n, close_n + 1)
                subset.pop()
        
        dfs(0,0)
        return sol