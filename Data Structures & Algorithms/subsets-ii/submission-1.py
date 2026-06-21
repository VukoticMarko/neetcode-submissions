class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort so duplicates are next to each other

        result = []  # Store all unique subsets
        current_subset = []  # Current subset being built

        def dfs(start_index):
            result.append(current_subset.copy())  # Save current subset state

            for i in range(start_index, len(nums)):

                # If same number appears at same level, skip it
                if i > start_index and nums[i] == nums[i - 1]:
                    continue

                current_subset.append(nums[i])  # Choose element
                dfs(i + 1)  # Move forward
                current_subset.pop()  # Undo choice (backtrack)

        dfs(0)
        return result