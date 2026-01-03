class Solution {
public:
    int maximum69Number (int num) {
        std::string str = std::to_string(num);
        for(char &c : str){
            if(c == '6'){
                c = '9';
                break;
            }
        }
        return std::stoi(str);
    }
};