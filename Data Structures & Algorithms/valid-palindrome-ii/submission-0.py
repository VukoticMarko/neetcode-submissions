class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        original = s

        for i in range(len(s)):

            new_s = s[:i] + s[i+1:]
            if self.isPalindrome(new_s):
                return True

        return False


    def isPalindrome(self, s:str):

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
