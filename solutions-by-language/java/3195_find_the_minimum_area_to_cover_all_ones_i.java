class Solution {
    public int minimumArea(int[][] grid) {
        Integer minRow = null, maxRow = null, minCol = null, maxCol = null;
        boolean singleArea = true;

        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[0].length; ++j) {
                if (grid[i][j] == 1) {
                    if (minRow == null) {
                        minRow = maxRow = i;
                        minCol = maxCol = j;
                    } else {
                        singleArea = false;
                        minRow = Math.min(minRow, i);
                        maxRow = Math.max(maxRow, i);
                        minCol = Math.min(minCol, j);
                        maxCol = Math.max(maxCol, j);
                    }
                }
            }
        }

        return (minRow == null) ? 0 : (singleArea ? 1 : (maxRow - minRow + 1) * (maxCol - minCol + 1));
    }
}