"""
Problem: 1039 - Minimum Score Triangulation of Polygon  
Description: Given an array of integers representing the vertices of a polygon, return the minimum score to triangulate the polygon. The score of a triangle is the product of its three vertices, and the total score is the sum of all triangle scores.  
Date: 2025-09-29
"""

class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]
