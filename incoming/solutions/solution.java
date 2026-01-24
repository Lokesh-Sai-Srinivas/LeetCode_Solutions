class Solution {
    public double separateSquares(int[][] squares) {
        double minY = Double.MAX_VALUE;
        double maxY = Double.MIN_VALUE;
        double totalArea = 0.0;

        for (int[] sq : squares) {
            double y = sq[1], l = sq[2];
            minY = Math.min(minY, y);
            maxY = Math.max(maxY, y + l);
            totalArea += l * l;
        }

        double lo = minY, hi = maxY;
        for (int iter = 0; iter < 70; iter++) {
            double mid = (lo + hi) / 2.0;
            double topArea = getTop(squares, mid);
            if (topArea > totalArea / 2.0) {
                lo = mid;   
            } else {
                hi = mid;   
            }
        }
        return (lo + hi) / 2.0;
    }

    private double getTop(int[][] squares, double line) {
        double area = 0.0;
        for (int[] sq : squares) {
            double y = sq[1], l = sq[2];
            if (y >= line) {
                area += l * l;
            } else if (y + l > line) {
                double heightAbove = y + l - line;
                area += l * heightAbove;
            }
        }
        return area;
    }
}
