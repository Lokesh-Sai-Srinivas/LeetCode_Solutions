"""
Problem: 3227 - Vowels Game in a String  
Description: Given a string `s`, determine whether Alice wins the game. Alice wins if the string contains at least one vowel. Vowels are defined as 'a', 'e', 'i', 'o', 'u'. Return `true` if Alice wins, otherwise return `false`.  
Date: 2025-09-12  
"""

class Solution {
public:
    bool doesAliceWin(string s) {
        string vowels = "aeiou";
        for(int i = 0; i < s.size(); i++){
            if(vowels.find(s[i]) != string::npos){
                return 1;
            }
        }
        return 0;
    }
};
