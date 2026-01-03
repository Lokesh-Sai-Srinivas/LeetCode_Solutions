class Solution {
public:
    bool isPowerOfThree(int n) {
        int maxPossible = 1162261467;
        return (n > 0 && maxPossible % n == 0);
    }
};