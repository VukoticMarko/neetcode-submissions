class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        r_list = []

        for n in range(len(nums)):
            for n2 in range(len(nums)):

                if nums[n] + nums[n2] == target and n!=n2:
                    r_list.append(n)
        
        return r_list


        