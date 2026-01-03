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