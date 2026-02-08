class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        return height(root) != -1;
    }

    private static int height (TreeNode root) {
        if(root == null) return 0;
        int hl = height(root.left);
        int hr = height(root.right);
        
        if(hr == -1 || hl == -1) return -1;

        return (Math.abs(hl - hr) > 1) ? -1 :1 + Math.max(hl,hr);
    }
}