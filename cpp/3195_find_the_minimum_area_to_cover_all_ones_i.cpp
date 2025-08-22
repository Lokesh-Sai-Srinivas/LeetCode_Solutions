"""
Problem: 3195 - Find the Minimum Area to Cover All Ones I  
Description: Given a binary matrix, return the minimum area of a rectangle that covers all the cells containing 1. If there is only one cell with 1, return 1. If there are no 1s, return 0.  
Date: 2025-08-22
"""

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
