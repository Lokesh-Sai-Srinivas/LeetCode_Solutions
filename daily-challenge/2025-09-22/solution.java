"""
Problem: 3005 - Count Elements With Maximum Frequency  
Description: Given an array of positive integers, return the total number of elements whose frequency equals the maximum frequency in the array.  
Date: 2025-09-22
"""

  import java.util.*;

class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        int maxFreq = 0, total = 0;

        for (int num : nums) {
            int count = freq.getOrDefault(num, 0) + 1;
            freq.put(num, count);
            maxFreq = Math.max(maxFreq, count);
        }

        for (int count : freq.values()) {
            if (count == maxFreq) total += count;
        }

        return total;
    }
}
