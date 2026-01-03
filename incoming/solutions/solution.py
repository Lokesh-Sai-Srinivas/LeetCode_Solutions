class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1000000007

        a,b = 6,6

        for i in range(1,n):
            a,b = ((a % mod) * 3 + (b % mod) * 2) % mod, ((a % mod) * 2 + (b % mod) * 2) % mod
        
        return int((a + b) % mod)
