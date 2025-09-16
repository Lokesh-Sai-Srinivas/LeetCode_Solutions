"""
Problem: 2197 - Replace Non-Coprime Numbers in Array  
Description: Given an array nums, repeatedly replace adjacent non-coprime numbers with their LCM until all adjacent pairs are coprime, and return the resulting array.  
Date: 2025-09-16
"""

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack: List[int] = []
        for x in nums:
            cur = x
            while stack:
                a = stack[-1]
                g = math.gcd(a, cur)
                if g == 1:
                    break
                stack.pop()
                cur = (a // g) * cur
            stack.append(cur)
        return stack
