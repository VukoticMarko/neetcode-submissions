class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:

            # if it's a closing bracket
            if c in pairs:

                if not stack or stack[-1] != pairs[c]:
                    return False

                stack.pop()

            else:
                stack.append(c)

        return len(stack) == 0

        