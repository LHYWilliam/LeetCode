#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # type: ignore
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                for k in range(len(nums1) - 1, i, -1):
                    nums1[k] = nums1[k - 1]
                nums1[i] = nums2[j]
                j += 1

            if i >= m + j:
                nums1[i] = nums2[j]
                j += 1

            i += 1
        """
        Do not return anything, modify nums1 in-place instead.
        """


# @lc code=end
