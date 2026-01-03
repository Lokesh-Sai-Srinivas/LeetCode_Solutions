import java.util.*;

class Solution {
    static class Box {
        int cnt = 0;
        int rmin = Integer.MAX_VALUE, rmax = Integer.MIN_VALUE;
        int cmin = Integer.MAX_VALUE, cmax = Integer.MIN_VALUE;

        void add(int r, int c) {
            cnt++;
            rmin = Math.min(rmin, r);
            rmax = Math.max(rmax, r);
            cmin = Math.min(cmin, c);
            cmax = Math.max(cmax, c);
        }

        int area() {
            if (cnt == 0) return 1; // must place 1x1 rectangle
            return (rmax - rmin + 1) * (cmax - cmin + 1);
        }
    }

    public int minimumSum(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        List<int[]> ones = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) ones.add(new int[]{i, j});
            }
        }

        if (ones.isEmpty()) return 3; // fallback (problem guarantees >=3 ones though)

        int ans = Integer.MAX_VALUE;

        // 1) Three vertical strips
        for (int x1 = 0; x1 <= m - 3; x1++) {
            for (int x2 = x1 + 1; x2 <= m - 2; x2++) {
                Box A = new Box(), B = new Box(), C = new Box();
                for (int[] p : ones) {
                    int r = p[0], c = p[1];
                    if (c <= x1) A.add(r, c);
                    else if (c <= x2) B.add(r, c);
                    else C.add(r, c);
                }
                ans = Math.min(ans, A.area() + B.area() + C.area());
            }
        }

        // 2) Three horizontal strips
        for (int y1 = 0; y1 <= n - 3; y1++) {
            for (int y2 = y1 + 1; y2 <= n - 2; y2++) {
                Box A = new Box(), B = new Box(), C = new Box();
                for (int[] p : ones) {
                    int r = p[0], c = p[1];
                    if (r <= y1) A.add(r, c);
                    else if (r <= y2) B.add(r, c);
                    else C.add(r, c);
                }
                ans = Math.min(ans, A.area() + B.area() + C.area());
            }
        }

        // 3) Mixed partitions
        for (int x = 0; x <= m - 2; x++) {
            for (int y = 0; y <= n - 2; y++) {
                // a) left single, right split
                {
                    Box L = new Box(), RT = new Box(), RB = new Box();
                    for (int[] p : ones) {
                        int r = p[0], c = p[1];
                        if (c <= x) L.add(r, c);
                        else if (r <= y) RT.add(r, c);
                        else RB.add(r, c);
                    }
                    ans = Math.min(ans, L.area() + RT.area() + RB.area());
                }
                // b) right single, left split
                {
                    Box R = new Box(), LT = new Box(), LB = new Box();
                    for (int[] p : ones) {
                        int r = p[0], c = p[1];
                        if (c > x) R.add(r, c);
                        else if (r <= y) LT.add(r, c);
                        else LB.add(r, c);
                    }
                    ans = Math.min(ans, R.area() + LT.area() + LB.area());
                }
                // c) top single, bottom split
                {
                    Box T = new Box(), BL = new Box(), BR = new Box();
                    for (int[] p : ones) {
                        int r = p[0], c = p[1];
                        if (r <= y) T.add(r, c);
                        else if (c <= x) BL.add(r, c);
                        else BR.add(r, c);
                    }
                    ans = Math.min(ans, T.area() + BL.area() + BR.area());
                }
                // d) bottom single, top split
                {
                    Box B = new Box(), TL = new Box(), TR = new Box();
                    for (int[] p : ones) {
                        int r = p[0], c = p[1];
                        if (r > y) B.add(r, c);
                        else if (c <= x) TL.add(r, c);
                        else TR.add(r, c);
                    }
                    ans = Math.min(ans, B.area() + TL.area() + TR.area());
                }
            }
        }

        // 4) Full 4-quadrant, pick any 3 quadrants
        for (int x = 0; x <= m - 2; x++) {
            for (int y = 0; y <= n - 2; y++) {
                Box TL = new Box(), TR = new Box(), BL = new Box(), BR = new Box();
                for (int[] p : ones) {
                    int r = p[0], c = p[1];
                    if (r <= y && c <= x) TL.add(r, c);
                    else if (r <= y && c > x) TR.add(r, c);
                    else if (r > y && c <= x) BL.add(r, c);
                    else BR.add(r, c);
                }
                int nonEmpty = 0;
                if (TL.cnt > 0) nonEmpty++;
                if (TR.cnt > 0) nonEmpty++;
                if (BL.cnt > 0) nonEmpty++;
                if (BR.cnt > 0) nonEmpty++;

                if (nonEmpty > 3) continue;

                int sum = 0;
                if (TL.cnt > 0) sum += TL.area();
                if (TR.cnt > 0) sum += TR.area();
                if (BL.cnt > 0) sum += BL.area();
                if (BR.cnt > 0) sum += BR.area();
                sum += (3 - nonEmpty); // remaining empty quadrants → 1x1 rectangles
                ans = Math.min(ans, sum);
            }
        }

        return ans;
    }
}