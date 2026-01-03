class Solution {
public:
    const long mod = 1000000007;
    int numOfWays(int n) {
        long a = 6;
        long b = 6;

        for(int i = 2; i <= n; i ++){
            long nA = ((a % mod) * 3) % mod + ((b % mod) * 2) % mod;
            long nB = ((a % mod) * 2) % mod + ((b % mod) * 2) % mod;
            a = nA;
            b = nB;
        }

        return (int) ((a + b) % mod);
    }
};
