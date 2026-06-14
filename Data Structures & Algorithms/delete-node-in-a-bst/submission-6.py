# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_min(node):
            # Finds inorder successor (smallest in right subtree)
            while node.left:
                node = node.left
            return node

        def delete_dfs(node, key):
            if not node:
                return None

            # Go left or right like BST search
            if key < node.val:
                node.left = delete_dfs(node.left, key)

            elif key > node.val:
                node.right = delete_dfs(node.right, key)

            else:
                # CASE 1: No left child
                if not node.left:
                    return node.right

                # CASE 2: No right child
                if not node.right:
                    return node.left

                # CASE 3: Two children
                successor = find_min(node.right)
                node.val = successor.val
                node.right = delete_dfs(node.right, successor.val)

            return node

        return delete_dfs(root, key)
        