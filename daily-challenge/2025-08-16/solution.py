"""
Problem: 1323 - Maximum 69 Number  
Description: Given a positive integer `num` consisting only of digits 6 and 9, return the maximum number you can get by changing at most one digit (6 becomes 9, or 9 becomes 6).  
Date: 2025-08-16  
"""

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """

        temp = str(num)
        temp = temp.replace('6','9',1)
        
        return int(temp)
        
