class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):

                if i != j:
                    total = total * nums[j]
            out.append(total)
        return out