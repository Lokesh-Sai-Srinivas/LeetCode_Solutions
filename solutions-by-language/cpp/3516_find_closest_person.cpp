class Solution {
public:
    int findClosest(int x, int y, int z) {
        int xz = (z - x);
        int yz = (z - y);

        return shortDis(giveAB(xz),giveAB(yz));
    }

    private:
        int shortDis(int p1, int p2){
            int dix = p1 - p2;
            if (dix > 0){
                return 2;
            }else if (dix < 0) {
                return 1;
            }
            return 0;
        }
        int giveAB(int n){
            if(n < 0){
                return -n;
            }
            return n;
        }
};