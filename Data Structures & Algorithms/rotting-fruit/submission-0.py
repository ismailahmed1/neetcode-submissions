class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        q = deque()
        
        fresh_fruit = 0 

        def bfs(r, c):
            nonlocal fresh_fruit
            if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == 2 or grid[r][c] == 0:
                return
            else:
                grid[r][c] = 2
                fresh_fruit -= 1
                q.append((r,c))


        for r in range (ROWS):
            for c in range (COLUMNS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        

        minutes = 0
        while q and fresh_fruit > 0:
            for i in range (len(q)):
                r, c = q.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            minutes += 1
        
        if fresh_fruit:
            return -1
        else:
            return minutes

        