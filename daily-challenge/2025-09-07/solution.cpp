"""
Problem: 1304 - Find N Unique Integers Sum up to Zero  
Description: Given an integer n, return any array containing n unique integers such that their sum is 0.  
Date: 2025-09-07
"""

class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> nums;
        fill(nums, n);
        if (n % 2){
            nums.push_back(0);
        }
        return nums;
    }

    void fill(vector<int>& nums, int n){
        for (int i = 1; i <= n/2; i++){
            nums.push_back(-i);
            nums.push_back(i);
        }
        return;
    }
};
