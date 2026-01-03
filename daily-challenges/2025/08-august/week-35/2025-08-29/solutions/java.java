class Solution {
    public long flowerGame(int n, int m) {
        long even_in_n = n/2;
        long odd_in_n = n - even_in_n;
        long even_in_m = m/2;
        long odd_in_m = m - even_in_m;

        return even_in_n * odd_in_m + even_in_m * odd_in_n;
    }
}