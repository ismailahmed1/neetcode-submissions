class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid) , len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
                return 1
            
            if (i, j) in visit:
                return 0 

            total = 0 
            visit.add((i,j))
            total += dfs(i + 1, j)
            total += dfs(i - 1, j)
            total += dfs(i, j + 1)
            total += dfs(i, j - 1)
            return total



        perimeter = 0 
        for i in range (ROWS):
            for j in range (COLS):
                if grid[i][j] == 1:
                    perimeter += dfs(i, j)
        
        return perimeter