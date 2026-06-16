class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0]) 

        island_size = 0
        max_island_size = 0

        def dfs(r, c):
            nonlocal island_size
            if (
                r < 0 
                or c < 0 
                or r >= ROWS 
                or c >= COLS 
                or grid[r][c] == 0
            ): # r and c < 0 -> out of bounds left/up | r, c >= ROWS/COLS -> out of bounds right/down
                return

            # Make parts of island to water so we don't count same land over and over with
            # other dfs iterations 1 -> 0
            grid[r][c] = 0
            island_size += 1

            for dr, dc in directions: # Direction row/column
                dfs(r + dr, c + dc) # Use directions [] for checking every neighbour
        
        # We check entire grid until we find first island (1) and then start sinking it
        # and after we continue hunt for other islands if they exist
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    island_size = 0 # Reset size for each new island
                    dfs(r, c) # Check all 1's (entire island)
                    max_island_size = max(island_size, max_island_size)

        return max_island_size