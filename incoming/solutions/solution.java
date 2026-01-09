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
    private static class Pair {
        int depth;
        TreeNode node;

        Pair(int d, TreeNode n) {
            depth = d;
            node = n;
        }
    }

    private Pair dfs(TreeNode node) {
        if (node == null)
            return new Pair(-1, null);
        Pair L = dfs(node.left), R = dfs(node.right);
        if (L.depth == R.depth)
            return new Pair(L.depth + 1, node);
        return (L.depth > R.depth) ? new Pair(L.depth + 1, L.node) : new Pair(R.depth + 1, R.node);
    }

    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return dfs(root).node;
    }
}
