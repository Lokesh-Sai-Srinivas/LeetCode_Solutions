class Solution {
    private static long MOD = 1_000_000_007;

    public int maxProduct(TreeNode root) {
        List<Long> pre = new ArrayList<>();

        long total = dfs(pre, root);
        
        long maxPro = 0;
        for(long ele : pre){
            long pro = ele * (total - ele);
            if(pro > maxPro) {
                maxPro = pro;
            }
        }
        
        return (int)(maxPro % MOD);
    }

    private static Long dfs(List<Long> pre,TreeNode root){
        if(root == null) return 0L;
        long res = root.val + dfs(pre, root.left) + dfs(pre,root.right);
        pre.add(res);
        return res;
    }
}