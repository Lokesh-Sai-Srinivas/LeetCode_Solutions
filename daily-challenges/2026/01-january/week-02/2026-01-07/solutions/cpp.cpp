class Solution {
    const long long MOD = 1'000'000'007;
    vector<long long> sums;
    long long dfs(TreeNode* root) {
        if (!root)
            return 0;
        long long total = root->val + dfs(root->left) + dfs(root->right);
        sums.push_back(total);
        return total;
    }

public:
    int maxProduct(TreeNode* root) {
        long long total = dfs(root);
        long long maxProd = 0;
        for (long long s : sums) {
            maxProd = max(maxProd, s * (total - s));
        }
        return (int)(maxProd % MOD);
    }
};