class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;

        if(digits[n - 1] != 9){
            digits[n - 1] ++;
            return digits;
        }
        
        for(int i = n - 1; i >= 0; i--){
            if(digits[i] != 9){
                digits[i] ++;
                return digits;
            }else{
                digits[i] = 0;
            }
        }

        int [] res = new int[n + 1];
        // Arrays.fill(res, 0);
        res[0] = 1;
        
        return res;
    }
}