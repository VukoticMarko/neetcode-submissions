class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # Store all permutations
        current_permutation = []  # Current built permutation
        used = [False] * len(nums)  # Track which elements are already used

        def dfs():
            # Base case: permutation is complete
            if len(current_permutation) == len(nums):
                result.append(current_permutation.copy())
                return

            for i in range(len(nums)):

                # Skip already used elements
                if used[i]:
                    continue

                # Choose element
                used[i] = True
                current_permutation.append(nums[i])

                dfs()  # Go deeper

                # Backtrack (undo choice)
                current_permutation.pop()
                used[i] = False

        dfs()
        return result