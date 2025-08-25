"""
Problem: 498 - Diagonal Traverse  
Description: Given an m x n matrix mat, return an array of all the elements of the matrix in diagonal order. The traversal should alternate between upward and downward diagonals.  
Date: 2025-08-25
"""

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        Map<Integer, List<Integer>> diagonals = new HashMap<>();
        int m = mat.length, n = mat[0].length;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                diagonals.computeIfAbsent(i + j, x -> new ArrayList<>()).add(mat[i][j]);

        List<Integer> result = new ArrayList<>();
        for (int k = 0; k < m + n - 1; k++) {
            List<Integer> diag = diagonals.get(k);
            if (k % 2 == 0)
                Collections.reverse(diag);
            result.addAll(diag);
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
