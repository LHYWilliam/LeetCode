#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = False
        if n == 1:
            flag = True
        if n >= 2 and "1" not in set(f"{bin(n)}"[3:]):
            flag = True

        return flag


# @lc code=end
