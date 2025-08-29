"""
Problem: 3021 - Alice and Bob Playing Flower Game  
Description: Alice and Bob are playing a turn-based game with two lanes of flowers. There are x flowers in the first lane and y flowers in the second. Alice starts first, and on each turn, a player picks one flower from either lane. The player who picks the last flower wins. Given integers n and m, return the number of pairs (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m, and Alice wins the game.  
Date: 2025-08-29
"""

class Solution {
    public long flowerGame(int n, int m) {
        long even_in_n = n/2;
        long odd_in_n = n - even_in_n;
        long even_in_m = m/2;
        long odd_in_m = m - even_in_m;

        return even_in_n * odd_in_m + even_in_m * odd_in_n;
    }
}
