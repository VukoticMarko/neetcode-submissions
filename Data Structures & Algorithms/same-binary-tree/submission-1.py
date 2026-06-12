# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_list = self.treeToList(p, [])
        q_list = self.treeToList(q, [])

        if p_list == q_list:
            return True
        return False

    def treeToList(self, tree: Optional[TreeNode], ret: List):

        if not tree:
            ret.append(None) # To keep exact same shapes
            return None

        ret.append(tree.val)
        self.treeToList(tree.left, ret)

        ret.append(tree.val)
        self.treeToList(tree.right, ret)

        return ret
        