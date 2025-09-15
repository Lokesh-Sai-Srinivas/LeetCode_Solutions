"""
Problem: 1935 - Maximum Number of Words You Can Type  
Description: Given a string `text` and a string `brokenLetters`, return the number of words in `text` that can be fully typed using a keyboard that has all the letters in `brokenLetters` broken. A word can be typed if none of its characters are in `brokenLetters`.  
Date: 2025-09-15  
"""

class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        std::stringstream iss(text);
        std::string word;
        int count = 0;
        while(iss >> word){
            if(!isBroken(word,brokenLetters)){
                count++;
            }
        }
        return count;
    }

    bool isBroken(string word, string bl){
        
        for(char ch : bl){
            if(word.find(ch) != std::string::npos ){
                return true;
            }
        }
        
        return false;
    }
};
