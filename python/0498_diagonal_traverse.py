"""
Problem: 498 - Diagonal Traverse  
Description: Given an m x n matrix mat, return an array of all the elements of the matrix in diagonal order. The traversal should alternate between upward and downward diagonals.  
Date: 2025-08-25
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])

        diagonals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])

        result = []
        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(reversed(diagonals[k]))
            else:
                result.extend(diagonals[k])
        
        return result
