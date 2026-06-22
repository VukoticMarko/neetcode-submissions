class Solution:
    def minDistance(self, word1, word2):
        rows = len(word1)
        cols = len(word2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # If word2 is empty, delete remaining chars from word1
        for row in range(rows + 1):
            dp[row][cols] = rows - row

        # If word1 is empty, insert remaining chars from word2
        for col in range(cols + 1):
            dp[rows][col] = cols - col

        # Fill table from bottom-right toward top-left
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):

                # Characters match, no operation needed
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row + 1][col + 1]

                else:
                    insert_cost = dp[row][col + 1]
                    delete_cost = dp[row + 1][col]
                    replace_cost = dp[row + 1][col + 1]

                    # Choose cheapest operation
                    dp[row][col] = 1 + min(
                        insert_cost,
                        delete_cost,
                        replace_cost
                    )

        return dp[0][0]