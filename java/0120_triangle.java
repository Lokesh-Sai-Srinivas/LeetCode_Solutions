"""
Problem: 120 - Triangle  
Description: Given a triangle array, return the minimum path sum from top to bottom. At each step, you may move to adjacent numbers on the row below.  
Date: 2025-09-25
"""

  class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        List<Integer> dp = new ArrayList<>(triangle.get(n - 1));
        for(int i = n - 2; i >= 0; i--){
            for(int j = 0; j <= i; j++) {
                int curr = triangle.get(i).get(j);
                dp.set(j , curr + Math.min(dp.get(j), dp.get(j + 1)));
            }
        }
        return dp.get(0);
    }
}
