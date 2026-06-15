class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-s for s in stones] # Add - to all numbers to make min heap become max heap
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if second > first:
                heapq.heappush(maxHeap, first - second)

        return -maxHeap[0] if maxHeap else 0
