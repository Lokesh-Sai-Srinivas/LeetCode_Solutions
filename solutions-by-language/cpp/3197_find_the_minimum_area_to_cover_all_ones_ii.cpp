#include <bits/stdc++.h>
using namespace std;

struct Box {
    int cnt = 0;
    int rmin, rmax, cmin, cmax;
    Box(): rmin(INT_MAX), rmax(INT_MIN), cmin(INT_MAX), cmax(INT_MIN) {}
    inline void add(int r, int c) {
        ++cnt;
        rmin = min(rmin, r);
        rmax = max(rmax, r);
        cmin = min(cmin, c);
        cmax = max(cmax, c);
    }
    inline int area() const {
        if (cnt == 0) return 1; // must place a 1x1 somewhere disjoint in this region
        return (rmax - rmin + 1) * (cmax - cmin + 1);
    }
};

class Solution {
public:
    int minimumSum(vector<vector<int>>& grid) {
        int n = (int)grid.size(), m = (int)grid[0].size();
        vector<pair<int,int>> ones;
        ones.reserve(n*m);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1) ones.emplace_back(i, j);

        // Safety: problem guarantees >= 3 ones, but handle anyway
        if (ones.empty()) return 3; // three 1x1 rectangles anywhere

        auto upd = [](Box &b, int r, int c){ b.add(r,c); };

        int ans = INT_MAX;

        // 1) Three vertical strips: [0..x1], [x1+1..x2], [x2+1..m-1]
        for (int x1 = 0; x1 <= m - 3; ++x1) {
            for (int x2 = x1 + 1; x2 <= m - 2; ++x2) {
                Box A, B, C;
                for (auto [r, c] : ones) {
                    if (c <= x1) upd(A, r, c);
                    else if (c <= x2) upd(B, r, c);
                    else upd(C, r, c);
                }
                ans = min(ans, A.area() + B.area() + C.area());
            }
        }

        // 2) Three horizontal strips: [0..y1], [y1+1..y2], [y2+1..n-1]
        for (int y1 = 0; y1 <= n - 3; ++y1) {
            for (int y2 = y1 + 1; y2 <= n - 2; ++y2) {
                Box A, B, C;
                for (auto [r, c] : ones) {
                    if (r <= y1) upd(A, r, c);
                    else if (r <= y2) upd(B, r, c);
                    else upd(C, r, c);
                }
                ans = min(ans, A.area() + B.area() + C.area());
            }
        }

        // 3) Mixed: one vertical line at x, one horizontal at y
        //    We need FOUR variants (and we'll also do the full 4-quadrant case below):
        //    a) left single | right split (top/bottom)
        //    b) right single | left split (top/bottom)
        //    c) top single | bottom split (left/right)
        //    d) bottom single | top split (left/right)
        for (int x = 0; x <= m - 2; ++x) {
            for (int y = 0; y <= n - 2; ++y) {
                // a) left single, right split
                {
                    Box L, RT, RB;
                    for (auto [r, c] : ones) {
                        if (c <= x) upd(L, r, c);
                        else if (r <= y) upd(RT, r, c);
                        else upd(RB, r, c);
                    }
                    ans = min(ans, L.area() + RT.area() + RB.area());
                }
                // b) right single, left split
                {
                    Box R, LT, LB;
                    for (auto [r, c] : ones) {
                        if (c > x) upd(R, r, c);
                        else if (r <= y) upd(LT, r, c);
                        else upd(LB, r, c);
                    }
                    ans = min(ans, R.area() + LT.area() + LB.area());
                }
                // c) top single, bottom split
                {
                    Box T, BL, BR;
                    for (auto [r, c] : ones) {
                        if (r <= y) upd(T, r, c);
                        else if (c <= x) upd(BL, r, c);
                        else upd(BR, r, c);
                    }
                    ans = min(ans, T.area() + BL.area() + BR.area());
                }
                // d) bottom single, top split
                {
                    Box B, TL, TR;
                    for (auto [r, c] : ones) {
                        if (r > y) upd(B, r, c);
                        else if (c <= x) upd(TL, r, c);
                        else upd(TR, r, c);
                    }
                    ans = min(ans, B.area() + TL.area() + TR.area());
                }
            }
        }

        // 4) Full 4-quadrant split (vertical x, horizontal y), choose ANY 3 quadrants.
        //    You MUST include all quadrants that contain 1's.
        //    If >3 quadrants contain 1's, this (x,y) split can't cover with 3 rectangles → skip.
        for (int x = 0; x <= m - 2; ++x) {
            for (int y = 0; y <= n - 2; ++y) {
                Box TL, TR, BL, BR;
                for (auto [r, c] : ones) {
                    if (r <= y && c <= x) upd(TL, r, c);
                    else if (r <= y && c >  x) upd(TR, r, c);
                    else if (r >  y && c <= x) upd(BL, r, c);
                    else upd(BR, r, c);
                }
                int nonEmpty = (TL.cnt>0) + (TR.cnt>0) + (BL.cnt>0) + (BR.cnt>0);
                if (nonEmpty > 3) continue; // impossible with 3 rectangles under this split
                // pick all non-empty quadrants + (3-nonEmpty) dummy 1x1s in empty quadrants
                int sum = 0;
                if (TL.cnt) sum += TL.area();
                if (TR.cnt) sum += TR.area();
                if (BL.cnt) sum += BL.area();
                if (BR.cnt) sum += BR.area();
                sum += (3 - nonEmpty) * 1; // add needed 1x1 rectangles
                ans = min(ans, sum);
            }
        }

        return ans;
    }
};