"""
  Problem: 2264 - Largest 3-Same-Digit Number in String  
  Description: Given a string `num` representing a large integer, return the largest good integer as a string. A good integer is a substring of length 3 that consists of the same digit repeated three times (e.g., "777", "000"). If no such substring exists, return an empty string `""`.
  Date: 2025-08-14  
"""

class Solution {
public:
    string largestGoodInteger(string num) {
        int target = -1;
        for(int i = 0; i < 10 ; i++){
            string pattren(3,'0' + i);
            if (num.find(pattren) != string::npos){
                target = i;
            }
        }
        if (target == -1){
            return "";
        } else{
            string pattren(3,'0' + target);
            return pattren;
        }
        
    }
};
