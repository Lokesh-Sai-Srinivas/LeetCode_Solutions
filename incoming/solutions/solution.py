# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root, nodes):
            if not root : return
            inorder(root.left, nodes)
            nodes.append(root)
            inorder(root.right, nodes)
        
        def build(nodes, left, right):
            if left > right : return None
            mid = (left + right) // 2
            root = nodes[mid]
            root.left = build(nodes, left, mid - 1)
            root.right = build(nodes, mid + 1, right)
            return root

        nodes = []
        inorder(root, nodes)
        return build(nodes, 0, len(nodes) - 1)
