"""
Problem: 611 - Valid Triangle Number  
Description: Given an array of non-negative integers, return the number of triplets that can form a triangle, i.e., for any triplet (i, j, k), the sum of any two sides must be greater than the third.  
Date: 2025-09-26
"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=2:
            return 0
        count=0
        for k in range(2,len(nums)):
            i,j=0,k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    count+=(j-i)
                    j-=1
                else:
                    i+=1
        return count
