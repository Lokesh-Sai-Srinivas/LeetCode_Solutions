class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        long NEG = Long.MIN_VALUE / 4;

        long[] dp1 = new long[n];
        long[] dp2 = new long[n];
        long[] dp3 = new long[n];

        for (int i = 0; i < n; i++) {
            dp1[i] = dp2[i] = dp3[i] = NEG;
        }

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                dp1[i] = nums[i - 1] + nums[i];
                if (dp1[i - 1] != NEG)
                    dp1[i] = Math.max(dp1[i], dp1[i - 1] + nums[i]);
            }

            if (nums[i] < nums[i - 1]) {
                if (dp1[i - 1] != NEG)
                    dp2[i] = dp1[i - 1] + nums[i];
                if (dp2[i - 1] != NEG)
                    dp2[i] = Math.max(dp2[i], dp2[i - 1] + nums[i]);
            }

            if (nums[i] > nums[i - 1]) {
                if (dp2[i - 1] != NEG)
                    dp3[i] = dp2[i - 1] + nums[i];
                if (dp3[i - 1] != NEG)
                    dp3[i] = Math.max(dp3[i], dp3[i - 1] + nums[i]);
            }
        }

        long ans = NEG;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, dp3[i]);
        }
        return ans;
    }
}