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