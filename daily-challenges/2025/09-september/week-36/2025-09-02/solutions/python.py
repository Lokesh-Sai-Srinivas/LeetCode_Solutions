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