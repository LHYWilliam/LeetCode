#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  # type: ignore
        left, right = 0, len(nums) - 1
        while left < len(nums) and nums[left] != val and left <= right:
            left += 1
        while right >= 0 and nums[right] == val and left <= right:
            right -= 1

        while left <= right:
            if left != right:
                nums[left] = nums[right]
            else:
                left -= 1
                break

            right -= 1
            while nums[left] != val and left <= right:
                left += 1
            while nums[right] == val and left <= right:
                right -= 1

        return left


# @lc code=end
