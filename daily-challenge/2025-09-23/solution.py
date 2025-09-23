"""
Problem: 165 - Compare Version Numbers  
Description: Given two version numbers as strings, compare them and return -1 if version1 < version2, 1 if version1 > version2, or 0 if they are equal.  
Date: 2025-09-23
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        max_len = max(len(v1), len(v2))
        v1 += [0] * (max_len - len(v1))
        v2 += [0] * (max_len - len(v2))
        
        for a, b in zip(v1, v2):
            if a < b: return -1
            if a > b: return 1
        return 0
