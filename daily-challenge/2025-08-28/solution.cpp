"""
Problem: 3446 - Sort Matrix by Diagonals  
Description: You are given an n × n square matrix of integers grid. Return the matrix such that .The diagonals in the bottom-left triangle (including the main diagonal) are sorted in non-increasing order.The diagonals in the top-right triangle are sorted in non-decreasing order.  
Date: 2025-08-28
"""


class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& mat) {
        int rows = mat.size();
        int cols = mat[0].size();

        // bottom-left & main diagonals → non-increasing
        for (int r = 0; r < rows; ++r) {
            sortDiagonal(mat, r, 0, /*increasing=*/false);
        }
        // top-right diagonals → non-decreasing
        for (int c = 1; c < cols; ++c) {
            sortDiagonal(mat, 0, c, /*increasing=*/true);
        }
        return mat;
    }

private:
    void sortDiagonal(vector<vector<int>>& mat,
                      int row, int col,
                      bool increasing) {
        int rows = mat.size();
        int cols = mat[0].size();
        int len = min(rows - row, cols - col);

        // extract
        vector<int> diag(len);
        for (int i = 0; i < len; ++i) {
            diag[i] = mat[row + i][col + i];
        }

        // sort ascending, then reverse if non-increasing
        sort(diag.begin(), diag.end());
        if (!increasing) {
            reverse(diag.begin(), diag.end());
        }

        // write back
        for (int i = 0; i < len; ++i) {
            mat[row + i][col + i] = diag[i];
        }
    }
};
