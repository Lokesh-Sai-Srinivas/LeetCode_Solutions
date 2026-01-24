class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0.0
        minY = float("inf")
        maxY = float("-inf")

        for x, y, l in squares:
            total += l * l
            minY = min(minY, y)
            maxY = max(maxY, y + l)

        target = total / 2.0
        lo, hi = minY, maxY

        def areaAbove(h: float) -> float:
            s = 0.0
            for x, y, l in squares:
                hAbove = y + l - h
                if hAbove <= 0:
                    continue
                if hAbove >= l:
                    s += l * l
                else:
                    s += l * hAbove
            return s

        for _ in range(70):  
            mid = (lo + hi) / 2.0
            if areaAbove(mid) > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2.0
