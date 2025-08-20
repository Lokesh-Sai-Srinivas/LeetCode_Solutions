"""
  Problem: 1323 - Maximum 69 Number  
  Description: Given a positive integer `num` consisting only of digits 6 and 9, return the maximum number you can get by changing at most one digit (6 becomes 9, or 9 becomes 6).  
  Date: 2025-08-16  
"""

class Solution {
    public int maximum69Number (int num) {
        int n = num;
        int rem;
        int rev = 0, count = 0;
        boolean flag= false;
        int k= 0, expo =1;

        while(n != 0){
            rem = n% 10;
            rev = rev * 10 + rem;
            n = n /10;
            count ++;
        }

        while(rev != 0){
            rem = rev %10;
            if( rem == 6){
                flag  = true;
                break;
            }
            k = k +1;
            rev = rev / 10;
        }
        
        if(!flag) return num;
        while(count != k){
            expo*=10;
            k++;
        }
        expo /= 10;
        return num + 3 * expo;
    }
}
