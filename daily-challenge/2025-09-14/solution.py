"""
Problem: 966 - Vowel Spellchecker  
Description: Given a wordlist and a list of queries, return the word from the wordlist that matches each query with the following priority: (1) exact match, (2) case-insensitive match, (3) vowel-error match (where vowels are treated as interchangeable). If no match is found, return an empty string.  
Date: 2025-09-14  
"""

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('*' if c.lower() in 'aeiou' else c.lower() for c in word)

        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            devoweled = devowel(lower)
            case_map.setdefault(lower, word)
            vowel_map.setdefault(devoweled, word)

        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            elif query.lower() in case_map:
                result.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:
                result.append(vowel_map[devowel(query)])
            else:
                result.append("")
        return result
