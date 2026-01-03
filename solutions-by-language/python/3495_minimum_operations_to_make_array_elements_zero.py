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