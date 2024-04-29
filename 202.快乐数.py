#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        flag = True
        while n != 1:
            n = sum([pow(int(one), 2) for one in f"{n}"])
            if n != 1 and n < 7:
                flag = False
                break

        return flag


# @lc code=end
