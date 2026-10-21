class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        output, subset = [], []
        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r >= ROWS or c >= COLS or r < 0 or c < 0
                or (r,c) in seen or board[r][c] != word[i]):
                return
            
            seen.add((r,c))
            if (dfs(r, c + 1, i + 1) or 
            dfs(r, c - 1, i + 1) or dfs(r + 1, c, i + 1) or 
            dfs(r - 1, c, i + 1)):
                return True
            seen.remove((r,c))
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
