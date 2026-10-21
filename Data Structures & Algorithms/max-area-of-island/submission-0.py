class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        max_islands = 0 

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
                return 0
            grid[i][j] = 0  
            count = 1  
            count += dfs(i + 1, j)  
            count += dfs(i - 1, j)  
            count += dfs(i, j + 1)  
            count += dfs(i, j - 1)  
            return count

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:  
                    num1 = dfs(i, j)  
                    max_islands = max(max_islands, num1)  

        return max_islands  # Return the maximum island area
