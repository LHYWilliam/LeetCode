#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#


# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10:
            num = sum([int(one) for one in f"{num}"])
        return num


# @lc code=end
