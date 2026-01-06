# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        max_sum = float('-inf')
        ans = 1
        curr_level = 1

        q = deque([root])

        while q :
            size = len(q)
            curr_sum = 0

            for _ in range(size):
                node = q.popleft()
                curr_sum += node.val

                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = curr_level
            
            curr_level += 1
        return ans
