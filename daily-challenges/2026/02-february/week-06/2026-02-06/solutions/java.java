class Solution {
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int ans = 0;
        int j = 0;

        for(int i = 0; i < n; i++) {
            while((long) nums[i] > (long) nums[j] * k){
                j ++;
            }
            ans = Math.max(ans, i - j + 1);
        }

        return n - ans;
    }
}