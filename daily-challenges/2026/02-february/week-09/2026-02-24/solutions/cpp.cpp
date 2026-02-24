class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        if(root == nullptr) return 0;
        return sum(root, 0);
    }
private:
    int sum(TreeNode* r, int res) {
        if(r == nullptr) return 0;
        int cur = res * 2 + r -> val;
        if(r->left == nullptr && r -> right == nullptr) return cur;
        int left = (r -> left != nullptr) ? sum(r->left, cur) : 0;
        int right = (r -> right != nullptr) ? sum(r->right, cur) : 0 ;

        return left + right;
    }
};