// Problem: 679 - 24 Game
// Description: Given four numbers, determine if they can be combined using +, -, *, / and parentheses to make exactly 24.
// Date: 2025-08-18

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        vector<double> nums(cards.begin(), cards.end());
        const double EPS = 1e-6;

        function<bool(vector<double>&)> dfs = [&](vector<double>& arr) -> bool {
            if (arr.size() == 1)
                return fabs(arr[0] - 24.0) < EPS;

            int n = arr.size();
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    double a = arr[i], b = arr[j];
                    
                    // All possible results of combining a and b
                    vector<double> candidates = {a + b, a - b, b - a, a * b};
                    if (fabs(b) > EPS) candidates.push_back(a / b);
                    if (fabs(a) > EPS) candidates.push_back(b / a);

                    // Remaining numbers after removing i and j
                    vector<double> rest;
                    for (int k = 0; k < n; ++k)
                        if (k != i && k != j) rest.push_back(arr[k]);

                    for (double v : candidates) {
                        rest.push_back(v);
                        if (dfs(rest)) return true;
                        rest.pop_back();
                    }
                }
            }
            return false;
        };

        return dfs(nums);
    }
};
