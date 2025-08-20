"""
Problem: 1277 - Count Square Submatrices with All Ones  
Description: Given a binary matrix, count the number of square submatrices that have all ones. Each square must be contiguous and filled entirely with 1s.  
Date: 2025-08-20
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                total += matrix[i][j]
        return total
