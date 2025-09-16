"""
Problem: 2197 - Replace Non-Coprime Numbers in Array  
Description: Given an array nums, repeatedly replace adjacent non-coprime numbers with their LCM until all adjacent pairs are coprime, and return the resulting array.  
Date: 2025-09-16
"""


class Solution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        List<Integer> res = new ArrayList<>();

        for(int num : nums){
            res.add(num);
            while (res.size() >= 2) {
                int a = res.remove(res.size() - 1);
                int b = res.remove(res.size() - 1);
                if( GCD(a,b) > 1 ){
                    res.add(LCM(a,b));
                } else {
                    res.add(b);
                    res.add(a);
                    break;
                }
            }
        }
        return res;
    }

    private static int LCM(int a, int b){
        return (a / GCD(a,b) )* b ; // a * b = lcm(a,b) * gcd(a,b)
    }

    private static int GCD(int a , int b){
        while(b != 0){
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
