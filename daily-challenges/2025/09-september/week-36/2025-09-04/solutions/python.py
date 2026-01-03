class Solution:
    def shortDis(self, p1:int , p2:int ) -> int:
        dix = p1 - p2
        if dix < 0 : return 1
        if dix > 0 : return 2
        return 0

    def findClosest(self, x: int, y: int, z: int) -> int:
        xz = abs(x - z)
        yz = abs(z - y)
        
        return self.shortDis(xz,yz)