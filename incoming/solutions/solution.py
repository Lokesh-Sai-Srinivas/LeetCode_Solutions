# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, r: Optional[TreeNode]) -> int:
        return self.sum(r, 0)
    def sum(self, r, res) -> int:
        if(r == None): return 0
        cur = res*2+r.val
        left = 0
        right = 0
        if(r.left == None and r.right == None): return cur
        if(r.left != None): left = self.sum(r.left, cur)
        if(r.right != None): right = self.sum(r.right, cur)
        return left+right
