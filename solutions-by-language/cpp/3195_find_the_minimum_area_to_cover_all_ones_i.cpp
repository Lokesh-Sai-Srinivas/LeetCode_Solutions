class Solution {
public:
    int minimumArea(vector<vector<int>>& grid) {
        int minRow = -1, maxRow, minCol, maxCol;
        bool singleArea = true;

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    if (minRow == -1) {
                        minRow = maxRow = i;
                        minCol = maxCol = j;
                    } else {
                        singleArea = false;
                        minRow = min(minRow, i);
                        maxRow = max(maxRow, i);
                        minCol = min(minCol, j);
                        maxCol = max(maxCol, j);
                    }
                }
            }
        }

        return (minRow == -1) ? 0 : (singleArea ? 1 : (maxRow - minRow + 1) * (maxCol - minCol + 1));
    }
};