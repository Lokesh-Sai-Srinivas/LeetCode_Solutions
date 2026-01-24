class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double total = 0.0;
        double minY = DBL_MAX, maxY = -DBL_MAX;

        for (auto &sq : squares) {
            int y = sq[1], l = sq[2];
            total += (double) l * l;
            minY = min(minY, (double) y);
            maxY = max(maxY, (double) y + l);
        }

        double target = total / 2.0;
        double lo = minY, hi = maxY;

        auto areaAbove = [&](double h) {
            double s = 0.0;
            for (auto &sq : squares) {
                int y = sq[1], l = sq[2];
                double hAbove = y + l - h;
                if (hAbove <= 0) continue;
                if (hAbove >= l) s += (double) l * l;
                else s += l * hAbove;
            }
            return s;
        };

        for (int iter = 0; iter < 70; iter++) {
            double mid = (lo + hi) / 2.0;
            if (areaAbove(mid) > target) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        return (lo + hi) / 2.0;
    }
};