class Solution {
public:
    int minimumDeletions(string s) {
        int bCo = 0;
        int op = 0;
        int n = s.length();
        for(int i = 0; i < n; i ++) {
            if(s[i] == 'b') {
                bCo ++;
            } else  {
                op = min(op + 1, bCo);
            }
        }

        return op;
    }
};
