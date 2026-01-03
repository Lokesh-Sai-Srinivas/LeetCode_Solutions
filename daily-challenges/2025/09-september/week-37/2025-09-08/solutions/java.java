class Solution {
    public int[] getNoZeroIntegers(int n) {
        int [] nums = {-1,-1};
        int i = 1;

        while(true){
            if(contains0(i) && contains0(n - i)){
                nums[0] = i;
                nums[1] = n - i;
                break;
            }else{
                i+=2;
            }
        }
        return nums;
    }
    private static boolean contains0(int n){
        
        while(n > 0){
            if(n % 10 == 0) return false;
            n /= 10 ;
        }

        return true;

    }
}