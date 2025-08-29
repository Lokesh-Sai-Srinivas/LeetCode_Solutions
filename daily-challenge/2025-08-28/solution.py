"""
Problem: 3446 - Sort Matrix by Diagonals  
Description: You are given an n × n square matrix of integers grid. Return the matrix such that .The diagonals in the bottom-left triangle (including the main diagonal) are sorted in non-increasing order.The diagonals in the top-right triangle are sorted in non-decreasing order.  
Date: 2025-08-28
"""

class Solution:
    def sortMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        # bottom-left & main diagonals → non-increasing
        for r in range(rows):
            self._sort_diagonal(mat, r, 0, increasing=False)

        # top-right diagonals → non-decreasing
        for c in range(1, cols):
            self._sort_diagonal(mat, 0, c, increasing=True)

        return mat

    def _sort_diagonal(
        self,
        mat: List[List[int]],
        row: int,
        col: int,
        increasing: bool
    ) -> None:
        rows, cols = len(mat), len(mat[0])
        length = min(rows - row, cols - col)

        # Extract diagonal
        diag = [mat[row + i][col + i] for i in range(length)]

        # Sort ascending, then reverse for non-increasing
        diag.sort()
        if not increasing:
            diag.reverse()

        # Write back sorted values
        for i, val in enumerate(diag):
            mat[row + i][col + i] = val
