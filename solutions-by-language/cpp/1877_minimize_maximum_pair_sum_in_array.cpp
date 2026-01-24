class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int s = 0;
        int l = n - 1;
        int maxi = nums[s++] + nums[l--];

        while(s < l) {
            maxi = max(nums[s++] + nums[l--], maxi);
        }

        return maxi;
    }
};