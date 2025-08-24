"""
Problem: 1493 - Longest Subarray of 1's After Deleting One Element  
Description: Given a binary array nums, return the length of the longest subarray containing only 1s after deleting exactly one element. You must delete one element, even if the array is already full of 1s.  
Date: 2025-08-24
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0 
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                
                left += 1
            max_len = max(max_len, right - left)

        
        return max_len
