"""
Problem: 2348 - Number of Zero-Filled Subarrays  
Description: Given an integer array nums, return the number of contiguous subarrays that are filled with 0. A subarray is a contiguous non-empty sequence of elements within an array.  
Date: 2025-08-19
"""

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(),total = 0;
        for(int i = 0; i < m ; ++i){
            for (int j = 0 ; j < n ; ++j ){
                if(matrix[i][j] && i && j)
                    matrix[i][j] = min({matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]}) + 1;
                total += matrix[i][j];
            }
        }
        return total;
    }
};
