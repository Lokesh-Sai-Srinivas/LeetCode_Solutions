class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;

        int carry = 0;

        StringBuilder ans = new StringBuilder();
        while(i >= 0 || j >= 0 || carry == 1) {
            int res = carry;

            if(i >= 0) res += a.charAt(i -- ) - '0';
            if(j >= 0) res += b.charAt(j -- ) - '0';

            ans.append(res % 2);
            carry = res / 2;

        }

        return ans.reverse().toString();
    }
}
