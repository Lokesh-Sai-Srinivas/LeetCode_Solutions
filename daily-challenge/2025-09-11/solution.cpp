"""
Problem: 2785 - Sort Vowels in a String  
Description: Given a string s, sort only the vowels of the string in ascending order and return the resulting string. The relative positions of the consonants and non-vowel characters must remain unchanged. Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).  
Date: 2025-09-11  
"""

class Solution {
public:
    string sortVowels(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        vector <char> vowels_chars;

        for (char c : s) {
            if(vowels.count(c)) {
                vowels_chars.push_back(c);
            }
        }

        sort(vowels_chars.begin(), vowels_chars.end());

        int idx = 0;
        for(int i = 0 ; i < s.size(); i++) {
            if(vowels.count(s[i])) {
                s[i] = vowels_chars[idx++];
            }
        }
        return s;
    }
};
