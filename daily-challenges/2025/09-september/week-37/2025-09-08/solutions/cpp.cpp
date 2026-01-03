class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        vector<int> nums;
        int i = 1;
        while(true){
            if(contains0(n - i) && contains0(i)){
                nums.push_back(i);
                nums.push_back(n-i);
                break;
            } else {
                i+=2;
            }
        }
        return nums;
    }
private:
    bool contains0(int n){
        while(n > 0){
            if(n % 10 == 0)
                return false;
            n /= 10;
        }
        return true;
    }
};