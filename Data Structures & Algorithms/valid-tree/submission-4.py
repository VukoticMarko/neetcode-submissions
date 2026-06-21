class Solution:
    def validTree(self, n, edges):
        graph = {}

        for i in range(n):
            graph[i] = []  # Create adjacency list for every node

        for a, b in edges:
            graph[a].append(b)  # Undirected edge
            graph[b].append(a)  # Add both directions

        visited = set()

        def tree_dfs(node, parent):
            if node in visited:
                return False  # Revisiting node means cycle

            visited.add(node)  # Mark node as visited

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Ignore edge back to parent

                if not tree_dfs(neighbor, node):
                    return False  # Cycle found deeper in DFS

            return True

        if not tree_dfs(0, -1):
            return False  # Graph contains a cycle

        if len(visited) != n:
            return False  # Some nodes are disconnected

        return True
