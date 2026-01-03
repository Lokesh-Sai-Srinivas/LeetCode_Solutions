class Solution {
    public int findClosest(int x, int y, int z) {
        int xz = Math.abs(z - x);
        int yz = Math.abs(z - y);

        return shortDis(xz, yz);
    }

    private int shortDis(int p1, int p2){
        int dix = p1 - p2;
        if(dix < 0) return 1;
        if(dix > 0) return 2;
        return 0;
    }

}