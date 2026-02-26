class Solution {
public:
    int numSteps(string s) {
        int ans = 0, car = 0;
        for(int i = s.size() - 1; i > 0; i--) {
            if((s[i] - '0') + car == 1) {
                ans += 2;
                car = 1;
            } else {
                ans += 1;
            }
        }

        return ans + car;
    }
};