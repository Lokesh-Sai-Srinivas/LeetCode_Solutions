class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int time = 0;
        for(int i = 0; i < points.length - 1; i ++) {
            int dx = Math.abs(points[i + 1][0] - points[i][0]);
            int dy = Math.abs(points[i + 1][1] - points[i][1]);
            time += Math.max(dx, dy);
        }
        return time;
    }
}