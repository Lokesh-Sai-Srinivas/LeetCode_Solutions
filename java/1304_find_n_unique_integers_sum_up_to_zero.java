"""
Problem: 1304 - Find N Unique Integers Sum up to Zero  
Description: Given an integer n, return any array containing n unique integers such that their sum is 0.  
Date: 2025-09-07
"""

class Solution {
    public int[] sumZero(int n) {
        int [] nums = new int [n];
        
        if (n % 2 == 0){
            fill(nums,true,n);
        }
        else {
            fill(nums,false,n);
        }
        return nums;
    }

    private void fill(int[] nums, boolean flag,int n){
        int j = 0;
        for (int i = -n/2 ; i <= n/2 ;i++){
            if(flag && i == 0) continue ;
            nums[j] = i;
            j++;
        }
        return;
    }
}
