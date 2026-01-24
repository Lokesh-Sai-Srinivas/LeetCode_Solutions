import java.util.Arrays;

class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);

        int n = nums.length;
        int maxi = Integer.MIN_VALUE;

        int l = n - 1;
        int s = 0;

        while(s < l) {
            int Psum = nums[s++] + nums[l--];
            maxi = Math.max(Psum, maxi);
        }

        return maxi;
    }
}
