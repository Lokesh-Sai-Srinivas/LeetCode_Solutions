"""
Problem: 36 - Valid Sudoku  
Description: Given a 9×9 board, determine if it is a valid Sudoku. Only filled cells (‘1’–‘9’) need to be checked: each row, each column, and each of the nine 3×3 sub-boxes must contain no duplicate digits. Empty cells are denoted by '.'.  
Date: 2025-08-30
"""

class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        for(int r = 0 ; r < 9 ; r++){
            for (int c = 0 ; c < 9 ; c++){
                char ch = board[r][c];
                if (ch == '.') continue;
                int d = ch - '1';
                int b = (r / 3) * 3 + (c / 3);
                if (rows[r][d] || cols[c][d] || boxes[b][d])
                    return false;
                rows[r][d] = cols[c][d] = boxes[b][d] = true;
            }
        }

        return true;
    }
}
