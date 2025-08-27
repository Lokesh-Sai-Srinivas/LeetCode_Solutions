"""
Problem: 3459 - Length of Longest V-Shaped Diagonal Segment  
Description: Given a 2D grid of integers, find the length of the longest V-shaped diagonal segment. A valid V-shape consists of two connected diagonals with alternating values (e.g., 1 → 2 → 1) and a single turning point. Diagonals must follow one of the four diagonal directions and may only turn once.  
Date: 2025-08-27
"""

from functools import lru_cache
import sys
from typing import List

sys.setrecursionlimit(1_000_000)

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # ↘, ↙, ↖, ↗

        # After seeing value v, the next required value is next_map[v]
        next_map = {1: 2, 2: 0, 0: 2}

        @lru_cache(None)
        def dp(x: int, y: int, turned: int, d: int, expect: int) -> int:
            # expect is the value that must appear at (x,y)
            if not (0 <= x < n and 0 <= y < m):
                return 0
            if grid[x][y] != expect:
                return 0

            best = 1
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            best = 1 + dp(nx, ny, turned, d, next_map[expect])

            # allow one clockwise 90° turn (only once)
            if turned == 0:
                nd = (d + 1) % 4
                tx, ty = x + dirs[nd][0], y + dirs[nd][1]
                best = max(best, 1 + dp(tx, ty, 1, nd, next_map[expect]))

            return best

        ans = 0
        # Start only from cells with 1 (segment must start with 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, dp(i, j, 0, d, 1))
        return ans
