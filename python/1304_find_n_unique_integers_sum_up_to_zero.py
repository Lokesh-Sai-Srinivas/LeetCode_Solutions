"""
Problem: 1304 - Find N Unique Integers Sum up to Zero  
Description: Given an integer n, return any array containing n unique integers such that their sum is 0.  
Date: 2025-09-07
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        self.fill(nums, n)
        if n % 2 :
            nums.append(0)
        return nums

    def fill(self, nums: list, n: int) :
        for i in range(1,n//2 + 1):
            nums.append(-i)
            nums.append(i)

        return
