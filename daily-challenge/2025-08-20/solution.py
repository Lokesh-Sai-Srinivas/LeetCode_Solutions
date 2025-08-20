"""
Problem: 2348 - Number of Zero-Filled Subarrays  
Description: Given an integer array nums, return the number of contiguous subarrays that are filled with 0. A subarray is a contiguous non-empty sequence of elements within an array.  
Date: 2025-08-19
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
