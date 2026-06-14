# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def alert_police_dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = alert_police_dfs(node.left)
            right = alert_police_dfs(node.right)

            # If we rob this node -> cannot rob children
            rob = node.val + left[1] + right[1] # [1] -> we are taking not_rob of the returns

            # If we do NOT rob this node -> take best of children
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(alert_police_dfs(root))
        