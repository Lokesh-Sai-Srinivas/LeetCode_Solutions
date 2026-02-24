/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumRootToLeaf(TreeNode r) {
        if(r == null) return 0;

        int ans = sum(r, 0);
        return ans;
    }

    private int sum(TreeNode r, int res){
        if(r == null) return 0;

        int cur = res * 2 + r.val;

        if(r.left == null && r.right == null) {
            return cur;
        }

        int left = (r.left != null) ? sum(r.left, cur): 0;
        int right = (r.right != null) ? sum(r.right, cur): 0;

        return left + right;
    }
}
