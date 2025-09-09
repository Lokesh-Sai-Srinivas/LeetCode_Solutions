"""
Problem: 2327 - Number of People Aware of a Secret  
Description: You are given integers n, delay, and forget. On day 1, one person discovers a secret. Each person who knows the secret can share it with others starting from 'delay' days after learning it, and stops sharing it after 'forget' days. Return the total number of people who know the secret at the end of day n. The answer should be returned modulo 10⁹ + 7.  
Date: 2025-09-09  
"""

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n
        dp[0] = 1
        s = 0
        for i in range(delay,n):
            s += dp[i-delay]
            dp[i] = s
            if i-forget+1 >= 0:
                s -= dp[i-forget+1]
        return(sum(dp[-forget:]))%(10**9+7)
