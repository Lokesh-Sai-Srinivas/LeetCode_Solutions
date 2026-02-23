class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> seen;

        for(int i = 0; i <= (int)s.size() - k; i++) {
            seen.insert(s.substr(i, k));
        }

        return seen.size() == (1 << k);
    }
};