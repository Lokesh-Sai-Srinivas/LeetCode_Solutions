class Solution {
    public int makeTheIntegerZero(int num1, int num2) {
        for (int i = 1; i <= 60; i++) {
            long remaining = (long) num1 - (long) i * num2;
            if (remaining < i) continue;

            int ones = 0;
            long temp = remaining;
            while (temp > 0) {
                ones += (temp & 1);
                temp >>= 1;
            }

            if (ones <= i) return i;
        }
        return -1;
    }
}