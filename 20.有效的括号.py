#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        match = ("()", "[]", "{}")
        stack = []
        for one in s:
            stack.append(one)

            if len(stack) > 1 and "".join(stack[-2:]) in match:
                del stack[-2:]

        flag = False if stack else True
        return flag


# @lc code=end
