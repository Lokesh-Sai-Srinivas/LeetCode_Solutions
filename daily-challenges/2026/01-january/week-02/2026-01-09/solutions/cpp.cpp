class Solution {
public:
    pair<int, TreeNode*> dfs(TreeNode* node) {
        if (!node)
            return {-1, nullptr};
        auto L = dfs(node->left), R = dfs(node->right);
        if (L.first == R.first)
            return {L.first + 1, node};
        return (L.first > R.first) ? make_pair(L.first + 1, L.second)
                                   : make_pair(R.first + 1, R.second);
    }
    TreeNode* subtreeWithAllDeepest(TreeNode* root) { return dfs(root).second; }
};