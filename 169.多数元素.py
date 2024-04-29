#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:  # type: ignore
        back = {}

        for one in nums:
            if one in back:
                back[one] += 1
            else:
                back[one] = 1

        back = [(num, time) for num, time in back.items()]
        back = sorted(back, key=lambda one: one[1])

        return back[-1][0]


# @lc code=end
