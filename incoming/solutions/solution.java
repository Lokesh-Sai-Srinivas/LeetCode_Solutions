import java.util.*;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            int p = nums.get(i);
            
            if ((p & 1) == 0) {
                ans[i] = -1;
                continue;
            }
            
            int t = 0;
            int temp = p;
            while ((temp & 1) == 1) {
                t++;
                temp >>= 1;
            }
            
            ans[i] = p ^ (1 << (t - 1));
        }
        
        return ans;
    }
}
