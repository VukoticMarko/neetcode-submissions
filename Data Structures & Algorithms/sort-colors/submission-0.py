class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        i = 0

        # Fill 0s
        for _ in range(count[0]):
            nums[i] = 0
            i += 1

        # Fill 1s
        for _ in range(count[1]):
            nums[i] = 1
            i += 1

        # Fill 2s
        for _ in range(count[2]):
            nums[i] = 2
            i += 1


            

            
