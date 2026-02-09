class Solution {
public:
    TreeNode* balanceBST(TreeNode* root) {
        vector<TreeNode* > nodes;
        inorder(nodes, root);
        return build(nodes, 0, nodes.size() - 1);
    }

private:
    void inorder(vector<TreeNode* >& nodes, TreeNode* root) {
        if(!root) return ;
        inorder(nodes, root -> left );
        nodes.push_back(root);
        inorder(nodes, root -> right);
    }
    TreeNode* build(vector<TreeNode* >& nodes, int left, int right) {
        if(left > right) return nullptr;
        int mid = (left + right) / 2;
        
        TreeNode* root = nodes[mid];
        root -> left = build(nodes, left, mid - 1);
        root -> right= build(nodes, mid + 1, right);
        return root;
    }
};