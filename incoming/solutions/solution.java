class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        Arrays.sort(hBars);
        Arrays.sort(vBars);

        int maxH = 1, cur = 1;
        for (int i = 1; i < hBars.length; i++) {
            if (hBars[i] == hBars[i - 1] + 1) {
                cur++;
            } else {
                maxH = Math.max(maxH, cur);
                cur = 1;
            }
        }
        maxH = Math.max(maxH, cur) + 1;

        int maxV = 1;
        cur = 1;
        for (int i = 1; i < vBars.length; i++) {
            if (vBars[i] == vBars[i - 1] + 1) {
                cur++;
            } else {
                maxV = Math.max(maxV, cur);
                cur = 1;
            }
        }
        maxV = Math.max(maxV, cur) + 1;

        int side = Math.min(maxH, maxV);
        return side * side;
    }
}
