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