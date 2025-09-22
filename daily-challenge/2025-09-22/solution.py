"""
Problem: 3005 - Count Elements With Maximum Frequency  
Description: Given an array of positive integers, return the total number of elements whose frequency equals the maximum frequency in the array.  
Date: 2025-09-22
"""

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(count for count in freq.values() if count == max_freq)
