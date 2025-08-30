"""
Problem: 36 - Valid Sudoku  
Description: Given a 9×9 board, determine if it is a valid Sudoku. Only filled cells (‘1’–‘9’) need to be checked: each row, each column, and each of the nine 3×3 sub-boxes must contain no duplicate digits. Empty cells are denoted by '.'.  
Date: 2025-08-30
"""

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<bitset<9>> rows(9), cols(9), boxes(9);
        
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char ch = board[r][c];
                if (ch == '.') continue;
                int d = ch - '1';
                int b = (r / 3) * 3 + (c / 3);
                if (rows[r].test(d) || cols[c].test(d) || boxes[b].test(d))
                    return false;
                rows[r].set(d);
                cols[c].set(d);
                boxes[b].set(d);
            }
        }
        return true;
    }
};
