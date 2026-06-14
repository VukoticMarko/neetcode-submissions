# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder_dfs(node):
            if not node:
                return

            inorder_dfs(node.left)
            res.append(node.val)
            inorder_dfs(node.right)

        inorder_dfs(root)
        return res