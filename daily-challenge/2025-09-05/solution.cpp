"""
Problem: 2749 - Minimum Operations to Make the Integer Zero  
Description: Given two integers num1 and num2, return the minimum number of operations to make num1 equal to 0 by repeatedly subtracting num2 and ensuring the result has at most i set bits in its binary form.  
Date: 2025-09-05
"""

class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        for(int i=1;i<=60;i++){
            long long remaining=num1-1LL * i*num2;
            if(remaining<i) continue;

            int ones=0;
            long long temp=remaining;
            while(temp>0){
                ones+=(temp & 1);
                temp>>=1;
            }
            if(ones<=i) return i;
        }
        return -1;

    }
};
