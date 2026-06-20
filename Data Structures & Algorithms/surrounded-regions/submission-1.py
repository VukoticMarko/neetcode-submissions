class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def mark_safe(row, col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if board[row][col] != "O":
                return

            board[row][col] = "S" # Every cell that is on the border is 
            # not surrounded and can be marked as Safe

            mark_safe(row + 1, col)
            mark_safe(row - 1, col)
            mark_safe(row, col + 1)
            mark_safe(row, col - 1)

        for row in range(rows):
            mark_safe(row, 0)
            mark_safe(row, cols - 1)

        for col in range(cols):
            mark_safe(0, col)
            mark_safe(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"