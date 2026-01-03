class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size(), count = 0;

        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];

                if (x1 < x2 && y1 > y2) {
                    bool valid = true;
                    for (int k = 0; k < n; ++k) {
                        if (k == i || k == j) continue;
                        int x = points[k][0], y = points[k][1];
                        if (x >= x1 && x <= x2 && y >= y2 && y <= y1) {
                            valid = false;
                            break;
                        }
                    }
                    if (valid) count++;
                }

                else if (x1 == x2 && y1 > y2) {
                    bool valid = true;
                    for (int k = 0; k < n; ++k) {
                        if (k == i || k == j) continue;
                        int x = points[k][0], y = points[k][1];
                        if (x == x1 && y > y2 && y < y1) {
                            valid = false;
                            break;
                        }
                    }
                    if (valid) count++;
                }

                else if (y1 == y2 && x1 < x2) {
                    bool valid = true;
                    for (int k = 0; k < n; ++k) {
                        if (k == i || k == j) continue;
                        int x = points[k][0], y = points[k][1];
                        if (y == y1 && x > x1 && x < x2) {
                            valid = false;
                            break;
                        }
                    }
                    if (valid) count++;
                }
            }
        }
        return count;
    }
};