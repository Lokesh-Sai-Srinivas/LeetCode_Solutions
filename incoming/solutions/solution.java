class Solution {
    public int concatenatedBinary(int n) {
        int binary = 0;
        long res = 0;
        final long MOD = (long)(1e9 + 7);

        for(int i=1;i<=n;i++){
            if((i & (i-1)) == 0) binary++;
            res = ((res << binary) + i) % MOD;
        }
        
        return (int)res;
    }
}
