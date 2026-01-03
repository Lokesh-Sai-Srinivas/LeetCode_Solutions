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