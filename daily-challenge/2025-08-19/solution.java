"""
Problem: 2348 - Number of Zero-Filled Subarrays  
Description: Given an integer array nums, return the number of contiguous subarrays that are filled with 0. A subarray is a contiguous non-empty sequence of elements within an array.  
Date: 2025-08-19
"""

class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long streak = 0;
        long count = 0;
        for(int i : nums){
            if (i == 0){
                streak += 1;
            } else {
                count += streak * (streak + 1) / 2;
                streak = 0;
            }
        }
        count += streak * (streak + 1) / 2;
        return count;
    }
}
