class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Simulate linked list and use Floyd's cycle
        slow = nums[0]
        fast = nums[0]

        # Phase 1: detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: find entry
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        