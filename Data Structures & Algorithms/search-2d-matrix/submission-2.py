class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length, col_length = len(matrix), len(matrix[0])

        l, r = 0, col_length - 1


        while l < row_length and r >= 0: 
            if matrix[l][r] == target:
                return True
            elif matrix[l][r] > target:
                r -= 1
            else:
                l += 1

        return False