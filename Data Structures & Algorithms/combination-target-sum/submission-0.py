class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []

        def dfs(i, target):

            if target == 0:
                res.append(path[:])
                return

            if target < 0 or i == len(nums):
                return

            # Take current number
            path.append(nums[i])
            dfs(i, target - nums[i])
            path.pop()

            # Skip current number
            dfs(i + 1, target)

        dfs(0, target)
        return res