class Solution {
    private final int MOD = 1_000_000_000 + 7;
    public int numOfWays(int n) {
        long a = 6 ,b = 6;
        
        for(int i = 2; i <= n ; i++ ){
           long newA = ((a % MOD) * 2 + (b % MOD) * 2) % MOD;
           long newB = ((b % MOD) * 3 + (a % MOD) * 2) % MOD;
           a = newA;
           b = newB;
        }

        return (int) ((a + b) % MOD);
    }
}