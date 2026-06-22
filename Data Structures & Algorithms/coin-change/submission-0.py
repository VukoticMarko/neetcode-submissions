class Solution:
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)  # dp[i] = min coins needed for amount i
        dp[0] = 0  # 0 coins needed to make amount 0

        for current_amount in range(1, amount + 1):

            for coin in coins:

                # Check if coin can be used
                if current_amount - coin >= 0:

                    # Try using this coin and keep best answer
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        # If still infinity, amount cannot be formed
        if dp[amount] == float("inf"):
            return -1

        return dp[amount]