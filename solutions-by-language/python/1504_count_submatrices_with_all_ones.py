class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            row_sum = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    row_sum[j] = row_sum[prev] + heights[j] * (j - prev)
                else:
                    row_sum[j] = heights[j] * (j + 1)

                stack.append(j)
                total += row_sum[j]

        return total