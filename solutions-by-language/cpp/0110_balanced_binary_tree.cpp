class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if(root == nullptr ) return true;
        return height(root) != -1;
    }

    int height(TreeNode* root) {
        if(root == nullptr) return 0;
        int l = height(root->left);
        int r = height(root->right);
        if(l == -1 || r == -1) return -1;

        return (abs(l - r) > 1) ? -1: 1 + max(l , r);
    }
};