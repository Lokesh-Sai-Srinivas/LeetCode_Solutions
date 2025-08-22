"""
Problem: 3195 - Find the Minimum Area to Cover All Ones I  
Description: Given a binary matrix, return the minimum area of a rectangle that covers all the cells containing 1. If there is only one cell with 1, return 1. If there are no 1s, return 0.  
Date: 2025-08-22
"""

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row = max_row = min_col = max_col = None
        single_area = True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if min_row is None:
                        min_row = max_row = i
                        min_col = max_col = j
                    else:
                        single_area = False
                        min_row = min(min_row, i)
                        max_row = max(max_row, i)
                        min_col = min(min_col, j)
                        max_col = max(max_col, j)

        return 1 if single_area else (max_row - min_row + 1) * (max_col - min_col + 1)
