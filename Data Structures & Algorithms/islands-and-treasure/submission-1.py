class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647 
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j, dist):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == -1 or grid[i][j] < dist:
                return 

            grid[i][j] = dist
            dfs(i + 1, j, dist + 1)
            dfs(i - 1, j, dist + 1)
            dfs(i, j + 1, dist + 1)
            dfs(i, j - 1, dist + 1)


        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        
                