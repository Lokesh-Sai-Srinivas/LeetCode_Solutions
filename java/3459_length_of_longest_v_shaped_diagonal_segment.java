"""
Problem: 3459 - Length of Longest V-Shaped Diagonal Segment  
Description: Given a 2D grid of integers, find the length of the longest V-shaped diagonal segment. A valid V-shape consists of two connected diagonals with alternating values (e.g., 1 → 2 → 1) and a single turning point. Diagonals must follow one of the four diagonal directions and may only turn once.  
Date: 2025-08-27
"""

import java.util.*;

class Solution {
    int n, m;
    int[][] grid;
    int[][] dirs = {{1,1},{1,-1},{-1,-1},{-1,1}}; // ↘, ↙, ↖, ↗
    int[] nextMap = new int[3];
    int[][][][][] dp;

    public int lenOfVDiagonal(int[][] grid) {
        this.grid = grid;
        n = grid.length;
        m = grid[0].length;

        // next value after v
        nextMap[1] = 2;
        nextMap[2] = 0;
        nextMap[0] = 2;

        dp = new int[n][m][2][4][3]; // -1 means uncomputed
        for (int[][][][] a : dp)
            for (int[][][] b : a)
                for (int[][] c : b)
                    for (int[] d : c)
                        Arrays.fill(d, -1);

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    for (int d = 0; d < 4; d++) {
                        ans = Math.max(ans, dfs(i, j, 0, d, 1));
                    }
                }
            }
        }
        return ans;
    }

    private int dfs(int x, int y, int turned, int dir, int expect) {
        if (x < 0 || y < 0 || x >= n || y >= m) return 0;
        if (grid[x][y] != expect) return 0;

        if (dp[x][y][turned][dir][expect] != -1)
            return dp[x][y][turned][dir][expect];

        int best = 1;
        int nx = x + dirs[dir][0], ny = y + dirs[dir][1];
        best = Math.max(best, 1 + dfs(nx, ny, turned, dir, nextMap[expect]));

        if (turned == 0) {
            int nd = (dir + 1) % 4;
            int tx = x + dirs[nd][0], ty = y + dirs[nd][1];
            best = Math.max(best, 1 + dfs(tx, ty, 1, nd, nextMap[expect]));
        }

        return dp[x][y][turned][dir][expect] = best;
    }
}
