# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MOD = 10**9 + 7

    def maxProduct(self, root: TreeNode) -> int:
        sums = []

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            sums.append(total)
            return total

        total_sum = dfs(root)
        max_prod = 0
        for s in sums:
            max_prod = max(max_prod, s * (total_sum - s))

        return max_prod % self.MOD