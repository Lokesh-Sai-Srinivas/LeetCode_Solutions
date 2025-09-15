"""
Problem: 1935 - Maximum Number of Words You Can Type  
Description: Given a string `text` and a string `brokenLetters`, return the number of words in `text` that can be fully typed using a keyboard that has all the letters in `brokenLetters` broken. A word can be typed if none of its characters are in `brokenLetters`.  
Date: 2025-09-15  
"""

public class Solution {
    public static int canBeTypedWords(String text, String brokenLetters) {
        boolean[] broken = new boolean[26];
        for (char ch : brokenLetters.toCharArray()) {
            broken[ch - 'a'] = true;
        }

        int count = 0;
        boolean canType = true;

        for (char ch : text.toCharArray()) {
            if (ch == ' ') {
                if (canType) count++;
                canType = true;
            } else if (broken[ch - 'a']) {
                canType = false;
            }
        }

        if (canType) count++; 

        return count;
    }
}
