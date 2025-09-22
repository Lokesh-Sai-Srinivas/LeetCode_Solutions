"""
Problem: 3005 - Count Elements With Maximum Frequency  
Description: Given an array of positive integers, return the total number of elements whose frequency equals the maximum frequency in the array.  
Date: 2025-09-22
"""

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> freq;
        int maxFreq = 0, total = 0;

        for (int num : nums) {
            freq[num]++;
            maxFreq = max(maxFreq, freq[num]);
        }

        for (auto& [_, count] : freq) {
            if (count == maxFreq) total += count;
        }

        return total;
    }
};
