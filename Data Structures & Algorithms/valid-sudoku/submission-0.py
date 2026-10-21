class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            visited = []
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in visited:
                    return False
                else:
                    visited.append(board[r][c])
        
        for c in range(9):
            visited = []
            for r in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in visited:
                    return False
                else:
                    visited.append(board[r][c])
        
        for block_row in range(3):  
            for block_col in range(3):
                visited = []
                for r in range(block_row * 3, block_row * 3 + 3):  
                    for c in range(block_col * 3, block_col * 3 + 3):  
                        if board[r][c] == '.':
                            continue
                        elif board[r][c] in visited:
                            return False
                        else:
                            visited.append(board[r][c])
                
        return True
                    