#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:  # type: ignore
        times = [0 for _ in range(60001)]

        for one in nums:
            times[one + 30000] += 1

        answer = times.index(1) - 30000

        return answer


# @lc code=end
