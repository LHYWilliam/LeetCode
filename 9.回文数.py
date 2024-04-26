#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == "".join(list(reversed(str(x))))


# @lc code=end
