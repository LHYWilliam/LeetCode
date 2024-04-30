#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:  # type: ignore
        nums.sort()
        answer = None
        if nums[0] != 0:
            answer = 0
        elif nums[-1] != len(nums):
            answer = len(nums)
        else:
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] != 1:
                    answer = nums[i - 1] + 1
                    break

        return answer

        # return list(set([one for one in range(0, len(nums) + 1)]) - set(nums))[0]


# @lc code=end
