# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1
        right = n

        if n < 2:
            return n     

        while left <= right:
            mid = (left + right) // 2
            hint = guess(mid) # -1 higher | 0 equal | 1 lower

            if hint == 0:
                return mid
            elif hint == -1: # We need to ignore everything on the right
                right = mid - 1
            else: # We need to ignore everything on the left
                left = mid + 1
        return mid
