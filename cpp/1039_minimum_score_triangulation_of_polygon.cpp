"""
Problem: 1039 - Minimum Score Triangulation of Polygon  
Description: Given an array of integers representing the vertices of a polygon, return the minimum score to triangulate the polygon. The score of a triangle is the product of its three vertices, and the total score is the sum of all triangle scores.  
Date: 2025-09-29
"""

class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int len = 3; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len - 1;
                dp[i][j] = INT_MAX;
                for (int k = i + 1; k < j; ++k) {
                    int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                    dp[i][j] = min(dp[i][j], cost);
                }
            }
        }

        return dp[0][n - 1];
    }
};
