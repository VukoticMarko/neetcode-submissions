class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def mark_safe_dfs(row, col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if board[row][col] != "O":
                return

            board[row][col] = "S" # Every cell that is on the border is 
            # not surrounded and can be marked as Safe

            mark_safe_dfs(row + 1, col)
            mark_safe_dfs(row - 1, col)
            mark_safe_dfs(row, col + 1)
            mark_safe_dfs(row, col - 1)

        for row in range(rows):
            mark_safe_dfs(row, 0)
            mark_safe_dfs(row, cols - 1)

        for col in range(cols):
            mark_safe_dfs(0, col)
            mark_safe_dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"