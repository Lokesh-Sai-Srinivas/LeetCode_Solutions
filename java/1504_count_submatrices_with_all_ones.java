"""
Problem: 1504 - Count Submatrices With All Ones  
Description: Given a binary matrix, count the number of submatrices that contain only 1s. A submatrix is defined as a contiguous rectangular block within the matrix.  
Date: 2025-08-21
"""

import java.util.*;

class Solution {
    public int numSubmat(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] heights = new int[n];
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
            int[] rowSum = new int[n];
            Deque<Integer> stack = new ArrayDeque<>();
            for (int j = 0; j < n; j++) {
                while (!stack.isEmpty() && heights[stack.peek()] >= heights[j]) {
                    stack.pop();
                }

                if (!stack.isEmpty()) {
                    int prev = stack.peek();
                    rowSum[j] = rowSum[prev] + heights[j] * (j - prev);
                } else {
                    rowSum[j] = heights[j] * (j + 1);
                }

                stack.push(j);
                total += rowSum[j];
            }
        }
        return total;
    }
}
