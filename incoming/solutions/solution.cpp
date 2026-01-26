class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int minDif = INT_MAX;
        vector<vector<int>> ans;

        for(int i = 0; i < arr.size() - 1; i ++) {
            int dif = arr[i + 1] - arr[i];
            if(dif < minDif) {
                ans.clear();
                minDif = dif;
            }

            if(dif == minDif) {
                ans.push_back({arr[i], arr[i + 1]});
            }
        }
        return ans;
    }
};
