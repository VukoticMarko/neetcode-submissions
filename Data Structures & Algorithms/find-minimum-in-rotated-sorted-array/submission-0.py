class Solution:
    def findMin(self, nums: List[int]) -> int:


        min = 99999999999

        for n in nums:

            if n < min:
                min = n
        return min
        