"""
Problem: 0001 - Two Sum
Description: Finds indices of two numbers in a list that add up to a target.
Date: 2025-08-13
"""

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        HashMap<Integer, Integer> seen = new HashMap<>();

        for(int i = 0; i < n ; i++){
            int c = target - nums[i];
            if (seen.containsKey(c)){
                return new int[] {seen.get(c) , i};
            }
            seen.put(nums[i] , i);
        }
        return new int[] { -1 ,-1};
    }
}
