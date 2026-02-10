class Solution {
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            Set<Integer> ev = new HashSet<>();
            Set<Integer> od = new HashSet<>();
            for (int j = i; j < n; j++) {
                int x = nums[j];
                if (x % 2 == 0) ev.add(x);
                else od.add(x);
                if (ev.size() == od.size()) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
}