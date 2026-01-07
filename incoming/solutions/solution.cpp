/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
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
