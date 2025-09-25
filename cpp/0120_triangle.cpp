"""
Problem: 120 - Triangle  
Description: Given a triangle array, return the minimum path sum from top to bottom. At each step, you may move to adjacent numbers on the row below.  
Date: 2025-09-25
"""

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> dp = triangle[n - 1];

        for (int i = n - 2; i >= 0; i-- ){
            for (int j = 0 ; j <= i; j++){
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
            }
        }
        return dp[0];
    }
};
