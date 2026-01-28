class Solution {
    static class State {
        int i, j, t;
        long d;
        State(long d, int i, int j, int t) {
            this.d = d;
            this.i = i;
            this.j = j;
            this.t = t;
        }
    }

    public int minCost(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        long INF = Long.MAX_VALUE / 4;

        long[][][] dist = new long[m][n][k + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                Arrays.fill(dist[i][j], INF);

        List<int[]> cells = new ArrayList<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cells.add(new int[]{grid[i][j], i, j});

        cells.sort(Comparator.comparingInt(a -> a[0]));
        int[] ptr = new int[k + 1];

        PriorityQueue<State> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a.d));
        dist[0][0][0] = 0;
        pq.add(new State(0, 0, 0, 0));

        int[] dx = {1, 0};
        int[] dy = {0, 1};

        while (!pq.isEmpty()) {
            State cur = pq.poll();
            if (cur.d != dist[cur.i][cur.j][cur.t]) continue;

            if (cur.i == m - 1 && cur.j == n - 1)
                return (int) cur.d;

            for (int d = 0; d < 2; d++) {
                int ni = cur.i + dx[d];
                int nj = cur.j + dy[d];
                if (ni < m && nj < n) {
                    long nd = cur.d + grid[ni][nj];
                    if (nd < dist[ni][nj][cur.t]) {
                        dist[ni][nj][cur.t] = nd;
                        pq.add(new State(nd, ni, nj, cur.t));
                    }
                }
            }

            if (cur.t < k) {
                while (ptr[cur.t] < cells.size() &&
                       cells.get(ptr[cur.t])[0] <= grid[cur.i][cur.j]) {
                    int[] c = cells.get(ptr[cur.t]++);
                    int x = c[1], y = c[2];
                    if (cur.d < dist[x][y][cur.t + 1]) {
                        dist[x][y][cur.t + 1] = cur.d;
                        pq.add(new State(cur.d, x, y, cur.t + 1));
                    }
                }
            }
        }

        return -1;
    }
}
