# Problem: 679 - 24 Game
 # Description: Given four numbers, determine if they can be combined using +, -, *, / and parentheses to make exactly 24.
 # Date: 2025-08-18

from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nums = [float(x) for x in cards]
        EPS = 1e-6

        def dfs(arr: List[float]) -> bool:
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPS

            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = arr[i], arr[j]

                    results = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        results.append(a / b)
                    if abs(a) > EPS:
                        results.append(b / a)

                    rest = [arr[k] for k in range(n) if k != i and k != j]
                    for val in results:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs(nums)