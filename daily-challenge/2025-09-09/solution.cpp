"""
Problem: 2327 - Number of People Aware of a Secret  
Description: You are given integers n, delay, and forget. On day 1, one person discovers a secret. Each person who knows the secret can share it with others starting from 'delay' days after learning it, and stops sharing it after 'forget' days. Return the total number of people who know the secret at the end of day n. The answer should be returned modulo 10⁹ + 7.  
Date: 2025-09-09  
"""

class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        constexpr int MOD = 1'000'000'007;
        vector<int> dp(n + 1);
        dp[1] = 1;
        int sharing = 0;

        for (int day = 2; day <= n; ++day) {
            if (day - delay >= 1)
                sharing = (sharing + dp[day - delay]) % MOD;
            if (day - forget >= 1)
                sharing = (sharing - dp[day - forget] + MOD) % MOD;
            dp[day] = sharing;
        }

        int result = 0;
        for (int day = n - forget + 1; day <= n; ++day)
            result = (result + dp[day]) % MOD;

        return result;
    }
};
