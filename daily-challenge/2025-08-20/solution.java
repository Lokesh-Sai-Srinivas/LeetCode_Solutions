"""
Problem: 1277 - Count Square Submatrices with All Ones  
Description: Given a binary matrix, count the number of square submatrices that have all ones. Each square must be contiguous and filled entirely with 1s.  
Date: 2025-08-20
"""


class Solution {
    public int countSquares(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length, total = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1 && i > 0 && j > 0)
                    matrix[i][j] = Math.min(Math.min(matrix[i-1][j], matrix[i][j-1]), matrix[i-1][j-1]) + 1;
                total += matrix[i][j];
            }
        return total;
    }
}
