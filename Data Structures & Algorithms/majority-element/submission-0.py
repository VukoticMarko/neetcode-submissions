class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = defaultdict(int)

        for n in nums:
            majority[n] += 1

        max_count = 0
        ret = 0

        for k, v in majority.items():
            if v > max_count:
                max_count = v
                ret = k

        return ret
        