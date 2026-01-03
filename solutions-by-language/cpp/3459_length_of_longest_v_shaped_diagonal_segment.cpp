#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n == 0) return 0;
        int m = grid[0].size();

        // diagonals: ↘, ↙, ↖, ↗
        int dxs[4] = {1, 1, -1, -1};
        int dys[4] = {1, -1, -1, 1};

        int NM = n * m;
        auto prefIndex = [&](int i, int j, int d){ return ((i * m + j) * 4 + d); };
        auto sufIndex  = [&](int i, int j, int d, int phase){ return (((i * m + j) * 4 + d) * 2 + phase); };

        vector<int> pref(NM * 4, 0);        // pref[(i,j,d)]
        vector<int> suf(NM * 4 * 2, 0);     // suf[(i,j,d,phase)]

        // Compute suf: lengths starting at (i,j) when (i,j) must be (phase-> 0:2, 1:0)
        for (int d = 0; d < 4; ++d) {
            int dx = dxs[d], dy = dys[d];
            int istart, iend, istep;
            if (dx == 1) { istart = n - 1; iend = -1; istep = -1; }
            else         { istart = 0;      iend = n;  istep = 1;  }
            int jstart, jend, jstep;
            if (dy == 1) { jstart = m - 1; jend = -1; jstep = -1; }
            else         { jstart = 0;      jend = m;  jstep = 1;  }

            for (int i = istart; i != iend; i += istep) {
                for (int j = jstart; j != jend; j += jstep) {
                    // phase 0 => expect 2 at (i,j). phase 1 => expect 0 at (i,j).
                    for (int phase = 0; phase <= 1; ++phase) {
                        int need = (phase == 0 ? 2 : 0);
                        int si = sufIndex(i, j, d, phase);
                        if (grid[i][j] != need) {
                            suf[si] = 0;
                        } else {
                            int ni = i + dx, nj = j + dy;
                            if (0 <= ni && ni < n && 0 <= nj && nj < m) {
                                // next cell must be of opposite phase
                                suf[si] = 1 + suf[sufIndex(ni, nj, d, phase ^ 1)];
                            } else {
                                suf[si] = 1;
                            }
                        }
                    }
                }
            }
        }

        // Compute pref: lengths ending at (i,j) along direction d which started with a 1 earlier
        for (int d = 0; d < 4; ++d) {
            int dx = dxs[d], dy = dys[d];
            int istart, iend, istep;
            // prev cell is (i-dx, j-dy). We want prev processed before current.
            if (dx == 1) { istart = 0;      iend = n;  istep = 1;  } // prev = i-1 smaller -> iterate i ascending
            else         { istart = n - 1; iend = -1; istep = -1; } // prev = i+1 larger -> iterate i descending
            int jstart, jend, jstep;
            if (dy == 1) { jstart = 0;      jend = m;  jstep = 1;  }
            else         { jstart = m - 1; jend = -1; jstep = -1; }

            for (int i = istart; i != iend; i += istep) {
                for (int j = jstart; j != jend; j += jstep) {
                    int pi = i - dx, pj = j - dy;
                    int idx = prefIndex(i, j, d);
                    if (grid[i][j] == 1) {
                        pref[idx] = 1;
                    } else if (0 <= pi && pi < n && 0 <= pj && pj < m) {
                        int pidx = prefIndex(pi, pj, d);
                        int Lprev = pref[pidx];
                        if (Lprev > 0) {
                            // next expected after Lprev elements:
                            // if Lprev is odd -> expect 2, else expect 0
                            int need = (Lprev % 2 == 1 ? 2 : 0);
                            if (grid[i][j] == need) pref[idx] = Lprev + 1;
                            else pref[idx] = 0;
                        } else {
                            pref[idx] = 0;
                        }
                    } else {
                        pref[idx] = 0;
                    }
                }
            }
        }

        int ans = 0;
        // any solitary '1'
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1) ans = max(ans, 1);

        // straight-only (no turn): from each 1, step one cell in dir (must be 2) then use suf starting there phase=0
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] != 1) continue;
                for (int d = 0; d < 4; ++d) {
                    int ni = i + dxs[d], nj = j + dys[d];
                    if (0 <= ni && ni < n && 0 <= nj && nj < m && grid[ni][nj] == 2) {
                        int len = 1 + suf[sufIndex(ni, nj, d, 0)]; // start phase=0 at the 2
                        ans = max(ans, len);
                    }
                }
            }
        }

        // with one clockwise turn:
        // turning point must be reached after at least one step (prefix length >= 2)
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                for (int d = 0; d < 4; ++d) {
                    int Lb = pref[prefIndex(i, j, d)];
                    if (Lb < 2) continue; // need at least one step before turning
                    int nd = (d + 1) % 4;
                    int tx = i + dxs[nd], ty = j + dys[nd];
                    if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
                    int next_expected = (Lb % 2 == 1 ? 2 : 0);
                    if (grid[tx][ty] != next_expected) continue;
                    int phase_after = (next_expected == 2 ? 0 : 1);
                    int len_after = suf[sufIndex(tx, ty, nd, phase_after)];
                    ans = max(ans, Lb + len_after);
                }
            }
        }

        return ans;
    }
};