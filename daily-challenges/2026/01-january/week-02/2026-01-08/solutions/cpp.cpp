class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        const int MINI = - 1000000000;
        int dp [n + 1][m + 1];

        for(int i = 0; i <= n; i ++){
            for(int j = 0; j <= m; j++){
                dp[i][j] = MINI;
            }
        }

        for(int i = n -1; i >= 0; i --) {
            for(int j = m - 1; j >= 0; j --) {
                int pair = nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1]);
                int skip1 = dp[i + 1][j];
                int skip2 = dp[i][j + 1];
                dp[i][j] = max(pair, max(skip1, skip2));
            }
        }

        return dp[0][0];
    }
};