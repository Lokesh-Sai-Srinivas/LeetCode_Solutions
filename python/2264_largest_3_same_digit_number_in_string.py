"""
  Problem: 2264 - Largest 3-Same-Digit Number in String  
  Description: Given a string `num` representing a large integer, return the largest good integer as a string. A good integer is a substring of length 3 that consists of the same digit repeated three times (e.g., "777", "000"). If no such substring exists, return an empty string `""`.
  Date: 2025-08-14  
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1, -1):
            pat = str(i) * 3
            if(num.find(pat) != -1) :
                return pat
        
        return ""
