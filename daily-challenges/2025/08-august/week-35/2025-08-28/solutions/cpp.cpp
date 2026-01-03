class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& mat) {
        int rows = mat.size();
        int cols = mat[0].size();

        // bottom-left & main diagonals → non-increasing
        for (int r = 0; r < rows; ++r) {
            sortDiagonal(mat, r, 0, false);
        }
        // top-right diagonals → non-decreasing
        for (int c = 1; c < cols; ++c) {
            sortDiagonal(mat, 0, c, true);
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