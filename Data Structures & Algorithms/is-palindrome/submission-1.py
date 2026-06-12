class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        if cleaned.lower()[::-1] == cleaned.lower():
            return True
        return False
        