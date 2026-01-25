class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        if(k <= 1) return 0;
        sort(nums.begin(), nums.end());

        int ans = INT_MAX;
        int n = nums.size();
        int i = 0; 
        int j = i + k - 1;

        while(j < n){
            ans = min(ans, nums[j++] - nums[i++]);
        }

        return ans;
    }
};
