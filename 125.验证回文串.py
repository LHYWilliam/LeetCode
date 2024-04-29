#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([one if one.isalpha() or one.isdigit() else "" for one in s])

        return s == "".join(list(reversed(s)))
        pass


# @lc code=end
