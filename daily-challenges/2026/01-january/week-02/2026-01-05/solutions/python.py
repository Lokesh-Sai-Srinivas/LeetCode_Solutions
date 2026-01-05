class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sumAbs = 0
        negCount = 0
        minAbs = 1000001
        hasZero = False

        for row in matrix:
            for val in row:
                if val == 0 : hasZero = True
                if val < 0 : negCount += 1
                ab = abs(val)
                sumAbs += ab
                if ab < minAbs : minAbs = ab
        
        if (negCount % 2 == 0 or hasZero): return sumAbs
        return sumAbs - 2 * minAbs

v