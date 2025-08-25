"""
Problem: 498 - Diagonal Traverse  
Description: Given an m x n matrix mat, return an array of all the elements of the matrix in diagonal order. The traversal should alternate between upward and downward diagonals.  
Date: 2025-08-25
"""

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        unordered_map<int, vector<int>> diagonals;
        int  m = mat.size(), n = mat[0].size();

        for(int i = 0; i < m ; ++i){
            for (int j = 0 ; j < n ; ++j){
                diagonals[i + j].push_back(mat[i][j]);
            }
        }

        vector<int> result;
        for(int k = 0 ; k < m + n - 1; ++k){
            if(k % 2 == 0)
                result.insert(result.end(), diagonals[k].rbegin(), diagonals[k].rend());
            else
                result.insert(result.end(), diagonals[k].begin(),   diagonals[k].end());
        }

        return result;
    }
};
