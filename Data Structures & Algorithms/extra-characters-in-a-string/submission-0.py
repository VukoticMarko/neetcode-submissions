class Solution:
    def minExtraChar(self, s, dictionary):
        words = set(dictionary)  # Fast word lookup

        dp = [0] * (len(s) + 1)

        # Process from right to left
        for start_index in range(len(s) - 1, -1, -1):

            # Option 1:
            # Treat current character as extra
            dp[start_index] = 1 + dp[start_index + 1]

            # Option 2:
            # Try every substring starting here
            for end_index in range(start_index, len(s)):

                current_word = s[start_index:end_index + 1]

                # If substring is a dictionary word
                if current_word in words:

                    # Skip the whole word
                    dp[start_index] = min(
                        dp[start_index],
                        dp[end_index + 1]
                    )

        return dp[0]