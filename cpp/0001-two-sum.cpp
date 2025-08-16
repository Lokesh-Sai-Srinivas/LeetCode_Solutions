"""
Problem: 0001 - Two Sum
Description: Finds indices of two numbers in a list that add up to a target.
Date: 2025-08-13
"""


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        int n = nums.size();
        for(int i = 0; i < n ; i ++) {
            int c = target - nums[i];
            if(seen.count(c)){
                return {seen[c] , i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
