class Solution {
public:
    int reverseBits(int n) {
        int res = 0;
        int power = 31;
        while (n != 0) {
            res += (n & 1) << power;
            n >>= 1; 
            power -= 1;
        }
        return res ;
    }
};