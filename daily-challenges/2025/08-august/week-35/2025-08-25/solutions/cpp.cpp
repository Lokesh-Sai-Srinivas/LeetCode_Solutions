class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        unordered_map<int, vector<int>> diagonals;
        int  m = mat.size(), n = mat[0].size();

        for(int i = 0; i < m ; ++i){
            for (int j = 0 ; j < n ; ++j){
                diagonals[i + j].push_back(mat[i][j]);
            }
        }

        vector<int> result;
        for(int k = 0 ; k < m + n - 1; ++k){
            if(k % 2 == 0)
                result.insert(result.end(), diagonals[k].rbegin(), diagonals[k].rend());
            else
                result.insert(result.end(), diagonals[k].begin(),   diagonals[k].end());
        }

        return result;
    }
};