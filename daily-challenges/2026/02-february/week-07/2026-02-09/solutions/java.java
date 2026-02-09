class Solution {
    public TreeNode balanceBST(TreeNode root) {
        ArrayList<TreeNode> node = new ArrayList<>();

        inorder(node, root);
        root = build(node, 0, node.size()- 1);
        return root;
    }

    private static void inorder(List<TreeNode> node, TreeNode root){
        if(root == null) return ;
        inorder(node, root.left);
        node.add(root);
        inorder(node,root.right);
    }

    private static TreeNode build(List<TreeNode> node,int left,int right){
        if(left > right) return null;
        int mid = (left + right) / 2;

        TreeNode root = node.get(mid);
        root.left = build(node, left, mid - 1);
        root.right = build(node, mid + 1, right);
        return root;
    }
}