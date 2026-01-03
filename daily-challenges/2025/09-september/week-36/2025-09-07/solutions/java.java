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