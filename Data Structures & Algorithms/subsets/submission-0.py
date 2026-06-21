class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        all_subsets = []  # Stores all generated subsets
        current_subset = []  # Current path (subset being built)

        def dfs(index):
            # Base case: we processed all elements
            if index >= len(nums):
                all_subsets.append(current_subset.copy())  # Store a snapshot of current subset
                return

            # OPTION 1: include nums[index] in subset
            current_subset.append(nums[index])  # choose element
            dfs(index + 1)  # Move to next element
            current_subset.pop()  # Undo choice (backtrack)

            # OPTION 2: exclude nums[index] from subset
            dfs(index + 1)  # Skip element and move forward

        dfs(0)
        return all_subsets