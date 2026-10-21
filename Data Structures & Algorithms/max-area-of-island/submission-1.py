class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        maxArea = 0 

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
                return 0
            
            area = 1
            grid[i][j] = 0
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)

            return area
        

        for i in range (rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    currArea = dfs(i, j)
                    maxArea = max(maxArea, currArea)
             
            
        return maxArea