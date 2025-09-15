"""
Problem: 1935 - Maximum Number of Words You Can Type  
Description: Given a string `text` and a string `brokenLetters`, return the number of words in `text` that can be fully typed using a keyboard that has all the letters in `brokenLetters` broken. A word can be typed if none of its characters are in `brokenLetters`.  
Date: 2025-09-15  
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(all(ch not in broken for ch in word) for word in text.split())
