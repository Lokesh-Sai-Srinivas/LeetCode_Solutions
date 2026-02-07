class Solution {
    public int minimumDeletions(String s) {
        int bCo = 0;
        int op = 0;

        for(char ch : s.toCharArray()) {
            if(ch == 'b') {
                bCo ++;
            } else if (bCo > 0) {
                op ++;
                bCo --;
            }
        }

        return op;
    }
}
