class Solution {
    public double champagneTower(int  ped, int qr, int qg) {
        double[][] tower = new double[qr + 2][qr + 2];
        tower[0][0] = ped;

        for(int r = 0; r <= qr; r ++) {
            for(int c = 0; c <= r; c++) {
                double overFlow = (tower[r][c] - 1.0) / 2.0;
                if(overFlow > 0) {
                    tower[r + 1][c] += overFlow;
                    tower[r + 1][c + 1] += overFlow;
                }
            }
        }

        return Math.min(1.0, tower[qr][qg]);
    }
}
