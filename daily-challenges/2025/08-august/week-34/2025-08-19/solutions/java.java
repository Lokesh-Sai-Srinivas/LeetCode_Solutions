class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long streak = 0;
        long count = 0;
        for(int i : nums){
            if (i == 0){
                streak += 1;
            } else {
                count += streak * (streak + 1) / 2;
                streak = 0;
            }
        }
        count += streak * (streak + 1) / 2;
        return count;
    }
}