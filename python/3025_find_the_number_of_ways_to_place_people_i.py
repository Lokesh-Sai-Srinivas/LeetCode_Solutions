"""
Problem: 3025 - Find the Number of Ways to Place People I  
Description: You are given a list of 2D coordinates representing people on a grid. Count the number of valid pairs (i, j) such that person i can see person j directly either horizontally or vertically, and no other person blocks the view. A person can see another if they are aligned and there are no other people between them.  
Date: 2025-09-02
"""

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]

                if x1 < x2 and y1 > y2:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if x1 <= x <= x2 and y2 <= y <= y1:
                            valid = False
                            break
                    if valid:
                        count += 1

                elif x1 == x2 and y1 > y2:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if x == x1 and y2 < y < y1:
                            valid = False
                            break
                    if valid:
                        count += 1

                elif y1 == y2 and x1 < x2:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if y == y1 and x1 < x < x2:
                            valid = False
                            break
                    if valid:
                        count += 1

        return count
