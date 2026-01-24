class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;

        int count = 0;
        while (!isSorted(nums)) {
            int idx = findMinPairIndex(nums);
            nums = merge(nums, idx);
            count++;
        }
        return count;
    }

    private boolean isSorted(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) return false;
        }
        return true;
    }

    private int findMinPairIndex(int[] nums) {
        int minSum = Integer.MAX_VALUE;
        int idx = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            int sum = nums[i] + nums[i + 1];
            if (sum < minSum) {
                minSum = sum;
                idx = i;
            }
        }
        return idx;
    }

    private int[] merge(int[] nums, int idx) {
        int n = nums.length;
        int[] ans = new int[n - 1];
        for (int i = 0; i < idx; i++) {
            ans[i] = nums[i];
        }
        ans[idx] = nums[idx] + nums[idx + 1];
        for (int i = idx + 1; i < n - 1; i++) {
            ans[i] = nums[i + 1];
        }
        return ans;
    }
}
