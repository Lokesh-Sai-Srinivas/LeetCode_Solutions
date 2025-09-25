"""
Problem: 120 - Triangle  
Description: Given a triangle array, return the minimum path sum from top to bottom. At each step, you may move to adjacent numbers on the row below.  
Date: 2025-09-25
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
