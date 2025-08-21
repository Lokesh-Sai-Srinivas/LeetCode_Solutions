"""
Problem: 1504 - Count Submatrices With All Ones  
Description: Given a binary matrix, count the number of submatrices that contain only 1s. A submatrix is defined as a contiguous rectangular block within the matrix.  
Date: 2025-08-21
"""

class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
       int m = mat.size(), n = mat[0].size();
        vector<int> heights(n, 0);
        int total = 0;

        for (int i = 0; i < m; i++) {
            // update histogram heights
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1)
                    heights[j] += 1;
                else
                    heights[j] = 0;
            }

            // monotonic stack
            vector<int> rowSum(n, 0);
            stack<int> st;
            for (int j = 0; j < n; j++) {
                while (!st.empty() && heights[st.top()] >= heights[j])
                    st.pop();

                if (!st.empty()) {
                    int prev = st.top();
                    rowSum[j] = rowSum[prev] + heights[j] * (j - prev);
                } else {
                    rowSum[j] = heights[j] * (j + 1);
                }

                st.push(j);
                total += rowSum[j];
            }
        }
        return total; 
    }
};
