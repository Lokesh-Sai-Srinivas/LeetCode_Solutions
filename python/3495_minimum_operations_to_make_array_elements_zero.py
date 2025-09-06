"""
Problem: 3495 - Minimum Operations to Make Array Elements Zero  
Description: Given multiple queries [l, r], each representing an array of integers from l to r inclusive, in one operation you can pick two numbers a and b and replace them with floor(a/4) and floor(b/4). For each query, find the minimum number of operations to make all elements zero, and return the sum over all queries.  
Date: 2025-09-06
"""

class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        def ops_for_range(l: int, r: int) -> int:
            steps_sum = 0
            start = 1
            level = 1

            while start <= r:
                end = start * 4 - 1
                left = max(l, start)
                right = min(r, end)

                if left <= right:
                    count = right - left + 1
                    steps_sum += count * level

                start *= 4
                level += 1

            return (steps_sum + 1) // 2 

        total = 0
        for l, r in queries:
            total += ops_for_range(l, r)
        return total
