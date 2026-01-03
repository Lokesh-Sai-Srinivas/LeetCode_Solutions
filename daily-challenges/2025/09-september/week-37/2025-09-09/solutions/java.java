class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        int MOD = 1_000_000_007;
        int [] dp = new int[n + 1];
        dp[1] = 1;
        int sharing = 0;
        for (int day = 2; day <= n; day++) {
            if (day - delay >= 1) sharing = (sharing + dp[day - delay]) % MOD;
            if (day - forget >= 1) sharing = (sharing - dp[day - forget]  + MOD) % MOD;
            dp[day] = sharing ;
        }

        int result = 0;
        for(int day = n - forget + 1; day <= n; day++) {
            result = (result + dp[day]) % MOD;
        }
        return result;
    }
}