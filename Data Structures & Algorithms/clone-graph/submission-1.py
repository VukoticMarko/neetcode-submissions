"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def clone_dfs(node):
            if node in oldToNew: # Have I already cloned this node?
                return oldToNew[node] # Return that cloned node

            copy = Node(node.val)
            oldToNew[node] = copy # Save new clone to dict

            for neigh in node.neighbors: # From original node that we copied
                copy.neighbors.append(clone_dfs(neigh)) # Copy original's neighbours to copy node
            return copy

        return clone_dfs(node) if node else None