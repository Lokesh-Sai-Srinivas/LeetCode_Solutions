# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None : return True
        return self.height(root) != -1

    def height(self, root) -> bool:
        if root == None : return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if (l == -1 or r == -1) : return -1

        if (abs(l - r) > 1) : return -1
        return 1 + max(l, r)
