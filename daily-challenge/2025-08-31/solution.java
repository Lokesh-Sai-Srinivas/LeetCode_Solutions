"""
Problem: 37 - Sudoku Solver  
Description: Write a program to solve a 9×9 Sudoku puzzle by filling the empty cells. Each digit from 1 to 9 must appear exactly once in each row, column, and 3×3 sub-box. The input board may contain empty cells denoted by '.'. The solution must modify the board in-place.  
Date: 2025-08-31
"""

class Solution {
    public void solveSudoku(char[][] board) {
        int[] rows = new int[9], cols = new int[9], boxes = new int[9];
        List<int[]> empties = new ArrayList<>();

        // initialize masks and empty list
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    empties.add(new int[]{r, c});
                } else {
                    int d = board[r][c] - '1';
                    int bit = 1 << d;
                    int idx = (r/3)*3 + c/3;
                    rows[r] |= bit;
                    cols[c] |= bit;
                    boxes[idx] |= bit;
                }
            }
        }

        dfs(board, 0, rows, cols, boxes, empties);
    }

    private boolean dfs(char[][] board, int k, int[] rows, int[] cols, int[] boxes, List<int[]> empties) {
        if (k == empties.size()) return true;

        // MRV: pick the empty with fewest candidates
        int best = k, minOpts = 10;
        for (int i = k; i < empties.size(); i++) {
            int r = empties.get(i)[0], c = empties.get(i)[1];
            int used = rows[r] | cols[c] | boxes[(r/3)*3 + c/3];
            int opts = 9 - Integer.bitCount(used);
            if (opts < minOpts) {
                minOpts = opts;
                best = i;
                if (opts == 1) break;
            }
        }

        Collections.swap(empties, k, best);
        int r = empties.get(k)[0], c = empties.get(k)[1], idx = (r/3)*3 + c/3;
        int used = rows[r] | cols[c] | boxes[idx];

        for (int d = 0; d < 9; d++) {
            int bit = 1 << d;
            if ((used & bit) == 0) {
                board[r][c] = (char)('1' + d);
                rows[r] |= bit; cols[c] |= bit; boxes[idx] |= bit;

                if (dfs(board, k + 1, rows, cols, boxes, empties)) return true;

                rows[r] ^= bit; cols[c] ^= bit; boxes[idx] ^= bit;
                board[r][c] = '.';
            }
        }

        Collections.swap(empties, k, best);
        return false;
    }
}
