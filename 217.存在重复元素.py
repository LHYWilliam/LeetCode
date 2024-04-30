#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  # type: ignore
        # answer = {}
        # flag = False

        # for num in nums:
        #     if num in answer:
        #         flag = True
        #         break
        #     else:
        #         answer[num] = num

        # return flag

        return len(nums) != len(set(nums))


# @lc code=end
