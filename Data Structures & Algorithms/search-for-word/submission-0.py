class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(row, col, word_index):
            if word_index == len(word):
                return True  # Entire word was matched

            if row < 0 or row >= num_rows:
                return False  # Outside board

            if col < 0 or col >= num_cols:
                return False  # Outside board

            if board[row][col] != word[word_index]:
                return False  # Current character does not match

            original_char = board[row][col]
            board[row][col] = "#"  # Mark cell as visited

            found_word = (
                dfs(row + 1, col, word_index + 1) or
                dfs(row - 1, col, word_index + 1) or
                dfs(row, col + 1, word_index + 1) or
                dfs(row, col - 1, word_index + 1)
            )

            board[row][col] = original_char  # Backtrack

            return found_word

        for row in range(num_rows):
            for col in range(num_cols):
                if dfs(row, col, 0):
                    return True

        return False
        