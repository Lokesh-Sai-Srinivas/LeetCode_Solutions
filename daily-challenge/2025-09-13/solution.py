"""
Problem: 3541 - Find Most Frequent Vowel and Consonant  
Description: Given a string `s` consisting of lowercase English letters, find the most frequent vowel and the most frequent consonant in the string. Return the sum of their frequencies. Vowels are defined as 'a', 'e', 'i', 'o', 'u'.  
Date: 2025-09-13  
"""

class Solution:
    def maxFreqSum(self, s: str) -> int:
        arr = [0] * 26  

        for ch in s:
            arr[ord(ch) - ord('a')] += 1

        freq1 = 0  
        freq2 = 0  

        for i in range(26):
            if i in [ord('a') - ord('a'), ord('e') - ord('a'), ord('i') - ord('a'), ord('o') - ord('a'), ord('u') - ord('a')]:
                freq1 = max(freq1, arr[i])
            else:
                freq2 = max(freq2, arr[i])

        return freq1 + freq2
