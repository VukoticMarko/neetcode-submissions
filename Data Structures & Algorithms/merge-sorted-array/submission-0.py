class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_ptr = m - 1          # Last real element in nums1
        nums2_ptr = n - 1          # Last element in nums2
        write_ptr = m + n - 1      # Last position in nums1 (including empty space)

        while nums2_ptr >= 0:
            if nums1_ptr >= 0 and nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[write_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[write_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1

            write_ptr -= 1
