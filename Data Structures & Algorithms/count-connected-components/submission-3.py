class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}

        for i in range(n):
            graph[i] = []  # Create neighbor list for every node

        for a, b in edges:
            graph[a].append(b)  # Undirected edge
            graph[b].append(a)  # Add both directions

        visited = set()
        components = 0

        def count_dfs(node):
            if node in visited:
                return  # Already explored

            visited.add(node)  # Mark current node

            for neighbor in graph[node]:
                count_dfs(neighbor)  # Visit all connected neighbors

        for node in range(n):
            if node not in visited:
                components += 1  # Found a new component
                count_dfs(node)  # Explore entire component

        return components