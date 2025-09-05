"""
Problem: 2749 - Minimum Operations to Make the Integer Zero  
Description: Given two integers num1 and num2, return the minimum number of operations to make num1 equal to 0 by repeatedly subtracting num2 and ensuring the result has at most i set bits in its binary form.  
Date: 2025-09-05
"""

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(61):
            target = num1 - num2 * i
            if target >= 0 and target.bit_count() <= i <= target:
                return i
        
        return -1
