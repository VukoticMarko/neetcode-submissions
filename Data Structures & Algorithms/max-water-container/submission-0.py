class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):

                height = min(heights[i], heights[j])
                width = j - i
                area = height * width

                max_area = max(max_area, area)

        return max_area
 