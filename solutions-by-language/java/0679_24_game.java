// Problem: 679 - 24 Game
// Description: Given four numbers, determine if they can be combined using +, -, *, / and parentheses to make exactly 24.
// Date: 2025-08-18

import java.util.*;

class Solution {
    public boolean judgePoint24(int[] cards) {
        List<Double> nums = new ArrayList<>();
        for (int x : cards) nums.add((double) x);
        final double EPS = 1e-6;
        return dfs(nums, EPS);
    }

    private boolean dfs(List<Double> nums, double EPS) {
        if (nums.size() == 1) {
            return Math.abs(nums.get(0) - 24.0) < EPS;
        }

        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double a = nums.get(i), b = nums.get(j);
                List<Double> candidates = new ArrayList<>(Arrays.asList(
                    a + b, a - b, b - a, a * b
                ));
                if (Math.abs(b) > EPS) candidates.add(a / b);
                if (Math.abs(a) > EPS) candidates.add(b / a);

                // Remaining numbers after removing i and j
                List<Double> rest = new ArrayList<>();
                for (int k = 0; k < n; ++k) {
                    if (k != i && k != j) rest.add(nums.get(k));
                }

                for (double val : candidates) {
                    rest.add(val);
                    if (dfs(rest, EPS)) return true;
                    rest.remove(rest.size() - 1);
                }
            }
        }
        return false;
    }
}