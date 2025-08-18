"""
Problem: 837 - New 21 Game
Description: Alice starts at 0. While her score is < k, she draws uniformly from 1..maxPts and adds to her score. She stops once the score >= k. Return the probability that her final score is <= n. Answers within 1e-5 are accepted.
Date: 2025-08-17
"""

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts -1:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k :
                window_sum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]
        
        return result
