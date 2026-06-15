class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0]) 
        # Note: grid[0] = "first row", with len of that we get n of columns

        islands = 0

        def dfs(r, c):
            if (
                r < 0 
                or c < 0 
                or r >= ROWS 
                or c >= COLS 
                or grid[r][c] == "0"
            ): # r and c < 0 -> out of bounds left/up | r, c >= ROWS/COLS -> out of bounds right/down
                return

            # Make parts of island to water so we don't count same land over and over with
            # other dfs iterations 1 -> 0
            grid[r][c] = "0" 

            for dr, dc in directions: # Direction row/column
                dfs(r + dr, c + dc) # Use directions [] for checking every neighbour
        
        # We check entire grid until we find first island (1) and then start sinking it
        # and after we continue hunt for other islands if they exist
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c) # Check all 1's (entire island)
                    islands += 1

        return islands