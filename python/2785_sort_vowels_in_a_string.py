"""
Problem: 2785 - Sort Vowels in a String  
Description: Given a string s, sort only the vowels of the string in ascending order and return the resulting string. The relative positions of the consonants and non-vowel characters must remain unchanged. Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).  
Date: 2025-09-11  
"""

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_chars = [c for c in s if c in vowels]
        vowel_chars.sort()

        result = []
        vowel_index = 0

        for c in s:
            if c in vowels:
                result.append(vowel_chars[vowel_index])
                vowel_index += 1
            else:
                result.append(c)

        return ''.join(result)
