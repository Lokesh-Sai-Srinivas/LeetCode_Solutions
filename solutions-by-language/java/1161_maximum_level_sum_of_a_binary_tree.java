class Solution {
    public int maxLevelSum(TreeNode root) {
        if (root.left == null && root.right == null)
            return 1;
        long maxSum = Long.MIN_VALUE;
        int ans = 1;
        int currLevel = 1;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            long currSum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                currSum += node.val;
                if (node.left != null)
                    q.add(node.left);
                if (node.right != null)
                    q.add(node.right);
            }
            if (currSum > maxSum) {
                maxSum = currSum;
                ans = currLevel;
            }
            currLevel++;
        }
        return ans;
    }
}