class Solution {
    public int sumFourDivisors(int[] nums) {
        int n = nums.length;
        int tSum = 0;

        for(int num : nums){
            int sum = 0; 
            int count = 0;

            for(int i = 1; i * i <= num; i++){
                if(num % i == 0) {
                    if(i * i == num) {
                        count ++;
                        sum += i;
                    } else {
                        count += 2;
                        sum += i + (num / i);
                    }
                }
                if(count > 4) break;
            }
            if(count == 4) {
                tSum += sum;
            }
        }
        return tSum;
    }
}
