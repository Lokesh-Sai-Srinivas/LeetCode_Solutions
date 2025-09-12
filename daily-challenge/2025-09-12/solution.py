"""
Problem: 3227 - Vowels Game in a String  
Description: Given a string `s`, determine whether Alice wins the game. Alice wins if the string contains at least one vowel. Vowels are defined as 'a', 'e', 'i', 'o', 'u'. Return `true` if Alice wins, otherwise return `false`.  
Date: 2025-09-12  
"""

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        if count == 0: return False
        else: return True
        
