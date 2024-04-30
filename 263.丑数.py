#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#


# @lc code=start
class Solution:
    def divide(self, n: int) -> bool:
        if n == 1:
            return True

        flag = False
        if n % 2 == 0:
            flag = flag or self.divide(n // 2)
        if n % 3 == 0:
            flag = flag or self.divide(n // 3)
        if n % 5 == 0:
            flag = flag or self.divide(n // 5)

        return flag

    def isUgly(self, n: int) -> bool:
        return self.divide(n) if n else False


# @lc code=end
