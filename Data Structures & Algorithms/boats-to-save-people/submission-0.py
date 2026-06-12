class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        left = 0
        right = len(people) - 1
        boats_used = 0

        while left <= right:

            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats_used += 1

        return boats_used