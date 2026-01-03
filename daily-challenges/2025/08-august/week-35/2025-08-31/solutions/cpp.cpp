class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<int> rows(9), cols(9), boxes(9);
        vector<pair<int,int>> empties;

        // initialize masks and empty list
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') {
                    empties.emplace_back(r, c);
                } else {
                    int d   = board[r][c] - '1';
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

private:
    bool dfs(vector<vector<char>>& board, int k,
             vector<int>& rows, vector<int>& cols,
             vector<int>& boxes, vector<pair<int,int>>& empties) {
        if (k == empties.size()) return true;

        // MRV: pick the empty with fewest candidates
        int best = k, minOpts = 10;
        for (int i = k; i < empties.size(); ++i) {
            auto [r, c] = empties[i];
            int used = rows[r] | cols[c] | boxes[(r/3)*3 + c/3];
            int opts = 9 - __builtin_popcount(used);
            if (opts < minOpts) {
                minOpts = opts;
                best    = i;
                if (opts == 1) break;
            }
        }

        swap(empties[k], empties[best]);
        int r   = empties[k].first;
        int c   = empties[k].second;
        int idx = (r/3)*3 + c/3;
        int used = rows[r] | cols[c] | boxes[idx];

        for (int d = 0; d < 9; ++d) {
            int bit = 1 << d;
            if (!(used & bit)) {
                board[r][c] = char('1' + d);
                rows[r] |= bit; cols[c] |= bit; boxes[idx] |= bit;

                if (dfs(board, k + 1, rows, cols, boxes, empties)) return true;

                rows[r] ^= bit; cols[c] ^= bit; boxes[idx] ^= bit;
                board[r][c] = '.';
            }
        }

        swap(empties[k], empties[best]);
        return false;
    }
};