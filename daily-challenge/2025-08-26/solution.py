"""
Problem: 3000 - Maximum Area of Longest Diagonal Rectangle  
Description: Given a list of rectangle dimensions, return the area of the rectangle with the longest diagonal. If multiple rectangles share the same diagonal length, return the one with the largest area among them.  
Date: 2025-08-26
"""

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = -1

        max_area = 0
        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > max_diag_sq or (diag_sq == max_diag_sq and area > max_area):
                max_diag_sq = diag_sq
                max_area = area
        return max_area
