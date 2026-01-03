class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        int n = nums.size();
        vector<int> st;
        st.reserve(n);

        for(int x : nums) {
            int cur = x;
            while (!st.empty()) {
                int a = st.back();
                int g = gcd(a,cur);
                if(g == 1) break;
                st.pop_back();
                cur = (a / g ) * cur;
            }
            st.push_back(cur);
        }
        return st;
    }

private:
    static int gcd(int a , int b){
        while(b) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
};