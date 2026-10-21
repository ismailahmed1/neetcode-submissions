class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rMap = defaultdict(set)
        cMap = defaultdict(set)
        squareMap = defaultdict(set)

        for r in range (9):
            for c in range (9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rMap[r] or board[r][c] in cMap[c] or board[r][c] in squareMap[r // 3, c // 3]):
                    return False
                else:
                    rMap[r].add(board[r][c])
                    cMap[c].add(board[r][c])
                    squareMap[r//3, c // 3].add(board[r][c])
        return True