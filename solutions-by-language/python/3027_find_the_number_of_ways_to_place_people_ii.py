class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x ascending, then y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for j in range(n):  # Bob at j
            yj = points[j][1]
            # m = minimum y among points strictly between i and j whose y >= yj
            m = float('inf')

            for i in range(j - 1, -1, -1):  # Alice to the left
                # include the immediate right neighbor into the "between" set
                if i + 1 < j:
                    yr = points[i + 1][1]
                    if yr >= yj and yr < m:
                        m = yr

                yi = points[i][1]
                # valid if yi >= yj and no blocking point in (i, j) with y in [yj, yi]
                if yi >= yj and yi < m:
                    ans += 1

        return ans