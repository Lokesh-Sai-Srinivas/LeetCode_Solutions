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