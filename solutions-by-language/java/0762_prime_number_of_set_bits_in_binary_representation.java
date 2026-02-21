class Solution {
    
    public int countPrimeSetBits(int left, int right) {
        int count = 0;
        while(left <= right) {
            count += (665772 >> Integer.bitCount(left++) ) & 1;
        }
        return count;
    }
}