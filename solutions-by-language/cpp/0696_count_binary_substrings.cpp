class Solution {
public:
    int countBinarySubstrings(string s) {
        int prev = 0, cur = 1, res = 0;
        
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                cur++;
            } else {
                res += min(prev, cur);
                prev = cur;
                cur = 1;
            }
        }
        
        res += min(prev, cur);
        return res;
    }
};