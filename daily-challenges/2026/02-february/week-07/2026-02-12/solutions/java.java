class Solution {
    public int longestBalanced(String s) {
        int n = s.length();
        int maxLen = 0;

        for (int start = 0; start < n; start++) {
            int[] frq = new int[26];
            for (int end = start; end < n; end++) {
                frq[s.charAt(end) - 'a']++;
                if (isBal(frq)) {
                    maxLen = Math.max(maxLen, end - start + 1);
                }
            }
        }
        return maxLen;
    }

    private static boolean isBal(int[] frq) {
        int prev = -1;
        for (int f : frq) {
            if (f > 0) {
                if (prev != -1 && f != prev) return false;
                prev = f;
            }
        }
        return true;
    }
}