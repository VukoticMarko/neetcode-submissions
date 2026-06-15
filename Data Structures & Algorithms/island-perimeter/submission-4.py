class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def grid_dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perimeter = grid_dfs(i, j + 1) 
            perimeter += grid_dfs(i + 1, j) 
            perimeter += grid_dfs(i, j - 1) 
            perimeter += grid_dfs(i - 1, j)
            return perimeter 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return grid_dfs(i, j)