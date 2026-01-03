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