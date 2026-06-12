class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        left = 1 # First nums[0] will always be unique and stay at index 0
        for right in range(1, len(nums)):

            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
                
        return left
        