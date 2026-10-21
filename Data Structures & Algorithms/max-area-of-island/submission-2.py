class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
                return 0
            
            area = 1
            grid[i][j] = 0
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area
        
        max_area = 0
        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area
