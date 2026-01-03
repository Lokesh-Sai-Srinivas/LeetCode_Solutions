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