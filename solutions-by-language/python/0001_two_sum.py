class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max3Possible = 1162261467
        return (n > 0 and max3Possible % n == 0)