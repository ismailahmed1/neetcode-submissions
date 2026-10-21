class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # take a count of how many fresh fruits we have first
        # we can then do a multi source bfs starting from rotten bananas
        # have a minutes var keeping track
        # as soon as fresh fruits == 0 we return
        ROWS, COLS = len(grid), len(grid[0])
        fresh_fruits = 0 
        q = deque()

        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        def addCell(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return
            
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r,c))
                nonlocal fresh_fruits
                fresh_fruits -= 1
                
        minutes = 0 
        while q and fresh_fruits:
            qLen = len(q)
            for i in range (qLen):
                r,c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            minutes += 1
        
        return minutes if fresh_fruits == 0 else -1
        



        
        