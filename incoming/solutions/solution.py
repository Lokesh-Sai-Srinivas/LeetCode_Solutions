class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        maxArea = 0
        stack = []   
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1': 
                    heights[j] += 1
                else: 
                    heights[j] = 0
            
            stack = []    
            for j in range(n+1):
                while len(stack) > 0 and (j == n or heights[stack[-1]] >= heights[j]):
                    h = heights[stack.pop()]
                    w = 0 if not stack else (j - stack[-1] - 1)   
                    maxArea = max(maxArea, h * w)
                    
                stack.append(j)
                
        return maxArea
