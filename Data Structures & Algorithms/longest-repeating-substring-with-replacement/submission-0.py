class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_freq = 0
        best = 0

        for right in range(len(s)):

            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Track most frequent character in window
            max_freq = max(max_freq, count[s[right]])

            # If window is invalid, shrink it
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update best result
            best = max(best, right - left + 1)

        return best



        