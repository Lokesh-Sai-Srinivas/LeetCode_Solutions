"""
Problem: 3197 - Find the Minimum Area to Cover All Ones II  
Description: You are given a 2D binary array grid. Find three non-overlapping rectangles (with non-zero areas and sides parallel to the axes) such that all the 1's in the grid lie inside these rectangles. Rectangles may touch but cannot overlap. Return the minimum possible sum of the areas of these rectangles.  
Date: 2025-08-23
"""


from typing import List

INF = 10**18

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Quick check: if no ones, answer is 0
        total_ones = sum(sum(row) for row in grid)
        if total_ones == 0:
            return 0

        def build_TL():
            has = [[False]*n for _ in range(m)]
            minR = [[INF]*n for _ in range(m)]
            maxR = [[-INF]*n for _ in range(m)]
            minC = [[INF]*n for _ in range(m)]
            maxC = [[-INF]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    v = grid[r][c] == 1
                    if r > 0:
                        has[r][c] = has[r][c] or has[r-1][c]
                        minR[r][c] = min(minR[r][c], minR[r-1][c])
                        maxR[r][c] = max(maxR[r][c], maxR[r-1][c])
                        minC[r][c] = min(minC[r][c], minC[r-1][c])
                        maxC[r][c] = max(maxC[r][c], maxC[r-1][c])
                    if c > 0:
                        has[r][c] = has[r][c] or has[r][c-1]
                        minR[r][c] = min(minR[r][c], minR[r][c-1])
                        maxR[r][c] = max(maxR[r][c], maxR[r][c-1])
                        minC[r][c] = min(minC[r][c], minC[r][c-1])
                        maxC[r][c] = max(maxC[r][c], maxC[r][c-1])
                    if v:
                        has[r][c] = True
                        minR[r][c] = min(minR[r][c], r)
                        maxR[r][c] = max(maxR[r][c], r)
                        minC[r][c] = min(minC[r][c], c)
                        maxC[r][c] = max(maxC[r][c], c)
            area = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if has[r][c]:
                        area[r][c] = (maxR[r][c]-minR[r][c]+1)*(maxC[r][c]-minC[r][c]+1)
            return area

        def build_TR():
            has = [[False]*n for _ in range(m)]
            minR = [[INF]*n for _ in range(m)]
            maxR = [[-INF]*n for _ in range(m)]
            minC = [[INF]*n for _ in range(m)]
            maxC = [[-INF]*n for _ in range(m)]
            for r in range(m):
                for c in range(n-1, -1, -1):
                    v = grid[r][c] == 1
                    if r > 0:
                        has[r][c] = has[r][c] or has[r-1][c]
                        minR[r][c] = min(minR[r][c], minR[r-1][c])
                        maxR[r][c] = max(maxR[r][c], maxR[r-1][c])
                        minC[r][c] = min(minC[r][c], minC[r-1][c])
                        maxC[r][c] = max(maxC[r][c], maxC[r-1][c])
                    if c+1 < n:
                        has[r][c] = has[r][c] or has[r][c+1]
                        minR[r][c] = min(minR[r][c], minR[r][c+1])
                        maxR[r][c] = max(maxR[r][c], maxR[r][c+1])
                        minC[r][c] = min(minC[r][c], minC[r][c+1])
                        maxC[r][c] = max(maxC[r][c], maxC[r][c+1])
                    if v:
                        has[r][c] = True
                        minR[r][c] = min(minR[r][c], r)
                        maxR[r][c] = max(maxR[r][c], r)
                        minC[r][c] = min(minC[r][c], c)
                        maxC[r][c] = max(maxC[r][c], c)
            area = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if has[r][c]:
                        area[r][c] = (maxR[r][c]-minR[r][c]+1)*(maxC[r][c]-minC[r][c]+1)
            return area

        def build_BL():
            has = [[False]*n for _ in range(m)]
            minR = [[INF]*n for _ in range(m)]
            maxR = [[-INF]*n for _ in range(m)]
            minC = [[INF]*n for _ in range(m)]
            maxC = [[-INF]*n for _ in range(m)]
            for r in range(m-1, -1, -1):
                for c in range(n):
                    v = grid[r][c] == 1
                    if r+1 < m:
                        has[r][c] = has[r][c] or has[r+1][c]
                        minR[r][c] = min(minR[r][c], minR[r+1][c])
                        maxR[r][c] = max(maxR[r][c], maxR[r+1][c])
                        minC[r][c] = min(minC[r][c], minC[r+1][c])
                        maxC[r][c] = max(maxC[r][c], maxC[r+1][c])
                    if c > 0:
                        has[r][c] = has[r][c] or has[r][c-1]
                        minR[r][c] = min(minR[r][c], minR[r][c-1])
                        maxR[r][c] = max(maxR[r][c], maxR[r][c-1])
                        minC[r][c] = min(minC[r][c], minC[r][c-1])
                        maxC[r][c] = max(maxC[r][c], maxC[r][c-1])
                    if v:
                        has[r][c] = True
                        minR[r][c] = min(minR[r][c], r)
                        maxR[r][c] = max(maxR[r][c], r)
                        minC[r][c] = min(minC[r][c], c)
                        maxC[r][c] = max(maxC[r][c], c)
            area = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if has[r][c]:
                        area[r][c] = (maxR[r][c]-minR[r][c]+1)*(maxC[r][c]-minC[r][c]+1)
            return area

        def build_BR():
            has = [[False]*n for _ in range(m)]
            minR = [[INF]*n for _ in range(m)]
            maxR = [[-INF]*n for _ in range(m)]
            minC = [[INF]*n for _ in range(m)]
            maxC = [[-INF]*n for _ in range(m)]
            for r in range(m-1, -1, -1):
                for c in range(n-1, -1, -1):
                    v = grid[r][c] == 1
                    if r+1 < m:
                        has[r][c] = has[r][c] or has[r+1][c]
                        minR[r][c] = min(minR[r][c], minR[r+1][c])
                        maxR[r][c] = max(maxR[r][c], maxR[r+1][c])
                        minC[r][c] = min(minC[r][c], minC[r+1][c])
                        maxC[r][c] = max(maxC[r][c], maxC[r+1][c])
                    if c+1 < n:
                        has[r][c] = has[r][c] or has[r][c+1]
                        minR[r][c] = min(minR[r][c], minR[r][c+1])
                        maxR[r][c] = max(maxR[r][c], maxR[r][c+1])
                        minC[r][c] = min(minC[r][c], minC[r][c+1])
                        maxC[r][c] = max(maxC[r][c], maxC[r][c+1])
                    if v:
                        has[r][c] = True
                        minR[r][c] = min(minR[r][c], r)
                        maxR[r][c] = max(maxR[r][c], r)
                        minC[r][c] = min(minC[r][c], c)
                        maxC[r][c] = max(maxC[r][c], c)
            area = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if has[r][c]:
                        area[r][c] = (maxR[r][c]-minR[r][c]+1)*(maxC[r][c]-minC[r][c]+1)
            return area

        TL = build_TL()
        TR = build_TR()
        BL = build_BL()
        BR = build_BR()

        # One-rect areas for full prefixes/suffixes by rows/cols
        up1 = [TL[r][n-1] for r in range(m)]
        down1 = [BL[r][n-1] for r in range(m)]
        left1 = [TL[m-1][c] for c in range(n)]
        right1 = [TR[m-1][c] for c in range(n)]

        # Row-wise interval one-rect areas (for HHH)
        rowMinCol = [INF]*m
        rowMaxCol = [-INF]*m
        anyRow = [False]*m
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    anyRow[r] = True
                    rowMinCol[r] = min(rowMinCol[r], c)
                    rowMaxCol[r] = max(rowMaxCol[r], c)

        rowsArea = [[0]*m for _ in range(m)]
        for i in range(m):
            minC = INF; maxC = -INF; have = False; top = INF; bot = -INF
            for j in range(i, m):
                if anyRow[j]:
                    have = True
                    top = min(top, j)
                    bot = max(bot, j)
                    minC = min(minC, rowMinCol[j])
                    maxC = max(maxC, rowMaxCol[j])
                rowsArea[i][j] = (bot-top+1)*(maxC-minC+1) if have else 0

        # Column-wise interval one-rect areas (for VVV)
        colMinRow = [INF]*n
        colMaxRow = [-INF]*n
        anyCol = [False]*n
        for c in range(n):
            for r in range(m):
                if grid[r][c] == 1:
                    anyCol[c] = True
                    colMinRow[c] = min(colMinRow[c], r)
                    colMaxRow[c] = max(colMaxRow[c], r)

        colsArea = [[0]*n for _ in range(n)]
        for i in range(n):
            minR = INF; maxR = -INF; have = False; left = INF; right = -INF
            for j in range(i, n):
                if anyCol[j]:
                    have = True
                    left = min(left, j)
                    right = max(right, j)
                    minR = min(minR, colMinRow[j])
                    maxR = max(maxR, colMaxRow[j])
                colsArea[i][j] = (maxR-minR+1)*(right-left+1) if have else 0

        ans = INF

        # HHH: top + middle + bottom (two row cuts)
        for r1 in range(m-2):
            for r2 in range(r1+1, m-1):
                ans = min(ans, rowsArea[0][r1] + rowsArea[r1+1][r2] + rowsArea[r2+1][m-1])

        # VVV: left + middle + right (two col cuts)
        for c1 in range(n-2):
            for c2 in range(c1+1, n-1):
                ans = min(ans, colsArea[0][c1] + colsArea[c1+1][c2] + colsArea[c2+1][n-1])

        # L-shapes: two-vertical in top + one-rect bottom; and two-vertical in bottom + one-rect top
        for r in range(m-1):
            bestTop2V = INF
            bestBot2V = INF
            for c in range(n-1):
                bestTop2V = min(bestTop2V, TL[r][c] + TR[r][c+1])
                bestBot2V = min(bestBot2V, BL[r+1][c] + BR[r+1][c+1])
            ans = min(ans, bestTop2V + rowsArea[r+1][m-1])
            ans = min(ans, bestBot2V + rowsArea[0][r])

        # L-shapes: two-horizontal in left + one-rect right; and two-horizontal in right + one-rect left
        for c in range(n-1):
            bestLeft2H = INF
            bestRight2H = INF
            for r in range(m-1):
                bestLeft2H = min(bestLeft2H, TL[r][c] + BL[r+1][c])
                bestRight2H = min(bestRight2H, TR[r][c+1] + BR[r+1][c+1])
            ans = min(ans, bestLeft2H + colsArea[c+1][n-1])
            ans = min(ans, bestRight2H + colsArea[0][c])

        return ans
