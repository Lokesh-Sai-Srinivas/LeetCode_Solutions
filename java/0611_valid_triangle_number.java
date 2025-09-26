"""
Problem: 611 - Valid Triangle Number  
Description: Given an array of non-negative integers, return the number of triplets that can form a triangle, i.e., for any triplet (i, j, k), the sum of any two sides must be greater than the third.  
Date: 2025-09-26
"""

class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int count = 0;
        for(int k = n - 1; k >= 2; k--){
            int i = 0, j = k - 1;
            while(i < j){
                if(nums[i] == 0) i++;
                if(nums[k] == 0) continue;
                if(nums[i] + nums[j] > nums[k]){
                    count += j - i;
                    j--;
                }
                else{
                    i++;
                }
            }
        }
        return count;
    }
}
