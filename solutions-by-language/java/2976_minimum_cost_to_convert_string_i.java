class Solution {
    public long minimumCost(String source, String target, char[] org, char[] chg, int[] cost) {
        final long INF = (long) 1e18;
        long[][] dist = new long[26][26];

        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dist[i][j] = (i == j) ? 0L : INF;
            }
        }

        for (int i = 0; i < org.length; i++) {
            int u = org[i] - 'a';
            int v = chg[i] - 'a';
            dist[u][v] = Math.min(dist[u][v], (long) cost[i]);
        }

        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                if (dist[i][k] == INF)
                    continue;
                for (int j = 0; j < 26; j++) {
                    if (dist[k][j] == INF)
                        continue;
                    long nd = dist[i][k] + dist[k][j];
                    if (nd < dist[i][j])
                        dist[i][j] = nd;
                }
            }
        }

        long ans = 0L;
        int n = source.length();
        for (int i = 0; i < n; i++) {
            char s = source.charAt(i);
            char t = target.charAt(i);
            if (s == t)
                continue;
            int c1 = s - 'a';
            int c2 = t - 'a';
            if (dist[c1][c2] == INF)
                return -1L; 
            ans += dist[c1][c2];
        }
        return ans;
    }
}