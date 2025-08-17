"""
Problem: 326 - Power of Three
Description: Given an integer n, return True if it is a power of three; otherwise, return False.An integer n is a power of three if there exists an integer x such that n == 3^x.Constraints: -2^31 <= n <= 2^31 - 1. Follow-up: Solve without using loops or recursion.
Date: 2025-08-13
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max3Possible = 1162261467
        return (n > 0 and max3Possible % n == 0)
