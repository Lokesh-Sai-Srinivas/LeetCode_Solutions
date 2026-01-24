class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length, n = mat[0].length;
        int[][] ps = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                ps[i][j] = mat[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1];
            }
        }

        int low = 0, high = Math.min(m, n), ans = 0;

        while (low <= high) {
            int mid = (low + high) / 2;
            boolean ok = false;

            for (int i = mid; i <= m && !ok; i++) {
                for (int j = mid; j <= n; j++) {
                    int sum = ps[i][j] - ps[i - mid][j] - ps[i][j - mid] + ps[i - mid][j - mid];
                    if (sum <= threshold) {
                        ok = true;
                        break;
                    }
                }
            }

            if (ok) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }
}