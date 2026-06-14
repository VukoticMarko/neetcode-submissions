# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def longest_path_dfs(node):
            nonlocal res

            if not node:
                return 0

            left_height = longest_path_dfs(node.left)
            right_height = longest_path_dfs(node.right)

            res = max(res, left_height + right_height)

            return 1 + max(left_height, right_height)

        longest_path_dfs(root)
        return res
        