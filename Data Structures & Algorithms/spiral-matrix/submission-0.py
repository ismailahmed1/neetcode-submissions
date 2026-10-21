class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        res = []
        i = j = d = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for _ in range (COLS * ROWS):
            res.append(matrix[i][j])
            visited.add((i,j))
            di, dj = dirs[d]
            if not ((i + di) >= 0 and (j + dj) 
                >= 0 and (i + di) < ROWS and (j + dj) < 
                COLS and (i + di, j + dj) not in visited):
                d = (d + 1) % 4
                di, dj = dirs[d]
            
            i, j = i + di, j + dj
        
        return res




        