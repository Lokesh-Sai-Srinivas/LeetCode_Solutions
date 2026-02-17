#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    static unordered_map<int, vector<string>> precomputed;

    static unordered_map<int, vector<string>> build() {
        unordered_map<int, vector<string>> mp;
        for (int h = 0; h < 12; h++) {
            for (int m = 0; m < 60; m++) {
                int bits = __builtin_popcount(h) + __builtin_popcount(m);
                char buf[6];
                sprintf(buf, "%d:%02d", h, m);
                mp[bits].push_back(string(buf));
            }
        }
        return mp;
    }

public:
    vector<string> readBinaryWatch(int turnedOn) {
        return precomputed[turnedOn];
    }
};
unordered_map<int, vector<string>> Solution::precomputed = Solution::build();