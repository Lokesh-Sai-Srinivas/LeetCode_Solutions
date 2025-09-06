"""
Problem: 3495 - Minimum Operations to Make Array Elements Zero  
Description: Given multiple queries [l, r], each representing an array of integers from l to r inclusive, in one operation you can pick two numbers a and b and replace them with floor(a/4) and floor(b/4). For each query, find the minimum number of operations to make all elements zero, and return the sum over all queries.  
Date: 2025-09-06
"""
class Solution {
    public long minOperations(int[][] queries) {
        long count = 0;

        for (int[] q : queries) {
            long l = q[0];
            long r = q[1];
            count += minOpe(l, r);
        }
        return count;
    }

    private long minOpe(long l, long r) {
        long stepsSum = 0;
        long start = 1;
        int level = 1;

        while (start <= r) {
            long end = start * 4 - 1;
            long left = Math.max(l, start);
            long right = Math.min(r, end);

            if (left <= right) {
                long count = right - left + 1;
                stepsSum += count * level;
            }

            start *= 4;
            level++;
        }

        return (stepsSum + 1) / 2;
    }
}
