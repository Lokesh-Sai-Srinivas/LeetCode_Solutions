"""
Problem: 837 - New 21 Game
Description: Alice starts at 0. While her score is < k, she draws uniformly from 1..maxPts and adds to her score. She stops once the score >= k. Return the probability that her final score is <= n. Answers within 1e-5 are accepted.
Date: 2025-08-17
"""

class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if( k == 0 || n >= k + maxPts - 1 ){
            return 1.0;
        }

        double[] dp = new double[n + 1];
        dp[0] = 1.0;
        double windowSum = 1.0 ;
        double result = 0.0;

        for(int i = 1 ; i <=n ; i++){
            dp[i] = windowSum / maxPts;

            if( i < k){
                windowSum += dp[i];
            }else {
                result += dp[i];
            }

            if(i - maxPts >= 0){
                windowSum -= dp[i - maxPts];
            }
        }
        return result;
    }
}
