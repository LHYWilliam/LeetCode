#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  # type: ignore
        cnt = 1
        for one in nums[1:]:
            if one != nums[cnt - 1]:
                nums[cnt] = one
                cnt += 1

        return cnt


# @lc code=end
