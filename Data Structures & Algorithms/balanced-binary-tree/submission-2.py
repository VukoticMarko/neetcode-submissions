# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balanced_dfs(node):
            if not node:
                return 0

            left = balanced_dfs(node.left)
            if left == -1:
                return -1

            right = balanced_dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) >= 2:
                return -1

            return 1 + max(left, right)

        return balanced_dfs(root) != -1
        