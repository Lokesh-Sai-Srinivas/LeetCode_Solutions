"""
Problem: 3227 - Vowels Game in a String  
Description: Given a string `s`, determine whether Alice wins the game. Alice wins if the string contains at least one vowel. Vowels are defined as 'a', 'e', 'i', 'o', 'u'. Return `true` if Alice wins, otherwise return `false`.  
Date: 2025-09-12  
"""

class Solution {
    public boolean doesAliceWin(String s) {
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            switch(c){
                case 'a', 'e','i','o','u':
                return true;
            }
        }
        return false;
    }
}
