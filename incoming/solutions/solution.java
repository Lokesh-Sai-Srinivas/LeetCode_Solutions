class Solution {
    public long maxMatrixSum(int[][] mat) {
        long sumAbs = 0L;
        int negCount = 0;
        int minAbs = Integer.MAX_VALUE;
        boolean hasZero = false;

        for(int [] row : mat) {
            for(int val : row){
                if(val == 0) hasZero = true;
                if(val < 0) negCount++;
                int abs = Math.abs(val);
                sumAbs += abs;
                if(abs < minAbs) minAbs = abs;
            }
        }

        if(negCount % 2 == 0 || hasZero){
            return sumAbs;
        }
        return sumAbs - 2L * minAbs;
    }
}
