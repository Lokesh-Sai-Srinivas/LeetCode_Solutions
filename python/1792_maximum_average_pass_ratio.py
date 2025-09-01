"""
Problem: 1792 - Maximum Average Pass Ratio  
Description: You are given a list of classes, each represented by [pass_i, total_i], and an integer extraStudents. Each extra student is guaranteed to pass any class they are assigned to. Assign these students to classes to maximize the average pass ratio across all classes. The pass ratio of a class is pass_i / total_i. Return the maximum possible average pass ratio after assigning all extra students.  
Date: 2025-09-01
"""

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p , t):
            return (p + 1) / (t + 1) - p / t
        
        heap = [(-gain(p,t), p , t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        return sum(p / t for _, p, t in heap ) / len(classes)
        
